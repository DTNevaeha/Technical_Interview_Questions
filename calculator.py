# Basic calculator using multiple classes depending on the input of the user.

print("Hello, please select what you would like to do below."
     "\n 1 - Add \n 2 - Subtract \n 3 - Multiply \n 4 - Divide \n Q - to quit")


class Addition:
    def add():
        # x = input("Enter the first number: ")
        # y = input("Enter the second number: ")
        try: 
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter a valid number \n"
                  " 1 - Add \n 2 - Subtract \n 3 - Multiply \n 4 - Divide \n Q - to quit")
            # continue
        else:
            z = float(x) + float(y)
            print(f"{x} + {y} = {z}")
            print("\n What would you like to do next?"
              "\n 1 - Add \n 2 - Subtract \n 3 - Multiply \n 4 - Divide \n Q - to quit")

class Subtration:
    pass

class Multiplication:
    pass

class Division:
    pass


while True:
    selection = input().lower()
    if selection == 'q':
        print("Thanks!")
        break
    elif selection == '1':
        print("You chose 1")
        Addition.add()
    elif selection == '2':
        print("You chose 2")
    elif selection == '3':
        print("You chose 3")
    elif selection == '4':
        print("You chose 4")
    else:
        print("That is not a valid input")

