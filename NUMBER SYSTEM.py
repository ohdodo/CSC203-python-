import os


def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        print(f"\nDecimal Values: {decimal} / 2 = {decimal//2}  remainder = {remainder}")
        decimal = decimal // 2
    return binary

def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        print(f"\nOctal Values: {decimal} / 8 = {decimal//8}  remainder = {remainder}")
        decimal = decimal // 8
    return octal

def decimal_to_hexadecimal(decimal):
    hexadecimal = ""
    hex_chars = "0123456789ABCDEF"
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        print(f"\nHexadecimal Values: {decimal} / 16 = {decimal//16}  remainder = {hex_chars[remainder]}")
        decimal = decimal // 16
    return hexadecimal
        
def binary_to_decimal(binary):
    decimal = 0
    binary = binary[:: -1] #reverses the code so it reads from right to left
    for i in range(len(binary)):
            if binary[i] =='1':
                increment = 2 ** i
                answer = increment * int(binary[i])
                decimal += increment
            elif binary [i] == '0': 
                answer = 0
            print(f"Binary Values: {binary[i]} * 2^{i} = {answer}")
                
    return decimal

def binary_to_octal(binary):
    binary = binary[::-1]  # Reverse the binary string so we can process it from right to left
    octal = ""

    # Pad the binary string with zeros to ensure it's a multiple of 3
    while len(binary) % 3 != 0:
        binary += '0'

    for i in range(0, len(binary), 3):
        # Take the next three binary digits and convert them to decimal
        chunk = binary[i:i + 3]
        binaryslice = chunk
        decimal = sum(int(chunk[j]) * (2 ** j) for j in range(3))

        # Convert the decimal chunk to octal and append to the result
        octal = str(decimal) + octal

        print(f"\nBinary Values : {binaryslice} -> {decimal}")

    return octal

def binary_to_hexadecimal(binary):
    binary = binary[::-1]  # Reverse the binary string so we can process it from right to left
    hexadecimal = ""

    # Pad the binary string with zeros to ensure it's a multiple of 4
    while len(binary) % 4 != 0:
        binary += '0'

    for i in range(0, len(binary), 4):
        # Take the next four binary digits and convert them to decimal
        chunk = binary[i:i + 4]
        binaryslice = chunk
        decimal = sum(int(chunk[j]) * (2 ** j) for j in range(4))

        # Convert the decimal chunk to hexadecimal and append to the result
        hexadecimal = hex(decimal)[2:] + hexadecimal

        print(f"Binary Values: {binaryslice} -> {hex(decimal)[2:]}")

    return hexadecimal

def octal_to_decimal(octal):
    decimal = 0
    octal = str(octal)  
    length = len(octal)  
    for i in range(length):
        digit = ord(octal[i]) - ord('0')
        decimal += digit * (8 ** (length - 1 - i)) 
        print(f"Step {i+1}: Convert {octal[i]} to decimal => {digit * (8 ** (length - 1 - i))}")

    # print(f"\nOctal {octal} in decimal is {decimal}")
    return decimal

def octal_to_binary(octal):
    octal = str(octal)
    length = len(octal)
    binary = ""
    binary_dict = {"0": "000", "1": "001", "2": "010", "3": "011", "4": "100", "5": "101", "6": "110", "7": "111"}

    for i in range(length):
        digit = octal[i]
        binary_digit = binary_dict[digit]
        binary += binary_digit
        print(f"Step {i+1}: Convert {digit} to binary => {binary_digit}")

    print(f"\nOctal {octal} in binary is {binary}")

    return binary

def octal_to_hexadecimal(octal):
    octal = str(octal)
    length = len(octal)
    hexadecimal = ""
    hexa_dict = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7"}

    for i in range(length):
        digit = octal[i]
        hexa_digit = hexa_dict[digit]
        hexadecimal += hexa_digit
        print(f"Step {i+1}: Convert {digit} to binary => {hexa_digit}")

    print(f"\nOctal {octal} in binary is {hexadecimal}")

    return hexadecimal

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def hexadecimal_to_binary(hexadecimal):
    decimal = int(hexadecimal, 16)
    return bin(decimal)[2:]

def hexadecimal_to_octal(hexadecimal):
    decimal = int(hexadecimal, 16)
    return oct(decimal)[2:]



def main():
    print("Number Systems Converter")
    print("Please Input What would you like to do.")
    print("[1] Decimal")
    print("[2] Binary")
    print("[3] Octal")
    print("[4] Hexadecimal")
    print("[5] Quit")

    choice = input("Your Choice: ")
        
    try:
        if choice == '5':
            print("Thank You for using this program. Quitting now!")
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again!")
    except ValueError:
            print('Invalid number.')

    num = input("Input Your Number: ")

    try:
        if choice == '1':
            print("Enter Decimal Number: ", num)
            print("Convert it into? ")
            print("[1] Binary")
            print("[2] Octal")
            print("[3] Hexadecimal")
            print("[4] Quit")
        
            select = input("Enter Option: ")

            if select == '1':
                result = decimal_to_binary(int(num))
                print(f"\nDecimal to Binary: {num} to {result}")
            elif select == '2':
                result = decimal_to_octal(int(num))
                print(f"\nDecimal to Octal: {num} to {result}")
            elif select == '3':
                result = decimal_to_hexadecimal(int(num))
                print(f"\nDecimal to Hexadecimal: {num} to {result}")
            elif select == '4':
                print("Thank You for using this program. Quitting now!")


        elif choice == '2':
            if (num == "01"):
                print("Enter Binary Number: ", num)
                print("Convert it into? ")
                print("[1] Decimal")
                print("[2] Octal")
                print("[3] Hexadecimal")
                print("[4] Quit")

                select = input("Enter Option: ")

                if select == '1':
                    result = binary_to_decimal(num)
                    print(f"\nBinary to Decimal: {num} to {result}")
                elif select == '2':
                    result = binary_to_octal(num)
                    print(f"\nBinary to Octal: {num} to {result}")
                elif select == '3':
                    result = binary_to_hexadecimal(num)
                    print(f"\nBinary to Hexadecimal: {num} to {result}")
                elif select == '4':
                    print("\nThank You for using this program. Quitting now!")
            elif ("Invalid Output. Try Again!"):
                os.close()

                
        
        elif choice == '3':
            print("Enter Octal Number: ", num)
            print("Convert it into? ")
            print("[1] Decimal")
            print("[2] Binary")
            print("[3] Hexadecimal")
            print("[4] Quit")

            select = input("Enter Option: ")
            
            if select == '1':
                result = octal_to_decimal(num)
                print( "Octal to Decimal: ", result)
            elif select == '2':
                result = octal_to_binary(num)
                print( "Octal to Binary: ", result)
            elif select == '3':
                result = octal_to_hexadecimal(num)
                print( "Octal to Hexadecimal: ", result)
            elif select == '4':
                print("Thank You for using this program. Quitting now!")
        
        elif choice == '4':
            print("Enter Hexadecimal Number: ", num)
            print("Convert it into? ")
            print("[1] Decimal")
            print("[2] Binary")
            print("[3] Octal")
            print("[4] Quit")

            select = input("Enter Option: ")
            
            if select == '1':
                result = hexadecimal_to_decimal(num)
                print( "Hexadecimal to Decimal: ", result)
            elif select == '2':
                result = hexadecimal_to_binary(num)
                print( "Hexadecimal to Binary: ", result)    
            elif select == '3':
                result = hexadecimal_to_octal(num)
                print( "Hexadecimal to Octal: ", result)
            elif select == '4':
                print("Thank You for using this program. Quitting now!")

    except ValueError:
            print('Invalid number.')
if __name__ == "__main__":
    main()