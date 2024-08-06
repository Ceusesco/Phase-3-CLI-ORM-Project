import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def log_debug(message):
    """Logs a debug message."""
    logging.debug(message)

def log_error(message):
    """Logs an error message."""
    logging.error(message)
