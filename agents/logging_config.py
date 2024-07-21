import logging
import sys
from logging import StreamHandler
from logging.handlers import RotatingFileHandler


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all levels of log messages

    # Console Handler
    console_handler = StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)

    # File Handler
    file_handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=5)
    file_handler.setLevel(logging.INFO)
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    file_handler.setFormatter(file_format)

    # Adding handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)