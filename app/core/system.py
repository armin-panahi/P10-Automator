import ctypes
import os
from pathlib import Path


class WindowsSystem:

    @staticmethod
    def is_admin():
        try:
            return bool(
                ctypes.windll.shell32.IsUserAnAdmin()
            )
        except Exception:
            return False

    @staticmethod
    def file_exists(path):
        return Path(path).exists()

    @staticmethod
    def directory_exists(path):
        return Path(path).is_dir()

    @staticmethod
    def get_windows_directory():
        return os.environ.get(
            "WINDIR",
            "C:\\Windows"
        )