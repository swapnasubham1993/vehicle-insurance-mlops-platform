#################################################################################
# Check the logging functionality from the src.logger package
# from src.logger import logging

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

# for i in range(50000):
#     logging.info(f"Log message {i} - Adding some content to increase file size...")

#################################################################################

# Check the custom exception handling from the src.exception package
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.error(e)
#     raise MyException(e, sys) from e

# try:
#     result = 10 / 0
# except Exception as e:
#     logging.error(e)
#     raise MyException(e, sys) from e