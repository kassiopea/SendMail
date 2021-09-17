from random import randrange

import allure

from constants import Urls
from helpers.letter_texts import generate_text
from models.letter import Letter
from pages.compose_page import ComposePage
from pages.letter_page import LetterPage
from pages.sent_page import SentPage


class TestSendMail:
    @allure.story('Письмо отправляется и после отправки'
                  ' появляется сообщение об успешной отправке')
    def test_check_sending_letter(
            self,
            browser,
            auth
    ):
        link = Urls.COMPOSE_PAGE
        page = ComposePage(browser, link)
        with allure.step("Открываем страницу compose "
                         "с формой для написания письма"):
            page.open()
        with allure.step("Проверяем,что открыт popup с формой"):
            page.should_be_compose_app()
        author_email = f'{auth["username"]}{auth["domain"]}'
        email = auth["to_email"]
        subject = f"Test subject{randrange(1, 1000)}"
        message = generate_text(length=120)
        letter = Letter(
            to=email,
            author=author_email,
            subject=subject,
            message=message
        )
        letter_for_send = vars(letter)
        with allure.step("Заполняем отправителя, заголовок,"
                         " текст письма и отправляем"):
            page.send_letter(letter_for_send)
        with allure.step("Проверяем наличие popup после отправки"):
            page.should_be_popup_after_dispatch()
        with allure.step("Проверяем наличие нотификации о том,"
                         " что письмо отправлено"):
            page.should_be_ntf_about_dispatch()

    @allure.story('Исходное письмо после отправки попадает в список'
                  ' отправленных. Письмо будет первым в списке')
    def test_check_letter_in_sent_after_dispatch_mail(
            self,
            browser,
            auth
    ):
        link = Urls.COMPOSE_PAGE
        page = ComposePage(browser, link)
        with allure.step("Открываем страницу compose "
                         "с формой для написания письма"):
            page.open()
        with allure.step("Проверяем,что открыт popup с формой"):
            page.should_be_compose_app()
        author_email = f'{auth["username"]}' \
                       f'{auth["domain"]}'
        email = auth["to_email"]
        subject = f"Test subject " \
                  f"{randrange(1, 1000)}"
        message = generate_text(length=100)
        letter = Letter(
            to=email,
            author=author_email,
            subject=subject,
            message=message
        )
        letter_for_send = vars(letter)
        with allure.step("Заполняем отправителя, заголовок,"
                         " текст письма и отправляем"):
            page.send_letter(letter_for_send)
        with allure.step("Проверяем наличие popup после отправки"):
            page.should_be_popup_after_dispatch()
        link_sent_page = Urls.SENT_PAGE
        page = SentPage(browser, link_sent_page)
        with allure.step("Открываем страницу отправленных сообщений"):
            page.open()
        with allure.step("Проверяем, что находимся на нужной странице"):
            page.should_be_sent_page()
            page.should_be_active_nav_sent()
        with allure.step("Открываем первое письмо из списка"):
            page.go_to_last_sent_mail()
            current_url = Urls.LETTER_PAGE
            page = LetterPage(browser, current_url)
            page.open()
        with allure.step("Проверяем, что находимся на странице с письмом"):
            page.should_be_letter_page()
            page.should_be_letter_content()
        with allure.step("Проверяем, что отправитель, заголовок, текст письма"
                         " совпадают с пиьмом, которое отправили"):
            page.should_be_current_letter(letter_for_send)
