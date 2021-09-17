from constants import Urls
from pages.base_page import BasePage
from pages.locators import SentPageLocators, LetterPageLocators


class SentPage(BasePage):

    def should_be_active_nav_sent(self):
        assert self.is_element_present(
            *SentPageLocators.ACTIVE_SENT_NAV
        )

    def go_to_last_sent_mail(self):
        link_to_last_sent_mail = self.browser.find_element(
            *SentPageLocators.LAST_SENT_ELEM
        )
        link_to_last_sent_mail.click()
        assert self.is_element_present(
            *LetterPageLocators.LETTER_CONTAINER
        ), "На странице нет блока с письмом"
        Urls.LETTER_PAGE = self.browser.current_url

    def should_be_sent_page(self):
        assert Urls.SENT_PAGE == self.browser.current_url


