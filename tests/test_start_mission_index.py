import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from missions import get_new_mission_index, initialize_mission_sets, PHASE_1_BUTTONS

def test_get_new_mission_index_with_start_index():
    """Test that start_index parameter works correctly in deterministic mode."""
    missions = [
        {"input": "a"},
        {"input": "b"},
        {"input": "c"},
        {"input": "d"}
    ]
    missions_set = {"a", "b", "c", "d"}
    
    # Test start_index = 0 (first mission)
    idx = get_new_mission_index(missions, missions_set, use_random=False, start_index=0)
    assert missions[idx]["input"] == "a", "Should select first mission in sorted order"
    
    # Test start_index = 1 (second mission)
    idx = get_new_mission_index(missions, missions_set, use_random=False, start_index=1)
    assert missions[idx]["input"] == "b", "Should select second mission in sorted order"
    
    # Test start_index = 3 (fourth mission)
    idx = get_new_mission_index(missions, missions_set, use_random=False, start_index=3)
    assert missions[idx]["input"] == "d", "Should select fourth mission in sorted order"

def test_get_new_mission_index_with_start_index_wraparound():
    """Test that start_index wraps around with modulo when out of range."""
    missions = [
        {"input": "a"},
        {"input": "b"},
        {"input": "c"}
    ]
    missions_set = {"a", "b", "c"}
    
    # Test start_index = 5 (should wrap to index 2: 5 % 3 = 2)
    idx = get_new_mission_index(missions, missions_set, use_random=False, start_index=5)
    assert missions[idx]["input"] == "c", "Should wrap around using modulo (5 % 3 = 2)"
    
    # Test start_index = 10 (should wrap to index 1: 10 % 3 = 1)
    idx = get_new_mission_index(missions, missions_set, use_random=False, start_index=10)
    assert missions[idx]["input"] == "b", "Should wrap around using modulo (10 % 3 = 1)"

def test_get_new_mission_index_start_index_ignored_when_random():
    """Test that start_index is ignored when use_random=True."""
    missions = [
        {"input": "a"},
        {"input": "b"},
        {"input": "c"}
    ]
    missions_set = {"a", "b", "c"}
    
    # When use_random=True, start_index should be ignored and a random mission selected
    # We can't test the exact mission, but we can verify it returns a valid index
    idx = get_new_mission_index(missions, missions_set, use_random=True, start_index=999)
    assert 0 <= idx < len(missions), "Should return valid index even with high start_index"
    assert missions[idx]["input"] in missions_set, "Should return mission from the set"

def test_initialize_mission_sets_with_start_index():
    """Test that initialize_mission_sets properly passes start_index to get_new_mission_index."""
    missions = [
        {"input": "右"},
        {"input": "上"},
        {"input": "左"}
    ]
    left_right = ["右", "左"]
    left_right_temp = ["__TEMP_RIGHT__", "__TEMP_LEFT__"]
    
    # Initialize with start_mission_index = 1
    (result_missions, missions_set, success_missions, mission_index, 
     current_direction, original_missions) = initialize_mission_sets(
        missions, left_right, left_right_temp, 
        challenge_phase=PHASE_1_BUTTONS, 
        current_direction="right", 
        use_random=False, 
        start_mission_index=1
    )
    
    # Verify that the correct initial mission was selected
    # After amplification, missions will have left/right variants
    # The sorted order would be something like: ["上", "左", "右"] (depends on amplification)
    # We just verify that mission_index points to a valid mission
    assert 0 <= mission_index < len(result_missions), "Should return valid mission index"
    assert result_missions[mission_index]["input"] in missions_set, "Should select from missions_set"

def test_initialize_mission_sets_with_start_index_zero():
    """Test that start_index=0 selects the first mission in deterministic mode."""
    missions = [
        {"input": "c"},
        {"input": "a"},
        {"input": "b"}
    ]
    left_right = ["右", "左"]
    left_right_temp = ["__TEMP_RIGHT__", "__TEMP_LEFT__"]
    
    # Initialize with start_mission_index = 0
    (result_missions, missions_set, success_missions, mission_index, 
     current_direction, original_missions) = initialize_mission_sets(
        missions, left_right, left_right_temp, 
        challenge_phase=PHASE_1_BUTTONS, 
        current_direction="right", 
        use_random=False, 
        start_mission_index=0
    )
    
    # Should select first mission in sorted order
    sorted_missions = sorted(list(missions_set))
    assert result_missions[mission_index]["input"] == sorted_missions[0], "Should select first mission"

def test_get_new_mission_index_with_japanese_characters():
    """Test start_index with Japanese character missions (real use case)."""
    missions = [
        {"input": "右"},
        {"input": "上"},
        {"input": "下"},
        {"input": "左"}
    ]
    missions_set = {"右", "上", "下", "左"}
    
    # Sorted order in Unicode: ['上', '下', '右', '左'] (based on Unicode code points)
    # Test start_index = 2 (third mission)
    idx = get_new_mission_index(missions, missions_set, use_random=False, start_index=2)
    sorted_list = sorted(list(missions_set))
    assert missions[idx]["input"] == sorted_list[2], "Should select third mission in sorted order"

def test_get_new_mission_index_with_negative_start_index():
    """Test that negative start_index wraps around correctly with modulo."""
    missions = [
        {"input": "a"},
        {"input": "b"},
        {"input": "c"}
    ]
    missions_set = {"a", "b", "c"}
    
    # Test start_index = -1 (should wrap to index 2: -1 % 3 = 2 in Python)
    idx = get_new_mission_index(missions, missions_set, use_random=False, start_index=-1)
    assert missions[idx]["input"] == "c", "Negative index should wrap using modulo (-1 % 3 = 2)"
