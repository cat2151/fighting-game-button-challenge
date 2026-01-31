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

def test_phase_transition_integration():
    """
    Integration test for phase transitions.
    Tests the complete flow: Phase 1 -> Phase 2 (right) -> Phase 2 (left) -> Phase 2 (right)
    """
    # Setup
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
    
    # Verify Phase 1 initialization - should amplify missions
    assert len(missions_list) == 2  # Both 右 and 左 exist (no duplication since they're swapped versions)
    
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
    
    # Simulate completing all missions in Phase 1
    remaining_missions = list(missions_set)
    for idx, mission_input in enumerate(remaining_missions):
        # Get current missions from state (like the main loop does)
        current_missions = state["missions"]
        
        # Find the mission
        mission_idx = next((i for i, m in enumerate(current_missions) if m["input"] == mission_input), -1)
        if mission_idx == -1:
            continue
        
        state["mission_index"] = mission_idx
        state["mission"] = current_missions[mission_idx]["input"]
        
        # If not the first mission, simulate button release
        if idx > 0:
            state["wait_for_all_buttons_release"] = False
        
        # Simulate successful mission completion
        state = check_and_update_mission(
            state, 
            current_missions,  # Pass current missions from state
            " + ", 
            mission_input,  # lever_plus_pressed matches mission
            [],  # no_count_names
            "なし",  # none_word
            args
        )
    
    # After Phase 1 completion, should transition to Phase 2 with right direction
    assert state.get("challenge_phase") == PHASE_2_MOVES, f"Expected Phase 2, got {state.get('challenge_phase')}"
    assert state.get("current_direction") == "right", f"Expected right direction, got {state.get('current_direction')}"
    
    # Verify missions are regenerated for Phase 2
    phase2_missions = state["missions"]
    assert len(phase2_missions) == 2  # Original missions count, not amplified
    mission_inputs = [m["input"] for m in phase2_missions]
    assert "右" in mission_inputs  # Right direction, so should have 右
    
    # Simulate button release after phase transition
    state["wait_for_all_buttons_release"] = False
    
    # Complete Phase 2 first cycle (right direction)
    remaining_missions = list(state["missions_set"])
    for idx, mission_input in enumerate(remaining_missions):
        # Get current missions from state
        current_missions = state["missions"]
        
        mission_idx = next((i for i, m in enumerate(current_missions) if m["input"] == mission_input), -1)
        if mission_idx == -1:
            continue
        
        state["mission_index"] = mission_idx
        state["mission"] = current_missions[mission_idx]["input"]
        
        # Simulate button release before each mission
        if idx > 0:
            state["wait_for_all_buttons_release"] = False
        
        state = check_and_update_mission(
            state, 
            current_missions,
            " + ", 
            mission_input,
            [],
            "なし",
            args
        )
    
    # After Phase 2 first cycle, should toggle to left direction
    assert state.get("challenge_phase") == PHASE_2_MOVES
    assert state.get("current_direction") == "left", f"Expected left direction, got {state.get('current_direction')}"
    
    # Verify missions are regenerated for left direction
    phase2_left_missions = state["missions"]
    mission_inputs = [m["input"] for m in phase2_left_missions]
    assert "左" in mission_inputs  # Left direction, so should have 左
    
    # Simulate button release after direction toggle
    state["wait_for_all_buttons_release"] = False
    
    # Complete Phase 2 second cycle (left direction)
    remaining_missions = list(state["missions_set"])
    for idx, mission_input in enumerate(remaining_missions):
        # Get current missions from state
        current_missions = state["missions"]
        
        mission_idx = next((i for i, m in enumerate(current_missions) if m["input"] == mission_input), -1)
        if mission_idx == -1:
            continue
        
        state["mission_index"] = mission_idx
        state["mission"] = current_missions[mission_idx]["input"]
        
        # Simulate button release before each mission
        if idx > 0:
            state["wait_for_all_buttons_release"] = False
        
        state = check_and_update_mission(
            state, 
            current_missions,
            " + ", 
            mission_input,
            [],
            "なし",
            args
        )
    
    # After Phase 2 second cycle, should toggle back to right direction
    assert state.get("challenge_phase") == PHASE_2_MOVES
    assert state.get("current_direction") == "right", f"Expected right direction, got {state.get('current_direction')}"
    
    # Verify missions are regenerated for right direction again
    phase2_right_again_missions = state["missions"]
    mission_inputs = [m["input"] for m in phase2_right_again_missions]
    assert "右" in mission_inputs  # Right direction again
