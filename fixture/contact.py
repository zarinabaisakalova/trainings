_author_ = 'zarina'
from selenium.webdriver.support.select import Select
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.app.fill_form("firstname", contact.firstname)
        self.app.fill_form("lastname", contact.lastname)
        self.app.fill_form("home", contact.homephone)
        self.app.fill_form("mobile", contact.mobilephone)
        self.app.fill_form("work", contact.workphone)
        self.app.fill_form("phone2", contact.secondaryphone)
        self.app.fill_form("address", contact.address)
        self.app.fill_form("email", contact.email)


    def modify_first(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.app.select_contact_by_index(index)
        # open modification form
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Edit")) > 0:
            return
        wd.find_elements_by_css_selector("img[title='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        if wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("update")) > 0:
            return
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact_new):
        wd = self.app.wd
        self.app.open_home_page()
        self.app.select_contact_by_id(id)
        # open modification form
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Edit")) > 0:
            return
        wd.find_element_by_xpath("//input[@id='%s']/parent::td/following-sibling::td[7]//img[@title='Edit']" % id).click()
        self.fill_contact_form(contact_new)
        # submit modification
        if wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("update")) > 0:
            return
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        self.app.select_contact_by_index(index)
        # submit deletion
        if wd.current_url.endswith("/delete.php?") and len(wd.find_elements_by_name("Delete")) > 0:
            return
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # accept to alert
        wd.switch_to_alert().accept()
        #alert = wd.switch_to_alert()
        #alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page()
        self.app.select_contact_by_id(id)
        # submit deletion
        if wd.current_url.endswith("/delete.php?") and len(wd.find_elements_by_name("Delete")) > 0:
            return
        self.select_contact_by_id(id)
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def return_to_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("home")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def count_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_emails_from_home_page=all_emails, address=address,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        #wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)

    def add_contact_in_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        # select contact
        self.select_contact_by_id(contact_id)
        # select group
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_css_selector("select[name=\"to_group\"]")).select_by_value('%s' % group_id)
        # add contact in group
        wd.find_element_by_name("add").click()

    def delete_contact_from_group(self, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.group_page_with_contact(group_id)
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@name='remove']").click()

    def group_page_with_contact(self, group_id):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_css_selector("select[name=\"group\"]")).select_by_value('%s' % group_id)