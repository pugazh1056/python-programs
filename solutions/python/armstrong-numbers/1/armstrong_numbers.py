def is_armstrong(number):
    digits = str(number)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == number

is_armstrong_number = is_armstrong