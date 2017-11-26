# -*- coding: utf-8 -*-
from model.contacts import Contacts
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contacts(firstname=firstname, lastname=lastname, nickname=nickname)
    for firstname in ["", random_string("Imie", 10)]
    for lastname in ["", random_string("Nazwisko", 20)]
    for nickname in ["", random_string("Nick", 20)]
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new(app, contact):
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.create(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)






