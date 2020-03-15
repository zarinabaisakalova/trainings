_author_ = 'zarina'

import re
from random import randrange


def test_information_on_home_page(app):
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_info_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_info_from_edit_page.lastname
    assert contact_from_home_page.address == contact_info_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_email_like_on_home_page(contact_info_from_edit_page)


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2,
                                                                                contact.email3])))