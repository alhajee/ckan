#!/bin/sh

# Database Creation
psql --host=ckan-postgres --username=ckan --command="CREATE USER ${FMLD_POSTGRES_USER} WITH PASSWORD '${FMLD_POSTGRES_PWD}' NOSUPERUSER NOCREATEDB NOCREATEROLE;"
createdb --encoding=utf-8 --host=ckan-postgres --username=ckan --owner=${FMLD_POSTGRES_USER} ${FMLD_POSTGRES_DB}
psql --host=ckan-postgres --username=ckan --command="CREATE USER ${FMLD_DATASTORE_POSTGRES_READ_USER} WITH PASSWORD '${FMLD_DATASTORE_POSTGRES_READ_PWD}' NOSUPERUSER NOCREATEDB NOCREATEROLE;"
psql --host=ckan-postgres --username=ckan --command="CREATE USER ${FMLD_DATASTORE_POSTGRES_WRITE_USER} WITH PASSWORD '${FMLD_DATASTORE_POSTGRES_WRITE_PWD}' NOSUPERUSER NOCREATEDB NOCREATEROLE;"
createdb --encoding=utf-8 --host=ckan-postgres --username=ckan --owner=${FMLD_DATASTORE_POSTGRES_WRITE_USER} ${FMLD_DATASTORE_POSTGRES_DB}

# Database Initialization
ckan -c test-core-circle-ci.ini datastore set-permissions | psql --host=ckan-postgres --username=ckan
psql --host=ckan-postgres --username=ckan --dbname=${FMLD_DATASTORE_POSTGRES_DB} --command="CREATE extension tablefunc;"
ckan -c test-core-circle-ci.ini db init
gunzip .test_durations.gz

# git doesn't like having the directory owned by a different user, and
# we're mounting this in from external, so we don't know the uid/gid.
# this is required to build the docs
git config --global --add safe.directory /usr/src
