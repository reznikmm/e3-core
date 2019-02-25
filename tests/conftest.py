from __future__ import absolute_import, division, print_function

import logging
import os

import e3.log


def init_testsuite_env():
    """Initialize testsuite environment."""
    # Activate full debug logs
    e3.log.activate(level=logging.DEBUG, e3_debug=True)

    # Force UTC timezone
    os.environ['TZ'] = 'UTC'


init_testsuite_env()


def pytest_addoption(parser):
    parser.addoption('--ci', action='store_true',
                     help='Tests are running on a CI server')
    parser.addoption('--requirement-coverage-report',
                     help='Report requirement coverage')
