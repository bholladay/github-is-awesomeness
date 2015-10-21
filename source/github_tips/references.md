{% extends "source/md.html" %}
{% block md %}

## GitHub provides references

1. GitHub automatically creates links in comments when using a git commit SHA-1.
2. Reference issues and PR's with the hashtag `#<number>` in comments.
3. Cross-references external repos with `<user>/<repo>#<issue_number>`.
4. Click on the line number to make a custom link to a specific line number.  Appends to the URL `#L<line_number>`.

{% endblock %}
