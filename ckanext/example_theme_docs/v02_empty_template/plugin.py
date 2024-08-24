# encoding: utf-8

'''plugin.py

'''
from ckan.common import FMLDConfig
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class ExampleThemePlugin(plugins.SingletonPlugin):
    '''An example theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config: FMLDConfig):

        # Add this plugin's templates dir to FMLD's extra_template_paths, so
        # that FMLD will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')
