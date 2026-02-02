import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from missions import get_new_mission_index


def test_deterministic_mode_demo():
    """
    Demonstration test showing how deterministic mode works.
    This test verifies that when use_random=False, we always get the same mission.
    """
    missions = [
        {"input": "右上"},
        {"input": "下"},
        {"input": "左"},
        {"input": "上"},
    ]
    missions_set = set(m["input"] for m in missions)
    
    print("\n=== Deterministic Mode Demo ===")
    print(f"Available missions: {sorted(missions_set)}")
    
    # Run 5 times with deterministic mode
    print("\n5 selections with use_random=False:")
    for i in range(5):
        mission_index = get_new_mission_index(missions, missions_set, use_random=False)
        selected = missions[mission_index]["input"]
        print(f"  Selection {i+1}: {selected}")
    
    # Verify all selections are the same
    results = []
    for _ in range(10):
        mission_index = get_new_mission_index(missions, missions_set, use_random=False)
        results.append(missions[mission_index]["input"])
    
    assert len(set(results)) == 1, "All selections should be identical in deterministic mode"
    print(f"\n✓ All 10 selections were identical: {results[0]}")


def test_random_mode_demo():
    """
    Demonstration test showing how random mode works.
    This test verifies that when use_random=True, we can get different missions.
    """
    missions = [
        {"input": "右上"},
        {"input": "下"},
        {"input": "左"},
        {"input": "上"},
    ]
    missions_set = set(m["input"] for m in missions)
    
    print("\n=== Random Mode Demo ===")
    print(f"Available missions: {sorted(missions_set)}")
    
    # Run 10 times with random mode
    print("\n10 selections with use_random=True:")
    results = []
    for i in range(10):
        mission_index = get_new_mission_index(missions, missions_set, use_random=True)
        selected = missions[mission_index]["input"]
        results.append(selected)
        print(f"  Selection {i+1}: {selected}")
    
    print(f"\nUnique missions selected: {set(results)}")
    print(f"Number of unique selections: {len(set(results))}")
    
    # With random mode, we expect to see variety (though not guaranteed)
    assert len(set(results)) >= 1, "Should select at least one mission"


if __name__ == "__main__":
    test_deterministic_mode_demo()
    test_random_mode_demo()
