import ctypes
import os
import time

from src.utils.resource_path import resource_path


# Constant values
IMAGE_ICON = 1
LR_LOADFROMFILE = 0x00000010 
"""
hexadecimal integer flag `0x00000010` such as `LR_LOADFROMFILE` 
Used when loading icons, cursors, or bitmaps from a disk file path via user32 APIs.

https://stackoverflow.com/questions/20995045/how-to-include-image-in-message-box-using-ctypes-in-python
"""

LR_DEFAULTSIZE = 0x00000040
"""
hexadecimal integer flag `0x00000040` such as `LR_DEFAULTSIZE`
Uses the width or height specified by the system metric values for cursors or icons, 
if the cxDesired or cyDesired values are set to zero. If this flag is not specified 
and cxDesired and cyDesired are set to zero, the function uses the actual resource size.

https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex
"""

WM_SETICON = 0x0080
"""
hexadecimal integer flag `0x0080` such as `WM_SETICON`
Associates a new large or small icon with a window. The system displays the large 
icon in the ALT+TAB dialog box, and the small icon in the window caption.

https://learn.microsoft.com/en-us/windows/win32/winmsg/wm-seticon
"""

# The type of icon to be set. This parameter can be one of the following values.
ICON_SMALL = 0
ICON_BIG = 1


def wait_for_hwnd(title, timeout=5.0, interval=0.01):
    """
    Repeatedly check for the HWND and proceed as soon as it exists.

    Args:
        tittle (str): The tittle of the window.

    Returns:
        int: hwnd value.
    """
    find_window = ctypes.windll.user32.FindWindowW
    deadline = time.monotonic() + timeout

    while time.monotonic() < deadline:
        hwnd = find_window(None, title)

        if hwnd:
            return hwnd

        time.sleep(interval)

    raise RuntimeError(f"No se encontró la ventana: {title}")


def set_window_icon(window):
    icon_path = os.path.abspath("dist/favicon.ico")
    hwnd = wait_for_hwnd("kort")
    
    with open(icon_path, "rb") as f:
        data = f.read()
    
    buffer = (ctypes.c_byte * len(data))(*data)
    icon = ctypes.windll.user32.CreateIconFromResourceEx(
        buffer, len(data), 1, 0x00030000, 0, 0, 0x0001
    )

    ctypes.windll.user32.SendMessageW(hwnd, 0x0080, 0, icon)
    ctypes.windll.user32.SendMessageW(hwnd, 0x0080, 1, icon)