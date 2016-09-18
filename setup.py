try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A text-based Role Playing Game.',
    'author': 'Engima',
    'url': 'https://github.com/engima424242/RPG/blob/master/textbasedrpgtest.py',
    'download_url': 'https://github.com/enigma424242/RPG.git',
    'author_email': 'auxiliary42@gmail.com',
    'version': '0.03',
    'install_requires': ['nose'],
    'packages': ['RPG'],
    'scripts': [],
    'name': 'Into the Shadows'
} 
