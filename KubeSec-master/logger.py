import logging
from datetime import datetime

def create_logger(script_name):
	logger = logging.getLogger('logs')
	logger.setLevel(logging.DEBUG)

	fileName = f"./logs/{script_name}_on_{datetime.now().strftime('%m-%d-%Y@%H:%M:%S')}.log"
	handler = logging.FileHandler(fileName, mode = 'w')
	formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

	handler.setFormatter(formatter)
	logger.addHandler(handler)		
