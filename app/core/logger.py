from datetime import datetime
from pathlib import Path


class Logger:
    def __init__(self, log_directory="logs"):
        self.log_directory = Path(log_directory)
        self.log_directory.mkdir(parents=True, exist_ok=True)

        self.log_file = (
            self.log_directory
            / f"{datetime.now().strftime('%Y-%m-%d')}.log"
        )

    def _write(self, level, message):
        timestamp = datetime.now().strftime("%H:%M:%S")

        log_message = (
            f"[{timestamp}] [{level}] {message}"
        )

        print(log_message)

        with self.log_file.open(
            "a",
            encoding="utf-8"
        ) as file:
            file.write(log_message + "\n")

    def info(self, message):
        self._write("INFO", message)

    def success(self, message):
        self._write("SUCCESS", message)

    def warning(self, message):
        self._write("WARNING", message)

    def error(self, message):
        self._write("ERROR", message)