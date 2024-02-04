while True:
    first_number = input("Type a number: ")
    second_number = input("Type other number: ")
    operator = input("Type a operator: ")

    operation_flag = None

    int_first_number = float(first_number)
    int_second_number = float(second_number)

    try:
        operation_flag = True
    except:
        operation_flag = None

    if operation_flag is None:  # check if variables is just numbers
        print("Please, type numbers only")
        continue

    operators = "+-*/"

    if operator not in operators:  # check if user typed a valid operator
        print("Invalid operator")
        continue

    if len(operator) > 1:  # check if user typed just one operator
        print("Please, type only one operator")
        continue

    if operator == "+":
        print(
            f"{int_first_number} + {int_second_number} = {int_first_number + int_second_number}"
        )
    elif operator == "-":
        print(
            f"{int_first_number} - {int_second_number} = {int_first_number - int_second_number}"
        )
    elif operator == "*":
        print(
            f"{int_first_number} * {int_second_number} = {int_first_number * int_second_number}"
        )
    elif operator == "/":
        print(
            f"{int_first_number} / {int_second_number} = {int_first_number / int_second_number}"
        )

    leave = input("Do you want to leave? [y]es / [n]o: ").lower().startswith("y")

    if leave is True:
        break
