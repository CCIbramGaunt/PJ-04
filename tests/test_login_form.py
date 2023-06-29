from calculated_variables import *
from locators import *


@pytest.mark.usefixtures('open_test_page_login')
class TestLoginForm:
    def test_auth_page(self):
        assert get_current_url(auth_page_title_locator).startswith(auth_url)

    class TestLoginFormElementsVisibility:  # Видимость элементов формы авторизации по логину и паролю
        def test_page_right_visible(self):  # Правый блок
            assert is_element_visible(page_right_locator) is True

        def test_page_left_visible(self):  # Левый блок
            assert is_element_visible(page_left_locator) is True

        def test_login_form_visible(self):  # Форма «Авторизация»
            assert is_element_visible(login_form_locator) is True

        def test_login_form_title_visible(self):
            assert is_element_visible(login_form_title_locator) is True
            assert find_element_and_get_text(login_form_title_locator) == login_form_title

        class TestLoginFormElementsPageRightVisibility:  # Элементы в правом блоке
            def test_login_form_page_right_visible(self):  # Форма «Авторизация» в правом блоке
                assert find_element(login_form_locator) == find_element(login_form_page_right_locator)

            def test_auth_type_menu_page_right_visible(self):  # Меню выбора типа аутентификации в правом блоке
                assert is_element_visible(auth_type_menu_login_form_locator) is True

            def test_auth_type_menu_tab_phone_visible(self):  # Таб выбора аутентификации по номеру, "Телефон", в правом
                # блоке в меню выбора типа аутентификации
                assert is_element_visible(auth_type_menu_tab_phone_locator) is True
                assert find_element_and_get_text(auth_type_menu_tab_phone_locator) == auth_type_menu_tab_phone_text

            def test_auth_type_menu_tab_mail_visible(self):  # Таб выбора аутентификации по почте, "Почта", в правом
                # блоке в меню выбора типа аутентификации
                assert is_element_visible(auth_type_menu_tab_mail_locator) is True
                assert find_element_and_get_text(auth_type_menu_tab_mail_locator) == auth_type_menu_tab_mail_text

            def test_auth_type_menu_tab_login_visible(self):  # Таб выбора аутентификации по логину, "Логин", в правом
                # блоке в меню выбора типа аутентификации
                assert is_element_visible(auth_type_menu_tab_login_locator) is True
                assert find_element_and_get_text(auth_type_menu_tab_login_locator) == auth_type_menu_tab_login_text

            def test_auth_type_menu_tab_personal_account_visible(self):  # Таб выбора аутентификации по лицевому счёту,
                # "Лицевой счёт", в правом блоке в меню выбора типа аутентификации
                assert is_element_visible(auth_type_menu_tab_personal_account_locator) is True
                assert find_element_and_get_text(auth_type_menu_tab_personal_account_locator) == \
                       auth_type_menu_tab_personal_account_text

            def test_input_form_phone_and_password_visible_default(self):  # Форма ввода "Телефон" и "Пароль" в правом
                # блоке по умолчанию
                assert is_element_visible(auth_type_menu_tab_phone_locator) is True
                assert is_element_visible(input_form_username_locator) is True
                assert is_element_visible(input_form_password_locator) is True
                assert find_element(auth_type_menu_tab_phone_locator) == find_element(auth_type_menu_tab_active_locator)
                assert find_element_and_get_text(input_form_username_placeholder_locator) ==\
                       input_form_username_phone_placeholder
                assert find_element_and_get_text(input_form_password_placeholder_locator) ==\
                       input_form_password_placeholder

            def test_input_form_mail_and_password_visible(self):  # Форма ввода "Почта" и "Пароль" в правом блоке
                assert is_element_visible(auth_type_menu_tab_mail_locator) is True
                find_element_and_click(auth_type_menu_tab_mail_locator)

                assert is_element_visible(input_form_username_locator) is True
                assert is_element_visible(input_form_password_locator) is True
                assert find_element_and_get_text(
                    input_form_username_placeholder_locator) == input_form_username_mail_placeholder
                assert find_element_and_get_text(
                    input_form_password_placeholder_locator) == input_form_password_placeholder

            def test_input_form_login_and_password_visible(self):  # Форма ввода "Логин" и "Пароль" в правом блоке
                assert is_element_visible(auth_type_menu_tab_login_locator) is True
                find_element_and_click(auth_type_menu_tab_login_locator)

                assert is_element_visible(input_form_username_locator) is True
                assert is_element_visible(input_form_password_locator) is True
                assert find_element_and_get_text(
                    input_form_username_placeholder_locator) == input_form_username_login_placeholder
                assert find_element_and_get_text(
                    input_form_password_placeholder_locator) == input_form_password_placeholder

            def test_input_form_personal_account_and_password_visible(self):  # Форма ввода "Лицевой счёт" и "Пароль"
                # в правом блоке
                assert is_element_visible(auth_type_menu_tab_personal_account_locator) is True
                find_element_and_click(auth_type_menu_tab_personal_account_locator)

                assert is_element_visible(input_form_username_locator) is True
                assert is_element_visible(input_form_password_locator) is True
                assert find_element_and_get_text(input_form_username_placeholder_locator) == \
                       input_form_username_personal_account_placeholder
                assert find_element_and_get_text(
                    input_form_password_placeholder_locator) == input_form_password_placeholder

            def test_register_link_visible(self):  # Ссылка "Зарегистрироваться"
                assert is_element_visible(register_link_locator) is True
                assert find_element_and_get_text(register_link_locator) == register_link_text

        class TestLoginFormElementsPageLeftVisibility:  # Элементы в левом блоке
            def test_what_is_visible(self):  # Продуктовый слоган ЛК "Личный кабинет" и вспомогательная информация для
                # клиента.
                assert is_element_visible(what_is_logo_locator) is True
                assert is_element_visible(what_is_title_locator) is True
                assert is_element_visible(what_is_description_locator) is True
                assert find_element_and_get_text(what_is_title_locator) == what_is_title_text
                assert find_element_and_get_text(what_is_description_locator) is not None

    def test_autochange_auth_type_tabs(self):  # Смена вкладки выбора способа авторизации в зависимости от ввода
        assertion_error = None

        for locator in login_tabs_locators_and_input_form_username_placeholders_dict:
            placeholder = login_tabs_locators_and_input_form_username_placeholders_dict[locator]
            tab_text = login_tabs_locators_and_auth_type_menu_tab_text_dict[locator]

            for locator_ in login_tabs_locators_and_data_correct_dict:
                assert is_element_visible(locator) is True
                assert find_element_and_get_text(locator) == tab_text

                find_element_and_click(locator)
                assert find_element(locator) == find_element(auth_type_menu_tab_active_locator)

                assert is_element_visible(input_form_username_locator) is True
                assert is_element_visible(input_form_password_locator) is True
                assert find_element_and_get_text(input_form_username_placeholder_locator) == placeholder
                assert find_element_and_get_text(input_form_password_placeholder_locator) == \
                       input_form_password_placeholder

                data_ = login_tabs_locators_and_data_correct_dict[locator_]
                placeholder_ = login_tabs_locators_and_input_form_username_placeholders_dict[locator_]
                tab_text_ = login_tabs_locators_and_auth_type_menu_tab_text_dict[locator_]

                find_element_and_send_keys(input_form_username_locator, data_)
                find_element_and_click(input_form_password_locator)
                try:
                    assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == data_
                    assert find_element(locator_) == find_element(auth_type_menu_tab_active_locator)
                    assert find_element_and_get_text(locator_) == tab_text_
                    assert find_element_and_get_text(input_form_username_placeholder_locator) == placeholder_
                except AssertionError: # если не переключается - выводим ошибку
                    received_data_value = find_element_and_get_attribute(input_form_username_value_locator,
                                                                         value_attribute)
                    active_tab_text = find_element_and_get_text(auth_type_menu_tab_active_locator)
                    assertion_error = f"Input Data: {data_};" \
                                      f" Received Data Value: {received_data_value};" \
                                      f" Expected Tab: {tab_text_};" \
                                      f" Active Tab: {active_tab_text}"
                    print("\n", "\033[31m{}".format(AssertionError), "\033[0m{}".format(assertion_error))
                finally:
                    refresh_page()
        if assertion_error:
            fail_test()

    class TestLoginFormElements:
        def test_input_form_username_mail_failure(self):  # Ввод e-mail с "@" в некорректной форме
            assertion_error = None
            for mail in incorrect_mail_list:
                find_element_and_click(auth_type_menu_tab_mail_locator)
                find_element_and_send_keys(input_form_username_locator, mail)
                find_element_and_click(input_form_password_locator)
                try:
                    assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == mail
                    assert find_element(auth_type_menu_tab_mail_locator) == \
                           find_element(auth_type_menu_tab_active_locator)
                    assert is_element_visible(input_form_error_text_locator) is True
                except AssertionError:
                    received_mail_value = find_element_and_get_attribute(input_form_username_value_locator,
                                                                         value_attribute)
                    tab_text = find_element_and_get_text(auth_type_menu_tab_mail_locator)
                    active_tab_text = find_element_and_get_text(auth_type_menu_tab_active_locator)
                    assertion_error = f"Input mail: {mail};" \
                                      f" Received mail Value: {received_mail_value};" \
                                      f" Expected Tab: {tab_text};" \
                                      f" Active Tab: {active_tab_text}"
                    print("\n", "\033[31m{}".format(AssertionError), "\033[0m{}".format(assertion_error),
                          f"Error visible: {is_element_visible(input_form_error_text_locator, 1)}")
                finally:
                    refresh_page()

            if assertion_error:
                fail_test()

    class TestLoginFormPhonePasswordScenario:  # тестируем логин по телефону и паролю

        def test_auth_phone_password_scenario_success(self):
            find_element_and_click(auth_type_menu_tab_phone_locator)  # нажимаем логин по телефону
            assert is_element_visible(input_form_username_locator) is True
            assert is_element_visible(input_form_password_locator) is True
            assert is_element_visible(forgot_password_link_locator) is True
            assert forgot_password_link_inactive_class in find_element_and_get_attribute(forgot_password_link_locator,
                                                                                         class_attribute)

            find_element_and_send_keys(input_form_username_locator, valid_phone)  # Вводим корректный номер телефона
            find_element_and_click(input_form_password_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == valid_phone or\
                   find_element_and_get_attribute(input_form_username_value_locator, value_attribute) ==\
                   valid_phone_form

            find_element_and_send_keys(input_form_password_locator, valid_password)  # Вводим корректный пароль
            assert find_element_and_get_attribute(input_form_password_locator, value_attribute) == valid_password

            find_element_and_click(button_login_locator)  # пробуем залогиниться
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert is_element_visible(auth_form_error_message_locator, 1) is False
            assert get_current_url(account_page_title_locator).startswith(account_url)

            find_element_and_click(button_account_page_logout_locator)  # если залогинились - сможем и разлогиниться
            assert get_current_url(auth_page_title_locator).startswith(auth_url)  # проверяем, куда вернулись

        def test_auth_phone_password_scenario_failure(self):
            find_element_and_click(auth_type_menu_tab_phone_locator) # нажимаем логин по телефону
            assert is_element_visible(input_form_username_locator) is True
            assert is_element_visible(input_form_password_locator) is True
            assert is_element_visible(forgot_password_link_locator) is True
            assert forgot_password_link_inactive_class in find_element_and_get_attribute(forgot_password_link_locator,
                                                                                         class_attribute)

            find_element_and_send_keys(input_form_username_locator, invalid_phone)  # Вводим некорректный номер телефона
            find_element_and_click(input_form_password_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == invalid_phone\
                   or find_element_and_get_attribute(input_form_username_value_locator, value_attribute) ==\
                   invalid_phone_form

            find_element_and_send_keys(input_form_password_locator, invalid_password)  # Вводим некорректный пароль
            assert find_element_and_get_attribute(input_form_password_locator, value_attribute) == invalid_password

            #  Пробуем залогиниться, если не получилось - выгружаем текст сообщения об ошибке, находим ссылку на
            #  восстановление пароля
            find_element_and_click(button_login_locator)
            assert get_current_url(auth_page_title_locator).startswith(auth_url)
            assert is_element_visible(auth_form_error_message_locator, 1) is True
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_text(auth_form_error_message_locator) == auth_form_error_message_text
            assert forgot_password_link_active_class in find_element_and_get_attribute(forgot_password_link_locator,
                                                                                       class_attribute)
            assert forgot_password_link_inactive_class not in find_element_and_get_attribute(
                forgot_password_link_locator, class_attribute)

    class TestLoginFormMailPasswordScenario:  # тестируем вход по почте и паролю. Все то же самое, ка ки с телефоном

        def test_auth_mail_password_scenario_success(self):
            find_element_and_click(auth_type_menu_tab_mail_locator)
            assert is_element_visible(input_form_username_locator) is True
            assert is_element_visible(input_form_password_locator) is True
            assert is_element_visible(forgot_password_link_locator) is True
            assert forgot_password_link_inactive_class in find_element_and_get_attribute(forgot_password_link_locator,
                                                                                         class_attribute)

            find_element_and_send_keys(input_form_username_locator, valid_mail)
            find_element_and_click(input_form_password_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == valid_mail

            find_element_and_send_keys(input_form_password_locator, valid_password)
            assert find_element_and_get_attribute(input_form_password_locator, value_attribute) == valid_password

            find_element_and_click(button_login_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert is_element_visible(auth_form_error_message_locator, 1) is False
            assert get_current_url(account_page_title_locator).startswith(account_url)

            find_element_and_click(button_account_page_logout_locator)
            assert get_current_url(auth_page_title_locator).startswith(auth_url)

        def test_auth_mail_password_scenario_failure(self):
            find_element_and_click(auth_type_menu_tab_mail_locator)
            assert is_element_visible(input_form_username_locator) is True
            assert is_element_visible(input_form_password_locator) is True
            assert is_element_visible(forgot_password_link_locator) is True
            assert forgot_password_link_inactive_class in find_element_and_get_attribute(forgot_password_link_locator,
                                                                                         class_attribute)

            find_element_and_send_keys(input_form_username_locator, invalid_mail)
            find_element_and_click(input_form_password_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == invalid_mail

            find_element_and_send_keys(input_form_password_locator, invalid_password)
            assert find_element_and_get_attribute(input_form_password_locator, value_attribute) == invalid_password

            find_element_and_click(button_login_locator)
            assert get_current_url(auth_page_title_locator).startswith(auth_url)
            assert is_element_visible(auth_form_error_message_locator, 1) is True
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_text(auth_form_error_message_locator) == auth_form_error_message_text
            assert forgot_password_link_active_class in find_element_and_get_attribute(forgot_password_link_locator,
                                                                                       class_attribute)
            assert forgot_password_link_inactive_class not in find_element_and_get_attribute(
                forgot_password_link_locator, class_attribute)

    class TestLoginFormLoginPasswordScenario:  # тестируем вход по логину и паролю. Логика та же что и в прежних тестах

        def test_auth_login_password_scenario_success(self):
            find_element_and_click(auth_type_menu_tab_login_locator)
            assert is_element_visible(input_form_username_locator) is True
            assert is_element_visible(input_form_password_locator) is True
            assert is_element_visible(forgot_password_link_locator) is True
            assert forgot_password_link_inactive_class in find_element_and_get_attribute(forgot_password_link_locator,
                                                                                         class_attribute)

            find_element_and_send_keys(input_form_username_locator, valid_login)
            find_element_and_click(input_form_password_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == valid_login

            find_element_and_send_keys(input_form_password_locator, valid_password)
            assert find_element_and_get_attribute(input_form_password_locator, value_attribute) == valid_password

            find_element_and_click(button_login_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert is_element_visible(auth_form_error_message_locator, 1) is False
            assert get_current_url(account_page_title_locator).startswith(account_url)

            find_element_and_click(button_account_page_logout_locator)
            assert get_current_url(auth_page_title_locator).startswith(auth_url)

        def test_auth_login_password_scenario_failure(self):
            find_element_and_click(auth_type_menu_tab_login_locator)
            assert is_element_visible(input_form_username_locator) is True
            assert is_element_visible(input_form_password_locator) is True
            assert is_element_visible(forgot_password_link_locator) is True
            assert forgot_password_link_inactive_class in find_element_and_get_attribute(forgot_password_link_locator,
                                                                                         class_attribute)

            find_element_and_send_keys(input_form_username_locator, invalid_login)
            find_element_and_click(input_form_password_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == invalid_login

            find_element_and_send_keys(input_form_password_locator, invalid_password)
            assert find_element_and_get_attribute(input_form_password_locator, value_attribute) == invalid_password

            find_element_and_click(button_login_locator)
            assert get_current_url(auth_page_title_locator).startswith(auth_url)
            assert is_element_visible(auth_form_error_message_locator, 1) is True
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_text(auth_form_error_message_locator) == auth_form_error_message_text
            assert forgot_password_link_active_class in find_element_and_get_attribute(forgot_password_link_locator,
                                                                                       class_attribute)
            assert forgot_password_link_inactive_class not in find_element_and_get_attribute(
                forgot_password_link_locator, class_attribute)

    class TestLoginFormPersonalAccountPasswordScenario:  # аналогичный тест входа по номеру ЛС и паролю

        def test_auth_personal_account_password_scenario_success(self):
            find_element_and_click(auth_type_menu_tab_personal_account_locator)
            assert is_element_visible(input_form_username_locator) is True
            assert is_element_visible(input_form_password_locator) is True
            assert is_element_visible(forgot_password_link_locator) is True
            assert forgot_password_link_inactive_class in find_element_and_get_attribute(
                forgot_password_link_locator,
                class_attribute)

            find_element_and_send_keys(input_form_username_locator, valid_personal_account)
            find_element_and_click(input_form_password_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
                   valid_personal_account

            find_element_and_send_keys(input_form_password_locator, valid_password)
            assert find_element_and_get_attribute(input_form_password_locator, value_attribute) == valid_password

            find_element_and_click(button_login_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert is_element_visible(auth_form_error_message_locator, 1) is False
            assert get_current_url(account_page_title_locator).startswith(account_url)

            find_element_and_click(button_account_page_logout_locator)
            assert get_current_url(auth_page_title_locator).startswith(auth_url)

        def test_auth_personal_account_password_scenario_failure(self):
            find_element_and_click(auth_type_menu_tab_personal_account_locator)
            assert is_element_visible(input_form_username_locator) is True
            assert is_element_visible(input_form_password_locator) is True
            assert is_element_visible(forgot_password_link_locator) is True
            assert forgot_password_link_inactive_class in find_element_and_get_attribute(forgot_password_link_locator,
                                                                                         class_attribute)

            find_element_and_send_keys(input_form_username_locator, invalid_personal_account)
            find_element_and_click(input_form_password_locator)
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_username_value_locator, value_attribute) == \
                   invalid_personal_account

            find_element_and_send_keys(input_form_password_locator, invalid_password)
            assert find_element_and_get_attribute(input_form_password_locator, value_attribute) == invalid_password

            find_element_and_click(button_login_locator)
            assert get_current_url(auth_page_title_locator).startswith(auth_url)
            assert is_element_visible(auth_form_error_message_locator, 1) is True
            assert is_element_visible(input_form_error_text_locator, 1) is False
            assert find_element_and_get_text(auth_form_error_message_locator) == auth_form_error_message_text
            assert forgot_password_link_active_class in find_element_and_get_attribute(forgot_password_link_locator,
                                                                                       class_attribute)
            assert forgot_password_link_inactive_class not in find_element_and_get_attribute(
                forgot_password_link_locator, class_attribute)
