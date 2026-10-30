def find_duplicates(numbers):
    seen = set()
    duplicates = []

    for number in numbers:
        if number in seen:
            if number not in duplicates:
                duplicates.append(number)
        else:
            seen.add(number)

    return duplicates


numbers = [1, 2, 2, 3, 4, 4]
print("Duplicate elements:", find_duplicates(numbers))