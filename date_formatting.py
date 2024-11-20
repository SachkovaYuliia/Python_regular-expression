# Завдання 4. Форматування дати
# Напишіть функцію, яка перетворює дати з формату DD/MM/YYYY у формат YYYY-MM-DD.

import re

def date_formatting(date_string):
    date_regex = r'^(\d{2})/(\d{2})/(\d{4})$'

    match = re.match(date_regex, date_string)
    if match:
        day, month, year = match.groups()  
        return f"{year}-{month}-{day}"    
    else:
        return "Invalid date format"

dates = [
    "20/11/2024",  
    "20/12/2024",  
]

for date in dates:
    print(f"{date} -> {date_formatting(date)}")
