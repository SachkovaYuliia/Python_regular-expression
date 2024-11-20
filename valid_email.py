# Завдання 1. Перевірка валідності email
# Напишіть функцію, яка перевіряє, чи є email-адреса валідною. Email вважається валідним, якщо він має формат example@domain.com, де:

# example — послідовність з букв, цифр або точок (але точка не може бути на початку або в кінці).
# domain — послідовність з букв або цифр.
# .com, .net, .org тощо — домен верхнього рівня (TLD) довжиною від 2 до 6 символів.

import re

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9](\.?[a-zA-Z0-9])*@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$'
    return bool(re.match(email_regex, email))

emails = [
    "test@gmail.com",     
    ".test@ukr.net",    
    "test.@test.com",    
    "test.test@gmail.com",   
    "example@test",          
    "example@//ukr.net",    
]

for email in emails:
    print(f"{email}: {is_valid_email(email)}")