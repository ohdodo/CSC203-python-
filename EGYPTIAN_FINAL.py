import math

def egyptian_fraction(numerator, denominator):
    result = []
    while numerator > 0:
        # Find the smallest unit fraction that is less than or equal to numerator/denominator.
        unit_denominator = -(-denominator // numerator)  # Ceiling division
        partialnum1 = (numerator * unit_denominator)
        partialnum2= (denominator * 1)
        totalnum = (partialnum1 - partialnum2)
        totalden = (denominator * unit_denominator)
        num_den = (totalden / totalnum)
        num_den = math.ceil(num_den)
        print(f"\nValue: {unit_denominator} = {numerator} / {denominator} - 1 / {unit_denominator} = {partialnum1} - {partialnum2} / {totalden}")
        print(f"\t\t\t = {totalnum} / {totalden} = {num_den}")

        gcd = math.gcd(totalnum, totalden)
        totalnum = totalnum // gcd
        totalden = totalden // gcd
        lowest = math.gcd(totalnum, totalden) 

        # If the numerator of the lowest term is not 1, skip the lowest term and divide the denominator by the numerator instead.
        if totalnum != 1:
            numerator = numerator * unit_denominator - denominator
            denominator = denominator * unit_denominator
            result.append(unit_denominator)
            continue

        if lowest == 1:
            print(f"\n{totalnum}/{totalden} is in its lowest terms")
            result.append(unit_denominator)
            result.append(totalden)
            break
        else:
            print(f"{totalnum} / {totalden} is not in its lowest terms")


        result.append(unit_denominator)

        # Update the numerator and denominator for the next iteration.
        numerator = numerator * unit_denominator - denominator
        denominator = denominator * unit_denominator

    return result


def main():
    print("\t\tE G Y P T I A N  G R E E D Y   A L G O R I T H M\n\n")
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    egyptian_fractions = egyptian_fraction(numerator, denominator)
    print(f"\n\nEgyptian fractions for {numerator}/{denominator}:")

    for unit_fraction in egyptian_fractions:
        print(f"1/{unit_fraction}", end=" ")

if __name__ == "__main__":
    main()
