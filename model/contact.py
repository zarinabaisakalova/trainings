_author_ = 'zarina'

from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, mobile=None, contact_id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.mobile = mobile
        self.contact_id = contact_id

    def __repr__(self):
        return f'{self.contact_id}:{self.firstname} {self.lastname}'

    def __eq__(self, other):
        return (self.contact_id == other.contact_id or self.contact_id is None or other.contact_id is None) \
               and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize

