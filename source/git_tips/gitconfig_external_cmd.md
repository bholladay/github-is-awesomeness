{% extends "source/md.html" %}
{% block md %}

## gitconfig external command

```bash
git config --global alias.visual '!gitk'
```

_Note_: This command just makes an entry in `~/.gitconfig

Without `--global` the config would get added to the repo `.git/config`.

{% endblock %}
