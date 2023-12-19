import logging
import colorlog


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    # Create a formatter
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
