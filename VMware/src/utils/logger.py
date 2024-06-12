import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO)
    logging.info("Logger setup complete")