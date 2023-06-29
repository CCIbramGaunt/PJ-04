from locators import *
import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv("valid_email")
valid_password = os.getenv("valid_password")

# Драйвер
driver_path = "/tests_drivers/msedgedriver.exe"

# URL
login_form_url = "https://b2c.passport.rt.ru/"
otp_form_url = "https://lk.rt.ru/"
reset_form_url = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials"
auth_url = "https://b2c.passport.rt.ru/auth/"
account_url = "https://b2c.passport.rt.ru/account_b2c"
start_url = "https://start.rt.ru"

# Данные для успешной авторизации/восстановления/регистрации
valid_phone_form = "valid_phone_form"  # в формате: +7 000 000-00-00
non_digital_chars_in_phone_form_list = ["+", " ", "-"]
valid_mail = "valid_mail"
valid_login = "valid_login"
valid_personal_account = "valid_personal_account"
valid_password = "valid_password"
valid_otp = "valid_otp"
valid_captcha = "valid_captcha"
password_valid_len_interval_list = [8, 20]
name_valid_len_interval_list = [2, 30]

# Данные для неуспешной авторизации/восстановления/регистрации
invalid_phone_form = "+7 999 999-99-99"
invalid_mail = "fail@fail.ru"
invalid_login = "faillogin"
invalid_personal_account = "9000lol"
invalid_password = "lolwut"
invalid_otp = "009900"
expired_otp = "expired_otp"
invalid_captcha = "wtf0203"

# Данные для заполнения формы авторизации в корректной форме
phone_correct = "70101010101"
mail_correct = "mail@mail.ru"
login_correct = "login"
personal_account_correct = "000000000001"

# Данные для заполнения формы авторизации в некорректной форме
mail_without_local = "@mail.ru"
mail_without_domain = "mail@"
mail_without_domain_before_dot = "mail@.ru"
mail_without_domain_after_dot = "mail@mail"
mail_with_double_dot = "mail@mail..ru"
mail_with_dot_in_local = ".mail@mail.ru"
mail_with_dot_in_domain = "mail@.mail.ru"

incorrect_mail_list = [mail_without_local, mail_without_domain, mail_without_domain_before_dot,
                       mail_without_domain_after_dot, mail_with_double_dot, mail_with_dot_in_local,
                       mail_with_dot_in_domain]

# Текст, названия, подписи, заголовки
auth_page_title = "Ростелеком ID"
start_page_title = "Ростелеком «Старт»"

# # Login form
login_form_title = "Авторизация"
auth_type_menu_tab_phone_text = "Телефон"
auth_type_menu_tab_mail_text = "Почта"
auth_type_menu_tab_login_text = "Логин"
auth_type_menu_tab_personal_account_text = "Лицевой счёт"
input_form_username_phone_placeholder = "Мобильный телефон"
input_form_password_placeholder = "Пароль"
input_form_username_mail_placeholder = "Электронная почта"
input_form_username_login_placeholder = "Логин"
input_form_username_personal_account_placeholder = "Лицевой счёт"
what_is_title_text = "Личный кабинет"
auth_form_error_message_text = "Неверный логин или пароль"
register_link_text = "Зарегистрироваться"

# # Otp form
otp_form_title = "Авторизация по коду"
otp_form_description = "Укажите почту или номер телефона, на которые необходимо отправить код подтверждения"
input_form_email_or_phone_placeholder = "E-mail или мобильный телефон"
button_get_code_text = "Получить код"

# # # Otp code form
otp_code_form_title = "Код подтверждения отправлен"
button_otp_back_phone_text = "Изменить номер"
button_otp_back_mail_text = "Изменить почту"
count_code_input = 6
resend_code_timeout_text = "Получить код повторно"
resend_code_timeout = 120
code_error_invalid_text = "Неверный код. Повторите попытку"
code_error_expired_text = "Срок действия кода истёк. Пожалуйста, запросите код снова"
code_error_exceeded_text = "Превышено количество отправленных кодов в сутки"

# # Reset form
reset_form_title = "Восстановление пароля"
button_reset_text = "Продолжить"
button_reset_back_text = "Вернуться назад"
reset_form_error_text = "Неверный логин или текст с картинки"

# # # Reset choice form
reset_choice_form_title = "Восстановление пароля"
radio_label_by_phone_text = "По номеру телефона"
radio_label_by_mail_text = "По e-mail"
button_reset_choice_text = "Продолжить"
button_reset_choice_back_text = "Вернуться назад"

# # # Reset confirm form
reset_confirm_form_title = "Восстановление пароля"
button_reset_confirm_back_text = "Вернуться назад"

# # # Update password form
update_password_form_title = "Восстановление пароля"
update_password_form_description = "Новый пароль должен содержать от 8 до 20 знаков, включать латинские, заглавные и" \
                                   " строчные буквы, цифры или специальные символы"
input_form_new_password_placeholder = "Пароль"
input_form_password_confirm_placeholder = "Подтверждение пароля"
button_update_text = "Сохранить"
input_form_password_error_less_len_text = "Длина пароля должна быть не менее 8 символов"
input_form_password_error_more_len_text = "Длина пароля должна быть не более 20 символов"
input_form_password_error_no_uppercase_letters_text = "Пароль должен содержать хотя бы одну заглавную букву"
input_form_password_error_no_lowercase_letters_text = "Пароль должен содержать хотя бы одну строчную букву"
input_form_password_error_no_digits_or_special_chars_text = "Пароль должен содержать хотя бы 1 спецсимвол или" \
                                                            " хотя бы одну цифру"
input_form_password_error_not_only_latin_letters_text = "Пароль должен содержать только латинские буквы"
input_form_password_error_passwords_mismatch_text = "Пароли не совпадают"

# # Register form
register_form_title = "Регистрация"
input_form_first_name_placeholder = "Имя"
input_form_last_name_placeholder = "Фамилия"
select_input_form_region_placeholder = "Регион"
input_form_address_placeholder = "E-mail или мобильный телефон"
input_form_password_register_placeholder = "Пароль"
input_form_password_confirm_register_placeholder = "Подтверждение пароля"
button_register_text = "Зарегистрироваться"
link_agreement_href = "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"
link_agreement_text_parts_list = ["политик", "конфиденциальност", "пользовательск", "соглашен"]
input_form_name_error_text = "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
input_form_address_error_text = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате" \
                                " example@email.ru"
region_default = "Москва"
regions_count = 88

# # # Register confirm form
register_confirm_form_title_phone = "Подтверждение телефона"
register_confirm_form_title_mail = "Подтверждение email"
button_register_confirm_back_text_phone = "Изменить номер"
button_register_confirm_back_text_mail = "Изменить email"

# Атрибуты
value_attribute = "value"
class_attribute = "class"
src_attribute = "src"
href_attribute = "href"
autocompleted_attribute = "autocompleted"

# Классы
forgot_password_link_active_class = "rt-link--orange"
forgot_password_link_inactive_class = "rt-link--muted"

# Словари для циклов в тестах
# # Login form
login_tabs_locators_and_auth_type_menu_tab_text_dict = {
    auth_type_menu_tab_phone_locator: auth_type_menu_tab_phone_text,
    auth_type_menu_tab_mail_locator: auth_type_menu_tab_mail_text,
    auth_type_menu_tab_login_locator: auth_type_menu_tab_login_text,
    auth_type_menu_tab_personal_account_locator: auth_type_menu_tab_personal_account_text
}

login_tabs_locators_and_input_form_username_placeholders_dict = {
    auth_type_menu_tab_phone_locator: input_form_username_phone_placeholder,
    auth_type_menu_tab_mail_locator: input_form_username_mail_placeholder,
    auth_type_menu_tab_login_locator: input_form_username_login_placeholder,
    auth_type_menu_tab_personal_account_locator: input_form_username_personal_account_placeholder
}

login_tabs_locators_and_data_correct_dict = {
    auth_type_menu_tab_phone_locator: phone_correct,
    auth_type_menu_tab_mail_locator: mail_correct,
    auth_type_menu_tab_login_locator: login_correct,
    auth_type_menu_tab_personal_account_locator: personal_account_correct
}

# # Reset form
reset_tabs_locators_and_auth_type_menu_tab_text_dict = {
    reset_type_menu_tab_phone_locator: auth_type_menu_tab_phone_text,
    reset_type_menu_tab_mail_locator: auth_type_menu_tab_mail_text,
    reset_type_menu_tab_login_locator: auth_type_menu_tab_login_text,
    reset_type_menu_tab_personal_account_locator: auth_type_menu_tab_personal_account_text
}

reset_tabs_locators_and_input_form_username_placeholders_dict = {
    reset_type_menu_tab_phone_locator: input_form_username_phone_placeholder,
    reset_type_menu_tab_mail_locator: input_form_username_mail_placeholder,
    reset_type_menu_tab_login_locator: input_form_username_login_placeholder,
    reset_type_menu_tab_personal_account_locator: input_form_username_personal_account_placeholder
}

reset_tabs_locators_and_data_correct_dict = {
    reset_type_menu_tab_phone_locator: phone_correct,
    reset_type_menu_tab_mail_locator: mail_correct,
    reset_type_menu_tab_login_locator: login_correct,
    reset_type_menu_tab_personal_account_locator: personal_account_correct
}

# Данные для тестирования полей ввода

letters_latin = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_latin_lowercase = "abcdefghijklmnopqrstuvwxyz"
letters_latin_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits_int = "0123456789"
special_chars = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
letters_cyrillic = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
letters_cyrillic_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
letters_cyrillic_uppercase = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
empty_input_list = ["", " "]

# # Update password form
# # # Поля ввода "Пароль" и "Подтверждение пароля"
valid_chars = letters_latin_lowercase + letters_latin_uppercase + digits_int + special_chars
no_uppercase_letters = letters_latin_lowercase + digits_int + special_chars
no_lowercase_letters = letters_latin_uppercase + digits_int + special_chars
no_digits_or_special_chars = letters_latin_lowercase + letters_latin_uppercase
not_only_latin_letters = valid_chars + letters_cyrillic_lowercase + letters_cyrillic_uppercase
password_valid_len_list = [password_valid_len_interval_list[0], password_valid_len_interval_list[0] + 1,
                           password_valid_len_interval_list[-1] - 1, password_valid_len_interval_list[-1]]
password_invalid_len_list = [0, 1, password_valid_len_interval_list[0] - 1, password_valid_len_interval_list[-1] + 1,
                             120, 121, 1001]

# Register form
# # # Поля "Имя" и "Фамилия"
special_chars_name = """-"""

valid_chars_name = letters_cyrillic_lowercase + letters_cyrillic_uppercase + special_chars_name
not_only_cyrillic_letters = valid_chars_name + letters_latin_lowercase + letters_latin_uppercase
with_digits = valid_chars_name + digits_int
name_valid_len_list = [name_valid_len_interval_list[0], name_valid_len_interval_list[0] + 1,
                       name_valid_len_interval_list[-1] - 1, name_valid_len_interval_list[-1]]
name_invalid_len_list = [0, 1, name_valid_len_interval_list[0] - 1, name_valid_len_interval_list[-1] + 1, 120, 121,
                         1001]
