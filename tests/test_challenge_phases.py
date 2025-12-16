import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from missions import (
    initialize_mission_sets, 
    generate_missions_for_direction, 
    toggle_direction_and_regenerate_missions,
    PHASE_1_BUTTONS,
    PHASE_2_MOVES
)


def test_initialize_mission_sets_phase1():
    """Test phase 1 (buttons) - should amplify missions with left/right variants"""
    missions = [
        {"input": "右上"},
        {"input": "上"},
    ]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    challenge_phase = PHASE_1_BUTTONS
    current_direction = "right"
    
    result_missions, missions_set, success_missions, mission_index, result_direction, original_missions = initialize_mission_sets(
        missions, left_right, left_right_temp, challenge_phase, current_direction
    )
    
    # Phase 1 should amplify missions (add left/right variants)
    assert len(result_missions) == 3  # 右上, 左上, 上 (上 doesn't get duplicated)
    mission_inputs = [m["input"] for m in result_missions]
    assert "右上" in mission_inputs
    assert "左上" in mission_inputs
    assert "上" in mission_inputs
    assert result_direction == "right"


def test_initialize_mission_sets_phase2_right():
    """Test phase 2 (moves) with right direction - should keep right-facing missions"""
    missions = [
        {"input": "右上"},
        {"input": "右 + 強"},
    ]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    challenge_phase = PHASE_2_MOVES
    current_direction = "right"
    
    result_missions, missions_set, success_missions, mission_index, result_direction, original_missions = initialize_mission_sets(
        missions, left_right, left_right_temp, challenge_phase, current_direction
    )
    
    # Phase 2 with right direction should keep missions as-is
    assert len(result_missions) == 2
    mission_inputs = [m["input"] for m in result_missions]
    assert "右上" in mission_inputs
    assert "右 + 強" in mission_inputs
    assert result_direction == "right"


def test_initialize_mission_sets_phase2_left():
    """Test phase 2 (moves) with left direction - should swap to left-facing missions"""
    missions = [
        {"input": "右上"},
        {"input": "右 + 強"},
    ]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    challenge_phase = PHASE_2_MOVES
    current_direction = "left"
    
    result_missions, missions_set, success_missions, mission_index, result_direction, original_missions = initialize_mission_sets(
        missions, left_right, left_right_temp, challenge_phase, current_direction
    )
    
    # Phase 2 with left direction should swap right/left
    assert len(result_missions) == 2
    mission_inputs = [m["input"] for m in result_missions]
    assert "左上" in mission_inputs
    assert "左 + 強" in mission_inputs
    assert result_direction == "left"


def test_generate_missions_for_direction_right():
    """Test generating missions for right direction"""
    missions = [
        {"input": "右上"},
        {"input": "右 + 強"},
        {"input": "上"},
    ]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    direction = "right"
    
    result = generate_missions_for_direction(missions, left_right, left_right_temp, direction)
    
    assert len(result) == 3
    mission_inputs = [m["input"] for m in result]
    assert "右上" in mission_inputs
    assert "右 + 強" in mission_inputs
    assert "上" in mission_inputs


def test_generate_missions_for_direction_left():
    """Test generating missions for left direction"""
    missions = [
        {"input": "右上"},
        {"input": "右 + 強"},
        {"input": "上"},
    ]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    direction = "left"
    
    result = generate_missions_for_direction(missions, left_right, left_right_temp, direction)
    
    assert len(result) == 3
    mission_inputs = [m["input"] for m in result]
    assert "左上" in mission_inputs
    assert "左 + 強" in mission_inputs
    assert "上" in mission_inputs


def test_toggle_direction_and_regenerate_missions():
    """Test toggling direction and regenerating missions"""
    original_missions = [
        {"input": "右上"},
        {"input": "右 + 強"},
    ]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    
    # Toggle from right to left
    new_missions, new_direction = toggle_direction_and_regenerate_missions(
        original_missions, left_right, left_right_temp, "right"
    )
    
    assert new_direction == "left"
    mission_inputs = [m["input"] for m in new_missions]
    assert "左上" in mission_inputs
    assert "左 + 強" in mission_inputs
    
    # Toggle from left back to right
    new_missions2, new_direction2 = toggle_direction_and_regenerate_missions(
        original_missions, left_right, left_right_temp, "left"
    )
    
    assert new_direction2 == "right"
    mission_inputs2 = [m["input"] for m in new_missions2]
    assert "右上" in mission_inputs2
    assert "右 + 強" in mission_inputs2
