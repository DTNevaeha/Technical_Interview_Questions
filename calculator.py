# Basic calculator using multiple classes depending on the input of the user.

print("Hello, please select what you would like to do below."
     "\n 1 - Add \n 2 - Subtract \n 3 - Multiply \n 4 - Divide \n Q - to quit")


class MathTime:
    def math(equation):
        try: 
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter a valid number \n"
                  " 1 - Add \n 2 - Subtract \n 3 - Multiply \n 4 - Divide \n Q - to quit")
        else:
            z = eval(f"{x} {equation} {y}")
            print(f"{x} {equation} {y} = {z}")
            print("\n What would you like to do next?"
            "\n 1 - Add \n 2 - Subtract \n 3 - Multiply \n 4 - Divide \n Q - to quit")


while True:
    selection = input().lower()
    if selection == 'q':
        print("Thanks!")
        break
    elif selection in ['1', '2', '3', '4']:
        if selection == '1':
            selection = "+"
            print("You chose Addition")
        elif selection == '2':
            selection = "-"
            print("You chose Subtraction")
        elif selection == '3':
            selection = "*"
            print("You chose Multiplication")
        else:
            selection = "/"
            print("You chose Division")
        MathTime.math(selection)
    else:
        print("That is not a valid input \n"
              " 1 - Add \n 2 - Subtract \n 3 - Multiply \n 4 - Divide \n Q - to quit")
