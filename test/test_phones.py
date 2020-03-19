_author_ = 'zarina'

import re
from random import randrange

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_info_from_edit_page)
    assert contact_from_home_page.firstname == contact_info_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_info_from_edit_page.lastname
    assert contact_from_home_page.address == contact_info_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_phones_like_on_home_page(contact_info_from_edit_page)
#def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_info_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_info_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_info_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_info_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[() -]", "", s)

#Техника обратных проверок
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone,
                                        contact.email, contact.email2, contact.email3]))))