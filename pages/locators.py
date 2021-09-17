from selenium.webdriver.common.by import By


class BasePageLocators:
    EMAIL_IN_HEADER = (By.CSS_SELECTOR, ".ph-project__user-name")
    PROFILE_DROPDOWN = (By.CSS_SELECTOR, ".ph-auth .ph-dropdown-icon")
    LOGOUT_LINK = (By.XPATH, "//a[contains(@href, 'logout')]")


class StartPageLocators:
    MAIL_BLOCK = (By.CSS_SELECTOR, ".mailbox-container")
    EMAIL_INPUT = (By.CSS_SELECTOR, ".email-input")
    EMAIL_DOMAIN_DROPDOWN = (By.CSS_SELECTOR, ".domain-select")
    PASSWORD_INPUT = (By.CSS_SELECTOR, ".password-input")
    ENTER_PWD_BTN = (By.CSS_SELECTOR, "[data-testid='enter-password']")
    ERROR_LOGIN = (By.CSS_SELECTOR, "[data-testid=logged-out-form] .error")
    LOGIN_TO_MAIL_BTN = (By.CSS_SELECTOR, "[data-testid=login-to-mail]")


class ComposePageLocators:
    COMPOSE_APP_OPEN_BTN = (By.CSS_SELECTOR, "a[href=/compose/]")
    COMPOSE_APP = (By.CSS_SELECTOR, ".compose-app")
    FIELD_TO = (By.XPATH, "//div[contains(@class, 'contactsContainer')]//input")
    SUBJECT_INPUT = (By.XPATH, "//div[contains(@class, 'subject__container')]//input")
    MESSAGE_FIELD = (By.XPATH, "//div[contains(@class, 'editable-container')]/div/div[1]")
    SEND_LETTER_BTN = (By.CSS_SELECTOR, ".compose-app__buttons .button2[title='Отправить']")
    POPUP_AFTER_DISPATCH = (By.CSS_SELECTOR, ".layer-sent-page")
    NTF_AFTER_DISPATCH = (By.CSS_SELECTOR, "a.layer__link")
    CONTACTS_NTF_AFTER_DISPATCH = (By.CSS_SELECTOR, ".layer-sent-page__contact-item")
    CLOSE_POPUP_AFTER_DISPATCH = (By.CSS_SELECTOR, ".layer__controls .button2[title='Закрыть']")


class SentPageLocators:
    LAST_SENT_ELEM = (By.XPATH, "//a[contains(@class, 'js-letter-list-item')][1]")
    ACTIVE_SENT_NAV = (By.CSS_SELECTOR, ".nav__item_active[href='/sent/']")


class LetterPageLocators:
    LETTER_CONTAINER = (By.CSS_SELECTOR, ".layout__main-frame .thread")
    LETTER_SUBJECT = (By.CSS_SELECTOR, ".thread__subject")
    LETTER_TO = (By.CSS_SELECTOR, ".letter__recipients .letter-contact")
    LETTER_TEXT_BODY = (By.XPATH, "//div[contains(@class, 'js-readmsg-msg')]"
                                  "//div[contains(@class, 'cl')]/div[1]"
                        )
    LETTER_FROM = (By.CSS_SELECTOR, ".letter-contact")
