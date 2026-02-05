from gui_utils import do_backmost, do_topmost, init_tkinter
from missions import PHASE_1_BUTTONS, PHASE_2_MOVES

def gui_init_tkinter(args):
    gui_label_count = 4
    theme_colors = getattr(args, 'theme_colors', None)
    return init_tkinter(args.title, args.geometry, (args.font_name, args.font_size), gui_label_count, theme_colors)

def update_display_with_mission(state, tkinter_root, labels, timer_id_dict, lever_plus_pressed, mission, wait_for_all_release, alias_conf, should_skip, none_word, args, move_name=""):
    if should_skip and none_word is not None:
        lever_plus_pressed = none_word
    if alias_conf is not None:
        mission = alias(mission, alias_conf)
        lever_plus_pressed = alias(lever_plus_pressed, alias_conf)
    text_lever_plus_pressed = f"{lever_plus_pressed}"
    if wait_for_all_release is not None and wait_for_all_release:
        text_lever_plus_pressed =  f"SUCCESS! {text_lever_plus_pressed} !SUCCESS"

    # Handle move name display based on challenge phase
    challenge_phase = state.get('challenge_phase', PHASE_1_BUTTONS)

    # Initialize direction_arrow for use in format_dict (used in phase2 only)
    direction_arrow = ""

    if challenge_phase == PHASE_1_BUTTONS:
        # Phase 1: Use phase1 display format, fallback to display_format for backward compatibility
        display_format = getattr(args, 'display_format_phase1', None) or getattr(args, 'display_format', {})
        # Phase 1: Don't display moves (仕様: ただしmovesは表示しない)
        displayed_move_name = ""
        displayed_mission = mission
    elif challenge_phase == PHASE_2_MOVES:
        # Phase 2: Use phase2 display format, fallback to display_format for backward compatibility
        display_format = getattr(args, 'display_format_phase2', None) or getattr(args, 'display_format', {})
        # Phase 2: Display only direction arrow, hide mission and move name
        current_direction = state.get('current_direction', 'right')
        direction_arrow = "→" if current_direction == "right" else "←"
        displayed_move_name = ""
        displayed_mission = ""  # Hide mission (button operation guide) in phase2
    else:
        # Unexpected phase value: fail fast to aid debugging, mirroring missions.initialize_mission_sets
        raise ValueError(
            f"Invalid challenge_phase: {challenge_phase!r}. "
            f"Expected {PHASE_1_BUTTONS!r} or {PHASE_2_MOVES!r}."
        )

    format_dict = {
        'mission': displayed_mission,
        'move_name': displayed_move_name,
        'direction_arrow': direction_arrow,
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
    # テーマカラーを取得
    theme_colors = getattr(args, 'theme_colors', None)
    bg_color = None
    if state.get('bg_flash_frames', 0) > 0:
        # フラッシュ中は設定された色を使用（テーマの成功/失敗色）
        bg_color = state['bg_flash_color']
        state['bg_flash_frames'] -= 1
    else:
        state['bg_flash_color'] = None
        state['bg_flash_frames'] = 0

    if texts != state['old_texts']:
        has_input = lever_plus_pressed != state["old_lever_plus_pressed"]
        show_input_frame_etc(tkinter_root, labels, texts, timer_id_dict, has_input, state, bg_color, theme_colors)
        state['old_texts'] = texts
    else:
        # text変化なしで、背景色だけ更新する用
        show_input_frame_etc(tkinter_root, labels, texts, timer_id_dict, False, state, bg_color, theme_colors)
    state["old_lever_plus_pressed"] = lever_plus_pressed
    return state['old_texts']

def show_input_frame_etc(root, label, text, timer, has_input, state, bg_color, theme_colors=None):
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
            # フラッシュ時はラベルの背景も同じ色にする
            if isinstance(label, list):
                for l in label:
                    l.config(bg=bg_color)
            else:
                label.config(bg=bg_color)
        else:
            # 通常時はテーマカラーを適用
            default_bg = theme_colors.get('bg_color', 'SystemButtonFace') if theme_colors else 'SystemButtonFace'
            default_fg = theme_colors.get('fg_color') if theme_colors else None
            root.config(bg=default_bg)
            if isinstance(label, list):
                for l in label:
                    if default_fg is not None:
                        l.config(bg=default_bg, fg=default_fg)
                    else:
                        l.config(bg=default_bg)
            else:
                if default_fg is not None:
                    label.config(bg=default_bg, fg=default_fg)
                else:
                    label.config(bg=default_bg)

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
