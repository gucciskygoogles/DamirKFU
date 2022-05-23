from pages.base_page import BasePage
from pages.locators import HomePageLocators, MainPageLocators


class HomePage(BasePage):

    def exit(self):
        self.browser.find_element(*HomePageLocators.EXIT).click()
        assert self.is_element_present(*MainPageLocators.REGISTRATION_MENU_BTN)