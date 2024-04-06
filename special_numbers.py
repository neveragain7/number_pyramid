entry = int(input())

for number in range(1111, 10000):
    is_special = True
    string_number = str(number)
    for index in string_number:
        if int(index) == 0 or entry % int(index) != 0:
            is_special = False
    if is_special:
        print(number, end=" ")