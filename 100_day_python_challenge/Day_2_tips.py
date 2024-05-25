# Calculate payment for the cost of a bill split between X amount of people and X percentage. Round to 2 decimal places.


while True:
    cost = input("What is the total cost of the meal? ")
    people: int = input("How many people are splitting the bill? ")
    tips: int = input("What percentage of tip for everyone? ")
    if tips.isdigit():
        if float(tips) >= 0:
            tip = (float(tips) / 100) + 1 # Convert a whole number into a percentage
            if cost.replace(".", "").isnumeric():
                value = float(cost)
                if people.isdigit() and int(people) >0:
                    total = (float(value) / int(people)) * tip
                    rounded_total = round(total, 2)
                    print(f"Each person would pay: {rounded_total} \n"
                        f"{cost} / {people} * {tip} = {rounded_total}")
                    break
                else:
                    print("Please enter, whole positive numbers for people")
            else:
                print("Please enter numbers only")
    else:
        print("Please enter a whole positive number for a tip")
