# Reveal.js Template 

This repository can be used to kickstart [Reveal.js](http://lab.hakim.se/reveal-js/) 
presentations and host them on [Github Pages](http://pages.github.com/).

It also uses [Jinja](http://jinja.pocoo.org/) in order to split up the 
`index.html` into smaller sub-files (i.e. one file per slide) and it uses
[Fabric](http://docs.fabfile.org/) to render your Jinja templates and publish
them to Github.


## Installation

In order to start a new presentation, do the following:

    git clone git@github.com:alanorth/reveal-template.git
    cd reveal-template
    git submodule init
    git submodule update
    mkvirtualenv -p `which python2.7` reveal-template
    workon reveal-template
    pip install -r requirements.txt

Now you should have all necessary Python software installed into a python virtual
environment called `reveal-template`.

**Note:** This assumes you've installed python-virtualenvwrapper in your distro
and configured your shell to use it.  Perhaps see the [Arch Linux wiki](https://wiki.archlinux.org/index.php/Python_VirtualEnv) for help.
Otherwise, you can use the vanilla python-virtualenv, but it's just a bit more
manual.


## Usage

In order to build your presentation you will create and manipulate files in 
the `source` folder.

You can trigger a build via

    fab build

Now make your changes in the source directory. When you are done, review your
changes:

    fab build
    xdg-open presentation/index.html

If all looks good, publish to Github:

    fab publish


## LICENSE

This repository contains the code of [Reveal.js](https://github.com/hakimel/reveal.js)
which is licensed under the [MIT license](https://github.com/hakimel/reveal.js/blob/master/LICENSE).
