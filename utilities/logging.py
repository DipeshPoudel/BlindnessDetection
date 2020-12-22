import os
import logging

try:
    if not os.path.exists("log"):
        os.makedirs("log")
    # Create and configure logger
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.basicConfig(filename="log/log.log", filemode='w')
    # Creating an object
    logger = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
except Exception as e:
    raise e
