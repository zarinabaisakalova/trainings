_author_ = 'zarina'

from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="New Petr"))


def test_modify_contact_header(app):
    app.contact.modify_first_contact(Contact(middlename="New Petrov"))


def test_modify_contact_footer(app):
    app.contact.modify_first_contact(Contact(mobile="New 89162935001"))