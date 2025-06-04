from gui_utils import do_backmost, do_topmost, init_tkinter

def gui_init_tkinter(args):
    gui_label_count = 3
    return init_tkinter(args.title, args.geometry, (args.font_name, args.font_size), gui_label_count)

def update_display_with_mission(tkinter_root, labels, timer_id_dict, score, old_texts, lever_plus_pressed, mission, wait_for_all_release=None):
    text_lever_plus_pressed = f"{lever_plus_pressed}"
    if wait_for_all_release is not None and wait_for_all_release:
        text_lever_plus_pressed += "...SUCCESS!" # 「全ボタンを離してください」の文言を入れるかは検討中

    texts = [f"mission : {mission}", f"{text_lever_plus_pressed}", f"score : {score}"]
    if texts != old_texts:
        show_input(tkinter_root, labels, texts, timer_id_dict)
        old_texts = texts
    return old_texts

def show_input(root, label, text, timer):
    do_topmost(root)

    if isinstance(label, list) and isinstance(text, list):
        for l, t in zip(label, text):
            l.config(text=t)
    else:
        label.config(text=text)
    root.update()

    # 入力から指定秒数後にbackmost化する用
    if timer["id"] is not None:
        root.after_cancel(timer["id"])
    timer["id"] = root.after(1000, lambda: do_backmost(root))
