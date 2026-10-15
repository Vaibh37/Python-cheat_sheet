# Python Cheat Sheet 🐍

> **Start here: [FAST CHEATSHEET.md](CHEATSHEET.md)** — concise syntax, real outputs, method lookups, mistakes, and what to learn next.

**Study flow:** look up a method → understand the example → type it yourself → solve a separate exercise → apply the concept in LeetCode. The goal is independent coding, not memorized solutions.

A practical Python refresher for LeetCode, DSA, and everyday coding.

This repo is built to answer the annoying questions that happen after not touching Python for a while:

- what was the method name again?
- does range include the end?
- what does // do?
- how do I count values fast?
- list vs set vs dict?
- how do I sort by the second item?
- what do I import for queue / heap / Counter / binary search?

## Current study checkpoint

**Updated:** 15 October 2026

**Python covered:** dictionaries and `.get()`, frequency counting, `enumerate()`, `zip()`, comprehensions, sorting with `key=lambda`, functions, basic slicing, and 2D nested-list indexing.

**Needs a little more practice:** 2D NumPy slicing and zero-based row/column indexing, plus occasional Python function and sorting drills. See the [NumPy mistakes and fixes](numpy_basics.md#11-common-mistakes-and-fixes) and [the pre-NumPy refresh](CHEATSHEET.md#14-pre-numpy-refresh--functions-slicing-2d-lists).

**Current focus:** NumPy fundamentals are **covered, not yet mastered**. On 15 October, matrix creation, multiplication, transpose, shape checks, and broadcasting were practiced in code. See the [NumPy matrix and dense-layer bridge](NUMPY_MATRICES.md). Training and backpropagation have **not** been implemented. Track gaps in the [learning roadmap](roadmap/PYTHON_ROADMAP.md).

## Files

- **[CHEATSHEET.md](CHEATSHEET.md) — START HERE:** quick lookup organized by task, worked examples, dictionary frequency tracing, and mistakes from practice
- [python_core.md](python_core.md) — syntax, built-ins, strings, lists, tuples, sets, dicts, functions, comprehensions, sorting, and useful methods
- [leetcode_dsa.md](leetcode_dsa.md) — Python tools and patterns used constantly in LeetCode/DSA
- [common_gotchas.md](common_gotchas.md) — common Python mistakes and quick fixes
- [NUMPY_CHEATSHEET.md](NUMPY_CHEATSHEET.md) — **fast NumPy lookup**: arrays, slicing, broadcasting, filtering, reshape, random numbers, common mistakes
- [numpy_basics.md](numpy_basics.md) — **full NumPy notes**: explanation, worked outputs, tutorial timestamps, ML connections, and exercises
- [NUMPY_MATRICES.md](NUMPY_MATRICES.md) — **matrix quick guide**: 2D arrays, @ versus *, transpose, column vectors, broadcasting, and dense-layer calculations
- [examples/matrix_operations.py](examples/matrix_operations.py) — runnable shape checks and output assertions
- [assets/numpy-matrix-shapes.svg](assets/numpy-matrix-shapes.svg) — visual guide to NumPy 1D versus column-array shapes
- [roadmap/PYTHON_ROADMAP.md](roadmap/PYTHON_ROADMAP.md) — Python learning progress and AI/ML track

## 30-second survival sheet

    # length
    len(nums)

    # sum / min / max
    sum(nums)
    min(nums)
    max(nums)

    # sorting
    sorted(nums)          # returns new list
    nums.sort()           # changes original list

    # reverse
    nums[::-1]
    nums.reverse()

    # count occurrence
    nums.count(x)

    # find index
    nums.index(x)

    # membership
    x in nums
    x not in nums

    # loop values
    for x in nums:
        ...

    # loop index + value
    for i, x in enumerate(nums):
        ...

    # loop by index
    for i in range(len(nums)):
        ...

    # integer division
    7 // 2        # 3

    # remainder
    7 % 2         # 1

    # power
    2 ** 3        # 8

    # dictionary frequency
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    # set
    seen = set()

    # unique values
    unique = set(nums)

    # list comprehension
    squares = [x * x for x in nums]

    # filter with comprehension
    evens = [x for x in nums if x % 2 == 0]

    # swap
    a, b = b, a

    # infinity
    inf = float("inf")
    neg_inf = float("-inf")

## range() reminder

    range(5)        # 0, 1, 2, 3, 4
    range(2, 6)     # 2, 3, 4, 5
    range(2, 10, 2) # 2, 4, 6, 8

The stop value is NOT included.

## Division reminder

    7 / 2   # 3.5   normal division
    7 // 2  # 3     floor/integer division
    7 % 2   # 1     remainder

## Most-used containers

    nums = [1, 2, 3]          # list
    point = (2, 5)            # tuple
    seen = {1, 2, 3}          # set
    freq = {"a": 2, "b": 1}   # dict

## LeetCode class format

    class Solution:
        def example(self, nums: list[int]) -> int:
            return 0

## Complexity quick view

| Operation | Typical complexity |
|---|---:|
| list append/pop end | O(1) |
| list search / count | O(n) |
| list insert/delete middle | O(n) |
| set lookup/add/remove | O(1) average |
| dict lookup/set | O(1) average |
| sort | O(n log n) |
| heap push/pop | O(log n) |
| deque append/popleft | O(1) |

Start with python_core.md when you forget syntax. Use leetcode_dsa.md when solving problems.
