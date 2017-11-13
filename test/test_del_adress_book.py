__autor__ = 'Roman'
from model.contacts import Contacts


def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="Tester", lastname="Test", nickname="ttest"))
    app.contacts.delete_first_contact()

