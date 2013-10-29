import logging
import logging.handlers
import sys
import os
import traceback

import crashlogger

MESSAGE_FORMAT = "%(levelname)s %(name)s thread %(thread)d %(module)s.%(funcName)s %(asctime)s:\n%(message)s"




try:
 logger
except NameError:
 logger = logging.getLogger()
 
def create_handler(filename=None, level=logging.DEBUG, handler_class=logging.FileHandler, handler_mode='w', formatter=None):
 if filename is None:
  handler = handler_class()
 else:
  handler = handler_class(filename, mode=handler_mode)
 handler.setLevel(level)
 handler.setFormatter(formatter)
 logger.addHandler(handler)
 return handler

def custom_excepthook(type, value, thrown_traceback):
 tb = traceback.format_exception(type, value, thrown_traceback)
 tb = "".join(tb)
 logger.error("An unhandled exception occurred.\n%s" % tb)
 sys.__excepthook__(type, value, thrown_traceback)

def setup_logging(console_level=logging.INFO, error_log=None, debug_log=None, message_format=MESSAGE_FORMAT, log_unhandled_exceptions=True, log_crashes=True, application_name=None, remote_address=None):
 if log_unhandled_exceptions:
  sys.excepthook = custom_excepthook
 logger.setLevel(logging.DEBUG)
 formatter = logging.Formatter(message_format)
 if error_log:
  error_handler = create_handler(error_log, logging.WARNING, formatter=formatter)
 if debug_log:
  create_handler(debug_log, logging.DEBUG, formatter=formatter)
 if console_level:
  console_handler = create_handler(level=console_level, handler_class=logging.StreamHandler, formatter=formatter)
 if error_log and log_crashes:
  crashlogger.enable_crashlogger(error_handler)
 remote_format = "1 %(asctime)s - " + application_name + " - - %(name)s thread %(thread)d %(module)s.%(funcName)s:\n%(message)s"
 remote_date_format = '%Y-%m-%dT%H:%M:%SZ'
 if remote_address:
  remote_handler = logging.handlers.SysLogHandler(address=remote_address)
  remote_handler.setLevel(logging.WARNING)
  remote_formatter = logging.Formatter(remote_format, datefmt=remote_date_format)
  remote_handler.setFormatter(remote_formatter)
  logger.addHandler(remote_handler)
 logger.info("Logging initialized. PID: %d" % os.getpid())
 return logger

def shutdown():
 logging.shutdown()
