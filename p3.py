def m_dgts_until_s_dgt(number):
    if number <= 9:
        return number
    while number > 9:
        product = 1
        for digit in str(number):
            product *= int(digit)
        number = product
    return number
user_input = int(input("Введіть ціле число: "))
result = m_dgts_until_s_dgt(user_input)
print("Результат:", result)
