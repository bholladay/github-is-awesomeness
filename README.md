# Reveal.js Presentation

## Tech
It also uses [Jinja](http://jinja.pocoo.org/) in order to split up the
`index.html` into smaller sub-files (i.e. one file per slide) and it uses
[Fabric](http://docs.fabfile.org/) to render your Jinja templates and publish
them to Github.


## Installation

In order to work on this presentation, do the following:

    git clone git@github.com:bholladay/github-is-awesomeness.git
    cd github-is-awesomeness
    git submodule init
    git submodule update
    virtualenv -p `which python2.7`
    . bin/activate
    pip install -r requirements.txt

Now you should have all necessary Python software installed into a python virtual
environment.


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
