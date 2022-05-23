import time
from pages.home_page import HomePage
from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.locators import HomePageLocators


class MainPage(BasePage):

    def input_login(self):
        login = self.browser.find_element(*MainPageLocators.LOGIN_FIELD)
        login.send_keys('iwillloveyou44@yandex.ru')

    def input_password(self):
        password = self.browser.find_element(*MainPageLocators.PASSWORD_FIELD)
        password.send_keys('12345qwerty')

    def autorisation_is_correct(self):
        self.input_login()
        self.input_password()
        button = self.browser.find_element(*MainPageLocators.ENTER_BTN)
        time.sleep(2)
        button.click()
        time.sleep(2)
        assert self.is_element_present(*HomePageLocators.PROFILE_BTN)
        return HomePage(browser=self.browser, url=self.browser.current_url)

    def switch_to_registration(self):
        registration_link = self.browser.find_element(*MainPageLocators.REGISTRATION_MENU_BTN)
        registration_link.click()

    def input_repeat_password(self):
        repeat = self.browser.find_element(*MainPageLocators.REPEAT_PASSWORD)
        repeat.send_keys('12345qwerty')

    def input_name(self):
        name = self.browser.find_element(*MainPageLocators.FIO)
        name.send_keys('Данилов Данилка Камилевич')

    def choose_role_stud(self):
        role_chooser = self.browser.find_element(*MainPageLocators.ROLE)
        role_chooser.click()
        self.browser.find_element(*MainPageLocators.FIO).click()
        self.browser.find_element(*MainPageLocators.ROLE_STUDENT).click()

    def choose_role_teacher(self):
        role_chooser = self.browser.find_element(*MainPageLocators.ROLE)
        role_chooser.click()
        self.browser.find_element(*MainPageLocators.FIO).click()
        self.browser.find_element(*MainPageLocators.ROLE_TEACHER).click()

    def registration_stud(self):
        self.switch_to_registration()
        self.input_login()
        self.input_password()
        self.input_repeat_password()
        self.input_name()
        self.choose_role_stud()
        self.browser.find_element(*MainPageLocators.REGISTRATION_BTN).click()
        assert self.is_element_present(*HomePageLocators.PROFILE_BTN)
        return HomePage(browser=self.browser, url=self.browser.current_url)

    def registration_teacher(self):
        self.switch_to_registration()
        self.input_login()
        self.input_password()
        self.input_repeat_password()
        self.input_name()
        self.choose_role_teacher()
        self.browser.find_element(*MainPageLocators.REGISTRATION_BTN).click()
        assert self.is_element_present(*HomePageLocators.PROFILE_BTN)
        return HomePage(browser=self.browser, url=self.browser.current_url)