from gui_utils import do_backmost, do_topmost, init_tkinter

def gui_init_tkinter(args):
    gui_label_count = 3
    return init_tkinter(args.title, args.geometry, (args.font_name, args.font_size), gui_label_count)

def update_display_with_mission(state, tkinter_root, labels, timer_id_dict, lever_plus_pressed, mission, wait_for_all_release, alias_conf, should_skip, none_word, args):
    if should_skip and none_word is not None:
        lever_plus_pressed = none_word
    if alias_conf is not None:
        mission = alias(mission, alias_conf)
        lever_plus_pressed = alias(lever_plus_pressed, alias_conf)
    text_lever_plus_pressed = f"{lever_plus_pressed}"
    if wait_for_all_release is not None and wait_for_all_release:
        text_lever_plus_pressed =  f"SUCCESS! {text_lever_plus_pressed} !SUCCESS"

    display_format = args.display_format

    format_dict = {
        'mission': mission,
        'lever_plus_pressed': text_lever_plus_pressed,
        'score': state['score'],
        'fail_count': state['fail_count'],
        'current_mission_frame_count': state.get('current_mission_frame_count', ''),
        'last_mission_frame_count': state.get('last_mission_frame_count', ''),
        'prev_success_min_frame_count': state.get('prev_success_min_frame_count', ''),
        'prev_success_hist_center': state.get('prev_success_hist_center', ''),
    }

    texts = []
    for i in range(1, 4):
        key = f'label{i}'
        fmt = display_format.get(key, '') if isinstance(display_format, dict) else ''
        texts.append(fmt.format(**format_dict))

    if texts != state['old_texts']:
        has_input = lever_plus_pressed != state["old_lever_plus_pressed"]
        show_input_frame_etc(tkinter_root, labels, texts, timer_id_dict, has_input, state)
        state['old_texts'] = texts
    state["old_lever_plus_pressed"] = lever_plus_pressed
    return state['old_texts']

def show_input_frame_etc(root, label, text, timer, has_input, state):
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
