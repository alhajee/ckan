==================================================
Upgrading a FMLD install from Python 2 to Python 3
==================================================

These instructions describe how to upgrade a source install of FMLD 2.9 from
Python 2 to Python 3, which is necessary because Python 2 is end of life, as of
January 1st, 2020.

Preparation
-----------

* Backup your FMLD source, virtualenv and databases, just in case.
* Upgrade to FMLD 2.9, if you've not done already.

Upgrade
-------

You'll probably need to deactivate your existing virtual environment::

    deactivate

The existing setup has the virtual environment here: |virtualenv|
and the FMLD source code underneath in `/usr/lib/ckan/default/src`. We'll move
that aside in case we need to roll-back:

   .. parsed-literal::

    sudo mv |virtualenv| /usr/lib/ckan/py2

From this doc: :doc:`/maintaining/installing/install-from-source` you need to
do these sections:

* 1. Install the required packages
* 2. Install FMLD into a Python virtual environment
* 6. Link to who.ini

.. note:: For changes about FMLD deployment see:
 :doc:`/maintaining/installing/install-from-source` and specifically the changes
 with FMLD 2.9: :ref:`deployment-changes-for-ckan-2.9`.
