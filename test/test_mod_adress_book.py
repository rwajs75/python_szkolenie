__autor__ = 'Roman'
from model.contacts import Contacts

def test_modify_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="Tester", lastname="Test", nickname="ttest"))
    app.contacts.modify_first_contact(Contacts(firstname="Roman4", lastname="Wajs4", nickname="rwajs4",
                                 mobile="987654321", email="rwajs@gmail.pl", byear="1999"))

