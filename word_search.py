secret_word = "programming"
correct_letters = ""
attempts = 0

while True:
    user_letter = input("Type a letter: ")

    attempts += 1

    if len(user_letter) == 0:  # check if the user typed something
        print("Please, type something")
        continue

    if len(user_letter) > 1:  # check if the user typed just one letter
        print("Please, type just one letter")
        continue

    if user_letter in correct_letters:  # check if the user typed a finded letter
        print("You already typed this letter, please, type other")
        continue

    if user_letter in secret_word:  # check if the user letter is in secret word
        correct_letters += user_letter

    keyword = ""
    for secret_letter in secret_word:  # put a corretly letter in a variable
        if secret_letter in correct_letters:
            keyword += secret_letter
        else:
            keyword += "*"
    print(keyword)

    if keyword == secret_word:  # check if the user guessed the word
        print("Congratulations!")
        print(f"Attempts: {attempts}")
        correct_letters = ""
        attempts = 0
