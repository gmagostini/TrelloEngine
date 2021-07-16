#!/usr/bin/env python3
import logging
import colorlog

def init_logger(dunder_name, level = "INFO") -> logging.Logger:
    log_format = (
        '%(asctime)s - '
        '%(name)s - '
        '%(funcName)s - '
        '%(levelname)s - '
        '%(message)s'
    )
    bold_seq = '\033[1m'
    colorlog_format = (
        f'{bold_seq} '
        '%(log_color)s '
        f'{log_format}'
    )
    colorlog.basicConfig(format=colorlog_format)
    logger = logging.getLogger(dunder_name)




    if level == "DEBUG":
        logger.setLevel(logging.DEBUG)
        logger.propagate = True
    elif level == "ERROR":
        logger.setLevel(logging.ERROR)
        logger.propagate = True
    elif level == "INFO":
        logger.setLevel(logging.INFO)
        logger.propagate = True
    elif level == "CRITICAL":
        logger.setLevel(logging.CRITICAL)
        logger.propagate = False
    else:
        logger.setLevel(logging.CRITICAL)
        logger.propagate = False

    # Output full log
    fh = logging.FileHandler('app.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Output warning log
    fh = logging.FileHandler('app.warning.log')
    fh.setLevel(logging.WARNING)
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Output error log
    fh = logging.FileHandler('app.error.log')
    fh.setLevel(logging.ERROR)
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger


