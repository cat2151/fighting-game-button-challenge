from gui_utils import do_backmost, do_topmost, init_tkinter
from missions import PHASE_1_BUTTONS, PHASE_2_MOVES

def gui_init_tkinter(args):
    gui_label_count = 4
    return init_tkinter(args.title, args.geometry, (args.font_name, args.font_size), gui_label_count)

def update_display_with_mission(state, tkinter_root, labels, timer_id_dict, lever_plus_pressed, mission, wait_for_all_release, alias_conf, should_skip, none_word, args, move_name=""):
    if should_skip and none_word is not None:
        lever_plus_pressed = none_word
    if alias_conf is not None:
        mission = alias(mission, alias_conf)
        lever_plus_pressed = alias(lever_plus_pressed, alias_conf)
    text_lever_plus_pressed = f"{lever_plus_pressed}"
    if wait_for_all_release is not None and wait_for_all_release:
        text_lever_plus_pressed =  f"SUCCESS! {text_lever_plus_pressed} !SUCCESS"

    display_format = args.display_format
    
    # Handle move name display based on challenge phase
    challenge_phase = state.get('challenge_phase', PHASE_1_BUTTONS)
    displayed_move_name = ""
    
    if challenge_phase == PHASE_1_BUTTONS:
        # Phase 1: Don't display moves (仕様: ただしmovesは表示しない)
        displayed_move_name = ""
    elif challenge_phase == PHASE_2_MOVES:
        # Phase 2: Display moves with direction indicator
        current_direction = state.get('current_direction', 'right')
        direction_indicator = "（右向き）" if current_direction == "right" else "（左向き）"
        displayed_move_name = f"{direction_indicator}{move_name}" if move_name else ""

    format_dict = {
        'mission': mission,
        'move_name': displayed_move_name,
        'lever_plus_pressed': text_lever_plus_pressed,
        'score': state['score'],
        'fail_count': state['fail_count'],
        'current_mission_frame_count': state.get('current_mission_frame_count', ''),
        'last_mission_frame_count': state.get('last_mission_frame_count', ''),
        'prev_success_min_frame_count': state.get('prev_success_min_frame_count', ''),
        'prev_success_hist_center': state.get('prev_success_hist_center', ''),
    }

    texts = []
    for i in range(1, 5):
        key = f'label{i}'
        fmt = display_format.get(key, '') if isinstance(display_format, dict) else ''
        texts.append(fmt.format(**format_dict))

    # 背景色フラッシュ処理
    bg_color = None
    if state.get('bg_flash_frames', 0) > 0:
        bg_color = state['bg_flash_color']
        state['bg_flash_frames'] -= 1
    else:
        state['bg_flash_color'] = None
        state['bg_flash_frames'] = 0

    if texts != state['old_texts']:
        has_input = lever_plus_pressed != state["old_lever_plus_pressed"]
        show_input_frame_etc(tkinter_root, labels, texts, timer_id_dict, has_input, state, bg_color)
        state['old_texts'] = texts
    else:
        # text変化なしで、背景色だけ更新する用
        show_input_frame_etc(tkinter_root, labels, texts, timer_id_dict, False, state, bg_color)
    state["old_lever_plus_pressed"] = lever_plus_pressed
    return state['old_texts']

def show_input_frame_etc(root, label, text, timer, has_input, state, bg_color):
    if has_input:
        do_topmost(root)
        state['is_backmost'] = False

    if not state['is_backmost']:
        def set_label_text(label, text):
            label.config(text=text)

        if isinstance(label, list) and isinstance(text, list):
            for l, t in zip(label, text):
                set_label_text(l, t)
        else:
            set_label_text(label, text)

        if bg_color:
            root.config(bg=bg_color)
        else:
            root.config(bg='SystemButtonFace')

    # 入力から指定秒数後にbackmost化する用
    if has_input:
        if timer["id"] is not None:
            root.after_cancel(timer["id"])
        def to_backmost():
            do_backmost(root)
            state['is_backmost'] = True
        timer["id"] = root.after(1000, to_backmost)

def alias(text, alias_conf):
    if text is None:
        return text
    if not alias_conf or not alias_conf.get('use_alias', False):
        return text
    rules = alias_conf.get('alias', [])
    rules_sorted_by_len = sorted(rules, key=lambda r: len(r.get('from', '')), reverse=True)
    result = text
    for rule in rules_sorted_by_len:
        frm = rule.get('from')
        to = rule.get('to')
        if frm and to:
            result = result.replace(frm, to)
    return result
