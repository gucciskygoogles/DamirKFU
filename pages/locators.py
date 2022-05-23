from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_FIELD = (By.NAME, 'login')
    PASSWORD_FIELD = (By.NAME, 'password')
    ENTER_BTN = (By.XPATH, '//*[@value="Войти"]')
    REGISTRATION_MENU_BTN = (By.XPATH, '//*[@id="root"]/main/div/div[1]/div/button')
    REPEAT_PASSWORD = (By.NAME, 'repeat-password')
    FIO = (By.XPATH, "//*[@name='name']")
    ROLE_STUDENT = (By.XPATH, '//*[@id="grid-state"]/option[2]')
    ROLE = (By.XPATH, '//*[@name="role"]')
    REGISTRATION_BTN = (By.XPATH, '//*[@id="root"]/main/div/div[1]/div/form/input')
    ROLE_TEACHER = (By.XPATH, '//*[@id="grid-state"]/option[3]')

class HomePageLocators:

    PROFILE_BTN = (By.XPATH, '//*[@id="root"]/div/main/div[1]/div/ul/li[2]/a')
    EXIT = (By.XPATH, "//div[@class='cursor-pointer justify-self-end']//*[name()='svg']")