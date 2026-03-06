"""
Basic Recursion Examples
Recursion is a technique where a function calls itself to solve a smaller version of the same problem.
Every recursive function needs:
1. A Base Case: The condition that stops the recursion.
2. A Recursive Step: The part where the function calls itself.
"""

def sum_n(n):
    """Example 1: Sum of first N numbers.
    sum_n(5) = 5 + 4 + 3 + 2 + 1 + 0 = 15
    """
    # 1. Base Case: If n is 0, we stop and return 0.
    if n <= 0:
        return 0
    # 2. Recursive Step: n + sum of (n-1)
    return n + sum_n(n - 1)

def print_backward(n):
    """Example 2: Tail Recursion (Countdown)
    The action (printing) happens BEFORE the recursive call.
    """
    if n <= 0:
        return
    print(n, end=" ")    # Action happens first
    print_backward(n - 1) # Then recurse

def print_forward(n):
    """Example 3: Head Recursion (Count-up)
    The action (printing) happens AFTER the recursive call returns.
    """
    if n <= 0:
        return
    print_forward(n - 1)  # Recurse first
    print(n, end=" ")     # Then action happens (on the way back up the stack)

if __name__ == "__main__":
    print("--- Example 1: Summation ---")
    print(f"Sum of first 5 numbers: {sum_n(5)}")

    print("\n--- Example 2: Printing Backward (Tail) ---")
    print_backward(5)

    print("\n\n--- Example 3: Printing Forward (Head) ---")
    print_forward(5)
    print()
