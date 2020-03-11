_author_ = 'zarina'

from model.contact import Contact

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
        self.app.fill_form("mobile", contact.mobile)

    def modify_first(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
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
            self.return_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                contact_id = element.find_element_by_css_selector("td:nth-child(1) input").get_attribute("id")
                lastname = element.find_element_by_css_selector("td:nth-child(2)").text
                firstname = element.find_element_by_css_selector("td:nth-child(3)").text
                self.contact_cache.append(Contact(contact_id=contact_id, firstname=firstname, lastname=lastname))
        return list(self.contact_cache)