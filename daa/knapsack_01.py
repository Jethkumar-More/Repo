def knapsack(weight, profit, n, capacity):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weight[i - 1] <= w:
                dp[i][w] = max(
                    profit[i - 1] + dp[i - 1][w - weight[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    print(f"\nMaximum Profit = {dp[n][capacity]}")

    # Display selected items
    print("\nSelected Items:")

    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            print(f"Item {i} (Weight: {weight[i - 1]}, Profit: {profit[i - 1]})")

            w -= weight[i - 1]


def main():
    n = 0
    capacity = 0
    weight = []
    profit = []

    while True:
        print("\n===== 0-1 KNAPSACK MENU =====")
        print("1. Enter Item Details")
        print("2. Display Item Details")
        print("3. Solve Knapsack Problem")
        print("4. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            n = int(input("\nEnter number of items: "))
            capacity = int(input("Enter knapsack capacity: "))

            weight = [0] * n
            profit = [0] * n

            for i in range(n):
                weight[i] = int(input(f"\nEnter weight of item {i + 1}: "))
                profit[i] = int(input(f"Enter profit of item {i + 1}: "))

            print("\nItem details entered successfully!")

        elif choice == 2:
            if n == 0:
                print("\nPlease enter item details first!")
                continue

            print("\nItem\tWeight\tProfit")

            for i in range(n):
                print(f"{i + 1}\t{weight[i]}\t{profit[i]}")

        elif choice == 3:
            if n == 0:
                print("\nPlease enter item details first!")
            else:
                knapsack(weight, profit, n, capacity)

        elif choice == 4:
            print("\nExiting Program...")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()

# TC: O(n * W)
# SC: O(n * W)
