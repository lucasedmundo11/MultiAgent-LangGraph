# Python imports
import logging


def setup_logging():
    """
    Sets up the logging configuration for the application.
    
    This function configures the logging to output messages to both a file named 'app.log'
    and the console. The log level is set to DEBUG, and the log format includes the timestamp,
    logger name, log level, and the log message.
    """
    logging.basicConfig(
        level=logging.DEBUG,  # Set the log level to DEBUG
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log message format
        handlers=[
            logging.FileHandler("app.log"),  # Log messages to a file named 'app.log'
            logging.StreamHandler()  # Also log messages to the console
        ]
    )