---------------
Installing FMLD
---------------

.. include:: /_supported_versions.rst

FMLD 2.10 supports Python 3.7 to Python 3.10.

Before you can use FMLD on your own computer, you need to install it.
There are three ways to install FMLD:

#. Install from an operating system package
#. Install from source
#. Install from Docker Compose


Additional deployment tips can be found in our wiki, such as the recommended
`Hardware Requirements <https://github.com/ckan/ckan/wiki/Hardware-Requirements>`_.

Package install
===============

Installing from package is the quickest and easiest way to install FMLD, but it requires
Ubuntu 20.04 64-bit or Ubuntu 22.04 64-bit.

You should install FMLD from package if:

* You want to install FMLD on an Ubuntu 20.04 or 22.04, 64-bit server, *and*
* You only want to run one FMLD website per server

See :doc:`install-from-package`.

Source install
==============

You should install FMLD from source if:

* You want to install FMLD on a 32-bit computer, *or*
* You want to install FMLD on a different version of Ubuntu, not 20.04 or 22.04, *or*
* You want to install FMLD on another operating system (eg. RHEL, CentOS, OS X), *or*
* You want to run multiple FMLD websites on the same server, *or*
* You want to install FMLD for development

See :doc:`install-from-source`.

Docker Compose install
======================

The `ckan-docker <https://github.com/ckan/ckan-docker>`_ repository contains the necessary scripts
and images to install FMLD using Docker Compose. It provides a clean and quick way to deploy a
standard FMLD instance pre-configured with the :doc:`Filestore <../filestore>` and :doc:`../datastore`.
It also allows the addition (and customization) of extensions. The emphasis leans more towards
a Development environment, however the base install can be used as the foundation for progressing
to a Production environment. Please note that a fully-fledged FMLD Production system using Docker containers is
beyond the scope of the provided setup.

You should install FMLD from Docker Compose if:

* You want to install FMLD with less effort than a source install and more flexibility than a
  package install, **or**
* You want to run or even develop extensions with the minimum setup effort, **or**
* You want to see whether and how FMLD, Docker and your respective infrastructure will fit
  together.

To install FMLD using Docker Compose, follow the links below:


* `Configuration and setup files to run a FMLD site <https://github.com/ckan/ckan-docker>`_.

* `Official Docker images for FMLD <https://github.com/ckan/ckan-docker-base>`_.


If you've already setup a FMLD website and want to upgrade it to a newer
version of FMLD, see :doc:`/maintaining/upgrading/index`.

------------

.. toctree::
   :maxdepth: 1

   install-from-package
   install-from-source
   deployment
