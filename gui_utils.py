import ctypes
import tkinter

def init_tkinter(title, geometry, font, label_count):
    root = tkinter.Tk()
    root.title(title)
    root.geometry(geometry)
    labels = []
    for _ in range(label_count):
        label = tkinter.Label(root, text="", font=font)
        label.pack()
        labels.append(label)
    return root, labels

def do_topmost(root):
    # print("ウィンドウを最前面にします。")
    root.attributes("-topmost", True)
    root.update()

    # ALT + TAB の対象にする
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    GWL_EXSTYLE = -20
    WS_EX_TOOLWINDOW = 0x00000080
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, current_style & ~WS_EX_TOOLWINDOW)
    root.update()

def do_backmost(root):
    # print("ウィンドウを背面にします。")
    root.attributes("-topmost", False)
    root.lower()
    root.update()

    # ALT + TAB の対象外にする
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    GWL_EXSTYLE = -20
    WS_EX_TOOLWINDOW = 0x00000080
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, current_style | WS_EX_TOOLWINDOW)
    root.update()
