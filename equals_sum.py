first_number = int(input())
last_number = int(input())

for number in range(first_number, last_number + 1):
    odd_sum = 0
    even_sum = 0
    string_number = str(number)
    for index, digit in enumerate(string_number):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if odd_sum == even_sum:
        print(number, end=" ")