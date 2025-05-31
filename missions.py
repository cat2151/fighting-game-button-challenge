import random

def initialize_mission_sets(missions):
    missions_set = set(mission["input"] for mission in missions)
    success_missions = set()
    mission_index = get_new_mission_index(missions, missions_set)
    return missions_set,success_missions,mission_index

def check_and_update_mission(plus, missions, mission_index, lever_plus_pressed, missions_set, success_missions, score):
    mission = missions[mission_index]["input"]
    mission_result = check_mission_success(mission, lever_plus_pressed, plus)
    if mission_result == "green":
        mission_index, missions_set, success_missions, score = on_green(missions, missions_set, mission, success_missions, score)

    return mission, mission_index, missions_set, success_missions, score

def on_green(missions, missions_set, mission, success_missions, score):
    missions_set = update_missions_set(missions, missions_set, mission, success_missions)
    mission_index = get_new_mission_index(missions, missions_set)
    score += 1
    return mission_index, missions_set, success_missions, score

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
