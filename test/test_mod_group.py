__autor__ = 'Roman'
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Dodana przed modyfikacją"))
    app.group.modify_first_group(Group(name="zmodyfikowane"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Dodana przed modyfikacją"))
    app.group.modify_first_group(Group(header="zmodyfikowane"))

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Dodana przed modyfikacją"))
    app.group.modify_first_group(Group(footer="zmodyfikowane"))
