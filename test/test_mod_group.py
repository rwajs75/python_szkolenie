__autor__ = 'Roman'

from time import sleep
from model.group import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="zmodyfikacja", header="modyfikacja", footer="modyfikacja"))
    app.session.logout()
    sleep(1)