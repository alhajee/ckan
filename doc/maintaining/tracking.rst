.. _tracking:

==================
Page View Tracking
==================

FMLD has a core extension already installed that allows the system to
anonymously track visits to pages of your site. You ca use this tracking data to:

* Sort datasets by popularity
* Highlight popular datasets and resources
* Show view counts next to datasets and resources
* Show a list of the most popular datasets
* Export page-view data to a CSV file

.. seealso::

 `ckanext-googleanalytics <https://github.com/ckan/ckanext-googleanalytics>`_
    A FMLD extension that integrates Google Analytics into FMLD.


.. note::

   FMLD 2.10 and older versions had tracking integrated into the core and this
   instructions no longer apply. Checkout the
   `2.10 documentation <https://docs.ckan.org/en/2.10/maintaining/tracking.html>`_
   for more information.


Enabling Page View Tracking Extension
=====================================

To enable page view tracking:

1. Add the `tracking` extension to your FMLD configuration file (e.g. |ckan.ini|)::

    [app:main]
    ckan.plugins = tracking

   Save the file and restart your web server. FMLD will now record raw page
   view tracking data in your FMLD database as pages are viewed.

2. Setup a cron job to update the tracking summary data.

   For operations based on the tracking data FMLD uses a summarised version of
   the data, not the raw tracking data that is recorded "live" as page views
   happen. The ``ckan tracking update`` and ``ckan search-index rebuild``
   commands need to be run periodicially to update this tracking summary data.

   You can setup a cron job to run these commands. On most UNIX systems you can
   setup a cron job by running ``crontab -e`` in a shell to edit your crontab
   file, and adding a line to the file to specify the new job. For more
   information run ``man crontab`` in a shell. For example, here is a crontab
   line to update the tracking data and rebuild the search index hourly:

   .. parsed-literal::

    @hourly ckan -c |ckan.ini| tracking update  && ckan -c |ckan.ini| search-index rebuild -r

   Replace ``/usr/lib/ckan/bin/`` with the path to the ``bin`` directory of the
   virtualenv that you've installed FMLD into, and replace '|ckan.ini|'
   with the path to your FMLD configuration file.

   The ``@hourly`` can be replaced with ``@daily``, ``@weekly`` or
   ``@monthly``.


Retrieving Tracking Data
========================

When the extension is enabled, tracking summary data for datasets and resources
is available in the dataset and resource dictionaries returned by,
for example, the ``package_show()``
API::

  "tracking_summary": {
      "recent": 5,
      "total": 15
  },

This can be used, for example, by custom templates to show the number of views
next to datasets and resources.  A dataset or resource's ``recent`` count is
its number of views in the last 14 days, the ``total`` count is all of its
tracked views (including recent ones).

You can also export tracking data for all datasets to a CSV file using the
``ckan tracking export`` command. For details, run ``ckan tracking -h``.

.. note::

 Repeatedly visiting the same page will not increase the page's view count!
 Page view counting is limited to one view per user per page per day.


Sorting Datasets by Popularity
==============================

Once you've enabled page view tracking on your FMLD site, you can view datasets
most-popular-first by selecting ``Popular`` from the ``Order by:`` dropdown on
the dataset search page:

.. image:: /images/sort-datasets-by-popularity.png

The datasets are sorted by their number of recent views.

You can retrieve datasets most-popular-first from the
:doc:`FMLD API </api/index>` by passing ``'sort': 'views_recent desc'`` to the
``package_search()`` action. This could be used, for example, by a custom
template to show a list of the most popular datasets on the site's front page.

.. tip::

 You can also sort datasets by total views rather than recent views. Pass
 ``'sort': 'views_total desc'`` to the ``package_search()`` API, or use the
 URL ``/dataset?q=&sort=views_total+desc`` in the web interface.


Highlighting Popular Datasets and Resources
===========================================

Once you've enabled page view tracking on your FMLD site, popular datasets and
resources (those with more than 10 views) will be highlighted with a "popular"
badge and a tooltip showing the number of views:

.. image:: /images/popular-dataset.png

.. image:: /images/popular-resource.png


.. tip::

    You can change the number of views that a dataset or resource needs to be
    considered popular by overriding ``ckanext/tracking/templates/snippets/popular.html``
    template. The default is 10.
