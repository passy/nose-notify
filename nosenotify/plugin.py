# -*- coding: utf-8 -*-
"""
nosenotify.plugin
~~~~~~~~~~~~~~~~~

Nose plugin implementation.

:copyright: 2010, Pascal Hartig <phartig@rdrei.net>
:license: BSD, see doc/LICENSE for more details.
"""

import pynotify
import datetime
from nose.plugins import Plugin


class NotifyPlugin(Plugin):
    """Enable notify-osd notifications."""

    def begin(self):
        """Displays the start message."""

        self.start_time = datetime.datetime.now()
        self.start_notification = pynotify.Notification(
            "Starting tests",
            "Started at {0}".format(self.start_time.isoformat())
        ).show()

    def finalize(self, result=None):
        """Display success or failure message."""

        timedelta = datetime.datetime.now() - self.start_time

        if result.wasSuccessful():
            notification = pynotify.Notification(
                "Completed in {0}.{1} seconds".format(timedelta.seconds,
                                                      timedelta.microseconds),
                "Ran {0} tests ({1} skipped)".format(result.testsRun,
                                                     len(result.skipped)),
                "dialog-info"
            )
        else:
            notification = pynotify.Notification(
                "Test Failure",
                "{0} tests, {1} failure, {2} errors".format(
                    result.testsRun, len(result.failures), len(result.errors)),
                "dialog-warning"
            )

        notification.show()
