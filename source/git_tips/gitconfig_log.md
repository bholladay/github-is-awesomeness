{% extends "source/md.html" %}
{% block md %}

## gitconfig tree visualization

```gitconfig
[alias]
# ...
    l = log --graph --pretty=format:'%C(yellow)%h%C(cyan)%d%Creset %s %C(white)- %aN %ar, %ai%Creset'
```

![git l](images/git_l.jpg)

_Hint_: You can see the git node tree with branches.

{% endblock %}
