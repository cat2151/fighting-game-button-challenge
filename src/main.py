from configs import load_game_configuration
from gui import gui_init_tkinter, update_display_with_mission
from joystick import create_button_states, get_buttons_as_bitstring, setup_pygame_and_joystick, shutdown_pygame, should_skip_input_processing
from missions import check_and_update_mission, initialize_mission_sets, on_mission_start, get_move_name_for_input, PHASE_1_BUTTONS
from check_playing_game import check_playing_game_and_do_backmost, init_timer_for_check_playing_game
from toml_hot_reload import TomlFileTracker, get_tracked_toml_files

def main():
    (args, names, plus, lever_names, missions, none_word, alias_conf, no_count_names, moves) = load_game_configuration()
    (tkinter_root, labels) = gui_init_tkinter(args)
    joystick = setup_pygame_and_joystick()
    
    # Initialize TOML file tracker for hot reload
    toml_tracker = TomlFileTracker()
    toml_files = get_tracked_toml_files(args)
    toml_tracker.track_files(toml_files)
    print(f"Tracking {len(toml_files)} TOML files for hot reload")
    
    # Get challenge_phase from config, default to PHASE_1_BUTTONS if not set
    challenge_phase = getattr(args, 'challenge_phase', PHASE_1_BUTTONS)
    current_direction = "right"  # Default direction for phase 2
    use_random_mission = getattr(args, 'use_random_mission', True)  # Default to random if not set
    start_mission_index = getattr(args, 'start_mission_index', 0)  # Default to 0 if not set
    
    # Validate start_mission_index
    if not isinstance(start_mission_index, int) or start_mission_index < 0:
        print(f"Warning: start_mission_index must be a non-negative integer. Got: {start_mission_index}. Using default value 0.")
        start_mission_index = 0
    
    (missions, missions_set, success_missions, mission_index, current_direction, original_missions) = initialize_mission_sets(
        missions, args.left_right, args.left_right_temp, challenge_phase, current_direction, use_random_mission, start_mission_index
    )
    
    (timer_id_dict, clock, check_interval_msec, last_check_msec) = init_timer_for_check_playing_game(args)
    try:
        main_loop(tkinter_root, args, check_interval_msec, last_check_msec, joystick, names, plus, lever_names, 
                  missions, mission_index, missions_set, success_missions, labels, timer_id_dict, clock, 
                  none_word, alias_conf, no_count_names, moves, challenge_phase, current_direction, original_missions, toml_tracker)
    except KeyboardInterrupt:
        print("プログラムを終了します。")
    finally:
        shutdown_pygame()

def main_loop(tkinter_root, args, check_interval_msec, last_check_msec, joystick, names, plus, lever_names, missions, mission_index, missions_set, success_missions, labels, timer_id_dict, clock, none_word, alias_conf, no_count_names, moves, challenge_phase, current_direction, original_missions, toml_tracker):
    state = {
        "score": 0,
        "fail_count": 0,
        "old_texts": [],
        "wait_for_all_buttons_release": False,
        "mission": missions[mission_index]["input"],
        "is_first_input_detected": False,
        "initial_bitstring": None,
        "last_failed_input": None,
        "mission_index": mission_index,
        "missions_set": missions_set,
        "success_missions": success_missions,
        "current_mission_frame_count": 0,
        "last_mission_frame_count": 0,
        "prev_success_min_frame_count": 0,
        "prev_success_frame_counts": [],
        "prev_success_mode_frame_count": 0,
        "old_lever_plus_pressed": None,
        "is_backmost": False,
        "mission_start_time": None,
        "mission_times": [],
        "challenge_phase": challenge_phase,
        "current_direction": current_direction,
        "original_missions": original_missions,
        "missions": missions,
    }
    state = on_mission_start(state)
    print("start!")
    
    frame_count = 0
    hot_reload_check_interval = 60  # Check every 60 frames (1 second at 60fps)
    
    while True:
        last_check_msec = check_playing_game_and_do_backmost(tkinter_root, args, check_interval_msec, last_check_msec)

        # Hot reload check - every 60 frames
        frame_count += 1
        if frame_count >= hot_reload_check_interval:
            frame_count = 0
            if toml_tracker.check_for_changes():
                print("\n=== TOML file changes detected, reloading configuration ===")
                reload_success = reload_configuration_and_reset(
                    tkinter_root, args, joystick, toml_tracker
                )
                if reload_success:
                    # Get updated values after reload
                    args, names, plus, lever_names, missions, none_word, alias_conf, no_count_names, moves = reload_success
                    
                    # Reset to Phase 1, mission index 0
                    challenge_phase = PHASE_1_BUTTONS
                    current_direction = "right"
                    use_random_mission = getattr(args, 'use_random_mission', True)
                    
                    (missions, missions_set, success_missions, mission_index, current_direction, original_missions) = initialize_mission_sets(
                        missions, args.left_right, args.left_right_temp, challenge_phase, current_direction, use_random_mission, 0
                    )
                    
                    # Reset state to beginning
                    state = {
                        "score": 0,
                        "fail_count": 0,
                        "old_texts": [],
                        "wait_for_all_buttons_release": False,
                        "mission": missions[mission_index]["input"],
                        "is_first_input_detected": False,
                        "initial_bitstring": None,
                        "last_failed_input": None,
                        "mission_index": mission_index,
                        "missions_set": missions_set,
                        "success_missions": success_missions,
                        "current_mission_frame_count": 0,
                        "last_mission_frame_count": 0,
                        "prev_success_min_frame_count": 0,
                        "prev_success_frame_counts": [],
                        "prev_success_mode_frame_count": 0,
                        "old_lever_plus_pressed": None,
                        "is_backmost": False,
                        "mission_start_time": None,
                        "mission_times": [],
                        "challenge_phase": challenge_phase,
                        "current_direction": current_direction,
                        "original_missions": original_missions,
                        "missions": missions,
                    }
                    state = on_mission_start(state)
                    print("=== Configuration reloaded, restarting from Phase 1 ===\n")

        # Get current missions from state (may have been regenerated)
        missions = state["missions"]
        
        # input
        buttons_bits = get_buttons_as_bitstring(joystick)
        if state["initial_bitstring"] is None:
            state["initial_bitstring"] = buttons_bits
        lever_plus_pressed = create_button_states(names, plus, lever_names, joystick, buttons_bits)

        should_skip, state["is_first_input_detected"] = should_skip_input_processing(buttons_bits, state["initial_bitstring"], state["is_first_input_detected"])
        if not should_skip:
            # check & 状態更新
            state = check_and_update_mission(
                state, missions, plus, lever_plus_pressed, no_count_names, none_word, args)

        # display
        move_name = get_move_name_for_input(state["mission"], moves, plus)
        state["old_texts"] = update_display_with_mission(
            state, tkinter_root, labels, timer_id_dict, lever_plus_pressed, state["mission"],
            state["wait_for_all_buttons_release"], alias_conf, should_skip, none_word, args, move_name
        )
        tkinter_root.update_idletasks()
        tkinter_root.update()
        clock.tick(60) # 60fps


def reload_configuration_and_reset(tkinter_root, args, joystick, toml_tracker):
    """
    Reload all configuration from TOML files and reset tracking.
    
    Args:
        tkinter_root: Tkinter root window
        args: Current configuration args
        joystick: Pygame joystick object
        toml_tracker: TomlFileTracker instance
    
    Returns:
        Tuple of (args, names, plus, lever_names, missions, none_word, alias_conf, no_count_names, moves) 
        on success, or None on failure
    """
    try:
        from configs import load_game_configuration
        
        # Reload configuration
        (args, names, plus, lever_names, missions, none_word, alias_conf, no_count_names, moves) = load_game_configuration()
        
        # Update tracked files with new configuration
        toml_files = get_tracked_toml_files(args)
        toml_tracker.track_files(toml_files)
        
        return (args, names, plus, lever_names, missions, none_word, alias_conf, no_count_names, moves)
    except Exception as e:
        print(f"Error reloading configuration: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    main()
