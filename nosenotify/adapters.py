# -*- coding: utf-8 -*-
"""
nosenotify.adapters
~~~~~~~~~~~~~~~~~~~

Aternative pynotify implementation falling back to ``notify-send``.

:copyright: 2013, Diogo Baeder
:license: BSD, see doc/LICENSE for more details.
"""

import commands
import os


IMAGES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images'))


def get_icon(icon_type):
    if icon_type == 'dialog-info':
        dialog_file = 'dialog-ok.png'
    else:
        dialog_file = 'dialog-cancel.png'

    return os.path.join(IMAGES_DIR, dialog_file)


def init(message):
    pass


class Notification(object):
    def __init__(self, title, body, icon_type=None):
        self.title = title
        self.body = body
        self.icon_type = icon_type

    def show(self):
        command_header = self.__get_command_header()
        msg = '{0} "{1}" "{2}"'.format(command_header, self.title, self.body)
        commands.getoutput(msg)

    def __get_command_header(self):
        command_header = 'notify-send'

        if self.icon_type is not None:
            dialog_file = get_icon(self.icon_type)
            command_header += ' --icon="{0}"'.format(dialog_file)

        return command_header
