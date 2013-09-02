from fabric.api import local
from jinja2 import Environment, FileSystemLoader


template_env = Environment(loader=FileSystemLoader('.'))

# copy reveal.js assets from submodule to presentation
def prepare():
    local('cp -r reveal.js/css/* presentation/css/')
    local('cp -r reveal.js/js/* presentation/js/')
    local('cp -r reveal.js/lib/* presentation/lib/')
    local('cp -r reveal.js/plugin/* presentation/plugin/')

def build():
    prepare()
    template = template_env.get_template('source/index.html')
    rendered_template = template.render()
    with open('presentation/index.html', 'wb') as fh:
        fh.write(rendered_template)

def publish():
    local('ghp-import -p presentation')
