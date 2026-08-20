import os
import sys

def resource_path(relative):
    """
    Get the absolute path to a resource, compatible with PyInstaller.

    Args:
        relative_path (str): The relative path to the resource.

    Returns:
        str: The absolute path to the resource.
    """
    
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    
    return os.path.abspath(relative)