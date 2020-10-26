from setuptools import setup, find_packages
from os import path

setup_file_location = path.abspath(path.dirname(__file__))
with open(path.join(setup_file_location, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='youtube-promoter', # Change here
    version='0.0.1',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ljlabs/youtube-promoter',
    author=[
        'Kyle Jordaan',
        'Liam Doult',
    ],
    author_email='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='Youtube Promotion',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.5, <4',
    install_requires=[
        "twython==3.8.2",
        "CouchDB==1.2",
        "click"
    ],
    extras_require={
        'dev': ['check-manifest'],
        'tests': [
            "pytest",
            "pytest-cov",
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/ljlabs/youtube-promoter/issues',
        'Source': 'https://github.com/ljlabs/youtube-promoter',
    },
)
