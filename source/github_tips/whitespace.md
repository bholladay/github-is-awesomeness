{% extends "source/md.html" %}
{% block md %}

## Whitespace options

### Git

git can ignore whitespace in a diff:

```bash
git diff -w
```

### Github

Add `?w=1` to any diff URL and GitHub will strip the whitespace.

[Original](https://github.com/bholladay/github-is-awesomeness/pull/3) vs [whitespace ignored with `?w=1`](https://github.com/bholladay/github-is-awesomeness/pull/3?w=1)

{% endblock %}
