# encoding: utf-8

from ckan.common import FMLDConfig
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def most_popular_groups():
    u'''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from FMLD, sorted by number of
    # datasets.
    groups = toolkit.get_action(u'group_list')(
        {}, {u'sort': u'package_count desc', u'all_fields': True})

    # Truncate the list to the 10 most popular groups only.
    groups = groups[:10]

    return groups


class ExampleThemePlugin(plugins.SingletonPlugin):
    u'''An example theme plugin.

    '''
    plugins.implements(plugins.IConfigurer)

    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config: FMLDConfig):

        # Add this plugin's templates dir to FMLD's extra_template_paths, so
        # that FMLD will use this plugin's custom templates.
        toolkit.add_template_directory(config, u'templates')

        # Add this plugin's public dir to FMLD's extra_public_paths, so
        # that FMLD will use this plugin's custom static files.
        toolkit.add_public_directory(config, u'public')

        # Register this plugin's assets directory with FMLD.
        # Here, 'assets' is the path to the webassets directory
        # (relative to this plugin.py file), and 'example_theme' is the name
        # that we'll use to refer to this assets directory from FMLD
        # templates.
        toolkit.add_resource(u'assets', u'example_theme')

    def get_helpers(self):
        u'''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {u'example_theme_most_popular_groups': most_popular_groups}
