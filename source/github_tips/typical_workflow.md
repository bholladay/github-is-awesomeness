{% extends "source/md.html" %}
{% block md %}

## Pull Request Workflow

This works well for internal groups.

1. Branch, branch, branch (even for a small change or fix)
1. Commit often
1. Push once tested (or earlier if you need help/collaboration)
1. `git push -u origin <branch_name>`
1. Create pull request
1. Tag for code review if ready and @mention reviewers
1. Tag "in progress" if not yet ready
1. Peer Review
1. Merge
1. Delete the branch

{% endblock %}
