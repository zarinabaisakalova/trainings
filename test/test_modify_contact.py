_author_ = 'zarina'

from model.contact import Contact
import random

def test_modify_some_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_new = Contact(firstname="New Petr", lastname="New Petrov")
    #contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact_new)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    def clean(contact):
        return Contact(id=contact.id, lastname=contact.lastname.strip(), firstname=contact.firstname.strip())
    if check_ui:
        assert sorted(map(clean, new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_modify_contact_header(app):
    #if app.contact.count_contact() == 0:
       # app.contact.create(Contact(lastname="test2"))
   # app.contact.modify_first_contact(Contact(lastname="New Petrov"))


#def test_modify_contact_footer(app):
   # if app.contact.count_contact() == 0:
    #    app.contact.create(Contact(mobilephone="test3"))
    #app.contact.modify_first_contact(Contact(mobilephone="New 89162935001"))