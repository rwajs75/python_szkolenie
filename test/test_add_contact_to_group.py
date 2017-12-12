__autor__ = 'Roman'
from model.contacts import Contacts
from model.group import Group
import random


def test_add_contact_to_group(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="Tester", lastname="Test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Dodana przed kasowaniem"))
    contacts = db.get_contacts_list()
    contact = random.choice(contacts)
    groups = db.get_group_list()
    group = random.choice(groups)
    app.contacts.contact_group(group.id)
    old_contact_group = app.contacts.get_contacts_list_in_group()
    app.contacts.all_contacts()
    app.contacts.add_contact_to_group_id(contact.id, group.id)
    new_contact_group = app.contacts.get_contacts_list_in_group()
    print(old_contact_group)
    print(new_contact_group)
    print(contact.id)
    assert sorted(old_contact_group, key=Contacts.id_or_max) == sorted(new_contact_group, key=Contacts.id_or_max)



