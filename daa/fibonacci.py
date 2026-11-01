recursion_counter = 0


# Iterative approach
def fibonacci_iterative(n, counter):
    # counter is a one-element list so the count can be updated in place
    fib = []
    a, b = 0, 1

    for _ in range(n):
        fib.append(a)
        nxt = a + b
        a = b
        b = nxt
        counter[0] += 1

    return fib


# Recursive approach
def fibonacci_recursive(n):
    global recursion_counter
    recursion_counter += 1

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    iteration_counter = [0]

    n = int(input("Enter total numbers to print in Fibonacci series: "))

    if n < 0:
        print("Please enter a non-negative number.")
        return 1

    # Iterative Fibonacci
    fib = fibonacci_iterative(n, iteration_counter)

    print("\nFibonacci using Iteration: ", end="")
    for num in fib:
        print(num, end=" ")

    print("\nIteration Counter: " + str(iteration_counter[0]), end="")
    print("\nTime Complexity: O(n)", end="")
    print("\nSpace Complexity: O(n)")

    print("\n" + "=" * 60)

    # Recursive Fibonacci
    print("Fibonacci using Recursion: ", end="")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

    print("\nRecursion Counter: " + str(recursion_counter), end="")
    print("\nTime Complexity: O(2^n)", end="")
    print("\nSpace Complexity: O(n)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
