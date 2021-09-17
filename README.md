# Тестирование UI отправки письма с mail.ru

## Инструменты
- python 3.9
- pytest >= 6
- selenium >= 3
- allure-pytest >= 2
- SeleniumHQ/docker-selenium
- allure-docker-service

## Общая информация
Тестовый проект по созданию тестов UI с паттерном Page object для проверки отправки писем с mail.ru.
Покрыты следующие кейсы:
- проверить, что письмо отправляется (получить сообщение об успешной отправки письма)
- проверить, что письмо после отправки:
  - появляется в списке отправленных
  - находится первым в списке отправленных
  - содержание соответствует содержанию отправленного письма

## Конфигурационные файлы
Перед запуском необходимо создать конфигурационный файл с расширением json
Примеры:
- Локальный запуск
```
{
    "username": "testUsername",
    "domain": "@mail.ru",
    "password": "TestPassword",
    "to_email": "testEmail@list.ru",
    "env": "local",
    "browser": "chrome",
    "drivers_path": "",
    "name_web_driver": "chromedriver.exe"
}
```
- Запуск с помощью докера
- 
```
{
    "username": "testUsername",
    "domain": "@mail.ru",
    "password": "TestPassword",
    "to_email": "testEmail@list.ru",
    "browser": "firefox",
    "env": "remote"
}
```

- username - название почтового ящика до `@`, с которого будут отправляться сообщения
- domain - домен почты `@mail.ru`, `@list.ru`, `@inbox.ru`
- password - пароль от почты, для авторизации
- to_mail - адрес почты, на которую будем отправлять письма
- env - окружение: `local` - запуск тестов локально, `remote` - запуск тестов в docker selenium grid
- browser - название браузера `chrome` или `firefox`
- drivers_path (необязательное поле) - указываем путь до веб драйвера, если запуск планируем локально. Пустая строка означает текущую директорию проекта.
- name_web_driver (необязательное поле) - указываем название веб драйва. Заполняем только если будем запускать тесты локально

## Старт проекта
- Установить зависимости `pip3 install -r requirements.txt`
- Запустить докер контейнеры `docker-compose up -d`
- Запустить тесты. Пример: `pytest tests/tests_compose_page.py --alluredir=./allure/allure-results --config=docker_chrome.json`
- Посмотреть результаты тестов в allure (с историей прогонов) по url `http://localhost:5252/allure-docker-service-ui/`
- Остановить докер контейнеры `docker-compose down`
