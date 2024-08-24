# -*- coding: utf-8 -*-

import pytest
from pytest_factoryboy import register

from ckan.tests.factories import FMLDFactory
from ckanext.activity.model import Activity


@register
class ActivityFactory(FMLDFactory):
    """A factory class for creating FMLD activity objects."""

    class Meta:
        model = Activity
        action = "activity_create"


@pytest.fixture()
def clean_db(reset_db, migrate_db_for):
    reset_db()
    migrate_db_for("activity")
