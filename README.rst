===========
nose-notify
===========

.. image:: https://api.travis-ci.org/passy/nose-notify.png
    :target: https://travis-ci.org/passy/nose-notify


Notify-OSD notifications for systems with libnotify support (e. g. Ubuntu)
on testsuite start and completion.

Usage
-----

Run nosetests with the ``--with-notify`` or set the environment variable
``NOSE_WITH_NOTIFYPLUGIN`` flag. Enjoy.

Options
~~~~~~~

Passing the ``--no-start-message`` flag skips the notification at the beginning
of your test run. This is useful in case your test suite passes really quickly.
Which it should.

Thanks
------

Thanks to Victor Ng and `nose-growl`_ for the inspiration.

.. _nose-growl: http://bitbucket.org/crankycoder/nosegrowl
