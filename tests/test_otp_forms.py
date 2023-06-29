import pytest

from calculated_variables import *
from locators import *


@pytest.mark.usefixtures('open_test_page_otp')
class TestOtpForms:

    def test_auth_page(self):
        assert get_current_url(auth_page_title_locator).startswith(auth_url)  # убеждаемся, что мы на начальной стр.

    class TestOtpFormsScenario:
        @pytest.mark.skip(reason="Нет временного кода valid_otp для теста")
        def test_otp_forms_phone_scenario_success(self):  # Случай верного кода
            assert is_element_visible(otp_form_locator) is True  # находим форму «Авторизация по коду»
            assert is_element_visible(otp_form_title_locator) is True
            assert find_element_and_get_text(otp_form_title_locator) == otp_form_title

            assert is_element_visible(otp_form_description_locator) is True  # видна подсказка
            assert find_element_and_get_text(otp_form_description_locator) == otp_form_description

            assert is_element_visible(input_form_email_or_phone_locator) is True  # видно поле ввода телефона или почты
            assert find_element_and_get_text(input_form_email_or_phone_placeholder_locator) == \
                   input_form_email_or_phone_placeholder

            assert is_element_visible(button_get_code_locator) is True  # есть кнопка "Получить код"
            assert find_element_and_get_text(button_get_code_locator) == button_get_code_text

            find_element_and_send_keys(input_form_email_or_phone_locator, valid_phone)  # Вводим корректный телефон
            find_element_and_click(otp_form_locator)
            assert is_element_visible(input_form_email_or_phone_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_email_or_phone_value_locator, value_attribute) ==\
                   valid_phone or find_element_and_get_attribute(input_form_email_or_phone_value_locator,
                                                                 value_attribute) == valid_phone_form
            try:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1) is False
            except Exception:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1, sleep=resend_code_timeout) is \
                       False

            find_element_and_click(button_get_code_locator)  # жмем "Получить код"
            assert is_element_visible(otp_code_form_locator) is True  # видна форма ввода кода подтверждения
            assert is_element_visible(otp_code_form_title_locator) is True
            assert find_element_and_get_text(otp_code_form_title_locator) == otp_code_form_title
            # далее убеждаемся, что код отправлен куда надо
            assert valid_phone in find_element_and_get_text(otp_code_form_description_locator)\
                   or valid_phone_form in find_element_and_get_text(otp_code_form_description_locator)

            assert is_element_visible(button_otp_back_phone_locator)  # видна ссылка "Изменить номер"
            assert find_element_and_get_text(button_otp_back_phone_locator) == button_otp_back_phone_text

            assert is_all_elements_visible(input_code_all_locator)  # Шесть отдельных полей для ввода кода подтверждения
            assert len(find_elements(input_code_all_locator)) == count_code_input

            assert is_element_visible(otp_resend_code_timeout_text_locator)  # Текст с обратным отсчётом
            assert is_element_visible(button_otp_resend_code_locator, sleep=resend_code_timeout) is True

            elements = find_elements(input_code_all_locator)  # начало ввода кода из СМС
            parent_elements = find_elements(input_code_parent_all_locator)

            i = 0
            while i < count_code_input:
                for element in elements:
                    assert parent_elements[i] == find_element(input_code_parent_active_locator)
                    element.send_keys(valid_otp[i])
                    i += 1
            # убеждаемся, что попали на стартовую страницу
            assert get_current_url(start_page_title_locator).startswith(start_url)
            # переходим на страницу авторизации по коду
            find_element_and_click(menu_start_page_account_locator)
            find_element_and_click(button_start_page_logout_locator)
            assert get_current_url(auth_page_title_locator).startswith(auth_url)

        @pytest.mark.skip(reason="Нет временного кода valid_otp для теста")
        def test_otp_forms_mail_scenario_success(self):  # Почта, верный код, логика как с телефоном
            assert is_element_visible(otp_form_locator) is True
            assert is_element_visible(otp_form_title_locator) is True
            assert find_element_and_get_text(otp_form_title_locator) == otp_form_title
            assert is_element_visible(otp_form_description_locator) is True
            assert find_element_and_get_text(otp_form_description_locator) == otp_form_description
            assert is_element_visible(input_form_email_or_phone_locator) is True
            assert find_element_and_get_text(input_form_email_or_phone_placeholder_locator) == \
                   input_form_email_or_phone_placeholder
            assert is_element_visible(button_get_code_locator) is True
            assert find_element_and_get_text(button_get_code_locator) == button_get_code_text
            find_element_and_send_keys(input_form_email_or_phone_locator, valid_mail)
            find_element_and_click(otp_form_locator)
            assert is_element_visible(input_form_email_or_phone_error_text_locator, 1) is False
            assert find_element_and_get_attribute(input_form_email_or_phone_value_locator, value_attribute) ==\
                   valid_mail
            try:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1) is False
            except Exception:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1, sleep=resend_code_timeout) is\
                       False
            find_element_and_click(button_get_code_locator)
            assert is_element_visible(otp_code_form_locator) is True
            assert is_element_visible(otp_code_form_title_locator) is True
            assert find_element_and_get_text(otp_code_form_title_locator) == otp_code_form_title
            assert valid_mail in find_element_and_get_text(otp_code_form_description_locator)
            assert is_element_visible(button_otp_back_phone_locator)
            assert find_element_and_get_text(button_otp_back_phone_locator) == button_otp_back_mail_text
            assert is_all_elements_visible(input_code_all_locator)
            assert len(find_elements(input_code_all_locator)) == count_code_input
            assert is_element_visible(otp_resend_code_timeout_text_locator) is True
            assert resend_code_timeout_text in find_element_and_get_text(otp_resend_code_timeout_text_locator)
            assert is_element_visible(button_otp_resend_code_locator, sleep=resend_code_timeout) is True
            elements = find_elements(input_code_all_locator)
            parent_elements = find_elements(input_code_parent_all_locator)

            i = 0
            while i < count_code_input:
                for element in elements:
                    assert parent_elements[i] == find_element(input_code_parent_active_locator)
                    element.send_keys(valid_otp[i])
                    i += 1

            assert get_current_url(start_page_title_locator).startswith(start_url)

            find_element_and_click(menu_start_page_account_locator)
            find_element_and_click(button_start_page_logout_locator)
            assert get_current_url(auth_page_title_locator).startswith(auth_url)

        def test_otp_forms_phone_scenario_failure_invalid_otp(self):  # Телефон, неверный код, логика прежняя
            assert is_element_visible(otp_form_locator) is True  # Форма «Авторизация по коду»
            assert is_element_visible(otp_form_title_locator) is True
            assert find_element_and_get_text(otp_form_title_locator) == otp_form_title

            assert is_element_visible(otp_form_description_locator) is True  # есть подсказка
            assert find_element_and_get_text(otp_form_description_locator) == otp_form_description

            assert is_element_visible(input_form_email_or_phone_locator) is True  # есть поле ввода
            assert find_element_and_get_text(input_form_email_or_phone_placeholder_locator) == \
                   input_form_email_or_phone_placeholder

            assert is_element_visible(button_get_code_locator) is True  # есть кнопка "Получить код"
            assert find_element_and_get_text(button_get_code_locator) == button_get_code_text

            find_element_and_send_keys(input_form_email_or_phone_locator, valid_phone)  # вводим телефон
            find_element_and_click(otp_form_locator)  # жмем подтверждение
            assert is_element_visible(input_form_email_or_phone_error_text_locator, 1) is False  # все без ошибок
            assert find_element_and_get_attribute(input_form_email_or_phone_value_locator, value_attribute) ==\
                   valid_phone or find_element_and_get_attribute(input_form_email_or_phone_value_locator,
                                                                 value_attribute) == valid_phone_form
            try:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1) is False
            except Exception:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1, sleep=resend_code_timeout) is \
                       False

            find_element_and_click(button_get_code_locator)  # жмем "Получить код"
            assert is_element_visible(otp_code_form_locator) is True  # видим форму ввода кода подтверждения
            assert is_element_visible(otp_code_form_title_locator) is True
            assert find_element_and_get_text(otp_code_form_title_locator) == otp_code_form_title
            # убеждаемся что код отправлен куда надо
            assert valid_phone in find_element_and_get_text(otp_code_form_description_locator)\
                   or valid_phone_form in find_element_and_get_text(otp_code_form_description_locator)

            assert is_element_visible(button_otp_back_phone_locator)  # есть кнопка "Изменить номер"
            assert find_element_and_get_text(button_otp_back_phone_locator) == button_otp_back_phone_text

            assert is_all_elements_visible(input_code_all_locator)  # есть 6 полей для ввода кода подтверждения
            assert len(find_elements(input_code_all_locator)) == count_code_input

            assert is_element_visible(otp_resend_code_timeout_text_locator)  # есть обратный отсчет
            # после отсчета появляется кнопка, чтобы перевыслать код
            assert is_element_visible(button_otp_resend_code_locator, sleep=resend_code_timeout) is True

            elements = find_elements(input_code_all_locator)  # посимвольно вводим код
            parent_elements = find_elements(input_code_parent_all_locator)

            i = 0
            while i < count_code_input:
                for element in elements:
                    assert parent_elements[i] == find_element(input_code_parent_active_locator)
                    element.send_keys(invalid_otp[i])
                    i += 1

            assert is_element_visible(otp_code_error_locator) is True  # введенный код неверен
            assert find_element_and_get_text(otp_code_error_locator) == code_error_invalid_text  # видим ошибку

            find_element_and_click(button_otp_back_phone_locator)  # вернулись на авторизацию по коду
            assert is_element_visible(otp_form_locator) is True

        def test_otp_forms_mail_scenario_failure_invalid_otp(self):  # Почта, неверный код
            assert is_element_visible(otp_form_locator) is True  # Форма «Авторизация по коду»
            assert is_element_visible(otp_form_title_locator) is True
            assert find_element_and_get_text(otp_form_title_locator) == otp_form_title

            assert is_element_visible(otp_form_description_locator) is True  # есть подсказка
            assert find_element_and_get_text(otp_form_description_locator) == otp_form_description

            assert is_element_visible(input_form_email_or_phone_locator) is True  # есть поле ввода
            assert find_element_and_get_text(input_form_email_or_phone_placeholder_locator) == \
                   input_form_email_or_phone_placeholder

            assert is_element_visible(button_get_code_locator) is True  # есть кнопка "Получить код"
            assert find_element_and_get_text(button_get_code_locator) == button_get_code_text

            find_element_and_send_keys(input_form_email_or_phone_locator, valid_mail)  # вводим почту
            find_element_and_click(otp_form_locator) # жмем подтверждение
            assert is_element_visible(input_form_email_or_phone_error_text_locator, 1) is False  # все без ошибок
            assert find_element_and_get_attribute(input_form_email_or_phone_value_locator, value_attribute) ==\
                   valid_mail
            try:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1) is False
            except Exception:
                assert is_element_visible(otp_form_timeout_text_locator, timeout=1, sleep=resend_code_timeout) is \
                       False

            find_element_and_click(button_get_code_locator)  # жмем "Получить код"
            assert is_element_visible(otp_code_form_locator) is True  # видим форму ввода кода подтверждения
            assert is_element_visible(otp_code_form_title_locator) is True
            assert find_element_and_get_text(otp_code_form_title_locator) == otp_code_form_title
            # убеждаемся что код отправлен куда надо
            assert valid_mail in find_element_and_get_text(otp_code_form_description_locator)

            assert is_element_visible(button_otp_back_phone_locator)  # видим ссылку "Изменить номер"
            assert find_element_and_get_text(button_otp_back_phone_locator) == button_otp_back_mail_text

            assert is_all_elements_visible(input_code_all_locator)  # видим 6 полей для кода подтверждения
            assert len(find_elements(input_code_all_locator)) == count_code_input

            assert is_element_visible(otp_resend_code_timeout_text_locator)  # Текст с обратным отсчётом
            # после отсчета появляется кнопка повторной отправки кода
            assert is_element_visible(button_otp_resend_code_locator, sleep=resend_code_timeout) is True

            elements = find_elements(input_code_all_locator)  # посимвольно вводим код
            parent_elements = find_elements(input_code_parent_all_locator)

            i = 0
            while i < count_code_input:
                for element in elements:
                    assert parent_elements[i] == find_element(input_code_parent_active_locator)
                    element.send_keys(invalid_otp[i])
                    i += 1

            assert is_element_visible(otp_code_error_locator) is True  # код неверен, видим ошибку
            assert find_element_and_get_text(otp_code_error_locator) == code_error_invalid_text

            find_element_and_click(button_otp_back_phone_locator)  # Возврат на страницу авторизации по коду
            assert is_element_visible(otp_form_locator) is True
