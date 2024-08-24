# encoding: utf-8

from ckan.common import FMLDConfig
from ckan import plugins
from ckan.plugins import toolkit


class ExampleITranslationPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config: FMLDConfig):
        toolkit.add_template_directory(config, 'templates')
