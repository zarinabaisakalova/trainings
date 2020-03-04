_author_ = 'zarina'

from model.contact import Contact


def test_modify_contact_name(app):
    old_contacts = app.contact.get_contact_list()
    #if app.contact.count_contact() == 0:
      # app.contact.create(Contact(firstname="test1"))
    #app.contact.modify_first_contact(Contact(firstname="New Petr"))
    contact = old_contacts[0]
    contact.firstname = "New Petr"
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_header(app):
    #if app.contact.count_contact() == 0:
       # app.contact.create(Contact(middlename="test2"))
   # app.contact.modify_first_contact(Contact(middlename="New Petrov"))


#def test_modify_contact_footer(app):
   # if app.contact.count_contact() == 0:
    #    app.contact.create(Contact(mobile="test3"))
    #app.contact.modify_first_contact(Contact(mobile="New 89162935001"))