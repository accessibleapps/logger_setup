# Goal

Replace only this package's handlers on repeated logging setup.

# State

Rebuilt on master after #2, #3, #4, #6 and #7 merged. Keep the root logger and existing helper API. After the staged replacement succeeds, detach and close the handlers this package installed previously.

# Decisions and why

Builds on #4's staging: a failed setup closes its staged handlers and leaves installed handlers, root level and exception hook untouched, so this change needs no rollback code of its own. Fault handling uses #3's crashlogger state: a call that does not enable crash logging disables it before old streams close; a call that enables it has already retargeted it to the new stream. Track only owned handlers, preserve unrelated ones, and restore the previous exception hook when a repeat call or shutdown turns it off. Setup and shutdown run on the main thread.

# Surprises

The earlier version of this PR duplicated #3's fault-handler tracking and #4's rollback; both were removed when rebuilding on merged master. Opening a file may still truncate its contents before a later failure.

# Next step

Read the PR's package checks and merge. No release.
