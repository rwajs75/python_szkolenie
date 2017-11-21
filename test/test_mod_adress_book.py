__autor__ = 'Roman'
from model.contacts import Contacts

def test_modify_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="Tester", lastname="Test", nickname="ttest"))
    old_contacts = app.contacts.get_contacts_list()
    contact =Contacts(firstname="Roman4", lastname="Wajs4", nickname="rwajs4",
                                 mobile="987654321", email="rwajs@gmail.pl", byear="1999")
    app.contacts.modify_first_contact(contact)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

