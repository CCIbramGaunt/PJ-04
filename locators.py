from selenium.webdriver.common.by import By


auth_page_title_locator = (By.XPATH, '//title[contains(text(), "Ростелеком ID")]')
account_page_title_locator = (By.XPATH, '//title[contains(text(), "Ростелеком ID")]')
start_page_title_locator = (By.XPATH, '//title[contains(text(), "Ростелеком «Старт»")]')

# Auth page
page_right_locator = (By.ID, 'page-right')
page_left_locator = (By.ID, 'page-left')

# # Login form
# # # page right
login_form_locator = (By.CLASS_NAME, 'login-form-container')
login_form_title_locator = (By.XPATH, '//*[contains(@class, "login-form-container")]//*[contains(@class,'
                                      ' "card-container__title")]')
login_form_page_right_locator = (By.XPATH, '//*[@id="page-right"]//*[contains(@class, "login-form-container")]')
auth_type_menu_login_form_locator = (By.XPATH, '//*[contains(@class, "login-form-container")]//*[contains(@class,'
                                               ' "tabs-input-container__tabs")]')
auth_type_menu_tab_phone_locator = (By.XPATH, '//*[contains(@class, "tabs-input-container__tabs")]//'
                                              '*[@id="t-btn-tab-phone"]')
auth_type_menu_tab_mail_locator = (By.XPATH, '//*[contains(@class, "tabs-input-container__tabs")]//'
                                             '*[@id="t-btn-tab-mail"]')
auth_type_menu_tab_login_locator = (By.XPATH, '//*[contains(@class, "tabs-input-container__tabs")]//'
                                              '*[@id="t-btn-tab-login"]')
auth_type_menu_tab_personal_account_locator = (By.XPATH, '//*[contains(@class, "tabs-input-container__tabs")]//'
                                                         '*[@id="t-btn-tab-ls"]')
auth_type_menu_tab_active_locator = (By.XPATH, '//*[contains(@class, "tabs-input-container__tabs")]//*[contains(@class,'
                                               ' "rt-tab--active")]')
input_form_username_locator = (By.XPATH, '//*[contains(@class, "login-form-container")]//input[@id="username"]')
input_form_password_locator = (By.XPATH, '//*[contains(@class, "login-form-container")]//input[@id="password"]')
input_form_username_placeholder_locator = (By.XPATH, '//input[@id="username"]//following-sibling::*[contains(@class,'
                                                     ' "rt-input__placeholder")]')
input_form_username_value_locator = (By.XPATH, '//input[@id="username"]//ancestor::*//*[@name = "username"]')
input_form_password_placeholder_locator = (By.XPATH, '//input[@id="password"]//following-sibling::*[contains(@class,'
                                                     ' "rt-input__placeholder")]')
input_form_password_text_locator = (By.XPATH, '//input[@id="password"]//preceding-sibling::*//*[contains(@class,'
                                              ' "rt-input__mask-start")]')
input_form_username_text_locator = (By.XPATH, '//input[@id="username"]//preceding-sibling::*//*[contains(@class,'
                                              ' "rt-input__mask-start")]')
input_form_error_text_locator = (By.XPATH, '//*[contains(@class, "rt-input-container__meta--error")]')
button_login_locator = (By.XPATH, '//*[contains(@class, "login-form-container")]//button[@id="kc-login"]')
forgot_password_link_locator = (By.XPATH, '//*[contains(@class, "login-form-container")]//*[@id="forgot_password"]')
auth_form_error_message_locator = (By.XPATH, '//*[contains(@class, "login-form-container")]//*[@id='
                                             '"form-error-message"]')
register_link_locator = (By.XPATH, '//*[contains(@class, "login-form-container")]//*[@id="kc-register"]')

# # # page left
what_is_locator = (By.XPATH, '//*[@id="page-left"]//*[contains(@class, "what-is-container")]')
what_is_logo_locator = (By.XPATH, '//*[@id="page-left"]//*[contains(@class, "rt-logo")]')
what_is_title_locator = (By.XPATH, '//*[@id="page-left"]//*[contains(@class, "what-is__title")]')
what_is_description_locator = (By.XPATH, '//*[@id="page-left"]//*[contains(@class, "what-is__desc")]')

# # Otp form
otp_form_locator = (By.CLASS_NAME, 'otp-form-container')
otp_form_title_locator = (By.XPATH, '//*[contains(@class, "otp-form-container")]//*[contains(@class,'
                                    ' "card-container__title")]')
otp_form_description_locator = (By.XPATH, '//*[contains(@class, "otp-form-container")]//*[contains(@class,'
                                          ' "card-container__desc")]')
input_form_email_or_phone_locator = (By.XPATH, '//*[contains(@class, "otp-form-container")]//*[@id="address"]')
input_form_email_or_phone_placeholder_locator = (By.XPATH, '//input[@id="address"]//following-sibling::'
                                                           '*[contains(@class, "rt-input__placeholder")]')
input_form_email_or_phone_value_locator = (By.XPATH, '//input[@id="address"]//ancestor::*//*[@name = "address"]')
input_form_email_or_phone_error_text_locator = (By.XPATH, '//*[contains(@class, "rt-input-container__meta--error")]')
button_get_code_locator = (By.XPATH, '//*[contains(@class, "otp-form-container")]//button[@id="otp_get_code"]')
otp_form_timeout_text_locator = (By.XPATH, '//*[contains(@class, "otp-form-container")]//*[contains(@class,'
                                           ' "otp-form__timeout")]')

# # # Otp code form
otp_code_form_locator = (By.CLASS_NAME, 'otp-code-form-container')
otp_code_form_title_locator = (By.XPATH, '//*[contains(@class, "otp-code-form-container")]//*[contains(@class,'
                                         ' "card-container__title")]')
otp_code_form_description_locator = (By.XPATH, '//*[contains(@class, "otp-code-form-container")]//*[contains(@class,'
                                               ' "otp-code-form-container__desc")]')
button_otp_back_phone_locator = (By.XPATH, '//*[contains(@class, "otp-code-form-container")]//*[contains(@name,'
                                           ' "otp_back_phone")]')
input_code_all_locator = (By.XPATH, '//*[contains(@class, "otp-code-form-container")]//*[contains(@id, "rt-code")]')
input_code_parent_all_locator = (By.XPATH, '//*[contains(@id, "rt-code")]//ancestor::*[contains(@class, "rt-input ")]')
input_code_parent_active_locator = (By.XPATH, '//*[contains(@class, "rt-input--active")]')
otp_resend_code_timeout_text_locator = (By.XPATH, '//*[contains(@class, "otp-code-form-container")]//*[contains(@class,'
                                                  ' "code-input-container__timeout")]')
button_otp_resend_code_locator = (By.XPATH, '//*[contains(@class, "otp-code-form-container")]//*[contains(@name,'
                                            ' "otp_resend_code")]')
otp_code_error_locator = (By.XPATH, '//*[contains(@class, "otp-code-form-container")]//*[contains(@id,'
                                    ' "form-error-message")]')

# # Reset form
reset_form_locator = (By.CLASS_NAME, 'reset-form-container')
reset_form_title_locator = (By.XPATH, '//*[contains(@class, "reset-form-container")]//*[contains(@class,'
                                      ' "card-container__title")]')
reset_type_menu_locator = (By.XPATH, '//*[contains(@class, "reset-form-container")]//*[contains(@class,'
                                     ' "tabs-input-container__tabs")]')
reset_type_menu_tab_phone_locator = (By.XPATH, '//*[contains(@class, "tabs-input-container__tabs")]//'
                                               '*[@id="t-btn-tab-phone"]')
reset_type_menu_tab_mail_locator = (By.XPATH, '//*[contains(@class, "tabs-input-container__tabs")]//'
                                              '*[@id="t-btn-tab-mail"]')
reset_type_menu_tab_login_locator = (By.XPATH, '//*[contains(@class, "tabs-input-container__tabs")]//'
                                               '*[@id="t-btn-tab-login"]')
reset_type_menu_tab_personal_account_locator = (By.XPATH, '//*[contains(@class, "tabs-input-container__tabs")]//'
                                                          '*[@id="t-btn-tab-ls"]')
reset_type_menu_tab_active_locator = (By.XPATH, '//*[contains(@class, "tabs-input-container__tabs")]//*[contains('
                                                '@class, "rt-tab--active")]')
input_form_username_reset_locator = (By.XPATH, '//*[contains(@class, "reset-form-container")]//input[@id="username"]')
input_form_captcha_locator = (By.XPATH, '//*[contains(@class, "reset-form-container")]//input[@id="captcha"]')
image_captcha_locator = (By.XPATH, '//*[contains(@class, "reset-form-container")]//img[contains(@class,'
                                   ' "rt-captcha__image")]')
button_reload_captcha_locator = (By.XPATH, '//*[contains(@class, "reset-form-container")]//button[contains(@class,'
                                           ' " rt-captcha__reload")]')
button_reset_locator = (By.XPATH, '//*[contains(@class, "reset-form-container")]//button[@id="reset"]')
button_reset_back_locator = (By.XPATH, '//*[contains(@class, "reset-form-container")]//button[@id="reset-back"]')
reset_form_error_text_locator = (By.XPATH, '//*[contains(@class, "reset-form-container")]//*[@id="form-error-message"]')

# # # Reset choice form
reset_choice_form_locator = (By.CLASS_NAME, 'reset-form-choice-container')
reset_choice_form_title_locator = (By.XPATH, '//*[contains(@class, "reset-form-choice-container")]//*[contains(@class,'
                                             ' "card-container__title")]')
radio_input_by_phone_locator = (By.XPATH, '//*[contains(@class, "reset-form-choice-container")]//input[@value="sms"]')
radio_input_by_mail_locator = (By.XPATH, '//*[contains(@class, "reset-form-choice-container")]//input[@value="email"]')
radio_input_active_locator = (By.XPATH, '//*[contains(@class, "reset-form-choice-container")]//input[@autocompleted]')
radio_label_by_phone_locator = (By.XPATH, '//input[@value="sms"]//..//*[@class="rt-radio__label"]')
radio_label_by_mail_locator = (By.XPATH, '//input[@value="email"]//..//*[@class="rt-radio__label"]')
button_reset_choice_locator = (By.XPATH, '//*[contains(@class, "reset-form-choice-container")]//button[@id="reset"]')
button_reset_choice_back_locator = (By.XPATH, '//*[contains(@class, "reset-form-choice-container")]//button[@id='
                                              '"reset-back"]')

# # # Reset confirm form
reset_confirm_form_locator = (By.CLASS_NAME, 'reset-form-confirm-container')
reset_confirm_form_title_locator = (By.XPATH, '//*[contains(@class, "reset-form-confirm-container")]//*[contains('
                                              '@class, "card-container__title")]')
reset_confirm_form_description_locator = (By.XPATH, '//*[contains(@class, "reset-form-confirm-container")]//*[contains('
                                                    '@class, "card-container__desc")]')
button_reset_confirm_back_locator = (By.XPATH, '//*[contains(@class, "reset-form-confirm-container")]//button[contains('
                                               '@name, "cancel_reset")]')
input_reset_code_all_locator = (By.XPATH, '//*[contains(@class, "reset-form-confirm-container")]//*[contains(@id,'
                                          ' "rt-code")]')
reset_resend_code_timeout_text_locator = (By.XPATH, '//*[contains(@class, "reset-form-confirm-container")]//*[contains('
                                                    '@class, "code-input-container__timeout")]')
button_reset_resend_code_locator = (By.XPATH, '//*[contains(@class, "reset-form-confirm-container")]//*[contains(@name,'
                                              ' "otp_resend_code")]')
reset_code_error_locator = (By.XPATH, '//*[contains(@class, "reset-form-confirm-container")]//*[contains(@id,'
                                      ' "form-error-message")]')

# # # Update password form
update_password_form_locator = (By.CLASS_NAME, 'update-password-form-container')
update_password_form_title_locator = (By.XPATH, '//*[contains(@class, "update-password-form-container")]//*[contains('
                                                '@class, "card-container__title")]')
update_password_form_description_locator = (By.XPATH, '//*[contains(@class, "update-password-form-container")]//'
                                                      '*[contains(@class, "card-container__desc")]')
input_form_new_password_locator = (By.XPATH, '//*[contains(@class, "update-password-form-container")]//input[@id='
                                             '"password-new"]')
input_form_new_password_placeholder_locator = (By.XPATH, '//input[@id="password-new"]//following-sibling::*[contains('
                                                         '@class, "rt-input__placeholder")]')
input_form_password_confirm_locator = (By.XPATH, '//*[contains(@class, "update-password-form-container")]//input[@id='
                                                 '"password-confirm"]')
input_form_password_confirm_placeholder = (By.XPATH, '//input[@id="password-confirm"]//following-sibling::*[contains('
                                                     '@class, "rt-input__placeholder")]')
input_form_new_password_error_text_locator = (By.XPATH, '//input[@id="password-new"]//..//..//*[contains(@class,'
                                                        ' "rt-input-container__meta--error")]')
input_form_password_confirm_error_text_locator = (By.XPATH, '//input[@id="password-confirm"]//..//..//*[contains('
                                                            '@class, "rt-input-container__meta--error")]')
button_update_locator = (By.XPATH, '//*[contains(@class, "update-password-form-container")]//button[@id='
                                   ' "t-btn-reset-pass"]')

# # Register form
register_form_locator = (By.CLASS_NAME, 'register-form-container')
register_form_page_right_locator = (By.XPATH, '//*[@id="page-right"]//*[contains(@class, "register-form-container")]')
register_form_title_locator = (By.XPATH, '//*[contains(@class, "register-form-container")]//*[contains(@class,'
                                         ' "card-container__title")]')
input_form_first_name_locator = (By.XPATH, '//*[contains(@class, "register-form-container")]//input[@name="firstName"]')
input_form_first_name_placeholder_locator = (By.XPATH, '//input[@name="firstName"]//following-sibling::*[contains('
                                                       '@class, "rt-input__placeholder")]')
input_form_first_name_error_text_locator = (By.XPATH, '//input[@name="firstName"]//..//..//*[contains(@class,'
                                                      ' "rt-input-container__meta--error")]')
input_form_last_name_locator = (By.XPATH, '//*[contains(@class, "register-form-container")]//input[@name="lastName"]')
input_form_last_name_placeholder_locator = (By.XPATH, '//input[@name="lastName"]//following-sibling::*[contains('
                                                      '@class, "rt-input__placeholder")]')
input_form_last_name_error_text_locator = (By.XPATH, '//input[@name="lastName"]//..//..//*[contains(@class,'
                                                     ' "rt-input-container__meta--error")]')
select_input_form_region_locator = (By.XPATH, '//*[contains(@class, "register-form-container")]//*[contains(@class,'
                                              ' "rt-select")]//input')
select_input_form_region_placeholder_locator = (By.XPATH, '//*[contains(@class, "rt-select")]//following-sibling::'
                                                          '*[contains(@class, "rt-input__placeholder")]')
select_item_list_region_locator = (By.XPATH, '//*[contains(@class, "rt-select")]//*[contains(@class,'
                                             ' "rt-scroll-container ")]')
select_item_region_locator = (By.XPATH, '//*[contains(@class, "rt-select__list-item")]')
input_form_address_locator = (By.XPATH, '//*[contains(@class, "register-form-container")]//input[@id="address"]')
input_form_address_placeholder_locator = (By.XPATH, '//input[@id="address"]//following-sibling::*[contains(@class,'
                                                    ' "rt-input__placeholder")]')
input_form_address_error_text_locator = (By.XPATH, '//input[@id="address"]//..//..//*[contains(@class,'
                                                   ' "rt-input-container__meta--error")]')
input_form_password_register_locator = (By.XPATH, '//*[contains(@class, "register-form-container")]//input[@id='
                                                  '"password"]')
input_form_password_register_placeholder_locator = (By.XPATH, '//input[@id="password"]//following-sibling::*[contains('
                                                              '@class, "rt-input__placeholder")]')
input_form_password_register_error_text_locator = (By.XPATH, '//input[@id="password"]//..//..//*[contains(@class,'
                                                             ' "rt-input-container__meta--error")]')
input_form_password_confirm_register_locator = (By.XPATH, '//*[contains(@class, "register-form-container")]//input[@id='
                                                          '"password-confirm"]')
input_form_password_confirm_register_placeholder_locator = (By.XPATH, '//input[@id="password-confirm"]//'
                                                                      'following-sibling::*[contains(@class,'
                                                                      ' "rt-input__placeholder")]')
input_form_password_confirm_register_error_text_locator = (By.XPATH, '//input[@id="password-confirm"]//..//..//'
                                                                     '*[contains(@class,'
                                                                     ' "rt-input-container__meta--error")]')
button_register_locator = (By.XPATH, '//*[contains(@class, "register-form-container")]//button[@name="register"]')
link_agreement_locator = (By.XPATH, '//*[contains(@class, "register-form-container")]//*[contains(@class,'
                                    ' "auth-policy")]//a')
input_form_register_error_text_locator = (By.XPATH, '//*[contains(@class, "register-form-container")]//'
                                                    '*[contains(@class, "rt-input-container__meta--error")]')

# # # Register confirm form
register_confirm_form_locator = (By.CLASS_NAME, 'register-confirm-form-container')
register_confirm_form_title_locator = (By.XPATH, '//*[contains(@class, "register-confirm-form-container")]//'
                                                 '*[contains(@class, "card-container__title")]')
register_confirm_form_description_locator = (By.XPATH, '//*[contains(@class, "register-confirm-form-container")]//'
                                                       '*[contains(@class, "card-container__desc")]')
button_register_confirm_back_locator = (By.XPATH, '//*[contains(@class, "register-confirm-form-container")]//'
                                                  'button[contains(@name, "otp_back_phone")]')
input_register_code_all_locator = (By.XPATH, '//*[contains(@class, "register-confirm-form-container")]//'
                                             '*[contains(@id, "rt-code")]')
register_resend_code_timeout_text_locator = (By.XPATH, '//*[contains(@class, "register-confirm-form-container")]//'
                                                       '*[contains(@class, "code-input-container__timeout")]')
button_register_resend_code_locator = (By.XPATH, '//*[contains(@class, "register-confirm-form-container")]//'
                                                 '*[contains(@name, "otp_resend_code")]')
register_code_error_locator = (By.XPATH, '//*[contains(@class, "register-confirm-form-container")]//*[contains(@id,'
                                         ' "form-error-message")]')


# Account page
button_account_page_logout_locator = (By.ID, 'logout-btn')

# Start page
menu_start_page_account_locator = (By.XPATH, '//*[contains(@class, "sc-emDsmM ccJkbA")]')
button_start_page_logout_locator = (By.XPATH, '//*[contains(text(), "Выйти")]//ancestor::*[contains(@type, "button")]')
