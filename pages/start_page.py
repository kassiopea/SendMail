from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from pages.locators import StartPageLocators


class StartPage(BasePage):

    def fill_the_mail_field(
            self,
            login: str
    ) -> None:
        email_input = self.browser.find_element(
            *StartPageLocators.EMAIL_INPUT
        )
        email_input.click()
        email_input.clear()
        email_input.send_keys(login)

    def click_on_enter_pwd_btn(self):
        self.click_button(
            *StartPageLocators.ENTER_PWD_BTN
        )

    def fill_the_password_field(self, password):
        password_input = self.browser.find_element(
            *StartPageLocators.PASSWORD_INPUT
        )
        password_input.click()
        password_input.clear()
        password_input.send_keys(password)

    def select_domain(self, domain):
        self.select_element_in_dropdown_by_value(
            *StartPageLocators.EMAIL_DOMAIN_DROPDOWN,
            domain
        )

    def send_login_form(self):
        self.click_button(
            *StartPageLocators.LOGIN_TO_MAIL_BTN
        )

    def should_be_enter_btn(self):
        assert self.is_element_present(
            *StartPageLocators.ENTER_PWD_BTN
        ),\
            "Нет кнопки 'Войти'"

    def should_be_mail_box(self):
        assert self.is_element_present(
            *StartPageLocators.MAIL_BLOCK
        ),\
            "Нет блока для авторизации почты"

    def should_not_be_error(self):
        assert self.is_not_element_present(
            *StartPageLocators.ERROR_LOGIN
        ),\
            "Ошибка при заполнении полей для логина"

    def open_login_popup(self):
        login_btn = self.browser.find_element(*StartPageLocators.LOGIN_BTN)
        login_btn.click()

    def should_be_login_bnt(self):
        assert self.is_element_present(*StartPageLocators.LOGIN_BTN)

    def should_be_login_popup(self):
        assert self.is_element_present(*StartPageLocators.LOGIN_POPUP, timeout=40)

    def fill_username_in_login_field(self, username):
        username_input = self.browser.find_element(*StartPageLocators.USERNAME_INPUT)
        action = ActionChains(self.browser)
        action.click(username_input).send_keys(username)