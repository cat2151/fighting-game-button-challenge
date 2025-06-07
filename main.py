from configs import load_game_configuration
from gui import gui_init_tkinter, update_display_with_mission
from joystick import create_button_states, get_buttons_as_bitstring, setup_pygame_and_joystick, shutdown_pygame
from missions import check_and_update_mission, initialize_mission_sets
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
    score = 0
    old_texts = []
    wait_for_all_buttons_release = False
    print("start!")
    while True:
        last_check_msec = check_playing_game_and_do_backmost(tkinter_root, args, check_interval_msec, last_check_msec)

        # input
        buttons_bits = get_buttons_as_bitstring(joystick)
        lever_plus_pressed = create_button_states(names, plus, lever_names, joystick, buttons_bits)

        # check
        (mission, mission_index, missions_set, success_missions, score, wait_for_all_buttons_release) = check_and_update_mission(
            plus, missions, mission_index, lever_plus_pressed, missions_set, success_missions, score, wait_for_all_buttons_release, no_count_names, none_word)

        # display
        old_texts = update_display_with_mission(
            tkinter_root, labels, timer_id_dict, score, old_texts, lever_plus_pressed, mission, wait_for_all_buttons_release, alias_conf)
        tkinter_root.update_idletasks()
        tkinter_root.update()

        clock.tick(60) # 60fps

if __name__ == "__main__":
    main()
