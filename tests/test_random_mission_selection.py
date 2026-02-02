import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from missions import get_new_mission_index, initialize_mission_sets, PHASE_1_BUTTONS


def test_get_new_mission_index_random():
    """Test that random mission selection can pick different missions"""
    missions = [
        {"input": "上"},
        {"input": "下"},
        {"input": "左"},
        {"input": "右"},
    ]
    missions_set = set(m["input"] for m in missions)
    
    # Run multiple times to increase likelihood of getting different results
    # Using 100 iterations to make the probability of false negatives negligible
    results = set()
    for _ in range(100):
        mission_index = get_new_mission_index(missions, missions_set, use_random=True)
        assert 0 <= mission_index < len(missions)
        results.add(missions[mission_index]["input"])
    
    # With random=True, we should get different missions (extremely high probability with 100 iterations)
    # Probability of picking only one mission in 100 tries from 4 options = (1/4)^100 ≈ 0
    assert len(results) > 1


def test_get_new_mission_index_deterministic():
    """Test that deterministic mission selection always picks the same mission"""
    missions = [
        {"input": "下"},
        {"input": "右"},
        {"input": "上"},
        {"input": "左"},
    ]
    missions_set = set(m["input"] for m in missions)
    
    # Run multiple times - should always get the same result
    results = set()
    for _ in range(10):
        mission_index = get_new_mission_index(missions, missions_set, use_random=False)
        assert 0 <= mission_index < len(missions)
        results.add(missions[mission_index]["input"])
    
    # With random=False, should always pick the same mission (sorted first)
    assert len(results) == 1
    # The sorted first mission should be "上" (comes first in Japanese sorting)
    assert results == {"上"}


def test_get_new_mission_index_deterministic_picks_sorted_first():
    """Test that deterministic selection picks the alphabetically first mission"""
    missions = [
        {"input": "C"},
        {"input": "A"},
        {"input": "B"},
    ]
    missions_set = set(m["input"] for m in missions)
    
    mission_index = get_new_mission_index(missions, missions_set, use_random=False)
    
    # Should pick "A" (first alphabetically) consistently
    selected_mission = missions[mission_index]["input"]
    assert selected_mission == "A"
    
    # Verify it's always "A" by running multiple times
    for _ in range(5):
        mission_index = get_new_mission_index(missions, missions_set, use_random=False)
        assert missions[mission_index]["input"] == "A"


def test_initialize_mission_sets_with_random():
    """Test initialize_mission_sets with random=True"""
    missions = [
        {"input": "右上"},
        {"input": "上"},
    ]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    
    result_missions, missions_set, success_missions, mission_index, result_direction, original_missions = initialize_mission_sets(
        missions, left_right, left_right_temp, PHASE_1_BUTTONS, "right", use_random=True
    )
    
    # Should return a valid mission index
    assert 0 <= mission_index < len(result_missions)


def test_initialize_mission_sets_with_deterministic():
    """Test initialize_mission_sets with random=False - should be consistent"""
    missions = [
        {"input": "右上"},
        {"input": "上"},
    ]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    
    # Run multiple times - should always get the same mission_index
    results = set()
    for _ in range(5):
        result_missions, missions_set, success_missions, mission_index, result_direction, original_missions = initialize_mission_sets(
            missions, left_right, left_right_temp, PHASE_1_BUTTONS, "right", use_random=False
        )
        results.add(mission_index)
    
    # Should always return the same mission index
    assert len(results) == 1


def test_get_new_mission_index_with_single_mission():
    """Test that both random and deterministic work with a single mission"""
    missions = [{"input": "上"}]
    missions_set = set(m["input"] for m in missions)
    
    # Both should return index 0 for a single mission
    random_index = get_new_mission_index(missions, missions_set, use_random=True)
    deterministic_index = get_new_mission_index(missions, missions_set, use_random=False)
    
    assert random_index == 0
    assert deterministic_index == 0
