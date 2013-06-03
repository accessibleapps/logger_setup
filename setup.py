import sys
from setuptools import setup, find_packages

install_requires = []
if sys.version_info[0] < 3:
 install_requires.append('faulthandler')

__version__ = 0.1
__doc__ = """Collects log setup and handling from all projects into one central place."""
__author__ = 'Q'

setup(
 name = 'logger_setup',
 version = __version__,
 author = __author__,
 author_email = 'q@q-continuum.net',
 description = __doc__,
 package_dir = {'logger_setup': 'logger_setup'},
 packages = find_packages(),
 install_requires = install_requires,
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
  'Topic :: Software Development :: Libraries',
 ],
)
