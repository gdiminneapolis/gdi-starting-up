# Setting up a Python Project

A few ways to set up a [Python] project.

Before you dive in, **all** projects should have the same basic
things:

- [ ] git initialized, with a `.gitignore` file
- [ ] a project README file

See the [Starting Up Instructions](../README.md) for more info.

## Understand what sort of project it is

As with most languages, you have to know what the purpose of your new
project is, as that determines how you'll set it up.

Some of the possibilities for Python include:

- [Jupyter] notebook, used a lot in data analysis projects
- Web application, using [Django]
- Simple web program, using [Flask]
- Simple command line script, a tool you'll use repeatedly, but
  without setup and ceremony
- Desktop application, containing several modules and a GUI
- Reusable library, which can be part of several projects (maybe
  uploaded to [PyPi])
- other (??)

Also, there are environments such as [Anaconda] that can help set things
up. This guide is more for standalone Python projects.

The [Django] framework does all the projecxt setup for you, so you
should [follow their instructions][django-instructions].

## A basic guide to setting up a standalone Python project

(A sample template is in the [template](./template/) directory.)

Starting in your projects folder:

```bash
cd ~/Projects
git init my_cool_python_thing
cd my_cool_python_thing
```

Add a `.gitignore` file with the following lines:

```
*.pyc
__pycache__
```


Create the following folders:

- NAME - this will actually be the name of your program
- docs - where to put your documentation
- tests - where your project's tests will live and run

Create a `setup.py` file with the following content:

```python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
```

(Modify it accordingly, of course. It's okay if you don't know the
answers right away.)

Add empty `__init__.py` files to the `NAME` and `test` folder.

Add an empty `.keep` file to the `docs` folder.

Create a `README.md` file in the project root directory to explain to
users what your project is and how to use it.

Add all the files to git and create an initial commit:

```
git add --all --verbose
git commit -m 'Initial Commit'
```

In the end, your project structure will looking like this:

```
.git/
.gitignore
NAME/
  __init.py__
docs/
  .keep
setup.py
tests/
  __init.py__
```
