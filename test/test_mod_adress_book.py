__autor__ = 'Roman'

from time import sleep
from model.contacts import Contacts

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.modify_first_contact(Contacts(firstname="Roman4", lastname="Wajs4", nickname="rwajs4",
                                 company="własna działalność4", adress="ul. Czapli 34, 05-830 Nadarzyn4", home="159753123",
                                 mobile="123654789", work="987654123", fax="456852159", email="rwajs@tlen.pl", byear="1999"))
    app.session.logout()
    sleep(1)
