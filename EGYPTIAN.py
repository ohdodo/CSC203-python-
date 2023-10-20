def egyptian_fraction(numerator, denominator):
    result = []
    while numerator > 0:
        # Find the smallest unit fraction that is less than or equal to numerator/denominator.
        unit_denominator = -(-denominator // numerator)  # Ceiling division
        totalnum = (numerator * unit_denominator)
        totalden = (denominator * 1)
        print(f"Value = {unit_denominator} = {numerator} / {denominator} - 1 / {unit_denominator} = {totalnum}/{totalden}")
        
        result.append(unit_denominator)

        # Update the numerator and denominator for the next iteration.
        numerator = numerator * unit_denominator - denominator
        denominator = denominator * unit_denominator

    return result

def main():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    egyptian_fractions = egyptian_fraction(numerator, denominator)
    print(f"Egyptian fractions for {numerator}/{denominator}:")

    for unit_fraction in egyptian_fractions:
        print(f"1/{unit_fraction}", end=" ")

if __name__ == "__main__":
    main()
