entry = input()
total_prime = 0
total_non_prime = 0

while entry != "stop":
    number = int(entry)
    is_prime = True
    if number < 0:
        print("Number is negative.")
        entry = input()
        continue
    for prime_check_index in range(2, number):
        if number % prime_check_index == 0:
            is_prime = False
            break
    if is_prime:
        total_prime += number
    else:
        total_non_prime += number
    entry = input()

print(f"Sum of all prime numbers is: {total_prime}")
print(f"Sum of all non prime numbers is: {total_non_prime}")
