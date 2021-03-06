import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contacts.get_contacts_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == clear(contact_from_edit_page.firstname)
    assert contact_from_home_page.lastname == clear(contact_from_edit_page.lastname)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.adress == contact_from_edit_page.adress
    assert contact_from_home_page.email == contact_from_edit_page.email

def test_phones_on_view_page(app):
    contact_from_view_page = app.contacts.get_from_view_page(0)
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.name == merge_name_on_home_page(contact_from_edit_page)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.fax == contact_from_edit_page.fax
    assert contact_from_view_page.adress == contact_from_edit_page.adress
    assert contact_from_view_page.email == contact_from_edit_page.email

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work]))))

def merge_name_on_home_page(contact):
    return " ".join([contact.firstname, contact.lastname])