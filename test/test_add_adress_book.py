# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_new(app):
    old_contacts = app.contacts.get_contacts_list()
    contact = Contacts(firstname="Roman", lastname="Wajs", nickname="rwajs",
                                 company="własna działalność", adress="ul. Czapli 3, 05-830 Nadarzyn", home="159753123",
                                 mobile="123654789", work="987654123", fax="456852159", email="rwajs@tlen.pl", byear="1975")
    app.contacts.create(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

# def test_add_new1(app):
#     old_contacts = app.contacts.get_contacts_list()
#     contact = Contacts(firstname="Roman1", lastname="Wajs1", nickname="rwajs1",
#                                  company="własna działalność1", adress="ul. Czapli 3, 05-830 Nadarzyn1", home="159753123",
#                                  mobile="123654789", work="987654123", fax="456852159", email="rwajs1@tlen.pl", byear="1979")
#     app.contacts.create(contact)
#     new_contacts = app.contacts.get_contacts_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)




