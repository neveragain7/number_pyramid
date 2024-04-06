end_number = int(input())
letter_index = int(input())

for number1 in range(1, end_number):
    for number2 in range(1, end_number):
        for letter1 in range(97, 97 + letter_index):
            for letter2 in range(97, 97 + letter_index):
                for number3 in range(1, end_number + 1):
                    if number3 > number1 and number3 > number2:
                        print(f"{number1}{number2}{chr(letter1)}{chr(letter2)}{number3}", end=" ")
