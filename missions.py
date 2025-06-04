import random
import copy
import os

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

def check_and_update_mission(plus, missions, mission_index, lever_plus_pressed, missions_set, success_missions, score, wait_for_all_buttons_release, _=None, none_word="なし"):
    if wait_for_all_buttons_release: # issues #8
        all_released = (lever_plus_pressed == none_word)
        if all_released:
            wait_for_all_buttons_release = False
        else:
            mission = missions[mission_index]["input"]
            return mission, mission_index, missions_set, success_missions, score, wait_for_all_buttons_release

    mission = missions[mission_index]["input"]
    mission_result = check_mission_success(mission, lever_plus_pressed, plus)
    if mission_result == "green":
        mission_index, missions_set, success_missions, score, wait_for_all_buttons_release = on_green(missions, missions_set, mission, success_missions, score, wait_for_all_buttons_release)

    return mission, mission_index, missions_set, success_missions, score, wait_for_all_buttons_release

def on_green(missions, missions_set, mission, success_missions, score, wait_for_all_release):
    # ミッション成功時に全ボタン離し待ち状態へ遷移
    wait_for_all_release = True
    missions_set = update_missions_set(missions, missions_set, mission, success_missions)
    mission_index = get_new_mission_index(missions, missions_set)
    score += 1
    return mission_index, missions_set, success_missions, score, wait_for_all_release

def update_missions_set(missions, missions_set, mission, success_missions):
    success_missions.add(mission)
    missions_set.remove(mission)
    if not missions_set:
        print("すべてのmissionを成功しました")
        success_missions.clear()
        missions_set = set(m["input"] for m in missions)
    return missions_set

def get_new_mission_index(missions, missions_set):
    mission = random.choice(list(missions_set))
    mission_index = next((i for i, m in enumerate(missions) if m["input"] == mission), -1)
    return mission_index

def check_mission_success(mission, lever_plus_pressed, plus):
    formated_mission = format_mission_string(mission, plus)
    formated_lever_plus_pressed = format_mission_string(lever_plus_pressed, plus)

    # print(f"mission: {formated_mission}, lever_plus_pressed: {formated_lever_plus_pressed}")
    if formated_lever_plus_pressed == formated_mission:
        return "green"
    return "red"

def format_mission_string(mission, plus):
    tokens = mission.split(plus)
    trimmed = [x.strip() for x in tokens]
    sorted_tokens = sorted(trimmed)
    combined = plus.join(sorted_tokens)
    return combined
