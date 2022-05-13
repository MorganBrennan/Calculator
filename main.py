print("Main Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division\n")
while True:
  try:
    userInput = int(input("What do you want to do? "))
    if userInput>0 and userInput<5:
      print("Entered successfully")
      break;
    else:
      print("Input should be between 1 and 4")
  except ValueError:
    print("Provide a value between 1 and 4")
    continue

if userInput == 1:
    while True:
        try:
            print("You chose addition. Please enter 2 numbers to add\n")
            number1 = int(input("Number 1: "))
            number2 = int(input("Number 2: "))
            sum = number1+number2
            total = print(number1, "+", number2, "=", sum)
            break
        except ValueError:
            print("Please provide a number")
            continue

elif userInput == 2:
    while True:
        try:
            print("You chose subtraction. Please enter 2 numbers to subtract\n")
            number1 = int(input("Number 1: "))
            number2 = int(input("Number 2: "))
            sum = number1-number2
            total = print(number1, "-", number2, "=", sum)
            break
        except ValueError:
            print("Please provide a number")
            continue

elif userInput == 3:
    while True:
        try:
            print("You chose multiplication. Please enter 2 numbers to multiply\n")
            number1 = int(input("Number 1: "))
            number2 = int(input("Number 2: "))
            sum = number1*number2
            total = print(number1, "*", number2, "=", sum)
            break
        except ValueError:
            print("Please provide a number")
            continue

elif userInput == 4:
    while True:
        try:
            print("You chose division. Please enter 2 numbers to divide\n")
            number1 = int(input("Number 1: "))
            number2 = int(input("Number 2: "))
            sum = number1/number2
            total = print(number1, "/", number2, "=", sum)
            break
        except ValueError:
            print("Please provide a number")
            continue
