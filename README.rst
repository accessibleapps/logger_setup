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
