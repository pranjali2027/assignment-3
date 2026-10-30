def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)

    reversed_num = 0

    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number = number // 10

    return sign * reversed_num