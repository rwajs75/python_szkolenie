from model.contacts import Contacts
import json


# testdata = [
#     Group(name="name1", header="header1", footer="footer1"),
#     Group(name="name2", header="header2", footer="footer2")
# ]


with open("../data/contacts.json") as f:
    try:
        read_plik = json.load(f)
    except ValueError as ex:
        print(ex)
        read_plik = []

testdata = [
    Contacts(firstname=read_plik[i]['firstname'], lastname=read_plik[i]['lastname'], nickname=read_plik[i]['nickname'])
    for i in range(len(read_plik))
]

