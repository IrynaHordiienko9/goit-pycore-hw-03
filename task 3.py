import re

def normalize_phone(phone_number):
   
    cleaned = re.sub(r'[^\d+]', '', phone_number.strip())
    if cleaned.startswith('+'):
        return cleaned
    elif cleaned.startswith('380'):
        return '+' + cleaned
    else:
        return '+38' + cleaned

numbers = [
    "   +38(050)123-32-34",
    "   0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

for num in numbers:
    print(normalize_phone(num))
