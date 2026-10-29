import atexit
import faulthandler

_enabled = False


def enable_crashlogger(error_handler):
    global _enabled
    faulthandler.enable(error_handler.stream)
    _enabled = True


def disable_crashlogger():
    global _enabled
    if _enabled:
        faulthandler.disable()
        _enabled = False


# logging registers its shutdown before importing this module. Exit callbacks
# run in reverse order, so release the fault descriptor before logs are closed.
atexit.register(disable_crashlogger)
