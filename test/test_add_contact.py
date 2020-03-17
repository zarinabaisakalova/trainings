# -*- coding: utf-8 -*-
from model.contact import Contact
import string
import random
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", homephone="", mobilephone="", workphone="", address="",
                   email="", email2="", email3="")] + \
          [Contact(firstname=random_string("first", 10), lastname=random_string("last", 9),
                   homephone=random_string("8900",7 ), mobilephone=random_string("8900", 7),
                   workphone=random_string("323537", 5), address=random_string("moscow", 7),
                   email=random_string("f@f.", 3), email2=random_string("f@f.", 3),
                   email3=random_string("f@f.", 3)) for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count_contact()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)