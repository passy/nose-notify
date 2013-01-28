# -*- coding: utf-8 -*-
"""
nose-notify
~~~~~~~~~~~

A nose plugin to display testsuite progress in the notify osd.


:copyright: 2010, Pascal Hartig <phartig@rdrei.net>
:license: BSD, see LICENSE for more details
"""

from setuptools import setup
from nosenotify import __version__


setup(
    name="nose-notify",
    version=__version__,
    author="Pascal Hartig",
    author_email="phartig@rdrei.de",
    description="A nose plugin to display testsuite progress "
    "in the notify osd",
    url="https://github.com/passy/nose-notify",
    packages=['nosenotify'],
    package_data={'nosenotify': ['images/*.png']},
    long_description=__doc__,
    requires=['nose (>=0.10)'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    entry_points={
        'nose.plugins.0.10': [
            'notify = nosenotify.plugin:NotifyPlugin'
        ]
    }
)
