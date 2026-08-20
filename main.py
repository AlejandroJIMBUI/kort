import ctypes
import sys
import os
import time
import webview

from src.utils.set_window_icon import set_window_icon
from src.utils.resource_path import resource_path

html_path = resource_path("dist/index.html")
window = webview.create_window("kort", f"file://{html_path}")
webview.start(set_window_icon, window)