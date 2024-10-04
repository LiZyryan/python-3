import string
import keyword

def is_valid_variable_name(name):
    if name in keyword.kwlist:
        return False
    if name.count('_') > 1:
        return False
    if name[0].isdigit():
        return False
    if any(char.isupper() for char in name):
        return False
    if any(char in string.punctuation.replace('_', '') for char in name) or ' ' in name:
        return False
    return True
while True:
    user_input = input("Введіть ім'я змінної (або 'exit' для виходу): ")
    if user_input.lower() == 'exit':
        break
    is_valid = is_valid_variable_name(user_input)
    print(is_valid)
