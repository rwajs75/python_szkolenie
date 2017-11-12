__autor__ = 'Roman'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        # otwarcie strony dodawania nowej grupy
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # zapisanie nowej grupy
        wd.find_element_by_name("submit").click()
        self.return_groups_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # przycisk delete group(s)
        wd.find_element_by_name("delete").click()
        self.return_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # przycisk delete group(s)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # zapisanie nowej grupy
        wd.find_element_by_name("update").click()
        self.return_groups_page()

    def return_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

