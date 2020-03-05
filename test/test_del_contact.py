__author__ = 'zarina'

from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count_contact()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts