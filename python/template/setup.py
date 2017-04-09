try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'author_email': 'my-email@example.com',
    'url': 'https://my_name.github.io/my_project'
    'download_url': 'https://github.com/my_name/my_project',
    'version': '0.1.0',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'my_project',
}

setup(**config)
