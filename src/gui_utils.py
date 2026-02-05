import ctypes
import tkinter

def init_tkinter(title, geometry, font, label_count, theme_colors=None):
    """
    Tkinterウィンドウを初期化する
    Initialize Tkinter window
    
    Args:
        title: ウィンドウタイトル / Window title
        geometry: ウィンドウサイズと位置 / Window size and position
        font: フォント設定 / Font settings
        label_count: ラベルの数 / Number of labels
        theme_colors: テーマカラー設定 (dict with bg_color, fg_color) / Theme color settings
    
    Returns:
        tuple: (root, labels)
    """
    root = tkinter.Tk()
    root.title(title)
    root.geometry(geometry)
    
    # テーマカラーを適用
    if theme_colors:
        root.config(bg=theme_colors.get('bg_color', 'SystemButtonFace'))
    
    labels = []
    for _ in range(label_count):
        label_config = {"text": "", "font": font}
        if theme_colors:
            label_config["bg"] = theme_colors.get('bg_color', 'SystemButtonFace')
            label_config["fg"] = theme_colors.get('fg_color', 'black')
        
        label = tkinter.Label(root, **label_config)
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
