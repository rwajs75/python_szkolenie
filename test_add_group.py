# -*- coding: utf-8 -*-
import pytest
from group import Group
from aplication import Aplication

@pytest.fixture
def app(request):
    fixture = Aplication
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test2", header="test2", footer="test2"))
    app.logout()

def test_add_empy_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
