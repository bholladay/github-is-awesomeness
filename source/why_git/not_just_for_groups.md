{% extends "source/md.html" %}
{% block md %}

## Not just for groups
- You can save the state of any project as often as you like.
- You can search over the comment associated with a changeset.

```shell
git log --grep=word
```

- You can search over the actual changes. Use the pickaxe.

```shell
git log -S <whatever> --source --all
```

- Easy to set up on any project, so why not?

```shell
git init
```

{% endblock %}
