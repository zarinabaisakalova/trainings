_author_ = 'zarina'

from sys import maxsize

class Contact:

    def __init__(self, id=None, firstname=None, lastname=None, middlename=None, nickname=None, title=None, company=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, fax=None,
                 homepage=None, address2=None, notes=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None,
                 ayear=None, email=None, email2=None, email3=None):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.nickname = nickname
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.fax = fax
        self.address = address
        self.address2 = address2
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.title = title
        self.company = company
        self.homepage = homepage
        self.notes = notes
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear


    def __repr__(self):
        #return f'{self.id}:{self.firstname} {self.lastname}'
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) \
               and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

