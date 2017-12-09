__autor__ = 'Roman'
from model.contacts import Contacts
import random
from time import sleep


def test_delete_some_contact(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="Tester", lastname="Test"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(contact.id)
    sleep(1)
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

