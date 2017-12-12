__autor__ = 'Roman'


class AddressInGroups:
    def __init__(self, id=None, group_id=None):
        self.group_id = group_id
        self.id = id

    def __repr__(self):
        return "%s" % self.group_id




