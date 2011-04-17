===========
nose-notify
===========

Notify-OSD notifications on Ubuntu systems on testsuite start and completions.


Usage
-----

Run nosetests with the ``--with-notify`` flag. Enjoy.

Options
~~~~~~~

Passing the ``--no-start-message`` flag skips the notification at the beginning
of your test run. This is useful in case your test suite passes really quickly.

Thanks
------

Thanks to Victor Ng and `nose-growl`_ for the inspiration.

.. _nose-growl: http://bitbucket.org/crankycoder/nosegrowl
