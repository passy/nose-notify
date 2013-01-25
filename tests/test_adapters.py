import os
from unittest import TestCase

from mock import patch
from nose.tools import istest

from nosenotify.adapters import get_icon, init, Notification


class HelpersTest(TestCase):
    @istest
    def gets_an_info_icon(self):
        icon = get_icon('dialog-info')

        self.assertTrue(os.path.isfile(icon))

    @istest
    def gets_a_warning_icon(self):
        icon = get_icon('dialog-warning')

        self.assertTrue(os.path.isfile(icon))

    @istest
    def differentiates_between_info_and_warning(self):
        info = get_icon('dialog-info')
        warning = get_icon('dialog-warning')

        self.assertNotEqual(info, warning)

    @istest
    def inits_pynotify(self):
        init('some message')


class NotificationTest(TestCase):
    @istest
    @patch('subprocess.call')
    @patch('nosenotify.adapters.get_icon')
    def shows_a_notification_with_icon(self, get_icon, call):
        get_icon.return_value = 'some-icon.png'

        notification = Notification('some title', 'some body', 'some-icon')
        notification.show()

        call.assert_called_with(['notify-send', '--icon="some-icon.png"',
                                 'some title', 'some body'])

    @istest
    @patch('subprocess.call')
    @patch('nosenotify.adapters.get_icon')
    def shows_a_notification_without_icon(self, get_icon, call):
        notification = Notification('some title', 'some body')
        notification.show()

        call.assert_called_with(['notify-send', 'some title', 'some body'])
        self.assertFalse(get_icon.called)

    @istest
    @patch('subprocess.call')
    @patch('nosenotify.adapters.get_icon')
    def doesnt_trigger_if_not_shown(self, get_icon, call):
        Notification('some title', 'some body')

        self.assertFalse(call.called)
        self.assertFalse(get_icon.called)
