# Завдання 8. Перевірка на наявність шаблону в тексті
# Напишіть функцію, яка перевіряє, чи міститься у тексті рядок формату AB12CD34, де A, B, C, D — великі літери, а 1, 2, 3, 4 — цифри.

import re

def contains_pattern(text):
    
    pattern = r'[A-Z]{2}\d{2}[A-Z]{2}\d{2}'
    return bool(re.search(pattern, text))

texts = [
    "Lorem AB12CD34",   
    "Lorem 1234ABCD",   
    "Lorem ab12cd34",    
    "Lorem GF89tg64"   
]

for text in texts:
    print(f"'{text}' -> {'Шаблон знайдено' if contains_pattern(text) else 'Шаблон не знайдено'}")
