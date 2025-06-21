import win32gui
import win32process
import psutil

def get_active_window_process_name():
    foreground = get_active_window_information()
    return foreground[1] if foreground else None

def get_active_window_information():
    hwnd = win32gui.GetForegroundWindow()
    return get_window_information(hwnd)

def get_window_information(hwnd):
    if not hwnd:
        return None

    window_title = win32gui.GetWindowText(hwnd)
    _thread_id, pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid <= 0:
        return None

    try:
        process_name = psutil.Process(pid).name()
    except psutil.NoSuchProcess:
        return None

    return window_title, process_name
