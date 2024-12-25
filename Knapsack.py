# Select spots using Knapsack Algorithm
def knapsack(m, n, w, p, budget):

    # (p[i]/w[i]) ratio
    ratio = []
    for i in range(n):
        ratio.append([w[i] / p[i], w[i], p[i], i])

    # Sorting in descending order
    for i in range(n):
        for j in range(i + 1, n):
            if ratio[i][0] < ratio[j][0]:
                ratio[i], ratio[j] = ratio[j], ratio[i]

    S = [0] * n  # Solution Vector
    selected_spots = []
    prof = 0
    u = m  # u = remaining capacity (time)

    for i in range(n):
        duration = ratio[i][1]
        expense = ratio[i][2]
        index = ratio[i][3]

        if duration <= u and prof + expense <= budget:
            S[index] = 1
            selected_spots.append(index + 1)

            u -= duration
            prof += expense

    # Display
    print("\nSelected spots:")
    for spot in selected_spots:
        print(f"Spot {spot}")
 
    print(f"\nTotal expense: {prof}")
    print(f"Remaining budget: {budget - prof}")
    print(f"Total time: {m - u}")
    print(f"Remaining time: {u}")

    return selected_spots


# Main Function
def main():

    # Inputs
    n = int(input("Enter the number of tourist spots: "))
    w = []  # Time
    p = []  # Expense
    for i in range(n):
        time = int(input(f"Enter the time required to visit the spot {i + 1}: "))
        expense = int(input(f"Enter the expense to visit spot {i + 1}: "))
        w.append(time)
        p.append(expense)
    max_time = int(input("\nEnter the maximum time limited: "))
    budget = int(input("Enter the maximum budget limited: "))

    selected_spots = knapsack(max_time, n, w, p, budget)

if __name__ == "__main__":
    main()