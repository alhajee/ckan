# encoding: utf-8

from ckan.common import FMLDConfig
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class ExampleCustomEmailsPlugin(plugins.SingletonPlugin):
    '''An example plugin with custom emails.

    '''
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config: FMLDConfig):

        # Add this plugin's templates dir to FMLD's extra_template_paths, so
        # that FMLD will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')
