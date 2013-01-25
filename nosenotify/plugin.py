# -*- coding: utf-8 -*-
"""
nosenotify.plugin
~~~~~~~~~~~~~~~~~

Nose plugin implementation.

:copyright: 2010, Pascal Hartig <phartig@rdrei.net>
:license: BSD, see doc/LICENSE for more details.
"""

import datetime
from nose.plugins import Plugin

try:
    import pynotify
except ImportError:
    from nosenotify import adapters as pynotify


class NotifyPlugin(Plugin):
    """Enable notify-osd notifications."""

    def begin(self):
        """Optionaly displays the start message."""


        pynotify.init("nose-notify")
        self.start_time = datetime.datetime.now()

        if self.show_start_message:
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

    def options(self, parser, env):
        super(NotifyPlugin, self).options(parser, env)
        parser.add_option('--no-start-message',
                          action='store_false',
                          dest='show_start_message',
                          default=True)

    def configure(self, options, conf):
        super(NotifyPlugin, self).configure(options, conf)
        self.show_start_message = options.show_start_message
