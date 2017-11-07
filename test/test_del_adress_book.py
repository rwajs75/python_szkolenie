__autor__ = 'Roman'

from time import sleep


def test_delete_first_contact(app):
    app.session.login(password="secret", username="admin")
    app.contacts.delete_first_contact()
    app.session.logout()
    sleep(1)
