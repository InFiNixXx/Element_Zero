#Error

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
        # 'description': 'My Project',
        'author': 'Sauronil Das',
        'url': 'URL to get it at',
        'download_url': 'where to download it',
        'author_email': 'sauronildas10@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'Dummy_Project',

        ]

setup(**config)
