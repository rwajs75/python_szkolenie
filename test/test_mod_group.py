__autor__ = 'Roman'
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Dodana przed modyfikacją"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "zmodyfikowane"
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Dodana przed modyfikacją"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="zmodyfikowane"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
# def test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Dodana przed modyfikacją"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="zmodyfikowane"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
