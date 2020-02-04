_author_ = 'zarina'

from model.contact import Contact


def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New Petr"))
    app.session.logout()


def test_modify_contact_header(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(middlename="New Petrov"))
    app.session.logout()


def test_modify_contact_footer(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(mobile="New 89162935001"))
    app.session.logout()