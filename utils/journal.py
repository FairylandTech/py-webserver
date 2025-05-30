# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-27 16:06:07 UTC+08:00
"""

import logging

from fairylandfuture.toolkit.journal import Journal

journal: Journal = Journal(debug=True, console=True)


class JournalHandler(logging.Handler):
    def emit(self, record):
        message = self.format(record)
        if record.levelno >= logging.CRITICAL:
            journal.critical(message)
        elif record.levelno >= logging.ERROR:
            journal.error(message)
        elif record.levelno >= logging.WARNING:
            journal.warning(message)
        elif record.levelno >= logging.INFO:
            journal.info(message)
        elif record.levelno >= logging.DEBUG:
            journal.debug(message)
