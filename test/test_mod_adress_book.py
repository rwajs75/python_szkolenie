__autor__ = 'Roman'
from model.contacts import Contacts
from random import randrange


def test_modify_contact_by_index(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="Tester", lastname="Test", nickname="ttest"))
    old_contacts = app.contacts.get_contacts_list()
    contact =Contacts(firstname="Roman4", lastname="Wajs4", nickname="rwajs4",
                                 mobile="987654321", email="rwajs@gmail.pl", byear="1999")
    index = randrange(len(old_contacts))
    app.contacts.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[index] = contact
    #assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

