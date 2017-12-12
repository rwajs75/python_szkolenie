__autor__ = 'Roman'
from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contacts import Contacts
from pymysql.converters import decoders
from model.address_in_groups import AddressInGroups

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        nickname = Optional(str, column='nickname')
        deprecated = Optional(datetime, column='deprecated')

    class ORMAddressInGroup(db.Entity):
        _table_ = 'address_in_groups'
        contact_id = PrimaryKey(int, column='id')
        group_id = Optional(int, column='group_id')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contacts(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname, nickname=contact.nickname)
        return list(map(convert, contacts))

    @db_session
    def get_contacts_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    def convert_to_list(self, address_in_groups):
        def convert(address_in_group):
            return AddressInGroups(id=address_in_group.id, group_id=address_in_group.group_id)
        return list(map(convert, address_in_groups))

    @db_session
    def get_contacts_in_group(self):
        return self.convert_to_list(select(a for a in ORMFixture.ORMAddressInGroup if a.deprecated is None))
