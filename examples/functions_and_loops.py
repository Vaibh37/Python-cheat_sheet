"""Beginner-friendly functions and loops, with executable sanity checks."""


def sum_to_n(n: int) -> int:
    """Return 1 + 2 + ... + n for non-negative n."""
    if n < 0:
        raise ValueError("n must be non-negative")

    total = 0
    for num in range(1, n + 1):
        total += num
    return total


def count_digits(n: int) -> int:
    """Count the decimal digits of an integer (not its minus sign)."""
    n = abs(n)
    if n == 0:
        return 1

    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def largest_number(nums: list[int]) -> int:
    """Return the largest integer; reject an empty list."""
    if not nums:
        raise ValueError("nums must not be empty")

    best = nums[0]
    for num in nums[1:]:
        if num > best:
            best = num
    return best


if __name__ == "__main__":
    assert sum_to_n(5) == 15
    assert sum_to_n(0) == 0
    assert count_digits(11111112) == 8
    assert count_digits(0) == 1
    assert count_digits(-42) == 2
    assert count_digits(-1000) == 4
    assert largest_number([1, 2, 3]) == 3
    assert largest_number([-8, -2, -5]) == -2

    for invalid_call in (lambda: sum_to_n(-1), lambda: largest_number([])):
        try:
            invalid_call()
        except ValueError:
            pass
        else:
            raise AssertionError("Expected ValueError")

    print("All functions-and-loops checks passed.")
