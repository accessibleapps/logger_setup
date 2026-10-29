# Goal

Keep fatal traceback output attached to an open error-log stream through shutdown.

# State

Pass the existing error-handler stream directly to faulthandler. Remove the wrapper that only forwarded fileno. Package shutdown and an exit callback disable package-enabled fault handling before logging closes its files. This PR is independently based on integrated master and contains no UTF-8 PR commits.

# Decisions and why

faulthandler retains a file descriptor, not a logging handler. Its stream must stay open until fault handling is disabled. The exit callback runs before logging's earlier registered shutdown callback. Disabling is a no-op when this package has not enabled fault handling. Fatal dumps remain raw output rather than formatted log records.

# Surprises

The removed StreamToLogger never redirected log writes; its description was misleading.

# Next step

Read this PR's existing package checks. Subsequent setup/reconfiguration changes must retain the same file-lifetime ordering. No merge or release.
