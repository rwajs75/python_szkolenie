__autor__ = 'Roman'
from model.contacts import Contacts
from model.group import Group
import random


def test_del_contact_from_group(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="Tester", lastname="Test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Dodana przed kasowaniem"))
    groups = db.get_group_list()
    group = random.choice(groups)
    old_contact_group = db.get_contacts_in_group(group)
    contact_group = random.choice(old_contact_group)
    if len(old_contact_group) == 0:
        contacts = db.get_contacts_list()
        contact = random.choice(contacts)
        app.contacts.add_contact_to_group_id(contact.id, group.id)
    app.contacts.del_contact_from_group_id(contact_group)
    new_contact_group = db.get_contacts_in_group(group)
    old_contact_group.remove(contact_group)
    assert sorted(old_contact_group, key=Contacts.id_or_max) == sorted(new_contact_group, key=Contacts.id_or_max)




