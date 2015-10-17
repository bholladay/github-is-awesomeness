from fabric.api import local
from jinja2 import Environment, FileSystemLoader


template_env = Environment(loader=FileSystemLoader('.'))


# copy reveal.js assets from submodule to presentation
def prepare():
    local('mkdir -p presentation/css && \
          cp -r reveal.js/css/* presentation/css/')
    local('mkdir -p presentation/js && \
          cp -r reveal.js/js/* presentation/js/')
    local('mkdir -p presentation/lib && \
          cp -r reveal.js/lib/* presentation/lib/')
    local('mkdir -p presentation/plugin && \
          cp -r reveal.js/plugin/* presentation/plugin/')
    local('mkdir -p presentation/images && \
          cp -r source/images/* presentation/images/')


def build():
    prepare()
    template = template_env.get_template('source/index.html')
    rendered_template = template.render()
    with open('presentation/index.html', 'wb') as fh:
        fh.write(rendered_template)


def publish():
    local('ghp-import -p presentation')
