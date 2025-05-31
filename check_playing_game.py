import pygame
from get_window_info import get_active_window_process_name
from gui import do_backmost

def init_timer_for_check_playing_game(args):
    timer_id_dict = {"id": None}
    clock = pygame.time.Clock()
    check_interval_msec = int(args.backmost_mode["check_interval_sec"] * 1000)
    last_check_msec = pygame.time.get_ticks()
    return timer_id_dict, clock, check_interval_msec, last_check_msec

def check_playing_game_and_do_backmost(root, args, check_interval_msec, last_check_msec):
    current_msec = pygame.time.get_ticks()
    if current_msec - last_check_msec >= check_interval_msec:
        if is_playing_game(args):
            do_backmost_and_wait(root, args)
        last_check_msec = current_msec
    return last_check_msec

def is_playing_game(args):
    active_process = get_active_window_process_name()
    process_names = args.backmost_mode["process_names"]
    return active_process in process_names

def do_backmost_and_wait(root, args):
    do_backmost(root)
    while is_playing_game(args):
        pygame.time.wait(10000)
