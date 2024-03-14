from wasteDetection.logger import logging
logging.info("welcome to my custom log")
from wasteDetection.exception import AppException
import sys
try:
    a=3/"d"
except Exception as e:
    raise AppException(e,sys)