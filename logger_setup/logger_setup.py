import logging
import sys
from os.path import join
from os import getpid
from traceback import format_exception

MESSAGE_FORMAT = "%(levelname)s %(asctime)s %(name)s: %(message)s"

try:
 logger
except NameError:
 logger = logging.getLogger()
 
def create_handler(filename=None, level=logging.DEBUG, handler_class=logging.FileHandler, formatter=None):
 if filename is None:
  handler = handler_class()
 else:
  handler = handler_class(filename)
 handler.setLevel(level)
 handler.setFormatter(formatter)
 logger.addHandler(handler)
 return handler

def custom_excepthook(type, value, traceback):
 tb = format_exception(type, value, traceback)
 tb = "".join(tb)
 logger.error("An unhandled exception occurred.\n%s" % tb)
 sys.__excepthook__(type, value, traceback)


def setup_logging(console_level=logging.INFO, error_log=None, debug_log=None, message_format=MESSAGE_FORMAT, log_unhandled_exceptions=True):
 if log_unhandled_exceptions:
  sys.excepthook = custom_excepthook
 logger.setLevel(logging.DEBUG)
 formatter = logging.Formatter(message_format)
 if error_log:
  create_handler(error_log, logging.ERROR, formatter=formatter)
 if debug_log:
  create_handler(debug_log, logging.DEBUG, formatter=formatter)
 if console_level:
  console_handler = create_handler(level=console_level, handler_class=logging.StreamHandler, formatter=formatter)
 logger.getChild('logger_setup').info("Logging initialized. PID: %d" % getpid())
 return logger

def shutdown():
 logging.shutdown()
