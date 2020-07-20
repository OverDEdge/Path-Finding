try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Visualization program of different path finding algorithms. A* search',
    'author': 'Niklas Moberg',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': '----',
    'version': '0.1',
    'install_requires': ['pygame'],
    'packages': ['path_finding'],
    'scripts': [],
    'name': 'PathFinding'
}


setup(**config)
