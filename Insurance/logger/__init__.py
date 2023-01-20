from datetime import datetime
import logging
import os

#Create a Directory where to store log files

LOG_DIR = "INSURANCE_LOG"
CURRENT_TIMESTAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
LOG_FILE_NAME = f"log_{CURRENT_TIMESTAMP}.log"

os.makedirs(LOG_DIR,exist_ok=True)

# Define log file path
LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format="[%(asctime)s:%(levelname)s]:%(message)s",
level= logging.DEBUG,
)