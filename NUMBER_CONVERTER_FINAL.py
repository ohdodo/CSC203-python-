import math

def converting_to_hexa(decNum):
    try:
        return hex(decNum).upper()[2:]
    except ValueError:
        print('Invalid input.')


def baseFrom_to_decimal(number, base):
    try:
        return int(number, base)
    except ValueError:
        print('Invalid number.')


def reversing(originalForm):
    reversedForm = ""
    for i in reversed(originalForm):
        reversedForm += i
    return reversedForm


def decimal_conversion(convertFrom, numberSystem):
    try:
        convertedNumber = ""
        floatNumber = "." in convertFrom
        convertFrom = float(convertFrom)

        currentNumber = math.floor(convertFrom)
        print("\nWhole Digits: ")
        while currentNumber != 0:
            remainder = currentNumber % numberSystem
            answer = math.floor(currentNumber / numberSystem)
            print(f"{currentNumber} / {numberSystem} = {answer} with r = {remainder}")
            if numberSystem == 16:
                remainder = converting_to_hexa(remainder)
            convertedNumber += str(remainder)
            currentNumber = answer
        convertedNumber = convertedNumber[::-1]

        if floatNumber:
            print("\nDecimal Digits")
            convertedNumber = convertedNumber + "."
            decimalDigits = float(convertFrom) - math.floor(convertFrom)
            while decimalDigits != 0:
                answer = decimalDigits * numberSystem
                print(f"{decimalDigits:.2f} * {numberSystem} = {round(answer, 2)}")
                singleDig = math.floor(answer)
                if numberSystem == 16:
                    singleDig = converting_to_hexa(math.floor(answer))
                convertedNumber += str(singleDig)
                decimalDigits = float(answer) - math.floor(answer)
                if int(decimalDigits * 10) == 0 and numberSystem == 2:
                    break

        return convertedNumber

    except ValueError:
        print("Invalid. Must be a decimal number.")


def toDecimal_conversion(convertFrom, numberSystem):
    floatNumber = '.' in convertFrom
    decNumbers = 0
    if floatNumber:
        wholeNumbers = convertFrom.find('.')
        decNumbers = convertFrom[wholeNumbers + 1:]
    else:
        wholeNumbers = len(convertFrom)

    print("\nWhole Digits: ")
    convertedNumber = 0.0
    for places in range(0, wholeNumbers):
        if numberSystem == 16:
            digit = baseFrom_to_decimal(convertFrom[places], 16)
        else:
            digit = int(convertFrom[places])
        result = digit * (numberSystem ** ((wholeNumbers - 1) - places))
        print(f'({digit} * {numberSystem} ^ {((wholeNumbers - 1) - places)}) = {result} + {convertedNumber}')
        convertedNumber += result
    print(convertedNumber)

    if floatNumber:
        print("\nDecimal Digits: ")
        convertedNumber2 = 0.0
        power = -1
        for places in decNumbers:
            if numberSystem == 16:
                digit = baseFrom_to_decimal(places, 16)
            else:
                digit = int(places)
            result = digit * (numberSystem ** power)
            print(f'({places} * {numberSystem} ^ {power}) = {result} + {convertedNumber2}')
            convertedNumber2 += result
            power -= 1
        print(convertedNumber2)
        convertedNumber = convertedNumber + convertedNumber2

    return convertedNumber


def conversion_All(convertFrom, baseFrom, baseTo):
    print("\n\nConverting into decimal first...")
    answer = toDecimal_conversion(convertFrom, baseFrom)
    print(f"{answer}")
    print(f"\n\nThen converting from decimal to base {baseTo}...")
    output = decimal_conversion(str(answer), baseTo)

    return output

def main():
    print("\n\t\tNumber Converter Program\n")
    print("\t\t[1] Decimal")
    print("\t\t[2] Binary")
    print("\t\t[3] Octal")
    print("\t\t[4] Hexadecimal")
    print("\t\t[5] Exit Program")

    select = input("\nSelect Base Number: ")

    if select == "5":
        print("Thank You for using our program")
        quit()

    if select == "1":
        print("\t\tYou Have chosen Decimal Base!\nPlease choose the conversion you want:")
        print("1. Decimal to Binary")
        print("2. Decimal to Octal")
        print("3. Decimal to Hexadecimal")
        choice = int(input("Enter: "))
        if choice == 1:
            convert_from = input("Enter Number to Convert: ")
            print(f'\nFrom {convert_from} to {decimal_conversion(convert_from, 2)}')
        elif choice == 2:
            convert_from = input("Enter Number to Convert: ")
            print(f'\nFrom {convert_from} to {decimal_conversion(convert_from, 8)}')
        elif choice == 3:
            convert_from = input("Enter Number to Convert: ")
            print(f'\nFrom {convert_from} to {decimal_conversion(convert_from, 16)}')
    elif select == "2":
        print("You Have chosen Binary Base! Please choose the conversion you want:")
        print("4. Binary to Decimal")
        print("5. Binary to Octal")
        print("6. Binary to Hexadecimal")
        choice = int(input("Enter: "))
        if choice == 4:
            convert_from = input("Enter Number to Convert: ")
            print(f'\nFrom {convert_from} to {toDecimal_conversion(convert_from, 2)}')
        elif choice == 5:
            convert_from = input("Enter Number to Convert: ")
            print(f'\nFrom {convert_from} to {conversion_All(convert_from, 2, 8)}')
        elif choice == 6:
            convert_from = input("Enter Number to Convert: ")
            print(f'\nFrom {convert_from} to {conversion_All(convert_from, 2, 16)}')
    elif select == "3":
        print("You Have chosen Octal Base! Please choose the conversion you want:")
        print("7. Octal to Decimal")
        print("8. Octal to Binary")
        print("9. Octal to Hexadecimal")
        choice = int(input("Enter: "))
        if choice == 7:
            convert_from = input("Enter Number to Convert: ")
            print(f'\nFrom {convert_from} to {toDecimal_conversion(convert_from, 8)}')
        elif choice == 8:
            convert_from = input("Enter Number to Convert: ")
            print(f'\nFrom {convert_from} to {conversion_All(convert_from, 8, 2)}')
        elif choice == 9:
            convert_from = input("Enter Number to Convert: ")
            print(f'\nFrom {convert_from} to {conversion_All(convert_from, 8, 16)}')
    elif select == "4":
        print("You Have chosen Decimal Base! Please choose the conversion you want:")
        print("10. Hexadecimal to Decimal")
        print("11. Hexadecimal to Binary")
        print("12. Hexadecimal to Octal")
        choice = int(input("Enter: "))
        if choice == 10:
            convert_from = input("Enter Number to Convert: ")
            print(f'\nFrom {convert_from} to {toDecimal_conversion(convert_from, 16)}')
        elif choice == 11:
            convert_from = input("Enter Number to Convert: ")
            print(f'\nFrom {convert_from} to {conversion_All(convert_from, 16, 2)}')
        elif choice == 12:
            convert_from = input("Enter Number to Convert: ")
            print(f'\nFrom {convert_from} to {conversion_All(convert_from, 16, 8)}')

if __name__ == "__main__":
    main()
