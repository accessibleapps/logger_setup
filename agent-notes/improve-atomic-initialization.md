# Goal

Keep a failed logging initialization from installing partial handlers or replacing the exception hook.

# State

Construct and format handlers before attaching them or changing process logging state. Close constructed handlers when a later setup step fails. This PR is independently based on integrated master and contains no other open PR's commits.

# Decisions and why

The framework catches setup failures and continues. Leaving an error handler installed when opening the debug file fails previously made its basicConfig fallback a no-op. A failure now preserves pre-existing root handlers, root level and exception hook. Fatal handling is enabled only after handler construction succeeds. File opens may still create or truncate files; this change does not roll back their contents.

# Surprises

create_handler is an internal module helper, not exported by the package. Its callers now receive an unattached handler; setup_logging attaches only the completed set. No consumer call site changes are required.

# Next step

Read the existing package checks. The separate app_framework failure-reporting PR makes its fallback status accurate. No merge or release.
