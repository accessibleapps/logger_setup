# Goal

Write application log files as UTF-8 on every supported platform.

# State

File handlers explicitly request UTF-8. Console handlers and file write mode are unchanged. The existing package/configuration CI runs on this PR; it does not run application logging scenarios.

# Decisions and why

QRead, QFeed and QCast log externally supplied titles. Their content must not depend on the Windows locale's default encoding. Use FileHandler's existing encoding argument, available on the consumers' Python 3.8 baseline.

# Surprises

The existing helper's filename branch is the only file-handler construction site.

# Next step

Read the published PR's checks. Merge and release are outside this task.
