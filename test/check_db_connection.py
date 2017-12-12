__autor__ = 'Roman'
from fixture.db import DbFixture


db = DbFixture(host="localhost", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_in_group()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
