import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from missions import initialize_mission_sets, PHASE_1_BUTTONS, PHASE_2_MOVES
from utils import read_toml


def test_phase2_config_in_button_challenge_toml():
    """Test that challenge_phase can be set to '2_moves' in button_challenge.toml"""
    config_path = os.path.join(
        os.path.dirname(__file__), 
        '../config/button_challenge.toml'
    )
    
    # Read the config file
    toml_data = read_toml(config_path)
    
    # Verify challenge_phase key exists
    assert 'challenge_phase' in toml_data
    
    # Verify the value is valid (either "1_buttons" or "2_moves")
    assert toml_data['challenge_phase'] in [PHASE_1_BUTTONS, PHASE_2_MOVES]


def test_initialize_mission_sets_with_phase2_config():
    """Test that initialize_mission_sets works correctly when phase is set to PHASE_2_MOVES"""
    missions = [
        {"input": "右 + 強"},
        {"input": "右上"},
    ]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    challenge_phase = PHASE_2_MOVES  # Simulating config value "2_moves"
    current_direction = "right"
    
    result_missions, missions_set, success_missions, mission_index, result_direction, original_missions = initialize_mission_sets(
        missions, left_right, left_right_temp, challenge_phase, current_direction
    )
    
    # Phase 2 should NOT amplify missions - should keep exactly the same number
    assert len(result_missions) == 2
    
    # Should generate missions for right direction (no swap)
    mission_inputs = [m["input"] for m in result_missions]
    assert "右 + 強" in mission_inputs
    assert "右上" in mission_inputs
    
    # Direction should remain right
    assert result_direction == "right"
    
    # Original missions should be preserved for direction toggling
    assert len(original_missions) == 2


def test_initialize_mission_sets_with_phase2_left_direction():
    """Test that initialize_mission_sets works correctly with phase 2 and left direction"""
    missions = [
        {"input": "右 + 強"},
        {"input": "右上"},
    ]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    challenge_phase = PHASE_2_MOVES
    current_direction = "left"  # Starting with left direction
    
    result_missions, missions_set, success_missions, mission_index, result_direction, original_missions = initialize_mission_sets(
        missions, left_right, left_right_temp, challenge_phase, current_direction
    )
    
    # Phase 2 should NOT amplify missions
    assert len(result_missions) == 2
    
    # Should generate missions for left direction (swapped)
    mission_inputs = [m["input"] for m in result_missions]
    assert "左 + 強" in mission_inputs
    assert "左上" in mission_inputs
    
    # Direction should be left
    assert result_direction == "left"


def test_phase2_start_config_flow():
    """Test the full flow of starting with phase 2 from configuration"""
    # This simulates what happens in main.py when challenge_phase = "2_moves"
    missions = [
        {"input": "右 + 強"},
        {"input": "下 + 弱"},
    ]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    
    # Simulate loading "2_moves" from config
    challenge_phase = PHASE_2_MOVES
    current_direction = "right"
    
    # This is what happens in main() function
    (missions_result, missions_set, success_missions, mission_index, 
     current_direction, original_missions) = initialize_mission_sets(
        missions, left_right, left_right_temp, challenge_phase, current_direction
    )
    
    # Verify phase 2 initialization
    assert len(missions_result) == 2
    assert len(missions_set) == 2
    assert len(success_missions) == 0
    assert mission_index >= 0
    assert current_direction == "right"
    
    # Verify missions are not amplified (phase 2 behavior)
    mission_inputs = [m["input"] for m in missions_result]
    assert "右 + 強" in mission_inputs
    assert "下 + 弱" in mission_inputs
    # Should NOT have left variants
    assert "左 + 強" not in mission_inputs
