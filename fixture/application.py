from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
_author_ = 'zarina'

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        #self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        if (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("user")) > 0):
            return

    def fill_form(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first(self):
        wd = self.wd
        wd.find_element_by_name("selected[]").click()

    def destroy(self):
        self.wd.quit()