# -*- coding: utf-8 -*-
"""
OpenHerb CloudLink
==================
Modified: 2021-11
"""

import logging
import logging.config

from cloudlink import __version__

__all__ = ['__version__']

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s"
)
logging.info("OpenHerb CloudLink Version: %s", __version__)
