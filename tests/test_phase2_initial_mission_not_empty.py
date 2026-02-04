"""
Test for issue #41: phase2で、初手で、空missionになってしまった
This test ensures that when transitioning from Phase 1 to Phase 2,
the initial mission is not empty.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from missions import (
    initialize_mission_sets,
    check_and_update_mission,
    on_mission_start,
    PHASE_1_BUTTONS,
    PHASE_2_MOVES
)

class Args:
    """Mock args object for testing"""
    def __init__(self):
        self.left_right = ["右", "左"]
        self.left_right_temp = ["みぎ", "ひだり"]
        self.histogram_mode_sample_count = 50

def test_phase2_initial_mission_not_empty():
    """
    Test that the initial mission in phase 2 is not empty after transitioning from phase 1.
    This is a regression test for issue #41.
    """
    # Setup with simple missions
    missions = [
        {"input": "右"},
        {"input": "左"},
    ]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    args = Args()
    
    # Initialize in Phase 1
    (missions_list, missions_set, success_missions, mission_index, current_direction, original_missions) = initialize_mission_sets(
        missions, left_right, left_right_temp, PHASE_1_BUTTONS, "right"
    )
    
    # Create initial state
    state = {
        "score": 0,
        "fail_count": 0,
        "wait_for_all_buttons_release": False,
        "mission": missions_list[mission_index]["input"],
        "last_failed_input": None,
        "mission_index": mission_index,
        "missions_set": missions_set,
        "success_missions": success_missions,
        "current_mission_frame_count": 0,
        "last_mission_frame_count": 0,
        "prev_success_min_frame_count": 0,
        "prev_success_frame_counts": [],
        "challenge_phase": PHASE_1_BUTTONS,
        "current_direction": current_direction,
        "original_missions": original_missions,
        "missions": missions_list,
    }
    state = on_mission_start(state)
    
    # Complete all Phase 1 missions
    remaining_missions = list(missions_set)
    for idx, mission_input in enumerate(remaining_missions):
        current_missions = state["missions"]
        
        mission_idx = next((i for i, m in enumerate(current_missions) if m["input"] == mission_input), -1)
        if mission_idx == -1:
            continue
        
        state["mission_index"] = mission_idx
        state["mission"] = current_missions[mission_idx]["input"]
        
        if idx > 0:
            state["wait_for_all_buttons_release"] = False
        
        # Complete the mission
        state = check_and_update_mission(
            state, 
            current_missions,
            " + ", 
            mission_input,
            [],
            "なし",
            args
        )
    
    # Verify transition to Phase 2
    assert state.get("challenge_phase") == PHASE_2_MOVES, f"Expected Phase 2, got {state.get('challenge_phase')}"
    assert state.get("current_direction") == "right", f"Expected right direction, got {state.get('current_direction')}"
    
    # THE KEY ASSERTION: Mission should NOT be empty
    mission = state.get("mission", "")
    assert mission != "", f"Mission should not be empty after transitioning to Phase 2! Got: '{mission}'"
    assert mission in ["右", "左"], f"Mission should be a valid input, got: '{mission}'"
    
    # Verify missions_set is properly rebuilt
    missions_set = state.get("missions_set", set())
    assert len(missions_set) > 0, "missions_set should not be empty after transitioning to Phase 2"
    
    # Verify the mission is in missions_set
    assert mission in missions_set, f"Mission '{mission}' should be in missions_set {missions_set}"
    
    print(f"✓ Phase 2 initial mission is valid: '{mission}'")
    print(f"✓ missions_set: {missions_set}")

if __name__ == "__main__":
    test_phase2_initial_mission_not_empty()
    print("\n✅ All tests passed!")
