from selenium.webdriver import ActionChains

from constants import ComposePageMessages
from pages.base_page import BasePage
from pages.locators import ComposePageLocators


class ComposePage(BasePage):

    def fill_email_field(
            self,
            email: str
    ) -> None:
        to_input = self.browser.find_element(
            *ComposePageLocators.FIELD_TO
        )
        action = ActionChains(self.browser)
        action.click(to_input).send_keys(email).perform()

    def fill_subject_field(
            self,
            subject: str
    ) -> None:
        subject_input = self.browser.find_element(
            *ComposePageLocators.SUBJECT_INPUT
        )
        action = ActionChains(self.browser)
        action.click(subject_input).send_keys(subject).perform()

    def fill_message_field(
            self,
            message: str
    ) -> None:
        message_field = self.browser.find_element(
            *ComposePageLocators.MESSAGE_FIELD
        )
        action = ActionChains(self.browser)
        action.click(message_field).send_keys(message).perform()

    def send_letter(
            self,
            letter: dict
    ) -> None:
        self.fill_email_field(
            email=letter["to"]
        )
        self.fill_subject_field(
            subject=letter["subject"]
        )
        self.fill_message_field(
            message=letter["message"]
        )
        send_letter_btn = self.browser.find_element(
            *ComposePageLocators.SEND_LETTER_BTN
        )
        send_letter_btn.click()

    def should_be_compose_app(self):
        assert self.is_element_present(
            *ComposePageLocators.COMPOSE_APP
        )

    def should_be_ntf_about_dispatch(self):
        element_with_ntf = self.browser.find_element(
            *ComposePageLocators.NTF_AFTER_DISPATCH
        )
        assert element_with_ntf.text == ComposePageMessages.\
            MSG_AFTER_SENT_LETTER,\
            "Нет сообщения об отправке"

    def should_be_popup_after_dispatch(self):
        assert self.is_element_present(
            *ComposePageLocators.POPUP_AFTER_DISPATCH
        )
