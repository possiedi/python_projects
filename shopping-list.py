import os

shopping_list = []

while True:
    option = input("What do you desire? [i]nsert, [d]elete, [s]how? ")

    if option == "i":
        os.system("cls")
        item = input("Type a item: ")
        shopping_list.append(item)  # put a item in shopping list
    elif option == "d":
        os.system("cls")

        try:
            str_index = input("Type an index you desire to delete: ")
            int_index = int(str_index)
            del shopping_list[int_index]
        except TypeError:
            print("Type just numbers")
        except IndexError:
            print("This index doesn't exist")
        except Exception:
            print("Unknown error")
    elif option == "s":
        os.system("cls")
        if len(shopping_list) == 0:  # if list is empty, show a message
            print("This list is empty")

        for i, item in enumerate(shopping_list):  # It shows the index and the item
            print(i, item)
    else:
        print("This option doesn't exist")
