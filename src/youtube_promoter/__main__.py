""" This acts as the applications main entry point.

When the application is installed using `python setup.py install/develop` the
application will be accessible by running `python -m template`.
"""
from youtube_promoter import cli

if __name__ == "__main__":
    cli.run()
