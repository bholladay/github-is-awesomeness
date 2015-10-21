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

  TODO: Add link to my whitespace example branch here.

  Only one real change.

{% endblock %}
