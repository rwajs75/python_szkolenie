# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_new(app, db, data_contacts, check_ui):
    contact = data_contacts
    old_contacts = db.get_contacts_list()
    app.contacts.create(contact)
    # assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contacts_list(), key=Contacts.id_or_max)





