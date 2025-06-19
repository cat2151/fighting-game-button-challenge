from gui_utils import do_backmost, do_topmost, init_tkinter

def gui_init_tkinter(args):
    gui_label_count = 3
    return init_tkinter(args.title, args.geometry, (args.font_name, args.font_size), gui_label_count)

def update_display_with_mission(tkinter_root, labels, timer_id_dict, score, fail_count, old_texts, lever_plus_pressed, mission, wait_for_all_release=None, alias_conf=None, should_skip=False, none_word=None):
    if should_skip and none_word is not None:
        lever_plus_pressed = none_word
    if alias_conf is not None:
        mission = alias(mission, alias_conf)
        lever_plus_pressed = alias(lever_plus_pressed, alias_conf)
    text_lever_plus_pressed = f"{lever_plus_pressed}"
    if wait_for_all_release is not None and wait_for_all_release:
        text_lever_plus_pressed += "...SUCCESS!" # 「全ボタンを離してください」の文言を入れるかは検討中

    texts = [f"mission : {mission}", f"{text_lever_plus_pressed}", f"score : {score}  fail : {fail_count}"]
    if texts != old_texts:
        show_input(tkinter_root, labels, texts, timer_id_dict)
        old_texts = texts
    return old_texts

def show_input(root, label, text, timer):
    do_topmost(root)

    def set_label_text(label, text):
        label.config(text=text)

    if isinstance(label, list) and isinstance(text, list):
        for l, t in zip(label, text):
            set_label_text(l, t)
    else:
        set_label_text(label, text)
    root.update()

    # 入力から指定秒数後にbackmost化する用
    if timer["id"] is not None:
        root.after_cancel(timer["id"])
    timer["id"] = root.after(1000, lambda: do_backmost(root))

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
