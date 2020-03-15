_author_ = 'zarina'

from model.contact import Contact
from random import randrange

def test_modify_some_contact_name(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="test1"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New Petr", lastname="New Petrov")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count_contact()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_header(app):
    #if app.contact.count_contact() == 0:
       # app.contact.create(Contact(lastname="test2"))
   # app.contact.modify_first_contact(Contact(lastname="New Petrov"))


#def test_modify_contact_footer(app):
   # if app.contact.count_contact() == 0:
    #    app.contact.create(Contact(mobilephone="test3"))
    #app.contact.modify_first_contact(Contact(mobilephone="New 89162935001"))