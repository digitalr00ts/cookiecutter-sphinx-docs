# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

import logging

from .__version__ import (
    __title__,
    __description__,
    __url__,
    __version__,
    __author__,
    __author_email__,
    __license__,
    __copyright__,
)


logging.getLogger(__name__).addHandler(logging.NullHandler())
