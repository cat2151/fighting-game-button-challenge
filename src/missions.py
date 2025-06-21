import random
import copy
import os
import numpy as np

def initialize_mission_sets(missions, left_right, left_right_temp):
    missions = amplify_missions_left_right(missions, left_right, left_right_temp) # 左右反転したミッションを追加
    missions_set = set(mission["input"] for mission in missions)
    success_missions = set()
    mission_index = get_new_mission_index(missions, missions_set)
    return missions, missions_set, success_missions, mission_index

def amplify_missions_left_right(missions, left_right, left_right_temp):
    def validate_left_right_temp(missions, left_right_temp):
        for temp in left_right_temp:
            for mission in missions:
                if temp in mission["input"]:
                    raise ValueError(f"left_right_tempの値 '{temp}' がmission '{mission['input']}' に含まれています。安全な一時置換のため、他のmission文字列と被らない値にしてください。")

    def swap_left_right(input_str):
        if len(left_right) != len(left_right_temp):
            raise ValueError("left_rightとleft_right_tempの要素数が一致していません。どちらも2要素にしてください。")
        swapped = input_str
        for orig, temp in zip(left_right, left_right_temp):
            swapped = swapped.replace(orig, temp)
        for temp, repl in zip(left_right_temp, reversed(left_right)):
            swapped = swapped.replace(temp, repl)
        return swapped

    validate_left_right_temp(missions, left_right_temp)

    amplified = []
    seen = set()
    for mission in missions:
        input_str = mission["input"]
        if input_str not in seen:
            amplified.append(copy.deepcopy(mission))
            seen.add(input_str)
        swapped = swap_left_right(input_str)
        if swapped != input_str and swapped not in seen:
            amplified.append({**copy.deepcopy(mission), "input": swapped})
            seen.add(swapped)

    print(f"[amplify_missions_left_right] 変更前 missions:\n{os.linesep.join(f'  {m}' for m in missions)}")
    print(f"[amplify_missions_left_right] 変更後 amplified:\n{os.linesep.join(f'  {a}' for a in amplified)}")

    return amplified

def check_and_update_mission(state, missions, plus, lever_plus_pressed, no_count_names, none_word, args):
    result = state.copy()
    result["current_mission_frame_count"] += 1 # 備忘、ここでの加算が必要。もしここより後ろだと、分岐によってはフレームカウンタが増えない
    if result["wait_for_all_buttons_release"]: # issues #8
        should_return, result = handle_wait_for_all_buttons_release(result, missions, lever_plus_pressed, none_word)
        if should_return:
            return result

    mission = missions[result["mission_index"]]["input"]
    mission_result = check_mission_success(mission, lever_plus_pressed, plus, no_count_names, none_word)
    result["status"] = mission_result
    if mission_result == "green":
        result.update(on_green(missions, result["missions_set"], mission, result["success_missions"], result["score"], result["wait_for_all_buttons_release"], result["fail_count"], state=result, args=args))
    elif mission_result == "red":
        result["fail_count"], result["last_failed_input"] = on_red(result["fail_count"], lever_plus_pressed, result["last_failed_input"])
    elif mission_result == "no_count":
        pass
    return result

def handle_wait_for_all_buttons_release(result, missions, lever_plus_pressed, none_word):
    all_released = lever_plus_pressed == none_word
    if all_released:
        result["wait_for_all_buttons_release"] = False
        result["status"] = "released"
        return True, result
    else:
        result["status"] = "wait_release"
        if 0 <= result["mission_index"] < len(missions):
            result["mission"] = missions[result["mission_index"]]["input"]
        else:
            result["mission"] = ""
        return True, result
    raise ValueError("wait_for_all_buttons_releaseがTrueのとき、lever_plus_pressedはnone_wordでなければなりません。") # 今後仕様変更時にここに到達したら問題検知できる用

def on_red(fail_count, lever_plus_pressed, last_failed_input):
    if last_failed_input != lever_plus_pressed:
        fail_count += 1
        last_failed_input = lever_plus_pressed
    return fail_count, last_failed_input

def on_green(missions, missions_set, mission, success_missions, score, wait_for_all_buttons_release, fail_count, state, args):
    wait_for_all_buttons_release = True
    missions_set, fail_count = update_missions_set(missions, missions_set, mission, success_missions, fail_count)
    mission_index = get_new_mission_index(missions, missions_set)
    score += 1
    if 0 <= mission_index < len(missions):
        mission_value = missions[mission_index]["input"] # 備忘、全ボタン離し待ち中も次のミッションをすぐ表示する用
    else:
        mission_value = ""
    if state is not None:
        state = update_success_frame_stats(state, score, args)
    return {
        "mission_index": mission_index,
        "missions_set": missions_set,
        "success_missions": success_missions,
        "score": score,
        "wait_for_all_buttons_release": wait_for_all_buttons_release,
        "fail_count": fail_count,
        "last_failed_input": None,
        "mission": mission_value,
        **({
            "current_mission_frame_count": 0,
            "last_mission_frame_count": state.get("last_mission_frame_count", 0) if state is not None else 0,
            "prev_success_min_frame_count": state.get("prev_success_min_frame_count", 0) if state is not None else 0,
            "prev_success_hist_center": state.get("prev_success_hist_center", 0) if state is not None else 0
        } if state is not None else {})
    }

def update_success_frame_stats(state, score, args):
    state["last_mission_frame_count"] = state.get("current_mission_frame_count", 0)
    last = state["last_mission_frame_count"]
    prev_min = state.get("prev_success_min_frame_count", 0)
    if score > 1: # 課題、初回が1フレなどで記録されることがある、対策、2回目以降を集計対象にする
        if last > 0 and (prev_min == 0 or last < prev_min):
            state["prev_success_min_frame_count"] = last
        if last > 0:
            state.setdefault("prev_success_frame_counts", []).append(last)
            sample_count = args.histogram_mode_sample_count
            if len(state["prev_success_frame_counts"]) > sample_count:
                state["prev_success_frame_counts"] = state["prev_success_frame_counts"][-sample_count:]
            arr = np.array(state["prev_success_frame_counts"])
            if len(arr) > 0:
                hist, bin_edges = np.histogram(arr, bins='auto')
                max_bin_idx = np.argmax(hist)
                bin_center = (bin_edges[max_bin_idx] + bin_edges[max_bin_idx+1]) / 2 # 備忘、これは「ヒストグラムの最頻ビンの中心」である。最も多く観測された値が属する区間の代表値として使う用。
                state["prev_success_hist_center"] = int(round(bin_center))
            else:
                state["prev_success_hist_center"] = 0
    state["current_mission_frame_count"] = 0
    return state

def update_missions_set(missions, missions_set, mission, success_missions, fail_count):
    success_missions.add(mission)
    missions_set.remove(mission)
    if not missions_set:
        missions_set, fail_count = on_all_mission_green(missions, success_missions, fail_count)
    return missions_set, fail_count

def on_all_mission_green(missions, success_missions, fail_count):
    print("すべてのmissionを成功しました")
    success_missions.clear()
    missions_set = set(m["input"] for m in missions)
    fail_count = 0  # 1周したらfail_countをリセット
    return missions_set, fail_count

def get_new_mission_index(missions, missions_set):
    mission = random.choice(list(missions_set))
    mission_index = next((i for i, m in enumerate(missions) if m["input"] == mission), -1)
    return mission_index

def check_mission_success(mission, lever_plus_pressed, plus, no_count_names, none_word):
    if lever_plus_pressed == none_word:
        return "no_count"
    formated_mission = format_mission_string(mission, plus)
    formated_lever_plus_pressed = format_mission_string(lever_plus_pressed, plus)

    if formated_lever_plus_pressed == formated_mission:
        return "green"
    if is_no_count_case(formated_mission, formated_lever_plus_pressed, no_count_names, plus):
        return "no_count"
    return "red"

def format_mission_string(mission, plus):
    tokens = mission.split(plus)
    trimmed = [x.strip() for x in tokens]
    sorted_tokens = sorted(trimmed)
    combined = plus.join(sorted_tokens)
    return combined

def is_no_count_case(
    mission_success: str,
    input_name: str,
    no_count_names_list: list[dict],
    plus: str
) -> bool:
    if not no_count_names_list:
        raise ValueError("no_count_names_listがNoneまたは空です。lever_names.toml に no_count_names を記載してください。")

    def create_allowed(mission_success, no_count_names_list, plus):
        allowed = set(x.strip() for x in mission_success.split(plus))
        allowed.add(mission_success)
        for nc in no_count_names_list:
            if nc['success'] == mission_success:
                allowed.update(nc['no_count'])
        return allowed

    allowed = create_allowed(mission_success, no_count_names_list, plus)
    input_parts = set(x.strip() for x in input_name.split(plus))
    return input_parts.issubset(allowed)
