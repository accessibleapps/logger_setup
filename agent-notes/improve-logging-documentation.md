# Goal

Document the package's real application use and exception coverage.

# State

Documentation-only PR independently based on integrated master. Explain the existing API, thresholds, write mode, fatal dumps, descriptor lifetime, process-wide shutdown, and framework-owned paths and retention. No open PR's commits are inherited.

# Decisions and why

Document behavior established by master, rather than promising behavior that exists only in other open PRs. Omit the old stack's claims about UTF-8, transactional construction, repeat replacement and corrected exit cleanup; those are independent proposed fixes. Keep the usage and coverage documentation useful without requiring those PRs.

# Surprises

Explicit shutdown is not exported at package level and calls global logging.shutdown. sys.excepthook, executor/wx error handling and fatal dumps cover different paths.

# Next step

Read this PR's existing package/README metadata checks. No merge or release.
