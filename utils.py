import logging

logging.basicConfig(filename = "pipeline_errors.log", level = logging.ERROR)

def log_error(error_message):
    logging.error(error_message)
    print(f"Error logged: {error_message}")