_author_ = 'zarina'

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

    def fill_contact_form(self, contact):
        self.app.fill_form("firstname", contact.firstname)
        self.app.fill_form("middlename", contact.middlename)
        self.app.fill_form("mobile", contact.mobile)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.select_first()
        # open modification form
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Edit")) > 0:
            return
        wd.find_element_by_css_selector("img[title='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        if wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("update")) > 0:
            return
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.select_first()
        # submit deletion
        if wd.current_url.endswith("/delete.php?") and len(wd.find_elements_by_name("Delete")) > 0:
            return
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # accept to alert
        wd.switch_to_alert().accept()
        #alert = wd.switch_to_alert()
        #alert.accept()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("home")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def count_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))