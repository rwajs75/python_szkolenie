__autor__ = 'Roman'
from model.contacts import Contacts

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

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_adress_page()
        self.select_first_contact()
        # przycisk delete
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, new_data_adress):
        wd = self.app.wd
        self.open_adress_page()
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contacts_form(new_data_adress)
        wd.find_element_by_xpath("//*[@id='content']/form[1]/input[22]").click()

    def count(self):
        wd = self.app.wd
        self.open_adress_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        wd = self.app.wd
        self.open_adress_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            lastname = element.find_elements_by_css_selector("td")[1].text
            firstname = element.find_elements_by_css_selector("td")[2].text
            contacts.append(Contacts(id=id, firstname=firstname, lastname=lastname))
        return contacts