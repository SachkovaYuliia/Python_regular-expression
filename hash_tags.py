# Завдання 3. Видобування хеш-тегів з тексту
# Напишіть функцію, яка з тексту повертає список хеш-тегів. Хеш-тег — це слово, що починається з #, і може включати лише букви та цифри.

import re

def hashtags_search(text):
    hashtag_regex = r'#\b[A-Za-z0-9]+\b'
    return re.findall(hashtag_regex, text)

text = "Here are some text with hashtags: #Python, #123 and #aaa*/+."

hashtags = hashtags_search(text)
print("Found hashtags:", hashtags)
