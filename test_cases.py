import pytest

from pages.main_page import MainPage


class TestCases:

    def test_autorisation(self, browser, url):
        page = MainPage(browser, url)
        page.open()
        page.autorisation_is_correct()

    @pytest.mark.xfail
    def test_registration_as_student(self, browser, url):
        page = MainPage(browser, url)
        page.open()
        page.registration_stud()

    @pytest.mark.xfail
    def test_registration_as_teacher(self, browser, url):
        page = MainPage(browser, url)
        page.open()
        page.registration_teacher()

    def test_auth_and_exit(self, browser, url):
        page = MainPage(browser, url)
        page.open()
        home_page = page.autorisation_is_correct()
        home_page.exit()