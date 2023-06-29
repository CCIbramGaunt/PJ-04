import pytest
import time
import secrets
import string
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from random import randint

from variables import *


# test
def fail_test():
    pytest.fail()


# page
def get_current_url(page_title_locator, timeout: int = 10):
    WebDriverWait(pytest.driver, timeout).until(ec.presence_of_element_located(page_title_locator))
    return pytest.driver.current_url


def refresh_page():
    pytest.driver.refresh()


def open_page(url: str):
    pytest.driver.get(url)


def is_element_visible(locator: tuple, timeout: int = 10, sleep: int = 0):
    time.sleep(sleep)
    try:
        WebDriverWait(pytest.driver, timeout).until(ec.visibility_of_element_located(locator))
        return True
    except Exception:
        return False


def is_element_presence(locator: tuple, timeout: int = 10):
    try:
        WebDriverWait(pytest.driver, timeout).until(ec.presence_of_element_located(locator))
        return True
    except Exception:
        return False


def is_element_clickable(locator: tuple, timeout: int = 10):
    try:
        WebDriverWait(pytest.driver, timeout).until(ec.element_to_be_clickable(locator))
        return True
    except Exception:
        return False


def find_element(locator: tuple, timeout: int = 10):
    locator_type = locator[0]
    locator_value = locator[1]
    if is_element_presence(locator, timeout):
        return pytest.driver.find_element(locator_type, locator_value)


def find_element_and_get_text(locator: tuple, timeout: int = 10):
    locator_type = locator[0]
    locator_value = locator[1]
    if is_element_presence(locator, timeout):
        return pytest.driver.find_element(locator_type, locator_value).text


def find_element_and_click(locator: tuple, timeout: int = 10):
    locator_type = locator[0]
    locator_value = locator[1]
    if is_element_clickable(locator, timeout):
        return pytest.driver.find_element(locator_type, locator_value).click()


def find_element_and_send_keys(locator: tuple, keys: str, timeout: int = 10):
    locator_type = locator[0]
    locator_value = locator[1]
    if is_element_clickable(locator, timeout):
        return pytest.driver.find_element(locator_type, locator_value).send_keys(keys)


def find_element_and_get_attribute(locator: tuple, attribute_name: str, timeout: int = 10):
    locator_type = locator[0]
    locator_value = locator[1]
    if is_element_presence(locator, timeout):
        return pytest.driver.find_element(locator_type, locator_value).get_attribute(attribute_name)


def move_to_element(locator: tuple, timeout: int = 10):
    locator_type = locator[0]
    locator_value = locator[1]
    if is_element_presence(locator, timeout):
        return ActionChains(pytest.driver).move_to_element(pytest.driver.find_element(locator_type, locator_value)).\
            perform()


def is_all_elements_visible(locator: tuple, timeout: int = 10):
    try:
        WebDriverWait(pytest.driver, timeout).until(ec.visibility_of_all_elements_located(locator))
        return True
    except Exception:
        return False


def is_all_elements_presence(locator: tuple, timeout: int = 10):
    try:
        WebDriverWait(pytest.driver, timeout).until(ec.presence_of_all_elements_located(locator))
        return True
    except Exception:
        return False


def find_elements(locator: tuple, timeout: int = 10):
    locator_type = locator[0]
    locator_value = locator[1]
    if is_all_elements_presence(locator, timeout):
        return pytest.driver.find_elements(locator_type, locator_value)


# variables
def replace_chars(base_string: str, *chars: str or list):
    string_result = base_string
    for char in chars:
        for c in char:
            string_result = string_result.replace(c, "")

    return string_result


def add_index_to_locator(locator: tuple, max_index: int) -> tuple:
    locator_type = locator[0]
    locator_value = locator[1]
    new_locator = (locator_type, locator_value + f'[{randint(1, max_index)}]')
    return new_locator


def generate_password(chars: str, length: str) -> str:
    """
    Функция работает только со следующими парами значений аргументов:\n
    ("valid_chars", "valid_len_interval")

    valid_password: пароль должен содержать от 8 до 20 знаков, включать латинские, заглавные и строчные буквы, цифры
                    или специальные символы
    """
    password = None

    if chars == "valid_chars" and length == "valid_len_interval":
        length = randint(password_valid_len_interval_list[0], password_valid_len_interval_list[1])

        while True:
            password = ''.join(secrets.choice(valid_chars) for i in range(length))
            if (sum(c.islower() for c in password) >= 1
                    and sum(c.isupper() for c in password) >= 1
                    and sum(c.isdigit() or c in string.punctuation for c in password) >= 1):
                break

    return password


def create_passwords_list(chars: str, length: str) -> list[str]:
    """
    Функция работает только со следующими парами значений аргументов:\n
    ("valid_chars", "valid_len")\n
    ("valid_chars", "invalid_len")\n
    ("no_uppercase_letters", "valid_len_interval")\n
    ("no_lowercase_letters", "valid_len_interval")\n
    ("no_digits_or_special_chars", "valid_len_interval")\n
    ("not_only_latin_letters","valid_len_interval")

    valid_password:  пароль должен содержать от 8 до 20 знаков, включать латинские, заглавные и строчные буквы, цифры
                     или специальные символы
    """
    passwords_list = []

    if chars == "valid_chars" and length == "valid_len":
        for num in password_valid_len_list:
            while True:
                password = ''.join(secrets.choice(valid_chars) for i in range(num))
                if (sum(c.islower() for c in password) >= 1
                        and sum(c.isupper() for c in password) >= 1
                        and sum(c.isdigit() or c in string.punctuation for c in password) >= 1):
                    passwords_list.append(password)
                    break

    elif chars == "valid_chars" and length == "invalid_len":
        for num in password_invalid_len_list:
            while True:
                password = ''.join(secrets.choice(valid_chars) for i in range(num))
                if num >= 3:
                    if (sum(c.islower() for c in password) >= 1
                            and sum(c.isupper() for c in password) >= 1
                            and sum(c.isdigit() or c in string.punctuation for c in password) >= 1):
                        passwords_list.append(password)
                        break
                else:
                    passwords_list.append(password)
                    break

    elif chars == "no_uppercase_letters" and length == "valid_len_interval":
        for num in password_valid_len_interval_list:
            while True:
                password = ''.join(secrets.choice(no_uppercase_letters) for i in range(num))
                if (sum(c.islower() for c in password) >= 1
                        and sum(c.isdigit() or c in string.punctuation for c in password) >= 1):
                    passwords_list.append(password)
                    break

    elif chars == "no_lowercase_letters" and length == "valid_len_interval":
        for num in password_valid_len_interval_list:
            while True:
                password = ''.join(secrets.choice(no_lowercase_letters) for i in range(num))
                if (sum(c.isupper() for c in password) >= 1
                        and sum(c.isdigit() or c in string.punctuation for c in password) >= 1):
                    passwords_list.append(password)
                    break

    elif chars == "no_digits_or_special_chars" and length == "valid_len_interval":
        for num in password_valid_len_interval_list:
            while True:
                password = ''.join(secrets.choice(no_digits_or_special_chars) for i in range(num))
                if (sum(c.islower() for c in password) >= 1
                        and sum(c.isupper() for c in password) >= 1):
                    passwords_list.append(password)
                    break

    elif chars == "not_only_latin_letters" and length == "valid_len_interval":
        for num in password_valid_len_interval_list:
            while True:
                password = ''.join(secrets.choice(not_only_latin_letters) for i in range(num))
                if (sum(c.islower() for c in password) >= 1
                        and sum(c.isupper() for c in password) >= 1
                        and sum(c.isdigit() or c in string.punctuation for c in password) >= 1
                        and sum(not c.isascii() for c in password) >= 1):
                    passwords_list.append(password)
                    break

    else:
        raise TypeError("""
    Функция работает только со следующими парами значений аргументов:\n
    ("valid_chars", "valid_len")\n
    ("valid_chars", "invalid_len")\n
    ("no_uppercase_letters", "valid_len_interval")\n
    ("no_lowercase_letters", "valid_len_interval")\n
    ("no_digits_or_special_chars", "valid_len_interval")\n
    ("not_only_latin_letters","valid_len_interval")
    """)

    return passwords_list


def generate_name(chars: str, length: str) -> str:
    """
    Функция работает только со следующими парами значений аргументов:\n
    ("valid_chars", "valid_len_interval")

    valid name: имя может содержать от 2 до 30 символов, состоящих из букв кириллицы или знака тире (-)
    """
    name = None

    if chars == "valid_chars" and length == "valid_len_interval":
        length = randint(name_valid_len_interval_list[0], name_valid_len_interval_list[1])

        while True:
            name = ''.join(secrets.choice(valid_chars_name) for i in range(length))
            if length <= 3:
                if (c not in special_chars_name for c in name):
                    break
            else:
                if (sum(c in string.punctuation for c in name) == 1)\
                        and (name[0] not in special_chars_name)\
                        and (name[1] not in special_chars_name)\
                        and (name[-1] not in special_chars_name):
                    break

    return name


def create_name_list(chars: str, length: str) -> list[str]:
    """
    Функция работает только со следующими парами значений аргументов:\n
    ("valid_chars", "valid_len")\n
    ("valid_chars", "invalid_len")\n
    ("not_only_cyrillic_letters", "valid_len_interval")\n
    ("with_digits", "valid_len_interval")\n
    ("with_other_special_chars", "valid_len_interval")

    valid name: имя может содержать от 2 до 30 символов, состоящих из букв кириллицы или знака тире (-)
    """
    name_list = []

    if chars == "valid_chars" and length == "valid_len":
        for num in name_valid_len_list:
            while True:
                name = ''.join(secrets.choice(valid_chars_name) for i in range(num))
                if len(name) <= 3:
                    if (c not in special_chars_name for c in name):
                        name_list.append(name)
                        break
                else:
                    if (sum(c in string.punctuation for c in name) == 1)\
                            and (name[0] not in special_chars_name)\
                            and (name[1] not in special_chars_name)\
                            and (name[-1] not in special_chars_name):
                        name_list.append(name)
                        break

    elif chars == "valid_chars" and length == "invalid_len":
        for num in name_invalid_len_list:
            while True:
                name = ''.join(secrets.choice(valid_chars_name) for i in range(num))
                if len(name) <= 3:
                    if (c not in special_chars_name for c in name):
                        name_list.append(name)
                        break
                else:
                    name_list.append(name)
                    break

    elif chars == "not_only_cyrillic_letters" and length == "valid_len_interval":
        for num in name_valid_len_interval_list:
            while True:
                name = ''.join(secrets.choice(not_only_cyrillic_letters) for i in range(num))
                if len(name) <= 3:
                    if (c not in special_chars_name for c in name)\
                            and (sum(c in letters_cyrillic for c in name) >= 1)\
                            and (sum(c in letters_latin for c in name) >= 1):
                        name_list.append(name)
                        break
                else:
                    if (sum(c in string.punctuation for c in name) == 1) \
                            and (sum(c in letters_cyrillic for c in name) >= 1)\
                            and (name[0] not in special_chars_name)\
                            and (name[1] not in special_chars_name)\
                            and (name[-1] not in special_chars_name)\
                            and (sum(c in letters_latin for c in name) >= 1):
                        name_list.append(name)
                        break

    elif chars == "with_digits" and length == "valid_len_interval":
        for num in name_valid_len_interval_list:
            while True:
                name = ''.join(secrets.choice(with_digits) for i in range(num))
                if len(name) <= 3:
                    if (c not in special_chars_name for c in name) \
                            and (sum(c in letters_cyrillic for c in name) >= 1)\
                            and (sum(c.isdigit() for c in name) >= 1):
                        name_list.append(name)
                        break
                else:
                    if (sum(c in string.punctuation for c in name) == 1)\
                            and (sum(c in letters_cyrillic for c in name) >= 1)\
                            and (name[0] not in special_chars_name)\
                            and (name[1] not in special_chars_name)\
                            and (name[-1] not in special_chars_name)\
                            and (sum(c.isdigit() for c in name) >= 1):
                        name_list.append(name)
                        break

    elif chars == "with_other_special_chars" and length == "valid_len_interval":
        other_special_chars = replace_chars(special_chars, special_chars_name)
        with_other_special_chars = valid_chars_name + other_special_chars
        for num in name_valid_len_interval_list:
            while True:
                name = ''.join(secrets.choice(with_other_special_chars) for i in range(num))
                if len(name) <= 3:
                    if (c not in special_chars_name for c in name) \
                            and (sum(c in letters_cyrillic for c in name) >= 1)\
                            and (sum(c in other_special_chars for c in name) >= 1):
                        name_list.append(name)
                        break
                else:
                    if (sum(c in string.punctuation for c in name) == 1)\
                            and (sum(c in letters_cyrillic for c in name) >= 1)\
                            and (name[0] not in special_chars_name)\
                            and (name[1] not in special_chars_name)\
                            and (name[-1] not in special_chars_name)\
                            and (sum(c in other_special_chars for c in name) >= 1):
                        name_list.append(name)
                        break

    return name_list
