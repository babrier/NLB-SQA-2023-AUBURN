import logging
from datetime import datetime

def create_logger(script_name):
	logger = logging.getLogger('logs')
	logger.setLevel(logging.DEBUG)

	fileName = f"./KubeSec-master/logs/{script_name}_on_{datetime.now().strftime('%m-%d-%Y@%H:%M:%S')}.log"

	fileName_Readme = f"./logs/README.md"
	fileName_Readme_Workflows = f"./KubeSec-master/logs/README.md"

	try:
		handler = logging.FileHandler(fileName_Readme_Workflows, mode = 'w')

	except FileNotFoundError:
		handler = logging.FileHandler(fileName_Readme, mode= 'w')

	formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

	handler.setFormatter(formatter)
	logger.addHandler(handler)		
