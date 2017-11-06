# -*- coding: utf-8 -*-

from model.group import Group
from time import sleep


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test2", header="test2", footer="test2"))
    app.session.logout()
    sleep(1)

def test_add_empy_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
    sleep(1)
