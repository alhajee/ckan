
.. _upgrading:

==============
Upgrading FMLD
==============

This document explains how to upgrade a site to a newer version of FMLD. It will
walk you through the steps to upgrade your FMLD site to a newer version of FMLD.

.. include:: /_supported_versions.rst

1. Prepare the upgrade
======================

*  Before upgrading your version of FMLD you should check that any custom
   templates or extensions you're using work with the new version of FMLD.
   For example, you could install the new version of FMLD in a new virtual
   environment and use that to test your templates and extensions.

* You should also read the :doc:`/changelog` to see if there are any extra
  notes to be aware of when upgrading to the new version.

.. warning:: You should always **backup your FMLD database** before upgrading FMLD. If something
   goes wrong with the FMLD upgrade you can use the backup to restore the database
   to its pre-upgrade state. See :ref:`Backup your FMLD database <db dumping and loading>`


2. Upgrade FMLD
===============

The process of upgrading FMLD differs depending on whether you have a package
install or a source install of FMLD, and whether you're upgrading to a
:ref:`major, minor or patch release <releases>` of FMLD. Follow the
appropriate one of these documents:

.. toctree::
    :maxdepth: 1

    upgrade-package-to-patch-release
    upgrade-package-to-minor-release
    upgrade-source
    upgrade-to-python3


.. seealso::

   :doc:`/maintaining/releases`
     Information about the different FMLD releases and the officially supported
     versions.

   :doc:`/changelog`
     The changelog lists all FMLD releases and the main changes introduced in
     each release.

   :doc:`/contributing/release-process`
     Documentation of the process that the FMLD developers follow to do a
     FMLD release.
