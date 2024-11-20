# Завдання 5. Видалення HTML-тегів
# Напишіть функцію, яка видаляє всі HTML-теги з тексту.

import re

def remove_html_tags(text):
    html_tag_regex = r'<[^>]+>'
    return re.sub(html_tag_regex, '', text)

html_text = """
<html>
<head><title>Test Page</title></head>
<body>
<h1> Найкращі пропозицій для вас </h1>
<p> Каталог <b> електро </b> товарів: </p>
<a href="https://goods.com"> тисни тут </a> щоб побачити більше.
</body>
</html>
"""

clean_text = remove_html_tags(html_text)
print(clean_text)
