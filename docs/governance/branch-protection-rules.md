# Branch Protection Rules — Structural Governance

Purpose: Protect `main` (and optionally `release/*`) with enforceable, repeatable controls using GitHub Rulesets.

Scope:
- Default branch: `main`
- Optional release branches: `refs/heads/release/*`

Recommended protections (Rulesets-backed):
- Require PRs (no direct updates to protected refs)
- Require CODEOWNERS review when relevant
- Require 1 approving review
- Dismiss stale approvals on push
- Require review thread resolution
- Require status checks (CI/lint/format)
- Require signed commits
- Require linear history
- Block force pushes
- Block branch deletion (unless explicitly bypassed)

Example Ruleset payload (matches GitHub REST Rulesets schema):
```json
{
  "name": "Default Branch Protection",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "include": ["refs/heads/main"],
      "exclude": []
    }
  },
  "rules": [
    {
      "type": "pull_request",
      "parameters": {
        "allowed_merge_methods": ["squash", "rebase"],
        "dismiss_stale_reviews_on_push": true,
        "require_code_owner_review": true,
        "require_last_push_approval": true,
        "required_approving_review_count": 1,
        "required_review_thread_resolution": true
      }
    },
    {
      "type": "required_status_checks",
      "parameters": {
        "required_status_checks": [
          { "context": "ci" },
          { "context": "lint" },
          { "context": "format" }
        ],
        "strict_required_status_checks_policy": true
      }
    },
    { "type": "required_signatures" },
    { "type": "required_linear_history" },
    { "type": "non_fast_forward" },
    { "type": "deletion" }
  ]
}
```

Notes:
- Replace status check contexts with your real workflow check names.
- If you later need bypass rules (owner/admin only), add `bypass_actors` per GitHub schema.

Definition of Done:
- Ruleset applied to `main`
- CODEOWNERS enforced
- Required checks configured and passing

References:
- [REST API endpoints for rules - GitHub Docs](https://docs.github.com/rest/repos/rules)
