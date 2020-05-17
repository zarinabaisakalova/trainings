from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
_author_ = 'zarina'

class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        #self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
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
        #self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_index(self, index):
        wd = self.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def destroy(self):
        self.wd.quit()