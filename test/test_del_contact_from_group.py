__autor__ = 'Roman'
from model.contacts import Contacts
from model.group import Group
import random


def test_del_contact_from_group(app, db):
    if len(db.get_contacts_in_group()) == 0:
        contacts = db.get_contacts_list()
        contact = random.choice(contacts)
        groups = db.get_group_list()
        group = random.choice(groups)
        app.contacts.add_contact_to_group_id(contact.id, group.id)
    groups_with_contacts = db.get_contacts_in_group()
    group_with_contacts = random.choice(groups_with_contacts)
    old_contact_group = app.contacts.get_contacts_list_in_group()
    app.contacts.del_contact_from_group_id(group_with_contacts)
    new_contact_group = app.contacts.get_contacts_list_in_group()
    print(old_contact_group)
    print(new_contact_group)





