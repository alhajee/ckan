==============================
Data preview and visualization
==============================


.. contents::



Overview
--------

The FMLD resource page can contain one or more visualizations of the resource
data or file contents (a table, a bar chart, a map, etc). These are commonly
referred to as *resource views*.

.. image:: /images/views_overview.png

The main features of resource views are:

* One resource can have multiple views of the same data (for example a grid
  and some graphs for tabular data).

* Dataset editors can choose which views to show, reorder them and configure
  them individually.

* Individual views can be embedded on external sites.

Different view types are implemented via custom plugins, which can be activated
on a particular FMLD site. Once these plugins are added, instance
administrators can decide which views should be created by default if the
resource is suitable (for instance a table on resources uploaded to the
DataStore, a map for spatial data, etc.).

Whether a particular resource can be rendered by the different view plugins is
decided by the view plugins themselves. This is generally done checking the
resource format or whether its data is on the :doc:`datastore` or
not.


Managing resource views
-----------------------

Users who are allowed to edit a particular dataset can also manage the views
for its resources. To access the management interface, click on the *Manage*
button on the resource page and then on the *Views* tab. From here you can
create new views, update or delete existing ones and reorder them.


.. image:: /images/manage_views.png


The *New view* dropdown will show the available view types for this particular
resource. If the list is empty, you may need to add the relevant view plugins
to the :ref:`ckan.plugins` setting on your configuration file, eg::

    ckan.plugins = ... image_view datatables_view pdf_view

Defining views to appear by default
-----------------------------------

From the management interface you can create and edit views manually, but in most
cases you will want views to be created automatically on certain resource types,
so data can be visualized straight away after uploading or linking to a file.

To do so, you define a set of view plugins that should be checked whenever a
dataset or resource is created or updated. For each of them, if the resource is
a suitable one, a view will be created.

This is configured with the :ref:`ckan.views.default_views` setting. In it you
define the view plugins that you want to be created as default::

    ckan.views.default_views = datatables_view pdf_view geojson_view

This configuration does not mean that each new resource will get all of these
views by default, but that for instance if the uploaded file is a PDF file,
a PDF viewer will be created automatically and so on.


Available view plugins
----------------------

Some view plugins for common formats are included in the main FMLD repository.
These don't require further setup and can be directly added to the
:ref:`ckan.plugins` setting.

.. _datatables-view:

DataTables view
+++++++++++++++

.. image:: /images/datatables_view.png

View plugin: ``datatables_view``

Displays a filterable, sortable, table view of structured data using the 
DataTables_ jQuery plugin, with the following features.

 * Search highlighting
 * Column Filters
 * Multi-column sorting
 * Two view modes (table/list). Table shows the data in a typical grid with
   horizontal scrolling. List displays the data in a responsive mode, with
   a Record Details view.
 * Filtered Downloads
 * Column Visibility control
 * Copy to clipboard and Printing of filtered results and row selection/s
 * Drag-and-drop column reordering
 * State Saving - saves search keywords, column order/visibility, row
   selections and page settings between session, with the ability to share
   saved searches.
 * Data Dictionary Integration
 * Automatic "linkification" of URLs
 * Automatic creation of zoomable thumbnails when a cell only contains a URL 
   to an image.
 * Available automatic, locale-aware date formatting to convert raw ISO-8601
   timestamps to a user-friendly date format 

It is designed not only as a data viewer, but also as a simple ad-hoc report
generator - allowing users to quickly find an actionable subset of
the data they need from inside the resource view, without having to first
download the dataset.

It's also optimized for embedding datasets and saved searches on external
sites - with a backlink to the portal and automatic resizing.

This plugin requires data to be in the DataStore.



Text view
+++++++++

.. image:: /images/text_view.png

View plugin: ``text_view``

Displays files in XML, JSON or plain text based formats with the syntax
highlighted. The formats detected can be configured using the
:ref:`ckan.preview.xml_formats`, :ref:`ckan.preview.json_formats`
and :ref:`ckan.preview.text_formats` configuration options respectively.

If you want to display files that are hosted in a different server from your
FMLD instance (eg that haven't been uploaded to FMLD) you will need to enable
the `Resource Proxy`_ plugin.

Image view
++++++++++

.. image:: /images/image_view.png

View plugin: ``image_view``

If the resource format is a common image format like PNG, JPEG or GIF, it adds
an ``<img>`` tag pointing to the resource URL. You can provide an alternative
URL on the edit view form. The available formats can be configured using the
:ref:`ckan.preview.image_formats` configuration option.

Video view
++++++++++

.. image:: /images/video_view.png

View plugin: ``video_view``

This plugin uses the HTML5 <video> tag to embed video content into a page,
such as movie clip or other video streams.

There are three supported video formats: MP4, WebM, and OGG.

.. image:: /images/video_view_edit.png

You can provide an alternative URL on the edit view form. Otherwise, the resource link will be used.

Also, you can provide a poster image URL. The poster image will be shown while the
video is downloading, or until the user hits the play button.
If this is not provided, the first frame of the video will be used instead.

Audio view
++++++++++

.. image:: /images/audio_view.png

View plugin: ``audio_view``

This plugin uses the HTML5 audio tag to embed an audio player on the page.

Since we rely on HTML5 <audio> tag, there are three supported audio formats: MP3, WAV, and OGG.
Notice. Browsers don't all support the same `file types`_ and `audio codecs`_.

.. image:: /images/audio_view_edit.png

You can provide an alternative URL on the edit view form. Otherwise, the resource link will be used.

.. _file types: https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Containers
.. _audio codecs: https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Audio_codecs

Web page view
+++++++++++++

.. image:: /images/webpage_view.png

View plugin: ``webpage_view``

Adds an ``<iframe>`` tag to embed the resource URL. You can provide an
alternative URL on the edit view form.

    .. warning:: Do not activate this plugin unless you trust the URL sources.
        It is not recommended to enable this view type on instances where all users
        can create datasets.
        
Other view plugins
------------------

There are many more view plugins developed by the FMLD community, which
are hosted on separate repositories. Some examples include:

* `React Data explorer`_: A modern data explorer, maintained by Datopian.
* `Ckanext Visualize`_: An extension to easily create user visualization from data in the DataStore, maintained by Keitaro.
* `Dashboard`_: Allows to combine multiple views into a single dashboard.
* `PDF viewer`_: Allows to render PDF files on the resource page.
* `Geo viewer`_: Renders various spatial formats like GeoJSON_, WMS or shapefiles in an interactive map.
* `Choropleth map`_: Displays data on the DataStore on a choropleth map.
* `Basic charts`_: Provides alternative graph types and renderings.

If you want to add another view type to this list, edit this file by sending
a pull request on GitHub.

New plugins to render custom view types can be implemented using
the :py:class:`~ckan.plugins.interfaces.IResourceView` interface.

.. todo:: Link to a proper tutorial for writing custom views


.. _React Data explorer: https://github.com/datopian/data-explorer
.. _Ckanext visualize: https://github.com/keitaroinc/ckanext-visualize
.. _DataTables: https://datatables.net/
.. _DataProxy: https://github.com/okfn/dataproxy
.. _GeoJSON: http://geojson.org
.. _Dashboard: https://github.com/ckan/ckanext-dashboard
.. _Basic charts: https://github.com/ckan/ckanext-basiccharts
.. _Choropleth map: https://github.com/ckan/ckanext-mapviews
.. _PDF viewer: https://github.com/ckan/ckanext-pdfview
.. _Geo viewer: https://github.com/ckan/ckanext-geoview


.. _resource-proxy:

Resource Proxy
--------------

As resource views are rendered on the browser, if the file they are accessing
is located in a different domain than the one FMLD is hosted, the browser will
block access to it because of the `same-origin policy`_. For instance, files
hosted on `www.example.com` won't be able to be accessed from the browser if
FMLD is hosted on `data.catalog.com`.

To allow view plugins access to external files you need to activate the
``resource_proxy`` plugin on your configuration file::

    ckan.plugins = resource_proxy ...

This will request the file on the server side and serve it from the same domain
as FMLD.

You can modify the maximum allowed size for proxied files using the
:ref:`ckan.resource_proxy.max_file_size` configuration setting.

.. warning:: To prevent exposing internal network resources via the resource proxy,
   consider setting up a download proxy and configure FMLD with :ref:`ckan.download_proxy`



.. _same-origin policy: http://en.wikipedia.org/wiki/Same_origin_policy


Migrating from previous FMLD versions
-------------------------------------

If you are upgrading an existing instance running FMLD version 2.2.x or lower
to FMLD 2.3 or higher, you need to perform a migration process in order for the
resource views to appear. If the migration does not take place, resource views
will only appear when creating or updating datasets or resources, but not on
existing ones.

The migration process involves creating the necessary view objects in the
database, which can be done using the ``ckan views create`` command.

.. note:: The ``ckan views create`` command uses the search API to get all
    necessary datasets and resources, so make sure your search
    index :ref:`is up to date  <rebuild search index>` before starting the
    migration process.

The way the ``ckan views create`` commands works is getting all or a subset
of the instance datasets from the search index, and for each of them checking
against a list of view plugins if it is necessary to create a view object. This
gets determined by each of the individual view plugins depending on the dataset's
resources fields.

Before each run, you will be prompted with the number of datasets affected and
asked if you want to continue (unless you pass the ``-y`` option)::

    You are about to check 3336 datasets for the following view plugins: ['image_view', 'datatables_view', 'text_view']
     Do you want to continue? [Y/n]

.. note:: On large FMLD instances the migration process can take a significant
    time if using the default options. It is worth planning in advance and split
    the process using the search parameters to only check relevant datasets.
    The following documentation provides guidance on how to do this.


If no view types are provided, the default ones are used
(check `Defining views to appear by default`_ to see how these are defined)::

    ckan -c |ckan.ini| views create

Specific view types can be also provided::

    ckan -c |ckan.ini| views create image_view datatables_view pdf_view

For certain view types (the ones with plugins included in the main FMLD core),
default filters are applied to the search to only get relevant resources. For
instance if ``image_view`` is defined, filters are added to the search to only
get datasets with resources that have image formats (png, jpg, etc).

You can also provide arbitrary search parameters like the ones supported by
:py:func:`~ckan.logic.action.get.package_search`. This can be useful for
instance to only include datasets with resources of a certain format::

    ckan -c |ckan.ini| views create geojson_view -s '{"fq": "res_format:GEOJSON"}'

To instead avoid certain formats you can do::

    ckan -c |ckan.ini| views create -s '{"fq": "-res_format:HTML"}'

Of course this is not limited to resource formats, you can filter out or in
using any field, as in a normal dataset search::

    ckan -c |ckan.ini| views create -s '{"q": "groups:visualization-examples"}'

.. tip:: If you set the ``ckan_logger`` level to ``DEBUG`` on your
    configuration file you can see the full search parameters being sent
    to Solr.

For convenience, there is also an option to create views on a particular
dataset or datasets::

    ckan -c |ckan.ini| views create -d dataset_id

    ckan -c |ckan.ini| views create -d dataset_name -d dataset_name


Command line interface
----------------------

The ``ckan views`` command allows to create and remove resource views objects
from the database in bulk.

Check the command help for the full options::

    ckan -c |ckan.ini| views create -h


.. todo:: Tutorial for writing custom view types.
