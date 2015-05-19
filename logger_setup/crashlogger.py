from future.builtins import object
import logging
import faulthandler

CRASHLOGGER_NAME = 'APPCRASH'

class StreamToLogger(object):
 """
 Fake file-like stream object that redirects writes to a logger instance.
 """
 def __init__(self, handler):
  self.handler = handler

 def fileno(self):
  return self.handler.stream.fileno()

def enable_crashlogger(error_handler):
 stream = StreamToLogger(error_handler)
 faulthandler.enable(stream)
