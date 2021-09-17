import json
import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from constants import Urls
from pages.start_page import StartPage


def pytest_addoption(parser):
    parser.addoption(
        '--config',
        action="store",
        help="Введите название config файла",
        default="local_win_chrome.json"
    )


@pytest.fixture(scope="session")
def get_config(request):
    cred_file = request.config.getoption("--config")
    path = os.path.join(
        os.path.dirname(__file__),
        cred_file)
    with open(path, encoding='utf-8') as file:
        return json.load(file)


@pytest.fixture(scope="session")
def get_path_to_driver(get_config):
    env = get_config["env"]
    path = None
    if env == "local":
        path_to_drivers = get_config["drivers_path"]
        if path_to_drivers == "":
            path = os.path.join(
                os.path.dirname(__file__),
                get_config["name_web_driver"]
            )
        else:
            path = f'{path_to_drivers}' \
                   f'{get_config["name_web_driver"]}'

    return path


@pytest.fixture(scope="session")
def browser(get_config, get_path_to_driver):
    env = get_config["env"]
    browser_name = get_config["browser"]
    caps = None
    browser = None
    if env == "remote":
        if browser_name == "chrome":
            caps = webdriver.DesiredCapabilities.CHROME

        elif browser_name == "firefox":
            caps = webdriver.DesiredCapabilities.FIREFOX

        browser = webdriver.Remote(
            desired_capabilities=caps,
            command_executor='http://localhost:4444/wd/hub'
        )
    elif env == "local":
        if browser_name == "chrome":
            browser = webdriver.Chrome(
                executable_path=get_path_to_driver
            )
        elif browser_name == "firefox":
            browser = webdriver.Firefox(
                executable_path=get_path_to_driver
            )
    # параметры размера окна можно было бы вынести
    # в конфигурационный файл
    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def auth(browser, get_config, request):
    link = Urls.START_PAGE
    username = get_config["username"]
    domain = get_config["domain"]
    password = get_config["password"]
    page = StartPage(browser, link)
    page.open()
    page.should_be_mail_box()
    page.fill_the_mail_field(
        login=username
    )
    page.select_domain(
        domain=domain
    )
    page.should_be_enter_btn()
    page.click_on_enter_pwd_btn()
    page.fill_the_password_field(
        password=password
    )
    page.should_not_be_error()
    page.send_login_form()
    page.should_not_be_error()
    page.should_be_current_page(browser.current_url)

    def logout_user():
        page.open_profile_dropdown()
        page.should_be_logout_link()
        page.logout()

    request.addfinalizer(logout_user)
    return get_config

