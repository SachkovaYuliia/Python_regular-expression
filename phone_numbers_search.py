# Завдання 2. Пошук телефонних номерів
# Напишіть функцію, яка знаходить усі телефонні номери в тексті. Номери можуть бути в форматах:

# (123) 456-7890
# 123-456-7890
# 123.456.7890
# 1234567890

import re

def phone_numbers_search(text):
    phone_regex = r'\(?\d{3}\)?[.\-\s]?\d{3}[.\-\s]?\d{4}'
    return re.findall(phone_regex, text)

text = "some text (123) 456-7890 text 123/456/789 123*456*789 123-456-7890 text 123.456.7890 text 1234567890"

phone_numbers = phone_numbers_search(text)
print("Found phone numbers:", phone_numbers)
