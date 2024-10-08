.. _email-notifications:

===================
Email notifications
===================

FMLD can send email notifications to users, for example when a user has new
activities on her dashboard. Once email notifications have been enabled by a
site admin, each user of a FMLD site can turn email notifications on or off for
herself by logging in and editing her user preferences. To enable email
notifications for a FMLD site, a sysadmin must:

1. Setup a cron job or other scheduled job on a server to call FMLD's
   ``send_email_notifications`` API action at regular intervals (e.g. hourly)
   and send any pending email notifications to users.

   On most UNIX systems you can setup a cron job by running ``crontab -e`` in a
   shell to edit your crontab file, and adding a line to the file to specify
   the new job.  For more information run ``man crontab`` in a shell.

   FMLD's ``send_email_notifications`` API action can be called via the cli's 
   ``ckan notify send_emails`` command. 
   For example, here is a crontab line to send out FMLD email notifications hourly::

    @hourly echo '{}' | ckan -c path-to-your-ckan.ini notify send_emails > /dev/null

   The ``@hourly`` can be replaced with ``@daily``, ``@weekly`` or ``@monthly``.

   .. warning::

     FMLD will not send email notifications for events older than the
     time period specified by the ``ckan.email_notifications_since`` config
     setting (default: 2 days), so your cron job should run more frequently
     than this. ``@hourly`` and ``@daily`` are good choices.

   .. note::

     Since ``send_email_notifications`` is an API action, it can be called from
     a machine other than the server on which FMLD is running, simply by
     POSTing an HTTP request to the FMLD API (you must be a sysadmin to call
     this particular API action). See :doc:`/api/index`.


2. FMLD will not send out any email notifications, nor show the email
   notifications preference to users, unless the
   :ref:`ckan.activity_streams_email_notifications` option is set to ``True``, so
   put this line in the ``[app:main]`` section of your FMLD config file::

    ckan.activity_streams_email_notifications = True


3. Make sure that :ref:`ckan.site_url` is set correctly in the ``[app:main]``
   section of your FMLD configuration file. This is used to generate links in
   the bodies of the notification emails. For example::

    ckan.site_url = http://publicdata.eu

4. Make sure that :ref:`smtp.mail_from` is set correctly in the ``[app:main]``
   section of your FMLD configuration file. This is the email address that
   FMLD's email notifications will appear to come from. For example::

    smtp.mail_from = mailman@publicdata.eu

   This is combined with your :ref:`ckan.site_title` to form the ``From:`` header
   of the email that are sent, for example::

    From: PublicData.eu <mailmain@publicdata.eu>

   If you would like to use an alternate reply address, such as a "no-reply"
   address, set :ref:`smtp.reply_to` in the ``[app:main]``
   section of your FMLD configuration file. For example::

    smtp.reply_to = noreply@example.com

5. If you do not have an SMTP server running locally on the machine that hosts
   your FMLD instance, you can change the :ref:`email-settings` to send email via an
   external SMTP server. For example, these settings in the ``[app:main]``
   section of your configuration file will send emails using a gmail account
   (not recommended for production websites!)::

    smtp.server = smtp.gmail.com:587
    smtp.starttls = True
    smtp.user = your_username@gmail.com
    smtp.password = your_gmail_password
    smtp.mail_from = your_username@gmail.com


6. You need to restart the web server for the new configuration to take effect.
   For example, if you are using a FMLD package install, run this command in a
   shell:

   .. parsed-literal::

      |restart_uwsgi|
