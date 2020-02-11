_author_ = 'zarina'

from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="test1"))
    app.contact.modify_first_contact(Contact(firstname="New Petr"))


def test_modify_contact_header(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(middlename="test2"))
    app.contact.modify_first_contact(Contact(middlename="New Petrov"))


def test_modify_contact_footer(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(mobile="test3"))
    app.contact.modify_first_contact(Contact(mobile="New 89162935001"))