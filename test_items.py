import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_element_by_css_selector(".btn-add-to-basket")
    except:
        assert False, 'The button "Add to basket" is not found'
    