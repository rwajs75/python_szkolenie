__autor__ = 'Roman'
from model.contacts import Contacts
from model.group import Group
import random


def test_add_contact_to_group(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="Tester", lastname="Test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Dodana przed kasowaniem"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.get_contacts_not_in_group_id(group)
    contact = random.choice(contacts)
    old_contact_group = db.get_contacts_in_group_id(group)
    app.contacts.add_contact_to_group_id(contact.id, group.id)
    new_contact_group = db.get_contacts_in_group_id(group)
    old_contact_group.append(contact)
    assert sorted(old_contact_group, key=Contacts.id_or_max) == sorted(new_contact_group, key=Contacts.id_or_max)



