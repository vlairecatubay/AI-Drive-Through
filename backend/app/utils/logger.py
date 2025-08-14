import logging

def get_logger(name: str):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        fmt = logging.Formatter('[%(asctime)s] %(levelname)s %(name)s: %(message)s')
        ch.setFormatter(fmt)
        logger.addHandler(ch)
    return logger
