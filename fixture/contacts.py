__autor__ = 'Roman'
from model.contacts import Contacts
import re

class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def open_adress_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def open_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contacts_form(self, data_adress):
        wd = self.app.wd
        self.change_field_value("firstname", data_adress.firstname)
        self.change_field_value("lastname", data_adress.lastname)
        self.change_field_value("nickname", data_adress.nickname)
        self.change_field_value("company", data_adress.company)
        self.change_field_value("address", data_adress.adress)
        self.change_field_value("home", data_adress.home)
        self.change_field_value("mobile", data_adress.mobile)
        self.change_field_value("work", data_adress.work)
        self.change_field_value("fax", data_adress.fax)
        self.change_field_value("email", data_adress.email)
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
        self.change_field_value("byear", data_adress.byear)

    def create(self, data_adress):
        wd = self.app.wd
        self.open_add_new()
        self.fill_contacts_form(data_adress)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_adress_page()
        self.select_contact_by_index(index)
        # przycisk delete
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def modify_first_contact(self, new_data_adress):
        self.modify_contact_by_index

    def modify_contact_by_index(self, index):
        wd = self.app.wd
        self.open_adress_page()
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[" + str(index+2) + "]/td[8]/a/img").click()
        # self.fill_contacts_form(new_data_adress)
        # wd.find_element_by_xpath("//*[@id='content']/form[1]/input[22]").click()
        # self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_adress_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_adress_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                adress = cells[3].text
                email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contacts(id=id, firstname=firstname, lastname=lastname,
                                                   all_phones_from_home_page = all_phones, adress=adress, email=email))
            return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.modify_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        adress = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        return Contacts(id=id, firstname=firstname, lastname=lastname,
                        home=home, mobile=mobile, work=work, fax=fax, adress=adress, email=email)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_adress_page()
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[7]/a/img").click()


    def get_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        name = re.search("(.*)", text).group(1)
        adress = re.search("\n(.*)\n(.*)\n(.*)", text).group(3)
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        text = wd.page_source
        email = re.search('mailto:(.*)"', text).group(1)
        return Contacts(name=name, home=home, mobile=mobile, work=work, fax=fax, adress=adress,
                        email=email)

