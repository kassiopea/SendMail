from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasePageLocators


class BasePage:
    def __init__(
            self,
            browser,
            url,
            timeout=2
    ):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def click_button(self, how, what):
        button = self.browser.find_element(how, what)
        button.click()

    def open_profile_dropdown(self):
        self.click_button(*BasePageLocators.PROFILE_DROPDOWN)

    def should_be_logout_link(self):
        assert self.is_element_present(*BasePageLocators.LOGOUT_LINK)

    def logout(self):
        self.click_button(*BasePageLocators.LOGOUT_LINK)

    def is_element_present(
            self,
            how,
            what,
            timeout=2
    ):
        try:
            WebDriverWait(
                self.browser,
                timeout
            ).until(
                EC.presence_of_element_located(
                    (
                        how,
                        what
                    )
                )
            )
        except:
            return False
        return True

    def is_not_element_present(
            self,
            how,
            what,
            timeout=2
    ):
        try:
            WebDriverWait(
                self.browser,
                timeout
            ).until(
                EC.presence_of_element_located(
                    (
                        how,
                        what
                    )
                )
            )
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def select_element_in_dropdown_by_value(
            self,
            how,
            what,
            value
    ):
        select = Select(self.browser.find_element(how, what))
        select.select_by_value(value)

    def should_be_current_email_in_header(
            self,
            email: str
    ) -> None:
        email_in_header = self.browser.find_element(
            *BasePageLocators.EMAIL_IN_HEADER
        ).text
        assert email_in_header == email

    def should_be_current_page(self, excepted_url):
        current_url = self.browser.current_url
        assert excepted_url == current_url,\
            f"Текущий url {current_url}" \
            f" не соответствует {excepted_url}"
