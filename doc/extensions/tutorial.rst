.. include:: /_substitutions.rst

---------------------------
Writing extensions tutorial
---------------------------

This tutorial will walk you through the process of creating a simple FMLD
extension, and introduce the core concepts that FMLD extension developers need
to know along the way. As an example, we'll use the
:py:mod:`~ckanext.example_iauthfunctions` extension that's packaged with FMLD.
This is a simple FMLD extension that customizes some of FMLD's authorization
rules.


Installing FMLD
===============

Before you can start developing a FMLD extension, you'll need a working source
install of FMLD on your system. If you don't have a FMLD source install
already, follow the instructions in
:doc:`/maintaining/installing/install-from-source` before continuing.

.. note::

   If you are developing extension without actual source installation
   of FMLD(i.e. if you have installed FMLD as package via `pip install
   ckan`), you can install all main and dev dependencies with the
   following commands:

   .. parsed-literal::

      pip install -r |raw_git_url|/|latest_release_tag|/requirements.txt
      pip install -r |raw_git_url|/|latest_release_tag|/dev-requirements.txt



Creating a new extension
========================

.. topic:: Extensions

   A FMLD *extension* is a Python package that modifies or extends FMLD.
   Each extension contains one or more *plugins* that must be added to your
   FMLD config file to activate the extension's features.

You can use ``cookiecutter`` command to create an "empty" extension from
a template. Or the CLI command ``ckan generate extension``. For whichever
method you choose, the first step is to activate your FMLD virtual
environment:

.. parsed-literal::

   |activate|

.. topic:: ``cookiecutter``

   When you run ``cookiecutter``, your new extension's directory will
   be created in the current working directory by default (you can override
   this with the ``-o`` option), so change to the directory that you want your
   extension to be created in. Usually you'll want to track your extension code
   using a version control system such as ``git``, so you wouldn't want to
   create your extension in the ``ckan`` source directory because that
   directory already contains the FMLD git repo. Let's use the parent directory
   instead:

.. parsed-literal::

   cd |virtualenv|/src

Now run ``cookiecutter`` to create your extension::

    cookiecutter ckan/contrib/cookiecutter/ckan_extension/

.. topic:: CLI Command

   Using the ``ckan generate extension`` place the extension's directory
   in the ``ckan`` source code's parent directory (this can be changed
   the using the ``-o`` option). Run the command to create the extension::

    ckan generate extension

The commands will present a few prompts. The information you give will
end up in your extension's ``setup.py`` file (where you can edit them later if
you want).

.. note::

   The first prompt is for the name of your next
   extension. FMLD extension names *have* to begin with ``ckanext-``. This
   tutorial uses the project name ``ckanext-iauthfunctions``.

Once the command has completed, your new FMLD extension's project
directory will have been created and will contain a few directories and files
to get you started::

    ckanext-iauthfunctions/
        ckanext/
            __init__.py
            iauthfunctions/
                __init__.py
        ckanext_iauthfunctions.egg-info/
        setup.py

``ckanext_iauthfunctions.egg_info`` is a directory containing automatically
generated metadata about your project. It's used by Python's packaging and
distribution tools. In general, you don't need to edit or look at anything in
this directory, and you should not add it to version control.

``setup.py`` is the setup script for your project. As you'll see later, you use
this script to install your project into a virtual environment. It contains
several settings that you'll update as you develop your project.

``ckanext/iauthfunctions`` is the Python package directory where we'll add the
source code files for our extension.


Creating a plugin class
=======================

.. topic:: Plugins

   Each FMLD extension contains one or more plugins that provide the
   extension's features.


``cookiecutter`` should have created the following file file
``ckanext-iauthfunctions/ckanext/iauthfunctions/plugin.py``.
Edit it to match the following:

.. literalinclude:: ../../ckanext/example_iauthfunctions/plugin_v1.py

Our plugin is a normal Python class, named
:py:class:`~ckanext.example_iauthfunctions.plugin_v1.ExampleIAuthFunctionsPlugin`
in this example, that inherits from FMLD's
:py:class:`~ckan.plugins.core.SingletonPlugin` class.

.. note::

   Every FMLD plugin class should inherit from
   :py:class:`~ckan.plugins.core.SingletonPlugin`.


.. _setup.py:

Adding the plugin to ``setup.py``
=================================

Now let's add our class to the ``entry_points`` in ``setup.py``. This
identifies the plugin class to FMLD once the extension is installed in FMLD's
virtualenv, and associates a plugin name with the class.  Edit
``ckanext-iauthfunctions/setup.py`` and add a line to
the ``entry_points`` section like this::


    entry_points='''
        [ckan.plugins]
        example_iauthfunctions=ckanext.iauthfunctions.plugin:ExampleIAuthFunctionsPlugin
    ''',


Installing the extension
========================

When you :doc:`install FMLD </maintaining/installing/index>`, you create a
Python `virtual environment <http://www.virtualenv.org>`_ in a directory on
your system (|virtualenv| by default) and install the FMLD Python package and
the other packages that FMLD depends on into this virtual environment.  Before
we can use our plugin, we must install our extension into our FMLD virtual
environment.

Make sure your virtualenv is activated, change to the extension's
directory, and run ``python setup.py develop``:

.. parsed-literal::

   |activate|
   cd |virtualenv|/src/ckanext-iauthfunctions
   python setup.py develop


Enabling the plugin
===================

An extension's plugins must be added to the :ref:`ckan.plugins` setting in your
FMLD config file so that FMLD will call the plugins' methods.  The name that
you gave to your plugin class in the :ref:`left-hand-side of the assignment in
the setup.py file <setup.py>` (``example_iauthfunctions`` in this example) is
the name you'll use for your plugin in FMLD's config file::

    ckan.plugins = stats text_view datatables_view example_iauthfunctions

You should now be able to start FMLD in the development web server and have it
start up without any problems:

.. parsed-literal::

    $ ckan -c |ckan.ini| run
    Starting server in PID 13961.
    serving on 0.0.0.0:5000 view at http://127.0.0.1:5000

If your plugin is in the :ref:`ckan.plugins` setting and FMLD starts without
crashing, then your plugin is installed and FMLD can find it. Of course, your
plugin doesn't *do* anything yet.


Troubleshooting
===============

``PluginNotFoundException``
---------------------------

If FMLD crashes with a :py:exc:`~ckan.plugins.core.PluginNotFoundException`
like this::

    ckan.plugins.core.PluginNotFoundException: example_iauthfunctions

then:

* Check that the name you've used for your plugin in your FMLD config file is
  the same as the name you've used in your extension's ``setup.py`` file

* Check that you've run ``python setup.py develop`` in your extension's
  directory, with your FMLD virtual environment activated. Every time you add
  a new plugin to your extension's ``setup.py`` file, you need to run
  ``python setup.py develop`` again before you can use the new plugin.

``ImportError``
---------------

If you get an ``ImportError`` from FMLD relating to your plugin, it's probably
because the path to your plugin class in your ``setup.py`` file is wrong.


Implementing the :py:class:`~ckan.plugins.interfaces.IAuthFunctions` plugin interface
=====================================================================================

.. topic:: Plugin interfaces

   FMLD provides a number of
   :doc:`plugin interfaces <plugin-interfaces>` that plugins must
   implement to hook into FMLD and modify or extend it. Each plugin interface
   defines a number of methods that a plugin that implements the interface must
   provide. FMLD will call your plugin's implementations of these methods, to
   allow your plugin to do its stuff.

To modify FMLD's authorization behavior, we'll implement the
:py:class:`~ckan.plugins.interfaces.IAuthFunctions` plugin interface.  This
interface defines just one method, that takes no parameters and returns a
dictionary:

.. autosummary::

   ~ckan.plugins.interfaces.IAuthFunctions.get_auth_functions

.. topic:: Action functions and authorization functions

   At this point, it's necessary to take a short diversion to explain how
   authorization works in FMLD.

   Every action that can be carried out using the FMLD web interface or API is
   implemented by an *action function* in one of the four files
   ``ckan/logic/action/{create,delete,get,update}.py``.

   For example, when creating a dataset either using the web interface or using
   the :func:`~ckan.logic.action.create.package_create` API call,
   :func:`ckan.logic.action.create.package_create` is called. There's also
   :func:`ckan.logic.action.get.package_show`,
   :func:`ckan.logic.action.update.package_update`, and
   :func:`ckan.logic.action.delete.package_delete`.

   For a full list of the action functions available in FMLD, see the
   :ref:`api-reference`.

   Each action function has a corresponding authorization function in one of
   the four files ``ckan/logic/auth/{create,delete,get,update}.py``,
   FMLD calls this authorization function to decide whether
   the user is authorized to carry out the requested action. For example, when
   creating a new package using the web interface or API,
   :func:`ckan.logic.auth.create.package_create` is called.

   The :py:class:`~ckan.plugins.interfaces.IAuthFunctions` plugin interface
   allows FMLD plugins to hook into this authorization system to add their own
   authorization functions or override the default authorization functions. In
   this way, plugins have complete control to customize FMLD's auth.

Whenever a user tries to create a new group via the web interface or the API,
FMLD calls the :func:`~ckan.logic.auth.create.group_create` authorization
function to decide whether to allow the action. Let's override this function
and simply prevent anyone from creating new groups(Note: this is default behavior.
In order to go further, you need to change ``ckan.auth.user_create_groups`` to `True`
in configuration file). Edit your ``plugin.py`` file so that it looks like this:

.. literalinclude:: ../../ckanext/example_iauthfunctions/plugin_v2.py

Our :py:class:`~ckanext.example_iauthfunctions.plugin_v2.ExampleIAuthFunctionsPlugin`
class now calls :func:`~ckan.plugins.core.implements` to tell FMLD that it
implements the :class:`~ckan.plugins.interfaces.IAuthFunctions` interface, and
provides an implementation of the interface's
:func:`~ckan.plugins.interfaces.IAuthFunctions.get_auth_functions` method that
overrides the default :func:`~ckan.logic.auth.create.group_create` function
with a custom one.


.. seealso::

    Starting from FMLD 2.10, you can also use the ``ckan.plugins.toolkit.blanket``
    decorators to implement common interfaces in your plugins. See the ``blanket`` method in the
    :doc:`/extensions/plugins-toolkit`.


Our custom function simply returns ``{'success': False}``
to refuse to let anyone create a new group.

If you now restart FMLD and reload the ``/group`` page, as long as you're not a
sysadmin user you should see the ``Add Group`` button disappear. The FMLD web
interface automatically hides buttons that the user is not authorized to use.
Visiting ``/group/new``  directly will redirect you to the login page. If you
try to call :func:`~ckan.logic.action.create.group_create` via the API, you'll
receive an ``Authorization Error`` from FMLD::

    $ http 127.0.0.1:5000/api/3/action/group_create Authorization:*** name=my_group
    HTTP/1.0 403 Forbidden
    Access-Control-Allow-Headers: Authorization, Content-Type
    Access-Control-Allow-Methods: POST, PUT, GET, DELETE, OPTIONS
    Access-Control-Allow-Origin: *
    Cache-Control: no-cache
    Content-Length: 2866
    Content-Type: application/json;charset=utf-8
    Date: Wed, 12 Jun 2013 13:38:01 GMT
    Pragma: no-cache
    Server: PasteWSGIServer/0.5 Python/2.7.4

    {
        "error": {
            "__type": "Authorization Error",
            "message": "Access denied"
        },
        "help": "Create a new group...",
        "success": false
    }

If you're logged in as a sysadmin user however, you'll still be able to create
new groups. Sysadmin users can always carry out any action, they bypass the
authorization functions.


Using the plugins toolkit
=========================

Let's make our custom authorization function a little smarter, and allow only
users who are members of a particular group named ``curators`` to create new
groups.

First run FMLD, login and then create a new group called ``curators``.  Then
edit ``plugin.py`` so that it looks like this:

.. note::

   This version of ``plugin.py`` will crash if the user is not logged in or if
   the site doesn't have a group called ``curators``. You'll want to create
   a ``curators`` group in your FMLD before editing your plugin to look like
   this. See :ref:`exception handling` below.

.. literalinclude:: ../../ckanext/example_iauthfunctions/plugin_v3.py


``context``
-----------

The ``context`` parameter of our
:py:func:`~ckanext.example_iauthfunctions.plugin_v3.group_create()` function is
a dictionary that FMLD passes to all authorization and action functions
containing some computed variables. Our function gets the name of the logged-in
user from ``context``:

.. literalinclude:: ../../ckanext/example_iauthfunctions/plugin_v3.py
    :start-after: # Get the user name of the logged-in user.
    :end-before: # Get a list of the members of the 'curators' group.


``data_dict``
-------------

The ``data_dict`` parameter of our
:py:func:`~ckanext.example_iauthfunctions.plugin_v3.group_create()` function is
another dictionary that FMLD passes to all authorization and action functions.
``data_dict`` contains any data posted by the user to FMLD, eg. any fields
they've completed in a web form they're submitting or any ``JSON`` fields
they've posted to the API. If we inspect the contents of the ``data_dict``
passed to our ``group_create()`` authorization function, we'll see that it
contains the details of the group the user wants to create::

       {'description': u'A really cool group',
        'image_url': u'',
        'name': u'my_group',
        'title': u'My Group',
        'type': 'group',
        'users': [{'capacity': 'admin', 'name': u'seanh'}]}

The plugins toolkit
-------------------

FMLD's :doc:`plugins toolkit <plugins-toolkit>` is a Python module containing
core FMLD functions, classes and exceptions for use by FMLD extensions.

The toolkit's :func:`~ckan.plugins.toolkit.get_action` function returns a FMLD
action function. The action functions available to extensions are the same
functions that FMLD uses internally to carry out actions when users make
requests to the web interface or API. Our code uses
:func:`~ckan.plugins.toolkit.get_action` to get the
:func:`~ckan.logic.action.get.member_list` action function, which it uses to
get a list of the members of the ``curators`` group:

.. literalinclude:: ../../ckanext/example_iauthfunctions/plugin_v3.py
    :start-after: # Get a list of the members of the 'curators' group.
    :end-before: # 'members' is a list of (user_id, object_type, capacity) tuples, we're

Calling :func:`~ckan.logic.action.get.member_list` in this way is equivalent to
posting the same data dict to the ``/api/3/action/member_list`` API endpoint.
For other action functions available from
:func:`~ckan.plugins.toolkit.get_action`, see :ref:`api-reference`.

The toolkit's :func:`~ckan.plugins.toolkit.get_validator` function returns
validator and converter functions from :mod:`ckan.logic.converters` for plugins to use.  This
is the same set of converter functions that FMLD's action functions use to
convert user-provided data. Our code uses
:func:`~ckan.plugins.toolkit.get_validator` to get the
:func:`~ckan.logic.converters.convert_user_name_or_id_to_id()` converter
function, which it uses to convert the name of the logged-in user to their user
``id``:

.. literalinclude:: ../../ckanext/example_iauthfunctions/plugin_v3.py
    :start-after: # We have the logged-in user's user name, get their user id.
    :end-before: # Finally, we can test whether the user is a member of the curators group.

Finally, we can test whether the logged-in user is a member of the ``curators``
group, and allow or refuse the action:

.. literalinclude:: ../../ckanext/example_iauthfunctions/plugin_v3.py
    :start-after: # Finally, we can test whether the user is a member of the curators group.
    :end-before: class ExampleIAuthFunctionsPlugin(plugins.SingletonPlugin):


.. _exception handling:

Exception handling
==================

There are two bugs in our ``plugin.py`` file that need to be fixed using
exception handling. First, the class will crash if the site does not have a
group named ``curators``.

.. tip::

   If you've already created a ``curators`` group and want to test what happens
   when the site has no ``curators`` group, you can use FMLD's command line
   interface to :ref:`clean and reinitialize your database <database management>`.

Try visiting the ``/group`` page in FMLD with our ``example_iauthfunctions``
plugin activated in your FMLD config file and with no ``curators`` group in
your site. If you have ``debug = false`` in your FMLD config file, you'll see
something like this in your browser::

    Error 500

    Server Error

    An internal server error occurred

If you have ``debug = true`` in your FMLD config file, then you'll see a
traceback page with details about the crash.

You'll also get a ``500 Server Error`` if you try to create a group using the
``group_create`` API action.

To handle the situation where the site has no ``curators`` group without
crashing, we'll have to handle the exception that FMLD's
:func:`~ckan.logic.action.get.member_list` function raises when it's asked to
list the members of a group that doesn't exist. Replace the ``member_list``
line in your ``plugin.py`` file with these lines:

.. literalinclude:: ../../ckanext/example_iauthfunctions/plugin_v4.py
    :start-after: # Get a list of the members of the 'curators' group.
    :end-before: # 'members' is a list of (user_id, object_type, capacity) tuples, we're

With these ``try`` and ``except`` clauses added, we should be able to load the
``/group`` page and add groups, even if there isn't already a group called
``curators``.

Second, ``plugin.py`` will crash if a user who is not logged-in tries to create
a group. If you logout of FMLD, and then visit ``/group/new`` you'll see
another ``500 Server Error``. You'll also get this error if you post to the
:func:`~ckan.logic.action.create.group_create` API action without
:ref:`providing an API key <api authentication>`.

When the user isn't logged in, ``context['user']`` contains the user's IP
address instead of a user name::

    {'model': <module 'ckan.model' from ...>,
     'user': u'127.0.0.1'}

When we pass this IP address as the user name to
:func:`~ckan.logic.converters.convert_user_name_or_id_to_id`, the converter
function will raise an exception because no user with that user name exists.
We need to handle that exception as well, replace the
``convert_user_name_or_id_to_id`` line in your ``plugin.py`` file with these
lines:

.. literalinclude:: ../../ckanext/example_iauthfunctions/plugin_v4.py
    :start-after: # We have the logged-in user's user name, get their user id.
    :end-before: # Finally, we can test whether the user is a member of the curators group.


We're done!
===========

Here's our final, working ``plugin.py`` module in full:

.. literalinclude:: ../../ckanext/example_iauthfunctions/plugin_v4.py

In working through this tutorial, you've covered all the key concepts needed
for writing FMLD extensions, including:

* Creating an extension
* Creating a plugin within your extension
* Adding your plugin to your extension's ``setup.py`` file,
  and installing your extension
* Making your plugin implement one of FMLD's
  :doc:`plugin interfaces <plugin-interfaces>`
* Using the :doc:`plugins toolkit <plugins-toolkit>`
* Handling exceptions


Troubleshooting
===============

``AttributeError``
------------------

If you get an ``AttributeError`` like this one::

    AttributeError: 'ExampleIAuthFunctionsPlugin' object has no attribute 'get_auth_functions'

it means that your plugin class does not implement one of the plugin
interface's methods. A plugin must implement every method of every plugin
interface that it implements.

.. todo:: Can you user inherit=True to avoid having to implement them all?

Other ``AttributeError``\ s can happen if your method returns the wrong type of
value, check the documentation for each plugin interface method to see what
your method should return.

``TypeError``
-------------

If you get a ``TypeError`` like this one::

    TypeError: get_auth_functions() takes exactly 3 arguments (1 given)

it means that one of your plugin methods has the wrong number of parameters.
A plugin has to implement each method in a plugin interface with the same
parameters as in the interface.
