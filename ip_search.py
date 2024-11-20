# Завдання 7. Пошук IP-адрес
# Напишіть функцію, яка з тексту витягує всі IPv4-адреси. IPv4-адреса складається з чотирьох чисел (від 0 до 255), розділених крапками.

import re

def find_ipv4_addresses(text):
    ipv4_regex = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    
    addresses = re.findall(ipv4_regex, text)

    valid_addresses = [addr for addr in addresses if all(0 <= int(part) <= 255 for part in addr.split('.'))]
    
    return valid_addresses

text = "Some IP addresses:192.192.192.192, 255.255.255.255 0.0.0.0 300.300.300.300"

ipv4_addresses = find_ipv4_addresses(text)
print("Found IPv4 addresses:", ipv4_addresses)
