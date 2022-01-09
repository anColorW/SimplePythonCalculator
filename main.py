print(' /$$$$$$            /$$                     /$$             /$$                           ')
print('/$$__  $$          | $$                    | $$            | $$                           ')
print('| $$  \__/  /$$$$$$ | $$  /$$$$$$$ /$$   /$$| $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$   ')
print('| $$       |____  $$| $$ /$$_____/| $$  | $$| $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$  ')
print('| $$        /$$$$$$$| $$| $$      | $$  | $$| $$  /$$$$$$$  | $$    | $$  \ $$| $$  \__/  ')
print('| $$    $$ /$$__  $$| $$| $$      | $$  | $$| $$ /$$__  $$  | $$ /$$| $$  | $$| $$        ')
print('|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$        ')
print(' \______/  \_______/|__/ \_______/ \______/ |__/ \_______/   \___/   \______/ |__/        ')


print("1. Add numbers")
print("2. Substract numbers")
print("3. Multiple numbers")
print("4. Divide numbers")
print("5. Divide numbers with rounding")
print("6. Modulo, rest of dividng 2 numbers")
print("7. Square numbers")

chnum = input("Choose math operator: ")

if chnum == '' or float(chnum) >= 8 or float(chnum) <= 0:
    print("Your math operator is invalid!")
    input("Click enter to exit program")
    exit()
num1 = input("Type 1st Number: ")
if num1 == '':
    print("")
    print("You didnt type anything!")
    print("")
    input("Click enter to exit program")
    exit()
num2 = input("Type 2nd Number: ")
if num2 == '':
    print("")
    print("You didnt type anything!")
    print("")
    input("Click enter to exit program")
    exit()

inc = "Your values are incorrect"

if float(num1) == 0 or float(num2) == 0:
    print("")
    print("Your values are incorrect, probably u type '0'!")
    input("Click enter to exit program")
    exit()
else:
    if chnum == '1':
        sumO = float(num1) + float(num2)
        print("Sum of your numbers equals to: " + str(sumO))
    elif chnum == '2':
        sub = float(num1) - float(num2)
        print("Substract of your numbers equals to: " + str(sub))
    elif chnum == '3':
        mul = float(num1) * float(num2)
        print("Multiple of your numbers equals to: " + str(mul))
    elif chnum == '4':
        div = float(float(num1)) / float(num2)
        print("Divide of your numbers equals to: " + str(div))
    elif chnum == '5':
        colname = float(num1) // float(num2)
        print("Divide with rounding of your numbers equals to: " + str(colname))
    elif chnum == '6':
        mod = float(num1) % float(num2)
        print("Modulo of your numbers equals to: " + str(mod))
    elif chnum == '7':
        sqr = float(num1) ** float(num2)
        print("Square of your numbers equals to: " + str(sqr))

input("Click enter to exit program.")
