__autor__ = 'Roman'
from model.contacts import Contacts
import random


def test_modify_contact_by_id(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="Tester", lastname="Test", nickname="ttest"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    contact.firstname = "Roman4"
    contact.lastname = "Wajs4"
    app.contacts.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contacts_list()
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contacts_list(), key=Contacts.id_or_max)
