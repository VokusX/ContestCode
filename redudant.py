def duplicate_items(list_numbers):
    list_numbers = sorted(list_numbers)
    redudant = []
    for i in range(1, len(list_numbers)):
        if(list_numbers[i - 1] == list_numbers[i]):
            redudant.append(list_numbers[i])
    return redudant
print(duplicate_items([1, 3, 4, 2, 1, 2]))