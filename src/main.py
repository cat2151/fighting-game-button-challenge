from configs import load_game_configuration
from gui import gui_init_tkinter, update_display_with_mission
from joystick import create_button_states, get_buttons_as_bitstring, setup_pygame_and_joystick, shutdown_pygame, should_skip_input_processing
from missions import check_and_update_mission, initialize_mission_sets, on_mission_start
from check_playing_game import check_playing_game_and_do_backmost, init_timer_for_check_playing_game

def main():
    (args, names, plus, lever_names, missions, none_word, alias_conf, no_count_names) = load_game_configuration()
    (tkinter_root, labels) = gui_init_tkinter(args)
    joystick = setup_pygame_and_joystick()
    (missions, missions_set, success_missions, mission_index) = initialize_mission_sets(missions, args.left_right, args.left_right_temp)
    (timer_id_dict, clock, check_interval_msec, last_check_msec) = init_timer_for_check_playing_game(args)
    try:
        main_loop(tkinter_root, args, check_interval_msec, last_check_msec, joystick, names, plus, lever_names, missions, mission_index, missions_set, success_missions, labels, timer_id_dict, clock, none_word, alias_conf, no_count_names)
    except KeyboardInterrupt:
        print("プログラムを終了します。")
    finally:
        shutdown_pygame()

def main_loop(tkinter_root, args, check_interval_msec, last_check_msec, joystick, names, plus, lever_names, missions, mission_index, missions_set, success_missions, labels, timer_id_dict, clock, none_word, alias_conf, no_count_names):
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
    }
    state = on_mission_start(state)
    print("start!")
    while True:
        last_check_msec = check_playing_game_and_do_backmost(tkinter_root, args, check_interval_msec, last_check_msec)

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
        state["old_texts"] = update_display_with_mission(
            state, tkinter_root, labels, timer_id_dict, lever_plus_pressed, state["mission"],
            state["wait_for_all_buttons_release"], alias_conf, should_skip, none_word, args
        )
        tkinter_root.update_idletasks()
        tkinter_root.update()
        clock.tick(60) # 60fps

if __name__ == "__main__":
    main()
