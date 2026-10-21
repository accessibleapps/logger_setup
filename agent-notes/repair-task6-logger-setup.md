# Goal
Provide a relevant safe hosted gate for configuration-only logger_setup #1 without changing process logging policy.

# State
Fresh master 4078436b051f461f008169c68db6b06550a0aeb5; published PR #1 62aff7e412e603cc20d36e52109d2b52329ab510. No prior local PR branch exists; exact local fetched/published tips are retained separately under archive/task6-logger-setup-pr1-local and archive/task6-logger-setup-pr1-published, with a canonical archive as well. Canonical README.rst is dirty (captured working blob 0fe1f09b6f134629e957fd3f4943e6b20bee64dc) and preserved. This isolated candidate rebases only the historical pip Dependabot config onto current master with --no-update-refs.

# Decisions and why
Validate the actual Dependabot config against its vendored schema, build existing setup.py wheel/sdist, and check their metadata with Twine. setup.py reads the tracked README and discovers packages without importing/configuring logger_setup. These package/config gates match the PR's scope; no artificial runtime tests, logging handlers, sockets, faulthandler activation or process policy changes are introduced. One Python 3.12/Linux runner is bounded gate coverage, not support metadata. Current pinned actions use a read-only token/no persisted checkout credentials and bounded concurrent execution; monthly Actions maintenance supplements the original unchanged pip schedule.

# Surprises
There are no tracked test suites or full test authority. The current README's dirty user edits are excluded from the candidate and preserved in the canonical checkout.

# Next step
actionlint 1.7.12 passed; offline zizmor 1.31.1 reported no findings (one default suppression). Return full local diff/head for coordinator review before publication. No local full CI, model calls, security/settings/merge/release actions or old-description edits. Hosted schema/build/metadata results remain pending.
