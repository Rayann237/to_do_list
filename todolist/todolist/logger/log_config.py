import logging

def setup_logger():
    # Logger pour debug
    debug_logger = logging.getLogger("debug_logger")
    debug_logger.setLevel(logging.DEBUG)
    debug_fh = logging.FileHandler("debug.log")
    debug_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    debug_fh.setFormatter(debug_format)
    debug_logger.addHandler(debug_fh)

    # Logger pour erreurs
    error_logger = logging.getLogger("error_logger")
    error_logger.setLevel(logging.ERROR)
    error_fh = logging.FileHandler("error.log")
    error_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    error_fh.setFormatter(error_format)
    error_logger.addHandler(error_fh)

setup_logger()