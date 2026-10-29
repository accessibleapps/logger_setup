logger_setup: Logging configuration used by accessible apps
===========================================================

This repository contains a collection of logging functions used mainly by applications from
`accessible apps <http://getaccessibleapps.com>`_.

While you are more than welcome to include this module standalone, it was meant specifically for use with continuum projects and might be considered somewhat uncompromising otherwise.

Features
--------

* A CrashLogger to handle unplanned application crashes
* Initialization of debug and error logs
* Optionally logs all unhandled tracebacks for later analysis
* Support for remote logging to a syslog server

Usage
-----

Call setup_logging during application startup on the main thread::

    import logging
    from logger_setup import setup_logging

    setup_logging(error_log="errors.log", debug_log="debug.log")
    logger = logging.getLogger(__name__)
    logger.info("Application started")

The function returns Python's root logger and sets its level to DEBUG.
Application and library loggers that propagate to the root use its handlers.
Importing the package does not install handlers or replace sys.excepthook.

``error_log`` receives WARNING and higher, despite its name. ``debug_log``
receives DEBUG and higher. Both filenames are optional, open in write mode,
and require existing parent directories. Opening a file replaces previous
contents, even if a later setup step fails; file contents are not rolled back.

The console handler writes to stderr at INFO by default. Disable it with
``console_level=None``. A packaged application that discards stderr also
discards that console output; configure an error file for retained diagnostics.

``remote_address=(host, port)`` enables the standard SysLogHandler, with an
ERROR threshold by default. Supply ``application_name`` and
``application_version`` alongside the address. Configuring this handler does
not confirm remote message delivery.

Exception coverage and lifetime
-------------------------------

``log_unhandled_exceptions=True`` installs sys.excepthook to log uncaught
main-thread Python exceptions and then call sys.__excepthook__. The delegate
is resolved when the exception occurs. app_framework's later debug bootstrap
uses this to install its debugger delegate.

With ``error_log`` and ``log_crashes=True``, faulthandler writes fatal traceback
dumps directly to the error-log file descriptor. These are raw dumps without
the normal logging format. This diagnoses crashes; it does not recover from
them. Keep the stream open while faulthandler uses it, and disable or retarget
fault handling before independently closing or replacing the stream.

The package does not install a thread exception hook or handle every GUI
callback. app_framework logs its executor and wx CallAfter failures separately.
RepeatingTimer also catches and logs callback exceptions. Those mechanisms
are distinct from sys.excepthook and fatal traceback dumps.

Configure logging before starting worker threads. Explicit process logging
shutdown is available as ``logger_setup.logger_setup.shutdown()``; it invokes
Python's process-wide logging.shutdown, which closes unrelated handlers too.
It is not a private per-package cleanup API.

Use through app_framework
-------------------------

app_framework supplies identity and paths under its application data directory,
preserves the preceding error log as ``errors.log.old``, enables debug logging
for source/debug runs, and passes the application's optional remote address.
Those policies belong to the framework; logger_setup does not rotate or retain
logs. The standard application startup path configures logging once.
