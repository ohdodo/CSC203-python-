def fractional_knapsack(capacity, weights, profits):
    n = len(profits)
    
    # Calculate value-to-weight ratio for each item
    ratio = [profits[i]/weights[i] for i in range(n)]

    # Sort items by ratio in descending order
    index = list(range(n))
    index.sort(key = lambda i: ratio[i], reverse=True)

    max_profit = 0
    fractions = [0]*n
    for i in index:
        if weights[i] <= capacity:
            fractions[i] = 1
            max_profit += profits[i]
            capacity -= weights[i]
        else:
            fractions[i] = capacity/weights[i]
            max_profit += profits[i]*capacity/weights[i]
            break

    return max_profit, fractions

def main():
    print(f"\n\n\t\t K N A P S A C K   A L G O R I T H M \n")
    capacity = int(input("Enter the knapsack capacity: "))
    n = int(input("Enter the number of items: "))
    
    profits = []
    weights = []

    for i in range(n):
        profit = int(input(f"\nEnter profit for item {i + 1}: "))
        weight = int(input(f"Enter weight for item {i + 1}: "))
        profits.append(profit)
        weights.append(weight)

    max_profit, fractions = fractional_knapsack(capacity, weights, profits)

    print("\n\tNumber of Items Selected:")
    for i, fraction in enumerate(fractions):
        temp_num = (weights[i]*fraction)
        if fraction > 0:
            print(f"\t\tItem {i + 1} Weight: {weights[i]} / {fraction} = {temp_num} \n")
    print(f"\t\tMaximum Capacity:",capacity)
    print("\n\tFinding the Maximum Profit:")
    for i, fraction in enumerate(fractions):
        temp_prof = (profits[i]*fraction)
        if fraction > 0:
            print(f"\t\tItem {i + 1} Profit: {profits[i]} / {fraction} = {temp_prof} \n")
    print("\t\tMaximum Profit:", max_profit)

    return main()

if __name__ == "__main__":
    main()
    
