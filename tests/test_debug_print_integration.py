import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from utils import set_debug_print_enabled, debug_print, read_toml, update_args_by_toml
from missions import amplify_missions_left_right, generate_missions_for_direction, extract_mission_elapsed_time
import argparse
import io
from contextlib import redirect_stdout


def test_debug_print_integration_with_missions():
    """Test that debug_print configuration affects missions.py output"""
    missions = [{"input": "右 + 強"}]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    
    # Test 1: With debug_print disabled (default)
    set_debug_print_enabled(False)
    f = io.StringIO()
    with redirect_stdout(f):
        result = amplify_missions_left_right(missions, left_right, left_right_temp)
    output = f.getvalue()
    
    assert len(result) == 2  # Function still works
    assert "[amplify_missions_left_right]" not in output  # No debug output
    
    # Test 2: With debug_print enabled
    set_debug_print_enabled(True)
    f = io.StringIO()
    with redirect_stdout(f):
        result = amplify_missions_left_right(missions, left_right, left_right_temp)
    output = f.getvalue()
    
    assert len(result) == 2  # Function still works
    assert "[amplify_missions_left_right]" in output  # Debug output present
    
    # Reset
    set_debug_print_enabled(False)


def test_debug_print_integration_with_generate_missions():
    """Test that debug_print configuration affects generate_missions_for_direction output"""
    missions = [{"input": "右 + 強"}]
    left_right = ["右", "左"]
    left_right_temp = ["みぎ", "ひだり"]
    
    # Test 1: With debug_print disabled
    set_debug_print_enabled(False)
    f = io.StringIO()
    with redirect_stdout(f):
        result = generate_missions_for_direction(missions, left_right, left_right_temp, "right")
    output = f.getvalue()
    
    assert len(result) == 1  # Function still works
    assert "[generate_missions_for_direction]" not in output  # No debug output
    
    # Test 2: With debug_print enabled
    set_debug_print_enabled(True)
    f = io.StringIO()
    with redirect_stdout(f):
        result = generate_missions_for_direction(missions, left_right, left_right_temp, "right")
    output = f.getvalue()
    
    assert len(result) == 1  # Function still works
    assert "[generate_missions_for_direction]" in output  # Debug output present
    
    # Reset
    set_debug_print_enabled(False)


def test_debug_print_integration_with_mission_elapsed_time():
    """Test that debug_print configuration affects extract_mission_elapsed_time output"""
    import time
    state = {
        "mission_start_time": time.time(),
        "mission_times": []
    }
    
    # Test 1: With debug_print disabled
    set_debug_print_enabled(False)
    f = io.StringIO()
    with redirect_stdout(f):
        result_state = extract_mission_elapsed_time(state)
    output = f.getvalue()
    
    assert len(result_state["mission_times"]) == 1  # Function still works
    assert "[DEBUG] mission_times:" not in output  # No debug output
    
    # Test 2: With debug_print enabled
    state = {
        "mission_start_time": time.time(),
        "mission_times": []
    }
    set_debug_print_enabled(True)
    f = io.StringIO()
    with redirect_stdout(f):
        result_state = extract_mission_elapsed_time(state)
    output = f.getvalue()
    
    assert len(result_state["mission_times"]) == 1  # Function still works
    assert "[DEBUG] mission_times:" in output  # Debug output present
    
    # Reset
    set_debug_print_enabled(False)


def test_config_loading_sets_debug_print_flag():
    """Test that loading button_challenge.toml correctly sets the debug_print flag"""
    # Load the actual config file
    args = argparse.Namespace()
    args.config_filename = os.path.join(
        os.path.dirname(__file__), 
        '../config/button_challenge.toml'
    )
    
    # Update args from config (this should set the global debug_print flag)
    args = update_args_by_toml(args)
    
    # Verify config was loaded
    assert hasattr(args, 'debug_print')
    
    # Since default is false, global flag should be false
    from utils import is_debug_print_enabled
    assert args.debug_print == False
    # The flag should be set by update_args_by_toml
    assert is_debug_print_enabled() == args.debug_print
