import logging
from datetime import datetime
from pathlib import Path

# Logging configuration
BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = f"{BASE_DIR}/logs"
C_MONTH = datetime.now().strftime("%b-%Y")

if not Path(LOGS_DIR).exists():
    Path.mkdir(LOGS_DIR)

class MicroFmt(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

# For terminal or console
st_handler = logging.StreamHandler()
st_handler.setFormatter(MicroFmt("[%(levelname)s](%(name)s) %(asctime)s \t\t- %(message)s"))
LOGGER.addHandler(st_handler)

# For log files
f_handler = logging.FileHandler(f"{LOGS_DIR}/{C_MONTH}.log")
f_handler.setFormatter(MicroFmt("[%(levelname)s](%(name)s) %(asctime)s \t\t- %(message)s"))
LOGGER.addHandler(f_handler)