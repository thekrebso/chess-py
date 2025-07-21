import logging

DEFAULT_LOGGING_LEVEL = logging.INFO


class Logger:
    def __init__(self, logging_level: int = DEFAULT_LOGGING_LEVEL):
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] %(message)s",
            level=logging_level
        )
        self.logger = logging.getLogger(__name__)

        self.levels = [logging.DEBUG, logging.INFO]
        self.current_level_index = self.levels.index(logging_level)
        self.logger.setLevel(self.levels[self.current_level_index])

    def set_level(self, level_index: int):
        self.current_level_index = level_index % len(self.levels)
        self.logger.setLevel(self.levels[self.current_level_index])
        self.logger.info(
            f"Logging level set to {logging.getLevelName(self.levels[self.current_level_index])}")

    def toggle_level(self):
        self.set_level(self.current_level_index + 1)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)
