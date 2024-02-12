import random

nine_digits = ""

for i in range(0, 9):
    nine_digits += str(random.randint(0, 9))

# first digit calculation
countdown_1 = 10
total = 0

for char in nine_digits:
    total += int(char) * countdown_1
    countdown_1 -= 1

calculation = (total * 10) % 11

first_digit = 0 if calculation > 9 else calculation

ten_digits = nine_digits + str(first_digit)

# second digit calculation
countdown_2 = 11
total = 0

for char in ten_digits:
    total += int(char) * countdown_2
    countdown_2 -= 1

calculation_2 = (total * 10) % 11

second_digit = 0 if calculation_2 > 9 else calculation_2

cpf = f"{nine_digits}{first_digit}{second_digit}"

print(cpf)
