from calculated_variables import *
from locators import *


class TestRegisterForm:
    def test_pass(self):
        pass

    @pytest.mark.usefixtures('open_test_page_register')
    class TestRegisterFormElements:
        def test_input_form_first_name_success(self):
            assert is_element_visible(input_form_first_name_locator) is True

            for name in valid_name_list:
                find_element_and_send_keys(input_form_first_name_locator, name)
                find_element_and_click(input_form_last_name_locator)
                name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                print(name, name_value)
                assert name_value.lower() == name.lower()

                for i in range(len(name)):
                    if i == 0:
                        assert name_value[i].isupper()
                    elif name_value[i] in special_chars_name:
                        assert name_value[i + 1].isupper()
                    elif name_value[i].isupper():
                        assert name_value[i - 1] in special_chars_name
                    else:
                        assert name_value[i].islower()

                assert is_element_visible(input_form_first_name_error_text_locator, 1) is False

                refresh_page()

        def test_input_form_last_name_success(self):
            assert is_element_visible(input_form_last_name_locator) is True

            for name in valid_name_list:
                find_element_and_send_keys(input_form_last_name_locator, name)
                find_element_and_click(input_form_first_name_locator)
                name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                print(name, name_value)
                assert name_value.lower() == name.lower()

                for i in range(len(name)):
                    if i == 0:
                        assert name_value[i].isupper()
                    elif name_value[i] in special_chars_name:
                        assert name_value[i + 1].isupper()
                    elif name_value[i].isupper():
                        assert name_value[i - 1] in special_chars_name
                    else:
                        assert name_value[i].islower()

                assert is_element_visible(input_form_last_name_error_text_locator, 1) is False

                refresh_page()

        class TestInputFormFirstNameFailure:
            def test_input_form_first_name_failure_valid_chars_invalid_len(self):
                for name in valid_chars_invalid_len_name_list:
                    find_element_and_send_keys(input_form_first_name_locator, name)
                    find_element_and_click(input_form_last_name_locator)
                    name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()

                    if 0 < len(name) < password_valid_len_interval_list[0]:
                        assert is_element_visible(input_form_first_name_error_text_locator, 1) is True
                        assert find_element_and_get_text(input_form_first_name_error_text_locator) == \
                               input_form_name_error_text
                    elif len(name) > password_valid_len_interval_list[1]:
                        assert is_element_visible(input_form_first_name_error_text_locator, 1) is True
                        assert find_element_and_get_text(input_form_first_name_error_text_locator) == \
                               input_form_name_error_text
                    elif len(name) == 0:
                        assert is_element_visible(input_form_first_name_error_text_locator, 1) is False

                    refresh_page()

            def test_input_form_first_name_failure_not_only_cyrillic_letters(self):
                for name in not_only_cyrillic_letters_name_list:
                    find_element_and_send_keys(input_form_first_name_locator, name)
                    find_element_and_click(input_form_last_name_locator)
                    name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()
                    assert is_element_visible(input_form_first_name_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_first_name_error_text_locator) == \
                           input_form_name_error_text

                    refresh_page()

            def test_input_form_first_name_failure_with_digits(self):
                for name in with_digits_name_list:
                    find_element_and_send_keys(input_form_first_name_locator, name)
                    find_element_and_click(input_form_last_name_locator)
                    name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()
                    assert is_element_visible(input_form_first_name_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_first_name_error_text_locator) == \
                           input_form_name_error_text

                    refresh_page()

            def test_input_form_first_name_failure_with_other_special_chars(self):
                for name in with_other_special_chars_name_list:
                    find_element_and_send_keys(input_form_first_name_locator, name)
                    find_element_and_click(input_form_last_name_locator)
                    name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()
                    assert is_element_visible(input_form_first_name_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_first_name_error_text_locator) == \
                           input_form_name_error_text

                    refresh_page()

        class TestInputFormLastNameFailure:
            def test_input_form_last_name_failure_valid_chars_invalid_len(self):
                for name in valid_chars_invalid_len_name_list:
                    find_element_and_send_keys(input_form_last_name_locator, name)
                    find_element_and_click(input_form_first_name_locator)
                    name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()

                    if 0 < len(name) < password_valid_len_interval_list[0]:
                        assert is_element_visible(input_form_last_name_error_text_locator, 1) is True
                        assert find_element_and_get_text(input_form_last_name_error_text_locator) == \
                               input_form_name_error_text
                    elif len(name) > password_valid_len_interval_list[1]:
                        assert is_element_visible(input_form_last_name_error_text_locator, 1) is True
                        assert find_element_and_get_text(input_form_last_name_error_text_locator) == \
                               input_form_name_error_text
                    elif len(name) == 0:
                        assert is_element_visible(input_form_last_name_error_text_locator, 1) is False

                    refresh_page()

            def test_input_form_last_name_failure_not_only_cyrillic_letters(self):
                for name in not_only_cyrillic_letters_name_list:
                    find_element_and_send_keys(input_form_last_name_locator, name)
                    find_element_and_click(input_form_first_name_locator)
                    name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()
                    assert is_element_visible(input_form_last_name_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_last_name_error_text_locator) == \
                           input_form_name_error_text

                    refresh_page()

            def test_input_form_last_name_failure_with_digits(self):
                for name in with_digits_name_list:
                    find_element_and_send_keys(input_form_last_name_locator, name)
                    find_element_and_click(input_form_first_name_locator)
                    name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()
                    assert is_element_visible(input_form_last_name_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_last_name_error_text_locator) == \
                           input_form_name_error_text

                    refresh_page()

            def test_input_form_last_name_failure_with_other_special_chars(self):
                for name in with_other_special_chars_name_list:
                    find_element_and_send_keys(input_form_last_name_locator, name)
                    find_element_and_click(input_form_first_name_locator)
                    name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                    print(name, name_value)
                    assert name_value.lower() == name.lower()
                    assert is_element_visible(input_form_last_name_error_text_locator, 1) is True
                    assert find_element_and_get_text(input_form_last_name_error_text_locator) == \
                           input_form_name_error_text

                    refresh_page()

    @pytest.mark.usefixtures('open_test_page_login')
    class TestRegisterFormScenario:
        def test_auth_page(self):
            assert get_current_url(auth_page_title_locator).startswith(auth_url)

        class TestRegisterFormScenarioSuccess:
            def test_register_form_by_phone_scenario_success(self):
                assert is_element_visible(login_form_locator) is True  # видим форму логина
                assert find_element_and_get_text(login_form_title_locator) == login_form_title

                assert is_element_visible(register_link_locator) is True  # жмем "Зарегистрироваться"
                assert find_element_and_get_text(register_link_locator) == register_link_text
                find_element_and_click(register_link_locator)

                assert is_element_visible(register_form_locator) is True  # видим форму из двух частей
                assert find_element_and_get_text(register_form_title_locator) == register_form_title
                assert is_element_visible(page_right_locator) is True
                assert is_element_visible(page_left_locator) is True
                # в правой части есть:
                assert find_element(register_form_locator) == find_element(register_form_page_right_locator)
                assert is_element_visible(input_form_first_name_locator) is True  # Поле ввода имени
                assert find_element_and_get_text(input_form_first_name_placeholder_locator) == \
                       input_form_first_name_placeholder

                assert is_element_visible(input_form_last_name_locator) is True  # Поле ввода фамилии
                assert find_element_and_get_text(input_form_last_name_placeholder_locator) == \
                       input_form_last_name_placeholder

                assert is_element_visible(select_input_form_region_locator) is True  # Поле выбора региона
                assert find_element_and_get_text(select_input_form_region_placeholder_locator) == \
                       select_input_form_region_placeholder

                assert is_element_visible(input_form_address_locator) is True  # Поле ввода email или телефона
                assert find_element_and_get_text(input_form_address_placeholder_locator) == \
                       input_form_address_placeholder

                assert is_element_visible(input_form_password_register_locator) is True  # Поле ввода пароля
                assert find_element_and_get_text(input_form_password_register_placeholder_locator) == \
                       input_form_password_register_placeholder

                assert is_element_visible(input_form_password_confirm_register_locator) is True  # Поле подтверждения
                assert find_element_and_get_text(input_form_password_confirm_register_placeholder_locator) == \
                       input_form_password_confirm_register_placeholder

                assert is_element_visible(button_register_locator) is True  # Кнопка "Продолжить"
                assert find_element_and_get_text(button_register_locator) == button_register_text

                assert is_element_visible(link_agreement_locator) is True  # Ссылки на политику и соглашение
                assert find_element_and_get_attribute(link_agreement_locator, href_attribute) == link_agreement_href
                assertion_error = None

                for word in link_agreement_text_parts_list:
                    try:
                        assert word in find_element_and_get_text(link_agreement_locator)
                    except AssertionError:
                        assertion_error = f"{word} not in {find_element_and_get_text(link_agreement_locator)}"
                        print("\n", "\033[31m{}".format(AssertionError), "\033[0m{}".format(assertion_error))
                if assertion_error:
                    fail_test()

                assert is_element_visible(what_is_logo_locator) is True  # Левая часть содержит логотип
                assert is_element_visible(what_is_title_locator) is True  # и слоган
                assert is_element_visible(what_is_description_locator) is True  # видим описание
                assert find_element_and_get_text(what_is_title_locator) == what_is_title_text  # мы в ЛК
                assert find_element_and_get_text(what_is_description_locator) is not None

                find_element_and_send_keys(input_form_first_name_locator, valid_name)  # вводим имя
                name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                assert name_value.lower() == valid_name.lower()  # ввели правильные символы
                assert is_element_visible(input_form_first_name_error_text_locator, 1) is False  # ошибок не видим

                find_element_and_send_keys(input_form_last_name_locator, valid_name)  # вводим фамилию
                name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                assert name_value.lower() == valid_name.lower()  # ввели правильные символы
                assert is_element_visible(input_form_last_name_error_text_locator, 1) is False  # ошибок не видим

                assert region_default in find_element_and_get_attribute(select_input_form_region_locator,
                                                                        value_attribute)  # Регион по умолчанию

                find_element_and_click(select_input_form_region_locator)  # жмем на выбор региона
                assert is_element_visible(select_item_list_region_locator) is True  # видим список регионов
                random_region_locator = add_index_to_locator(select_item_region_locator, regions_count)  # перемещаемся
                random_region_text = find_element_and_get_text(random_region_locator)
                move_to_element(random_region_locator)
                find_element_and_click(random_region_locator)
                assert find_element_and_get_attribute(select_input_form_region_locator, value_attribute) ==\
                       random_region_text  # переместились

                find_element_and_send_keys(input_form_address_locator, valid_phone)  # ввели email или телефон
                find_element_and_click(input_form_password_register_locator)
                assert find_element_and_get_attribute(input_form_address_locator, value_attribute) == valid_phone_form\
                       or find_element_and_get_attribute(input_form_address_locator, value_attribute) == valid_phone
                assert is_element_visible(input_form_address_error_text_locator, 1) is False  # символы подходят

                find_element_and_send_keys(input_form_password_register_locator, new_valid_password)  # вводим пароль
                find_element_and_click(input_form_password_confirm_register_locator)
                assert find_element_and_get_attribute(input_form_password_register_locator, value_attribute) ==\
                       new_valid_password
                assert is_element_visible(input_form_password_register_error_text_locator, 1) is False  # символы ок

                find_element_and_send_keys(input_form_password_confirm_register_locator, new_valid_password)
                # подтверждаем пароль
                find_element_and_click(input_form_password_register_locator)
                assert find_element_and_get_attribute(input_form_password_confirm_register_locator, value_attribute) ==\
                       new_valid_password
                assert is_element_visible(input_form_password_confirm_register_error_text_locator, 1) is False
                # ошибок не видимЮ символы подходят и пароли совпадают

                find_element_and_click(button_register_locator)  # жмем "Продолжить"

                assert is_element_visible(register_confirm_form_locator) is True  # видим поле ввода кода
                # проверяем телефон
                assert find_element_and_get_text(register_confirm_form_title_locator) ==\
                       register_confirm_form_title_phone
                assert valid_phone in find_element_and_get_text(register_confirm_form_description_locator)\
                       or valid_phone_form in find_element_and_get_text(register_confirm_form_description_locator)
                assert is_all_elements_visible(input_register_code_all_locator) is True  # видим шесть полей для кода
                assert len(find_elements(input_register_code_all_locator)) == count_code_input
                assert is_element_visible(register_resend_code_timeout_text_locator) is True  # обратный отсчет
                assert resend_code_timeout_text in find_element_and_get_text(register_resend_code_timeout_text_locator)
                # видим кнопку "Получить код повторно"
                assert is_element_visible(button_register_resend_code_locator, sleep=resend_code_timeout) is True

                assert is_element_visible(button_register_confirm_back_locator) is True  # видим "Вернуться назад"
                assert find_element_and_get_text(button_register_confirm_back_locator) ==\
                       button_register_confirm_back_text_phone

                elements = find_elements(input_register_code_all_locator)  # вводим код посимвольно
                parent_elements = find_elements(input_code_parent_all_locator)

                i = 0
                while i < count_code_input:
                    for element in elements:
                        assert parent_elements[i] == find_element(input_code_parent_active_locator)
                        element.send_keys(valid_otp[i])
                        i += 1

                assert get_current_url(account_page_title_locator).startswith(account_url)  # попадаем на страницу ЛК

                find_element_and_click(button_account_page_logout_locator)  # разлогиниваемся и назад на стр авторизации
                assert get_current_url(auth_page_title_locator).startswith(auth_url)

            def test_register_form_by_mail_scenario_success(self):
                assert is_element_visible(login_form_locator) is True  # перешли на стр авторизации
                assert find_element_and_get_text(login_form_title_locator) == login_form_title  # есть заголовок формы

                assert is_element_visible(register_link_locator) is True  # видим "Зарегистрироваться"
                assert find_element_and_get_text(register_link_locator) == register_link_text
                find_element_and_click(register_link_locator)

                assert is_element_visible(register_form_locator) is True  # видим форму регистрации из двух частей
                assert find_element_and_get_text(register_form_title_locator) == register_form_title
                assert is_element_visible(page_right_locator) is True
                assert is_element_visible(page_left_locator) is True

                assert find_element(register_form_locator) == find_element(register_form_page_right_locator)  # Правая

                assert is_element_visible(input_form_first_name_locator) is True  # Поле ввода имени
                assert find_element_and_get_text(input_form_first_name_placeholder_locator) == \
                       input_form_first_name_placeholder

                assert is_element_visible(input_form_last_name_locator) is True  # Поле ввода фамилии
                assert find_element_and_get_text(input_form_last_name_placeholder_locator) == \
                       input_form_last_name_placeholder

                assert is_element_visible(select_input_form_region_locator) is True  # Поле выбора региона
                assert find_element_and_get_text(select_input_form_region_placeholder_locator) == \
                       select_input_form_region_placeholder

                assert is_element_visible(input_form_address_locator) is True  # Поле ввода email или телефона
                assert find_element_and_get_text(input_form_address_placeholder_locator) == \
                       input_form_address_placeholder

                assert is_element_visible(input_form_password_register_locator) is True  # Поле ввода пароля
                assert find_element_and_get_text(input_form_password_register_placeholder_locator) == \
                       input_form_password_register_placeholder

                assert is_element_visible(input_form_password_confirm_register_locator) is True  # Поле подтверждения
                assert find_element_and_get_text(input_form_password_confirm_register_placeholder_locator) == \
                       input_form_password_confirm_register_placeholder

                assert is_element_visible(button_register_locator) is True  # Кнопка "Продолжить"
                assert find_element_and_get_text(button_register_locator) == button_register_text

                assert is_element_visible(link_agreement_locator) is True  # Ссылки на политику и соглашение
                assert find_element_and_get_attribute(link_agreement_locator, href_attribute) == link_agreement_href
                assertion_error = None

                for word in link_agreement_text_parts_list:
                    try:
                        assert word in find_element_and_get_text(link_agreement_locator)
                    except AssertionError:
                        assertion_error = f"{word} not in {find_element_and_get_text(link_agreement_locator)}"
                        print("\n", "\033[31m{}".format(AssertionError), "\033[0m{}".format(assertion_error))
                if assertion_error:
                    fail_test()

                assert is_element_visible(what_is_logo_locator) is True  # Левая часть содержит логотип и слоган
                assert is_element_visible(what_is_title_locator) is True
                assert is_element_visible(what_is_description_locator) is True
                assert find_element_and_get_text(what_is_title_locator) == what_is_title_text
                assert find_element_and_get_text(what_is_description_locator) is not None

                find_element_and_send_keys(input_form_first_name_locator, valid_name)  # вводим имя
                name_value = find_element_and_get_attribute(input_form_first_name_locator, value_attribute)
                assert name_value.lower() == valid_name.lower()
                assert is_element_visible(input_form_first_name_error_text_locator, 1) is False  # ошибок нет

                find_element_and_send_keys(input_form_last_name_locator, valid_name)  # вводим фамилию
                name_value = find_element_and_get_attribute(input_form_last_name_locator, value_attribute)
                assert name_value.lower() == valid_name.lower()
                assert is_element_visible(input_form_last_name_error_text_locator, 1) is False  # ошибок нет

                assert region_default in find_element_and_get_attribute(select_input_form_region_locator,
                                                                        value_attribute)  # Регион по умолчанию

                find_element_and_click(select_input_form_region_locator)
                assert is_element_visible(select_item_list_region_locator) is True  # видим список регионов
                # меняем регон
                random_region_locator = add_index_to_locator(select_item_region_locator, regions_count)
                random_region_text = find_element_and_get_text(random_region_locator)
                move_to_element(random_region_locator)
                find_element_and_click(random_region_locator)
                assert find_element_and_get_attribute(select_input_form_region_locator, value_attribute) == \
                       random_region_text

                find_element_and_send_keys(input_form_address_locator, valid_mail)  # вводим email или телефон
                find_element_and_click(input_form_password_register_locator)
                assert find_element_and_get_attribute(input_form_address_locator, value_attribute) == valid_mail
                assert is_element_visible(input_form_address_error_text_locator, 1) is False  # ошибок ввода нет

                find_element_and_send_keys(input_form_password_register_locator, new_valid_password)  # вводим пароль
                find_element_and_click(input_form_password_confirm_register_locator)
                assert find_element_and_get_attribute(input_form_password_register_locator, value_attribute) == \
                       new_valid_password
                assert is_element_visible(input_form_password_register_error_text_locator, 1) is False  # ошибок ввода нет
                find_element_and_send_keys(input_form_password_confirm_register_locator, new_valid_password)
                # подтверждаем пароль
                find_element_and_click(input_form_password_register_locator)
                assert find_element_and_get_attribute(input_form_password_confirm_register_locator, value_attribute) ==\
                       new_valid_password
                assert is_element_visible(input_form_password_confirm_register_error_text_locator, 1) is False
                # пароли совпадают, ошибок ввода нет

                find_element_and_click(button_register_locator)  # жмем "Продолжить"

                assert is_element_visible(register_confirm_form_locator) is True  # видим форму ввода кода
                assert find_element_and_get_text(register_confirm_form_title_locator) == \
                       register_confirm_form_title_mail
                assert valid_mail in find_element_and_get_text(register_confirm_form_description_locator)
                assert is_all_elements_visible(input_register_code_all_locator) is True  # видим 6 полей для кода
                assert len(find_elements(input_register_code_all_locator)) == count_code_input
                assert is_element_visible(register_resend_code_timeout_text_locator) is True  # видим обратный отсчет
                assert resend_code_timeout_text in find_element_and_get_text(register_resend_code_timeout_text_locator)

                assert is_element_visible(button_register_resend_code_locator, sleep=resend_code_timeout) is True
                # видим кнопку "Получить код повторно"
                assert is_element_visible(button_register_confirm_back_locator) is True  # видим Кнопку "Вернуться"
                assert find_element_and_get_text(button_register_confirm_back_locator) == \
                       button_register_confirm_back_text_mail

                elements = find_elements(input_register_code_all_locator)  # вводим код посимвольно
                parent_elements = find_elements(input_code_parent_all_locator)

                i = 0
                while i < count_code_input:
                    for element in elements:
                        assert parent_elements[i] == find_element(input_code_parent_active_locator)
                        element.send_keys(valid_otp[i])
                        i += 1

                assert get_current_url(account_page_title_locator).startswith(account_url)  # переходим в ЛК

                find_element_and_click(button_account_page_logout_locator)  # разлогиниваемся - и на стр авторизации
                assert get_current_url(auth_page_title_locator).startswith(auth_url)
