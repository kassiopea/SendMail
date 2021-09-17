from constants import Urls
from models.letter import Letter
from pages.base_page import BasePage
from pages.locators import LetterPageLocators


class LetterPage(BasePage):
    def should_be_letter_page(self):
        self.should_be_current_page(Urls.LETTER_PAGE)

    def should_be_letter_content(self):
        assert self.is_element_present(
            *LetterPageLocators.LETTER_CONTAINER
        )

    def should_be_current_letter(
            self,
            expected_letter: dict
    ) -> None:
        subject = self.browser.find_element(
            *LetterPageLocators.LETTER_SUBJECT
        ).text
        letter_from = self.browser.find_element(
            *LetterPageLocators.LETTER_FROM
        )
        mail_from = letter_from.get_attribute("title")
        mail_to = self.browser.find_element(
            *LetterPageLocators.LETTER_TO
        ).text
        letter_msg = self.browser.find_element(
            *LetterPageLocators.LETTER_TEXT_BODY
        ).text
        actual_letter = Letter(
            to=mail_to,
            author=mail_from,
            subject=subject,
            message=letter_msg
        )
        current_letter = vars(actual_letter)
        assert expected_letter == current_letter
