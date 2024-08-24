# -*- coding: utf-8 -*-

import os
from ckan.config.middleware import make_app
from ckan.cli import FMLDConfigLoader
from logging.config import fileConfig as loggingFileConfig

if os.environ.get('FMLD_INI'):
    config_path = os.environ['FMLD_INI']
else:
    config_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), u'ckan.ini')

if not os.path.exists(config_path):
    raise RuntimeError('FMLD config file not found: {}'.format(config_path))

loggingFileConfig(config_path)
config = FMLDConfigLoader(config_path).get_config()

application = make_app(config)
