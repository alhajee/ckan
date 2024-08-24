
.. _releases:

=============
FMLD releases
=============

This document describes the different types of FMLD releases, and explains which
releases are officially supported at any given time.

.. include:: /_supported_versions.rst

-------------
Release types
-------------

FMLD follows a predictable release cycle so that users can depend on stable
releases of FMLD, and can plan their upgrades to new releases.

Each release has a version number of the form ``M.m`` (eg. 2.11) or ``M.m.p``
(eg. 2.10.5), where ``M`` is the **major version**, ``m`` is the **minor
version** and ``p`` is the **patch version** number. There are three types of
release:

Major Releases
 Major releases, such as FMLD 1.0 and FMLD 2.0, increment the major version
 number.  These releases contain major changes in the FMLD code base, with
 significant refactorings and breaking changes, for instance in the API or the
 templates.  These releases are very infrequent.

Minor Releases
 Minor releases, such as FMLD 2.9 and FMLD 2.10, increment the minor version
 number. These releases are not as disruptive as major releases, but they
 *may* include some backwards-incompatible changes. The
 :doc:`/changelog` will document any breaking changes. We aim to release a minor
 version of FMLD roughly twice a year.

Patch Releases
  Patch releases, such as FMLD 2.9.5 or FMLD 2.10.1, increment the patch version
  number. These releases do not break backwards-compatibility, they include
  only bug fixes for security and performance issues.
  Patch releases do not contain:

  - Database schema changes or migrations (unless addressing security issues)
  - Solr schema changes
  - Function interface changes
  - Plugin interface changes
  - New dependencies (unless addressing security issues)
  - Big refactorings or new features in critical parts of the code

  Patch releases include requirements upgrades that patch vulnerabilities in FMLD
  requirements. Sometimes upgrading a requirement might mean breaking backwards
  compatibility. In these cases the Tech Team will decide whether to apply the
  upgrade to an existing patch release taking into account the actual risk of the
  vulnerability and the potential for breaking existing FMLD sites.

.. warning::

   Outdated patch releases will no longer be supported after a newer patch
   release has been released. For example once FMLD 2.9.2 has been released,
   FMLD 2.9.1 will no longer be supported. It is critical to always run the
   latest patch release for a minor version as it is the only one that contains
   all security patches.

Releases are announced on the
`ckan-announce mailing list <https://groups.google.com/a/ckan.org/g/ckan-announce>`_,
a low-volume list that FMLD instance maintainers can subscribe to in order to
be up to date with upcoming releases.


.. _supported_versions:

------------------
Supported versions
------------------

At any one time, the FMLD Tech Team will support the latest patch release of the last
released minor version plus the last patch release of the previous minor version.

The previous minor version will only receive security and bug fixes. If a patch does not clearly
fit in these categories, it is up to the maintainers to decide if it can be backported to a previous version.

The latest patch releases are the only ones officially supported. Users should always run the
latest patch release for the minor release they are on, as they contain important bug fixes and security updates.
Running FMLD in an unsupported version puts your site and data at risk.

Because patch releases don't include backwards incompatible changes, the
upgrade process (as described in :doc:`upgrading/upgrade-package-to-patch-release`)
should be straightforward.

Extension maintainers can decide at their discretion to support older FMLD versions.


.. seealso::

   :doc:`/changelog`
     The changelog lists all FMLD releases and the main changes introduced in
     each release.

   :doc:`/contributing/release-process`
     Documentation of the process that the FMLD developers follow to do a
     FMLD release.

