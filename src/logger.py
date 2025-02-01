import logging
import os
from datetime import datetime

LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)  

LOG_FILE = f"{datetime.now().strftime('%d-%m-%y')}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)  

logger = logging.getLogger(__name__) 
logger.setLevel(logging.INFO) 


file_handler = logging.FileHandler(LOG_PATH)
formatter = logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)


logger.info("Logging system initialized successfully.")
