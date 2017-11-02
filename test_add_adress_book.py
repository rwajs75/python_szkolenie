# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contacts import Contacts

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_adress_book(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_new(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, password="secret", username="admin")
        self.open_add_new(wd)
        self.create_new_adress_book(wd, Contacts(firstname="Roman", lastname="Wajs", nickname="rwajs",
                                                 company="własna działalność", adress="ul. Czapli 3, 05-830 Nadarzyn", home="159753123",
                                                 mobile="123654789", work="987654123", fax="456852159", email="rwajs@tlen.pl", byear="1975"))
        self.details(wd)
        self.logout(wd)

    def test_add_new1(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, password="secret", username="admin")
        self.open_add_new(wd)
        self.create_new_adress_book(wd, Contacts(firstname="Roman1", lastname="Wajs1", nickname="rwajs1",
                                                 company="własna działalność1", adress="ul. Czapli 3, 05-830 Nadarzyn1", home="159753123",
                                                 mobile="123654789", work="987654123", fax="456852159", email="rwajs1@tlen.pl", byear="1979"))
        self.details(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def details(self, wd):
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()

    def create_new_adress_book(self, wd, data_adress):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(data_adress.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(data_adress.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(data_adress.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(data_adress.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(data_adress.adress)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(data_adress.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(data_adress.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(data_adress.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(data_adress.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(data_adress.email)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[25]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[25]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[25]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[25]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(data_adress.byear)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_add_new(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, password, username):
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
