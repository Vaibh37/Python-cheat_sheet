# Python Functions and Loops: Small, Practical Examples

Use this guide when you know what an exercise is asking, but you get stuck turning it into Python. Run the companion script with `python examples/functions_and_loops.py`.

## 1. `print` displays a value; `return` sends it back

```python
def show_double(n):
    print(n * 2)

result = show_double(5)  # displays 10
print(result)           # displays None
```

`show_double` has no `return`, so the function returns `None`. If you need a result for another calculation, use `return`:

```python
def double(n):
    return n * 2

answer = double(5)
print(answer + 1)  # 11
```

## 2. `return` inside a loop ends the entire function

**Bug:** This returns after the first item, even if more numbers remain.

```python
def first_even_only(nums):
    for num in nums:
        if num % 2 == 0:
            return num
        return None  # Too early: runs on the first odd number
```

**Fix:** Only return `None` *after* the loop has checked everything.

```python
def first_even(nums):
    for num in nums:
        if num % 2 == 0:
            return num
    return None

print(first_even([1, 3, 6, 8]))  # 6
```

For collecting *all* even numbers, build a list and return it after the loop:

```python
def get_evens(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result

print(get_evens([1, 2, 3, 4]))  # [2, 4]
```

## 3. Loop over numbers, not over an integer

`n = 5` is one integer, not a list. `for num in n:` raises `TypeError`.

Use `range(1, n + 1)` to generate the integers from 1 through `n`. The endpoint of a `range` is excluded, which is why `+ 1` matters.

```python
for num in range(1, 6):
    print(num)  # prints 1, 2, 3, 4, 5 on separate lines
```

## 4. Sum values with an integer accumulator

```python
def sum_to_n(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    total = 0
    for num in range(1, n + 1):
        total += num
    return total

print(sum_to_n(5))  # 15
```

The initial value is `0`, **not** `[0]`. The latter is a list, and `[0] += 1` is invalid. Put `return total` after the loop so all additions occur. `sum_to_n(0)` returns `0`.

## 5. Count digits with integer division

```python
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

print(count_digits(11111112))  # 8
print(count_digits(-42))       # 2
print(count_digits(0))         # 1
```

`n //= 10` removes the last decimal digit each time. Taking `abs(n)` means a minus sign is not counted as a digit. Zero has one digit.

## 6. Find the largest value: compare against the best *seen so far*

Don't compare `num > num - 1`: this is true for every integer and tells you nothing about the other list items.

```python
def largest_number(nums):
    if not nums:
        raise ValueError("nums must not be empty")
    best = nums[0]
    for num in nums[1:]:
        if num > best:
            best = num
    return best

print(largest_number([1, 2, 3]))      # 3
print(largest_number([-8, -2, -5]))   # -2
```

Starting with the first list element also works for all-negative inputs. An empty list has no largest number, so this function raises `ValueError`.

## Run the examples

```bash
python examples/functions_and_loops.py
```

Expected output: `All functions-and-loops checks passed.`

Next: [Common Python Gotchas](common_gotchas.md) for quick reminders and [For-Loop Trace](FOR_LOOP_TRACE.md) for step-by-step iteration state.
