"""
Flask-CloudStorage

A simple Flask Extension (also standalone) library to upload and save files on the cloud.

Supported storage:

- AWS S3
- Google Storage
- Microsoft Azure
- Rackspace CloudFiles
- Local

"""

from setuptools import setup, find_packages


__NAME__ = "flask-CloudStorage"
__version__ = "0.2.0"
__author__ = "Mardix"
__license__ = "MIT"
__copyright__ = "2015"

setup(
    name=__NAME__,
    version=__version__,
    license=__license__,
    author=__author__,
    author_email='mardix@github.com',
    description="Flask-CloudStorage is a simple flask extension and standalone library to upload and save files on the cloud",
    long_description=__doc__,
    url='https://github.com/mardix/flask-cloudstorage/',
    download_url='http://github.com/mardix/flask-cloudstorage/tarball/master',
    py_modules=['flask_cloudstorage'],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "werkzeug==0.10.1",
        "apache-libcloud==0.17.0",
        "lockfile==0.10.2",
        "shortuuid==0.1"
    ],

    keywords=["flask", "s3", "aws", "cloudfiles", "storage", "azure", "google"],
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False
)

