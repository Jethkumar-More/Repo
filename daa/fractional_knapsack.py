class Item:
    def __init__(self, value=0, weight=0):
        self.value = value
        self.weight = weight


def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio (highest first)
    items.sort(key=lambda it: it.value / it.weight, reverse=True)

    total_value = 0.0

    print("\nItems selected:")

    for item in items:
        if capacity == 0:
            break

        if item.weight <= capacity:
            # Take the complete item
            capacity -= item.weight
            total_value += item.value

            print(f"Value: {item.value}, Weight: {item.weight} -> Full")
        else:
            # Take only the required fraction
            fraction = capacity / item.weight

            total_value += item.value * fraction

            print(f"Value: {item.value}, Weight: {item.weight} -> {fraction * 100:.2f}%")

            capacity = 0

    print(f"\nMaximum total value: {total_value:.2f}")


def main():
    items = []
    choice = 0

    while True:
        print("\n===== FRACTIONAL KNAPSACK =====")
        print("1. Enter Items")
        print("2. Solve Knapsack")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            items.clear()

            n = int(input("Enter number of items: "))

            i = 0
            while i < n:
                print(f"\nItem {i + 1}:")
                value = int(input("Enter value: "))
                weight = int(input("Enter weight: "))

                if weight <= 0 or value < 0:
                    print("Invalid input! Weight must be positive "
                          "and value cannot be negative.")
                    continue

                items.append(Item(value, weight))
                i += 1

        elif choice == 2:
            if not items:
                print("Please enter items first!")
                continue

            capacity = int(input("Enter knapsack capacity: "))

            if capacity < 0:
                print("Capacity cannot be negative!")
                continue

            fractional_knapsack(items, capacity)

        elif choice == 3:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()

# TC: O(nlogn)

# SC: O(logn)
