def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]


def main():
    while True:
        print("Number Systems Converter")
        print("Please Input What would you like to do.")
        print("[1] Decimal")
        print("[2] Binary")
        print("[3] Octal")
        print("[4] Hexadecimal")
        print("[5] Quit")

        choice = input("Your Choice: ")
        num = input("Enter Number: ")
        select = input("Enter Option: ")
        if choice == '0':
            print("Thank You for using this program. Quitting now!")
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again!")
            break

    if choice == '1':
        print("Enter Decimal Number: ", num)
        print("Convert it into? ")
        print("[1] Binary")
        print("[2] Octal")
        print("[3] Hexadecimal")
        print("[4] Quit")
        
        if select == '1':
            return decimal_to_binary(int(num))
        elif select == '2':
            return decimal_to_octal(int(num))
        elif select == '3':
            return decimal_to_hexadecimal(int(num))
        elif select == '4':
            print("Thank You for using this program. Quitting now!")
    elif choice == '2':
        print("Enter Binary Number: ", num)
        print("Convert it into? ")
        print("[1] Decimal")
        print("[2] Octal")
        print("[3] Hexadecimal")
        print("[4] Quit")
    elif choice == '3':
        print("Enter Octal Number: ", num)
        print("Convert it into? ")
        print("[1] Decimal")
        print("[2] Binary")
        print("[3] Hexadecimal")
        print("[4] Quit")
    elif choice == '4':
        print("Enter Hexadecimal Number: ", num)
        print("Convert it into? ")
        print("[1] Decimal")
        print("[2] Binary")
        print("[3] Octal")
        print("[4] Quit")

main()