__autor__ = 'Roman'
from sys import maxsize

class Contacts:
    def __init__(self, firstname=None, lastname=None, nickname=None, company=None, adress=None, home=None, mobile=None,
                 work=None, fax=None, email=None, byear=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.adress = adress
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.byear = byear
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize