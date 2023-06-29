from functions import *

valid_phone = replace_chars(valid_phone_form, non_digital_chars_in_phone_form_list)
invalid_phone = replace_chars(invalid_phone_form, non_digital_chars_in_phone_form_list)

new_valid_password = generate_password("valid_chars", "valid_len_interval")
valid_passwords_list = create_passwords_list("valid_chars", "valid_len")
valid_chars_invalid_len_passwords_list = create_passwords_list("valid_chars", "invalid_len")
no_uppercase_letters_passwords_list = create_passwords_list("no_uppercase_letters", "valid_len_interval")
no_lowercase_letters_passwords_list = create_passwords_list("no_lowercase_letters", "valid_len_interval")
no_digits_or_special_chars_passwords_list = create_passwords_list("no_digits_or_special_chars", "valid_len_interval")
not_only_latin_letters_passwords_list = create_passwords_list("not_only_latin_letters", "valid_len_interval")

valid_name = generate_name("valid_chars", "valid_len_interval")
valid_name_list = create_name_list("valid_chars", "valid_len")
valid_chars_invalid_len_name_list = create_name_list("valid_chars", "invalid_len")
not_only_cyrillic_letters_name_list = create_name_list("not_only_cyrillic_letters", "valid_len_interval")
with_digits_name_list = create_name_list("with_digits", "valid_len_interval")
with_other_special_chars_name_list = create_name_list("with_other_special_chars", "valid_len_interval")
