import logging
from datetime import datetime
import os

LOG_DIR = "housing_log"
time_stamp = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
file_name = f"log_{time_stamp}.log"

os.makedirs(LOG_DIR)

file_path = os.path.join(LOG_DIR,file_name)

logging.basicConfig(filename=file_path,filemode='w',format='[%(sctime)s] %(name)s %(levelname)s %(message)s', level=logging.info)
