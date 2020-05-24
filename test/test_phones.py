_author_ = 'zarina'

import re
from random import randrange
from model.contact import Contact

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_info_from_edit_page)
    assert contact_from_home_page.firstname == contact_info_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_info_from_edit_page.lastname
    assert contact_from_home_page.address == contact_info_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_email_like_on_homepage(contact_info_from_edit_page)
#def test_phones_on_contact_view_page(app):
    #contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    #contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    #assert contact_from_view_page.homephone == contact_info_from_edit_page.homephone
    #assert contact_from_view_page.workphone == contact_info_from_edit_page.workphone
    #assert contact_from_view_page.mobilephone == contact_info_from_edit_page.mobilephone
    #assert contact_from_view_page.secondaryphone == contact_info_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[() -]", "", s)

#Техника обратных проверок
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_email_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3]))))


def test_check_all_contact_fields(app, db):
    if len(db.get_contact_list()) == 0:
        contact = (Contact(firstname="Petr", lastname="Petrov", middlename="Petrovich", nickname="Petya", title="empty",
            company="New_company", address="Msk", homephone="1234567", workphone="7654321", mobilephone="89162345678",
            fax="9876543", email="test1@test.ru", email2="test2@test.ru", email3="test3@test.ru",
            homepage="empty", address2="Spb", secondaryphone="909876678", notes="empty", aday="1",
            amonth="March", ayear="1990", bday="1", bmonth="March", byear="1990"))
        app.contact.create(contact)
    contacts_list = app.contact.get_contact_list()
    for contact in contacts_list:
        assert contact.firstname == db.get_contact_id(contact.id).firstname
        assert contact.lastname == db.get_contact_id(contact.id).lastname
        assert contact.address == db.get_contact_id(contact.id).address
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(db.get_contact_id(contact.id))
        assert contact.all_emails_from_home_page == merge_email_like_on_homepage(db.get_contact_id(contact.id))