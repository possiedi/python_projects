questions = [
    {
        "Questions": "What is 2+2?",
        "Options": ["1", "3", "4", "5"],
        "Answer": "4",
    },
    {
        "Questions": "What is 5*5?",
        "Options": ["25", "55", "10", "51"],
        "Answer": "25",
    },
    {
        "Questions": "What is 10/2?",
        "Options": ["4", "5", "2", "1"],
        "Answer": "5",
    },
]

number_of_hits = 0
for question in questions:
    print("Question:", question["Questions"])

    options = question["Options"]

    for i, option in enumerate(options):
        print(f"{i})", option)

    user_option = input("Choose a option: ")

    hit = False
    user_option_int = None
    number_of_options = len(options)

    if user_option.isdigit():
        user_option_int = int(user_option)

    if user_option_int is not None:
        if user_option_int >= 0 and user_option_int < number_of_options:
            if options[user_option_int] == question["Answer"]:
                hit = True

    if hit:
        print("You are correct")
        number_of_hits += 1
    else:
        print("You are incorrect")

print("You hitted", number_of_hits, "times of", len(questions))
