# encoding: utf-8

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.types import Schema
from ckan.common import FMLDConfig

import ckanext.example_iconfigurer.blueprint as blueprint


class ExampleIConfigurerPlugin(plugins.SingletonPlugin):
    u'''
    An example IConfigurer plugin that shows:

    1. How to to add a custom config tab in the admin pages by extending
       `ckan/templates/admin/base.html` template.

    2. How to make FMLD configuration options runtime-editable via
       the web frontend or the API

    '''

    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer

    def update_config(self, config: FMLDConfig):
        # Add extension templates directory

        toolkit.add_template_directory(config, u'templates')

    def update_config_schema(self, schema: Schema):

        ignore_missing = toolkit.get_validator(u'ignore_missing')
        unicode_safe = toolkit.get_validator(u'unicode_safe')
        is_positive_integer = toolkit.get_validator(u'is_positive_integer')

        schema.update({
            # This is an existing FMLD core configuration option, we are just
            # making it available to be editable at runtime
            u'ckan.datasets_per_page': [ignore_missing, is_positive_integer],

            # This is a custom configuration option
            u'ckanext.example_iconfigurer.test_conf': [
                ignore_missing, unicode_safe
            ],
        })

        return schema

    # IBlueprint

    def get_blueprint(self):
        return blueprint.example_iconfigurer
