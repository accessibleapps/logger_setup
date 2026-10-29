# Goal

Make remote log timestamps ending in Z represent UTC.

# State

Set only the syslog formatter's converter to time.gmtime. This PR is independently based on integrated master. Local formatting, remote transport and application settings remain unchanged.

# Decisions and why

logging.Formatter defaults to local time. Its existing converter setting provides UTC without changing any global formatter behavior or requiring another open PR.

# Surprises

No inspected application manifest enabled remote logging. This correction does not establish server receipt.

# Next step

Read the corrected PR's existing package checks. No merge or release.
