from core.logger import Logger
from core.executor import Executor
from core.system import WindowsSystem


def main():

    logger = Logger()

    logger.info("P10 Automator started")

    if WindowsSystem.is_admin():
        logger.success(
            "Administrator privileges detected"
        )
    else:
        logger.warning(
            "Application is not running as Administrator"
        )

    executor = Executor(logger)

    logger.info("Core system initialized")

    logger.success(
        "P10 Automator is ready"
    )


if __name__ == "__main__":
    main()