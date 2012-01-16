import logging
from os.path import join
from os import getpid

MESSAGE_FORMAT = "%(levelname)s %(asctime)s %(name)s: %(message)s"

try:
 logger
 formatter
except NameError:
 logger = logging.getLogger()
 formatter = logging.Formatter(MESSAGE_FORMAT)

def create_handler(filename=None, level=logging.DEBUG, handler_class=logging.FileHandler):
 if filename is None:
  handler = handler_class()
 else:
  handler = handler_class(filename)
 handler.setLevel(level)
 handler.setFormatter(formatter)
 logger.addHandler(handler)
 return handler

def setup_logging(console_level=logging.INFO, error_log=None, debug_log=None):
 logger.setLevel(logging.DEBUG)
 if error_log:
  create_handler(error_log, logging.ERROR)
 if debug_log:
  create_handler(debug_log, logging.DEBUG)
 if console:
  console_handler = create_handler(level=CONSOLE_LOGGING_LEVEL, handler_class=logging.StreamHandler)
 logger.getChild('logger_setup').info("Logging initialized. PID: %d" % getpid())
 return logger

def shutdown():
 logging.shutdown()
