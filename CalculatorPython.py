import os

def clear():
    os.system("cls")

while True:
    clear()
    print("Calculator made by Gamerjig!")

    chose = str(input("Enter what sign to use {+, -, /, *}: "))

    amount = int(input("Enter how many numbers to " + chose + ": "))

    a = 0
    numbers = []

    for i in range(amount):
        numbers.append(int(input("Enter num to " + chose + ": ")))

    if chose == "+":
        a = sum(numbers)
    elif chose == "-":
        a = numbers[0]
        for num in numbers[1:]:
            a -= num
    elif chose == "*":
        a = 1
        for num in numbers:
            a *= num
    elif chose == "/":
        a = numbers[0]
        for num in numbers[1:]:
            a /= num
    else:
        print("Warning you must choose from +, -, /, * ")

    print("the total number is: "+ str(a))

    print("Use again?")
    print("1 - Yes")
    print("2 - No")
    again = str(input("Enter your chose: "))
    if again == "1":
        print("Restarting..")
    elif again == "2":
        break
    else:
        print("Must be 1 or 2")
