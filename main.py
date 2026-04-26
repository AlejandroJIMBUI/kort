import ctypes
import sys
import os
import time
import webview

def set_icon(window):
    time.sleep(0.5)
    
    icon_path = os.path.abspath("dist/favicon.ico")
    hwnd = ctypes.windll.user32.FindWindowW(None, "kort")
    
    with open(icon_path, "rb") as f:
        data = f.read()
    
    buf = (ctypes.c_byte * len(data))(*data)
    icon = ctypes.windll.user32.CreateIconFromResourceEx(
        buf, len(data), 1, 0x00030000, 0, 0, 0x0001
    )

    ctypes.windll.user32.SendMessageW(hwnd, 0x0080, 0, icon)
    ctypes.windll.user32.SendMessageW(hwnd, 0x0080, 1, icon)

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.abspath(relative)

html_path = resource_path("dist/index.html")
window = webview.create_window("kort", f"file://{html_path}")
webview.start(set_icon, window)