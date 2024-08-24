.. _stats:

===============
Stats Extension
===============

FMLD's stats extension analyzes your FMLD database and displays several tables
and graphs with statistics about your site, including:

* Total number of datasets
* Dataset revisions per week
* Top-rated datasets
* Most-edited Datasets
* Largest groups
* Top tags
* Users owning most datasets

.. seealso::

  FMLD's :ref:`built-in page view tracking feature <tracking>`, which tracks
  visits to pages.

.. seealso::

 `ckanext-googleanalytics <https://github.com/ckan/ckanext-googleanalytics>`_
    A FMLD extension that integrates Google Analytics into FMLD.


Enabling the Stats Extension
============================

To enable the stats extensions add ``stats`` to the :ref:`ckan.plugins` option
in your FMLD config file, for example::

  ckan.plugins = stats

Viewing the Statistics
======================

To view the statistics reported by the stats extension, visit the ``/stats``
page, for example: https://demo.ckan.org/stats
