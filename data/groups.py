from model.group import Group
import json


# testdata = [
#     Group(name="name1", header="header1", footer="footer1"),
#     Group(name="name2", header="header2", footer="footer2")
# ]


with open("c:/Users/rwajs/Documents/GitHub/python_szkolenie/data/groups.json") as f:
    try:
        read_plik = json.load(f)
    except ValueError as ex:
        print(ex)
        read_plik = []

testdata = [
    Group(name=read_plik[i]['name'], header=read_plik[i]['header'], footer=read_plik[i]['footer'])
    for i in range(len(read_plik))
]

