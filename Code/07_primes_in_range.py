def primes_in_range(start, end):
    prime_numbers = []

    for number in range(start, end + 1):
        if number < 2:
            continue

        is_prime = True

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(number)

    return prime_numbers