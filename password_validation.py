# Завдання 6. Перевірка валідності пароля
# Напишіть функцію, яка перевіряє, чи є пароль надійним. Пароль вважається надійним, якщо він:

# містить як мінімум 8 символів,
# містить принаймні одну цифру,
# має хоча б одну велику літеру та одну малу,
# містить хоча б один спеціальний символ (@, #, $, %, &, тощо).

import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    
    has_digit = re.search(r'\d', password)            
    has_upper = re.search(r'[A-Z]', password)         
    has_lower = re.search(r'[a-z]', password)         
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)  

    return all([has_digit, has_upper, has_lower, has_special])

passwords = [
    "Test123***", 
    "test",     
    "TEST123",   
    "=*&()123",       
    "Test@Test1"   
]

for item in passwords:
    print(f"{item} -> {'Пароль є надійним' if is_strong_password(item) else 'Пароль є ненадійним'}")
