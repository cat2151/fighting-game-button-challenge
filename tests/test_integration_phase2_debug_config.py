import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from missions import initialize_mission_sets, PHASE_1_BUTTONS, PHASE_2_MOVES
from utils import read_toml


def test_debug_phase2_config_file_exists():
    """Test that the debug phase 2 config file exists and is valid"""
    config_path = os.path.join(
        os.path.dirname(__file__), 
        '../config/button_challenge_debug_phase2.toml'
    )
    
    # Verify file exists
    assert os.path.exists(config_path), "Debug phase 2 config file should exist"
    
    # Read the config file
    toml_data = read_toml(config_path)
    
    # Verify challenge_phase key exists
    assert 'challenge_phase' in toml_data
    
    # Verify it's set to phase 2
    assert toml_data['challenge_phase'] == PHASE_2_MOVES
    
    # Verify title mentions DEBUG
    assert 'title' in toml_data
    assert 'debug' in toml_data['title'].lower()


def test_integration_phase2_start_from_config():
    """Integration test: Verify entire flow when starting from phase 2"""
    # This simulates the main() function flow when using the debug config
    config_path = os.path.join(
        os.path.dirname(__file__), 
        '../config/button_challenge_debug_phase2.toml'
    )
    
    # Load configuration
    toml_data = read_toml(config_path)
    challenge_phase = toml_data['challenge_phase']
    
    # Verify we're starting from phase 2
    assert challenge_phase == PHASE_2_MOVES
    
    # Load mission data (using same missions as the main config)
    mission_toml_path = os.path.join(
        os.path.dirname(__file__), 
        '../config/mission.toml'
    )
    mission_data = read_toml(mission_toml_path)
    missions = mission_data.get('missions', [])
    left_right = mission_data.get('left_right', ["右", "左"])
    left_right_temp = mission_data.get('left_right_temp', ["みぎ", "ひだり"])
    
    # Initialize mission sets with phase 2
    current_direction = "right"
    (result_missions, missions_set, success_missions, mission_index, 
     result_direction, original_missions) = initialize_mission_sets(
        missions, left_right, left_right_temp, challenge_phase, current_direction
    )
    
    # Verify phase 2 initialization characteristics
    assert len(result_missions) == len(missions), "Phase 2 should not amplify missions"
    assert result_direction == "right", "Should start with right direction"
    assert len(original_missions) == len(missions), "Original missions should be preserved"
    
    # Verify missions were not amplified (phase 2 behavior vs phase 1)
    # Phase 1 would have created left/right variants, phase 2 does not
    mission_inputs = [m["input"] for m in result_missions]
    
    # Count how many unique inputs we have
    # In phase 2, this should equal the original count
    # In phase 1, this would be greater due to left/right variants
    assert len(set(mission_inputs)) == len(missions), "Phase 2 should have exact mission count"


def test_both_configs_are_valid():
    """Test that both main and debug configs are valid"""
    main_config_path = os.path.join(
        os.path.dirname(__file__), 
        '../config/button_challenge.toml'
    )
    debug_config_path = os.path.join(
        os.path.dirname(__file__), 
        '../config/button_challenge_debug_phase2.toml'
    )
    
    # Both should exist
    assert os.path.exists(main_config_path)
    assert os.path.exists(debug_config_path)
    
    # Both should have valid challenge_phase values
    main_data = read_toml(main_config_path)
    debug_data = read_toml(debug_config_path)
    
    assert main_data['challenge_phase'] in [PHASE_1_BUTTONS, PHASE_2_MOVES]
    assert debug_data['challenge_phase'] in [PHASE_1_BUTTONS, PHASE_2_MOVES]
    
    # Main should be phase 1 (default), debug should be phase 2
    assert main_data['challenge_phase'] == PHASE_1_BUTTONS
    assert debug_data['challenge_phase'] == PHASE_2_MOVES
