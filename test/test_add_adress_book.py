# -*- coding: utf-8 -*-

from model.contacts import Contacts


def test_add_new(app):
    app.contacts.create(Contacts(firstname="Roman", lastname="Wajs", nickname="rwajs",
                                 company="własna działalność", adress="ul. Czapli 3, 05-830 Nadarzyn", home="159753123",
                                 mobile="123654789", work="987654123", fax="456852159", email="rwajs@tlen.pl", byear="1975"))

def test_add_new1(app):
    app.contacts.create(Contacts(firstname="Roman1", lastname="Wajs1", nickname="rwajs1",
                                 company="własna działalność1", adress="ul. Czapli 3, 05-830 Nadarzyn1", home="159753123",
                                 mobile="123654789", work="987654123", fax="456852159", email="rwajs1@tlen.pl", byear="1979"))



