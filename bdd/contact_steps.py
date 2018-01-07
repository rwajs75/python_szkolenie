__autor__ = 'Roman'

from pytest_bdd import given, when, then
from model.contacts import Contacts
import random


@given('a contact list')
def contact_list(db):
    return db.get_contacts_list()

@given('a contact with <firstname> and <lastname>')
def new_contact(firstname, lastname):
    return Contacts(firstname=firstname, lastname=lastname)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contacts.create(new_contact)

@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, new_contact, contact_list):
    old_contacts = contact_list
    new_contacts = db.get_contacts_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="Tester", lastname="Test"))
    return db.get_contacts_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    return app.contacts.delete_contact_by_id(random_contact.id)

@then('the new contact list is equal to the old list without deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contacts_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contacts_list(),
                                                                      key=Contacts.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="Tester", lastname="Test"))
    return db.get_contacts_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I modify the contact from the list')
def modify_contact(app, random_contact):
    return app.contacts.modify_contact_by_id(random_contact.id, random_contact)

@then('the modify contact list is equal to the old list without modified contact')
def verify_contact_modified(db, non_empty_contact_list, random_contact, check_ui, firstname, lastname):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contacts_list()
    old_contacts.rename(random_contact, Contacts(firstname=firstname, lastname=lastname))
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contacts_list(),
                                                                      key=Contacts.id_or_max)