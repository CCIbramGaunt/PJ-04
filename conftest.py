from selenium import webdriver

from calculated_variables import *


@pytest.fixture
def edge_options(edge_options):
    edge_options.add_argument('--no-sandbox')
    edge_options.add_argument('--log-level=DEBUG')

    return edge_options


@pytest.fixture(autouse=False, scope='class')
def open_test_page_login():
    pytest.driver = webdriver.Edge(driver_path)
    pytest.driver.maximize_window()
    pytest.driver.get(login_form_url)

    yield

    pytest.driver.quit()


@pytest.fixture(autouse=False, scope='class')
def open_test_page_otp():
    pytest.driver = webdriver.Edge(driver_path)
    pytest.driver.maximize_window()
    pytest.driver.get(otp_form_url)

    yield

    pytest.driver.quit()


@pytest.fixture(autouse=False, scope='class')
def open_test_page_reset():
    pytest.driver = webdriver.Edge(driver_path)
    pytest.driver.maximize_window()
    pytest.driver.get(reset_form_url)

    yield

    pytest.driver.quit()


@pytest.fixture(autouse=False, scope='class')
def open_test_page_register():
    pytest.driver = webdriver.Edge(driver_path)
    pytest.driver.maximize_window()
    pytest.driver.get(login_form_url)

    assert is_element_visible(register_link_locator) is True
    assert find_element_and_get_text(register_link_locator) == register_link_text

    find_element_and_click(register_link_locator)
    assert is_element_visible(register_form_locator)
    assert find_element_and_get_text(register_form_title_locator) == register_form_title

    yield

    pytest.driver.quit()


@pytest.fixture(autouse=True, scope='function')
def refresh_test_page():
    yield

    pytest.driver.refresh()


@pytest.fixture(autouse=False, scope='class')
def go_to_reset_choice_form():
    pytest.driver = webdriver.Edge(driver_path)
    pytest.driver.maximize_window()
    pytest.driver.get(reset_form_url)

    assert is_element_visible(reset_type_menu_tab_phone_locator) is True

    find_element_and_click(reset_type_menu_tab_phone_locator)
    assert find_element(reset_type_menu_tab_phone_locator) == find_element(reset_type_menu_tab_active_locator)
    assert is_element_visible(input_form_username_reset_locator) is True
    assert find_element_and_get_text(input_form_username_placeholder_locator) == \
           input_form_username_phone_placeholder
    assert is_element_visible(input_form_captcha_locator)
    assert is_element_visible(button_reset_locator)

    find_element_and_send_keys(input_form_username_reset_locator, valid_phone)
    find_element_and_click(input_form_captcha_locator)
    assert is_element_visible(input_form_error_text_locator, 1) is False
    assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
           valid_phone or find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
           valid_phone_form

    find_element_and_send_keys(input_form_captcha_locator, valid_captcha)
    find_element_and_click(input_form_username_reset_locator)
    assert find_element_and_get_attribute(input_form_captcha_locator, value_attribute) == valid_captcha

    find_element_and_click(button_reset_locator)
    assert is_element_visible(reset_choice_form_locator) is True  # Форма для восстановления пароля
    assert find_element_and_get_text(reset_choice_form_title_locator) == reset_choice_form_title
    assert is_element_visible(radio_input_by_phone_locator) is True  # Вариант "По SMS на номер телефона"
    assert is_element_visible(radio_label_by_phone_locator) is True
    assert find_element_and_get_text(radio_label_by_phone_locator) == radio_label_by_phone_text
    assert is_element_visible(radio_input_by_mail_locator) is True  # Вариант "По ссылке на почту"
    assert is_element_visible(radio_label_by_mail_locator) is True
    assert find_element_and_get_text(radio_label_by_mail_locator) == radio_label_by_mail_text
    assert is_element_visible(button_reset_choice_locator) is True  # Кнопка "Продолжить"
    assert find_element_and_get_text(button_reset_choice_locator) == button_reset_choice_text
    assert is_element_visible(button_reset_choice_back_locator) is True  # Кнопка "Вернуться назад"
    assert find_element_and_get_text(button_reset_choice_back_locator) == button_reset_choice_back_text

    yield

    pytest.driver.quit()


@pytest.fixture(autouse=False, scope='class')
def go_to_reset_confirm_form():
    pytest.driver = webdriver.Edge(driver_path)
    pytest.driver.maximize_window()
    pytest.driver.get(reset_form_url)

    assert is_element_visible(reset_type_menu_tab_phone_locator) is True

    find_element_and_click(reset_type_menu_tab_phone_locator)
    assert find_element(reset_type_menu_tab_phone_locator) == find_element(reset_type_menu_tab_active_locator)
    assert is_element_visible(input_form_username_reset_locator) is True
    assert find_element_and_get_text(input_form_username_placeholder_locator) == \
           input_form_username_phone_placeholder
    assert is_element_visible(input_form_captcha_locator)
    assert is_element_visible(button_reset_locator)

    find_element_and_send_keys(input_form_username_reset_locator, valid_phone)
    find_element_and_click(input_form_captcha_locator)
    assert is_element_visible(input_form_error_text_locator, 1) is False
    assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
           valid_phone or find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
           valid_phone_form

    find_element_and_send_keys(input_form_captcha_locator, valid_captcha)
    find_element_and_click(input_form_username_reset_locator)
    assert find_element_and_get_attribute(input_form_captcha_locator, value_attribute) == valid_captcha

    find_element_and_click(button_reset_locator)
    assert is_element_visible(reset_choice_form_locator) is True  # Форма для восстановления пароля
    assert find_element_and_get_text(reset_choice_form_title_locator) == reset_choice_form_title
    assert is_element_visible(radio_input_by_phone_locator) is True  # Вариант "По SMS на номер телефона"
    assert is_element_visible(radio_label_by_phone_locator) is True
    assert find_element_and_get_text(radio_label_by_phone_locator) == radio_label_by_phone_text
    assert is_element_visible(radio_input_by_mail_locator) is True  # Вариант "По ссылке на почту"
    assert is_element_visible(radio_label_by_mail_locator) is True
    assert find_element_and_get_text(radio_label_by_mail_locator) == radio_label_by_mail_text
    assert is_element_visible(button_reset_choice_locator) is True  # Кнопка "Продолжить"
    assert find_element_and_get_text(button_reset_choice_locator) == button_reset_choice_text
    assert is_element_visible(button_reset_choice_back_locator) is True  # Кнопка "Вернуться назад"
    assert find_element_and_get_text(button_reset_choice_back_locator) == button_reset_choice_back_text

    find_element_and_click(radio_input_by_phone_locator)  # Если хотим восстановить по номеру телефона
    assert find_element(radio_input_by_phone_locator) == find_element(radio_input_active_locator)

    find_element_and_click(button_reset_choice_locator)
    assert is_element_visible(reset_confirm_form_locator) is True  # Открылась форма с полем для ввода кода из СМС
    assert find_element_and_get_text(reset_confirm_form_title_locator) == reset_confirm_form_title
    assert valid_phone in find_element_and_get_text(reset_confirm_form_description_locator)\
           or valid_phone_form in find_element_and_get_text(reset_confirm_form_description_locator)
    assert is_all_elements_visible(input_reset_code_all_locator) is True  # нашли ровно шесть отдельных полей для ввода
    # кода подтверждения
    assert len(find_elements(input_reset_code_all_locator)) == count_code_input
    assert is_element_visible(reset_resend_code_timeout_text_locator) is True  # нашли текстовое поле
    # с обратным отсчётом времени до повторной попытки отправки код
    assert resend_code_timeout_text in find_element_and_get_text(reset_resend_code_timeout_text_locator)

    assert is_element_visible(button_reset_resend_code_locator, sleep=resend_code_timeout) is True  # Кнопка
    # "Получить код повторно"
    assert is_element_visible(button_reset_confirm_back_locator) is True  # Кнопка "Назад"
    assert find_element_and_get_text(button_reset_confirm_back_locator) == button_reset_confirm_back_text

    yield

    pytest.driver.quit()


@pytest.fixture(autouse=False, scope='class')
def go_to_update_password_form():
    pytest.driver = webdriver.Edge(driver_path)
    pytest.driver.maximize_window()
    pytest.driver.get(reset_form_url)

    assert is_element_visible(reset_type_menu_tab_phone_locator) is True

    find_element_and_click(reset_type_menu_tab_phone_locator)
    assert find_element(reset_type_menu_tab_phone_locator) == find_element(reset_type_menu_tab_active_locator)
    assert is_element_visible(input_form_username_reset_locator) is True
    assert find_element_and_get_text(input_form_username_placeholder_locator) == \
           input_form_username_phone_placeholder
    assert is_element_visible(input_form_captcha_locator)
    assert is_element_visible(button_reset_locator)

    find_element_and_send_keys(input_form_username_reset_locator, valid_phone)
    find_element_and_click(input_form_captcha_locator)
    assert is_element_visible(input_form_error_text_locator, 1) is False
    assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
           valid_phone or find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
           valid_phone_form

    find_element_and_send_keys(input_form_captcha_locator, valid_captcha)
    find_element_and_click(input_form_username_reset_locator)
    assert find_element_and_get_attribute(input_form_captcha_locator, value_attribute) == valid_captcha

    find_element_and_click(button_reset_locator)
    assert is_element_visible(reset_choice_form_locator) is True  # Форма для восстановления пароля
    assert find_element_and_get_text(reset_choice_form_title_locator) == reset_choice_form_title
    assert is_element_visible(radio_input_by_phone_locator) is True  # Выбор SMS
    assert is_element_visible(radio_label_by_phone_locator) is True
    assert find_element_and_get_text(radio_label_by_phone_locator) == radio_label_by_phone_text
    assert is_element_visible(radio_input_by_mail_locator) is True  # Выбор по почте
    assert is_element_visible(radio_label_by_mail_locator) is True
    assert find_element_and_get_text(radio_label_by_mail_locator) == radio_label_by_mail_text
    assert is_element_visible(button_reset_choice_locator) is True  # Кнопка "Продолжить"
    assert find_element_and_get_text(button_reset_choice_locator) == button_reset_choice_text
    assert is_element_visible(button_reset_choice_back_locator) is True  # Кнопка "Вернуться назад"
    assert find_element_and_get_text(button_reset_choice_back_locator) == button_reset_choice_back_text

    find_element_and_click(radio_input_by_phone_locator)  # Если хотим восстановить по телефону
    assert find_element(radio_input_by_phone_locator) == find_element(radio_input_active_locator)

    find_element_and_click(button_reset_choice_locator)
    assert is_element_visible(reset_confirm_form_locator) is True  # Нашли поле для ввода кода из СМС
    assert find_element_and_get_text(reset_confirm_form_title_locator) == reset_confirm_form_title
    assert valid_phone in find_element_and_get_text(reset_confirm_form_description_locator)\
           or valid_phone_form in find_element_and_get_text(reset_confirm_form_description_locator)
    assert is_all_elements_visible(input_reset_code_all_locator) is True  # нашли шесть отдельных полей для ввода кода
    # подтверждения
    assert len(find_elements(input_reset_code_all_locator)) == count_code_input
    assert is_element_visible(reset_resend_code_timeout_text_locator) is True  # Текст с обратным отсчётом
    assert resend_code_timeout_text in find_element_and_get_text(reset_resend_code_timeout_text_locator)

    assert is_element_visible(button_reset_resend_code_locator, sleep=resend_code_timeout) is True  # Кнопка
    # "Получить код повторно"
    assert is_element_visible(button_reset_confirm_back_locator) is True  # Кнопка "Вернуться назад"
    assert find_element_and_get_text(button_reset_confirm_back_locator) == button_reset_confirm_back_text

    elements = find_elements(input_reset_code_all_locator)  # Клиент начинает вводить полученный код
    parent_elements = find_elements(input_code_parent_all_locator)

    i = 0
    while i < count_code_input:
        for element in elements:
            assert parent_elements[i] == find_element(input_code_parent_active_locator)
            element.send_keys(valid_otp[i])
            i += 1

    assert is_element_visible(update_password_form_locator) is True  # Форма для ввода нового пароля
    assert find_element_and_get_text(update_password_form_title_locator) == update_password_form_title
    assert is_element_visible(update_password_form_description_locator) is True  # Правила для создания пароля
    assert find_element_and_get_text(update_password_form_description_locator) == update_password_form_description
    assert is_element_visible(input_form_new_password_locator) is True  # Поле ввода нового пароля
    assert find_element_and_get_text(input_form_new_password_placeholder) == input_form_new_password_placeholder
    assert is_element_visible(input_form_password_confirm_locator) is True  # Поле ввода для подтверждения нового пароля
    assert find_element_and_get_text(input_form_password_confirm_placeholder) == input_form_password_confirm_placeholder
    assert is_element_visible(button_update_locator) is True  # Кнопка "Сохранить" для подтверждения нового пароля
    assert find_element_and_get_text(button_update_locator) == button_update_text
    assert is_element_clickable(button_update_locator) is False

    yield

    pytest.driver.quit()
