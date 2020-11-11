# -*- coding: utf-8 -*-
# Intro: JSON 日志模块
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 1.0.0
# Date: 2020-11-11
# Github: https://github.com/ztj1993/py-json-logging

import json
import logging
import threading

__version__ = '1.0.0'


class JsonLogger(logging.Logger):
    _glob = dict()
    _local = threading.local()

    def glob(self, k, v):
        self._glob[k] = v

    def set(self, k, v):
        self._local.__setattr__(k, v)

    def get(self, k):
        if hasattr(self._local, k):
            return self._local.__getattribute__(k)
        return self._glob.get(k)

    def handle(self, record):
        for k, v in self._glob.items():
            record.__setattr__(k, v)
        for k, v in self._local.__dict__.items():
            record.__setattr__(k, v)
        super().handle(record)


class JsonFormatter(logging.Formatter):
    json_options = dict(
        ensure_ascii=True,
        indent=None
    )

    def set_ensure_ascii(self, value):
        self.json_options['ensure_ascii'] = bool(value)

    def set_indent(self, value):
        self.json_options['indent'] = int(value)

    def formatMessage(self, record):
        record.args = list(record.args)
        record.created_fmt = self.formatTime(record, self.datefmt)
        record.thread_name = record.threadName
        record.process_name = record.processName
        record.func_name = record.funcName
        record.line_no = record.lineno
        record.level_no = record.levelno
        record.level_name = record.levelname
        record.path_name = record.pathname

        record.relativeCreated = None
        record.threadName = None
        record.msecs = None
        record.msg = None
        record.funcName = None
        record.levelno = None
        record.levelname = None
        record.processName = None
        record.pathname = None

        record = {k: v for k, v in record.__dict__.items() if v}
        return json.dumps(record, **self.json_options)
