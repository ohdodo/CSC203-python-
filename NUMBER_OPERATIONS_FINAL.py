def add_binary(binary1, binary2):
    decimal1 = int(binary1, 2)
    decimal2 = int(binary2, 2)
    result = decimal1 + decimal2
    return bin(result)[2:]

def subtract_binary(binary1, binary2):
    decimal1 = int(binary1, 2)
    decimal2 = int(binary2, 2)
    result = decimal1 - decimal2
    return bin(result)[2:]

def multiply_binary(binary1, binary2):
    decimal1 = int(binary1, 2)
    decimal2 = int(binary2, 2)
    result = decimal1 * decimal2
    return bin(result)[2:]

def divide_binary(binary1, binary2):
    decimal1 = int(binary1, 2)
    decimal2 = int(binary2, 2)
    if decimal2 == 0:
        return "Division by zero error."
    result = decimal1 // decimal2
    return bin(result)[2:]

def add_octal(octal1, octal2):
    decimal1 = int(octal1, 8)
    decimal2 = int(octal2, 8)
    result = decimal1 + decimal2
    return oct(result)[2:]

def subtract_octal(octal1, octal2):
    decimal1 = int(octal1, 8)
    decimal2 = int(octal2, 8)
    result = decimal1 - decimal2
    return oct(result)[2:]

def multiply_octal(octal1, octal2):
    decimal1 = int(octal1, 8)
    decimal2 = int(octal2, 8)
    result = decimal1 * decimal2
    return oct(result)[2:]

def divide_octal(octal1, octal2):
    decimal1 = int(octal1, 8)
    decimal2 = int(octal2, 8)
    if decimal2 == 0:
        return "Division by zero error."
    result = decimal1 // decimal2
    return oct(result)[2:]

def add_hexadecimal(hex1, hex2):
    decimal1 = int(hex1, 16)
    decimal2 = int(hex2, 16)
    result = decimal1 + decimal2
    return hex(result).upper()[2:]  # Convert to uppercase

def subtract_hexadecimal(hex1, hex2):
    decimal1 = int(hex1, 16)
    decimal2 = int(hex2, 16)
    result = decimal1 - decimal2
    return hex(result).upper()[2:]  # Convert to uppercase

def multiply_hexadecimal(hex1, hex2):
    decimal1 = int(hex1, 16)
    decimal2 = int(hex2, 16)
    result = decimal1 * decimal2
    return hex(result).upper()[2:]  # Convert to uppercase

def divide_hexadecimal(hex1, hex2):
    decimal1 = int(hex1, 16)
    decimal2 = int(hex2, 16)
    if decimal2 == 0:
        return "Division by zero error."
    result = decimal1 // decimal2
    return hex(result).upper()[2:]  # Convert to uppercase

def number_system_operations(base, operator, num1, num2):
    if base == 2:
        if operator == "+":
            return add_binary(num1, num2)
        elif operator == "-":
            return subtract_binary(num1, num2)
        elif operator == "*":
            return multiply_binary(num1, num2)
        elif operator == "/":
            return divide_binary(num1, num2)
    elif base == 3:
        if operator == "+":
            return add_octal(num1, num2)
        elif operator == "-":
            return subtract_octal(num1, num2)
        elif operator == "*":
            return multiply_octal(num1, num2)
        elif operator == "/":
            return divide_octal(num1, num2)
    elif base == 4:
        if operator == "+":
            return add_hexadecimal(num1, num2)
        elif operator == "-":
            return subtract_hexadecimal(num1, num2)
        elif operator == "*":
            return multiply_hexadecimal(num1, num2)
        elif operator == "/":
            return divide_hexadecimal(num1, num2)
    elif base == 1:
        if operator == "+":
            return str(float(num1) + float(num2))
        elif operator == "-":
            return str(float(num1) - float(num2))
        elif operator == "*":
            return str(float(num1) * float(num2))
        elif operator == "/":
            if float(num2) == 0:
                return "Division by zero error."
            return str(float(num1) / float(num2))
    else:
        print("Invalid base.")
        return "Invalid base."


def main():
    print("\n\t\tNumber Operator Program\n")
    print("\t\t[1] Decimal")
    print("\t\t[2] Binary")
    print("\t\t[3] Octal")
    print("\t\t[4] Hexadecimal")
    print("\t\t[5] Exit Program")

    select = int(input("\nSelect Base Number: "))

    if select == 5:
        print("Thank you for using our program.")
        quit()

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operator = input("Enter the operator (+, -, *, /): ")

    result = number_system_operations(select, operator, num1, num2)
    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()
