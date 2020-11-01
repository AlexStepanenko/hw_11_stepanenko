import logging


class Logger:
    def __init__(self):
        self.formatter = logging.Formatter(logging.BASIC_FORMAT)

    def setup_logger(self, name, log_file, level=logging.INFO):
        handler = logging.FileHandler(log_file)
        handler.setFormatter(self.formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger
