import subprocess
from pathlib import Path


class Executor:

    def __init__(self, logger):
        self.logger = logger

    def run_executable(
        self,
        executable_path,
        args=None,
        wait=True
    ):
        executable = Path(executable_path)

        if not executable.exists():
            self.logger.error(
                f"File not found: {executable}"
            )
            return False

        if not executable.is_file():
            self.logger.error(
                f"Path is not a file: {executable}"
            )
            return False

        command = [str(executable)]

        if args:
            command.extend(args)

        self.logger.info(
            f"Starting: {executable.name}"
        )

        try:

            if wait:

                result = subprocess.run(
                    command,
                    check=False
                )

                if result.returncode == 0:

                    self.logger.success(
                        f"Process completed: {executable.name}"
                    )

                    return True

                self.logger.error(
                    f"Process failed: "
                    f"{executable.name} "
                    f"(code: {result.returncode})"
                )

                return False

            subprocess.Popen(command)

            self.logger.success(
                f"Process started: {executable.name}"
            )

            return True

        except Exception as error:

            self.logger.error(
                f"Execution error: {error}"
            )

            return False