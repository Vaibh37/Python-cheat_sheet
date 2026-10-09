# Common Python Gotchas

## 1. len(num) vs len(nums)

If:

    nums = [3, 2, 3]

then:

    len(nums)   # 3

But inside:

    for num in nums:

num is one integer such as 3.

So:

    len(num)

is an error because an int has no length.

## 2. return num vs return count

If the problem asks for the actual value:

    if count == 1:
        return num

Do not return count unless the answer should literally be the count.

## 3. Missing return = None

This:

    def f():
        x = 10

returns None.

LeetCode often displays that as:

    null

## 4. = vs ==

Assignment:

    x = 5

Comparison:

    x == 5

## 5. / vs //

    7 / 2   # 3.5
    7 // 2  # 3

Use // often for:
- mid index
- half length
- integer math

Example:

    mid = (left + right) // 2

## 6. range stop is excluded

    list(range(5))

gives:

    [0, 1, 2, 3, 4]

For 0 through n inclusive:

    range(n + 1)

## 7. sorted() vs .sort()

    new_nums = sorted(nums)

returns a new sorted list.

    nums.sort()

changes nums itself and returns None.

Wrong:

    nums = nums.sort()

Now nums becomes None.

## 8. reverse gotcha

New reversed list:

    nums[::-1]

In-place:

    nums.reverse()

Iterator:

    reversed(nums)

If you need a list:

    list(reversed(nums))

## 9. list.pop(0) is slow

This is O(n):

    q.pop(0)

For queues use:

    from collections import deque
    q = deque()
    q.popleft()

## 10. nums.count(x) inside loop can be O(n²)

Slow:

    for x in nums:
        if nums.count(x) > 1:
            ...

Better frequency dict:

    freq = {}

    for x in nums:
        freq[x] = freq.get(x, 0) + 1

Or:

    from collections import Counter
    freq = Counter(nums)

## 11. set() vs {}

Empty set:

    s = set()

This:

    s = {}

creates an empty dict, NOT a set.

## 12. remove vs discard

Set:

    s.remove(x)

raises an error if x is missing.

    s.discard(x)

does nothing if x is missing.

## 13. dict.get()

Instead of:

    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

Use:

    freq[x] = freq.get(x, 0) + 1

## 14. Copying lists

This does NOT copy:

    b = a

Both names point to the same list.

Copy:

    b = a.copy()

or:

    b = a[:]

For nested structures:

    import copy
    b = copy.deepcopy(a)

## 15. 2D list alias bug

Wrong:

    grid = [[0] * 3] * 3

Changing one row can change all rows.

Correct:

    grid = [[0] * 3 for _ in range(3)]

## 16. String is immutable

Wrong:

    s[0] = "a"

Instead create a new string:

    s = "a" + s[1:]

Or convert:

    chars = list(s)
    chars[0] = "a"
    s = "".join(chars)

## 17. Negative indexing

    nums[-1]   # last
    nums[-2]   # second last

## 18. Slicing

    nums[start:stop]

stop excluded.

    nums[:k]
    nums[k:]
    nums[a:b]
    nums[::2]
    nums[::-1]

## 19. Chained comparisons are allowed

Instead of:

    x >= 0 and x < n

Python allows:

    0 <= x < n

Very useful for grid bounds:

    0 <= r < rows and 0 <= c < cols

## 20. Boolean operators return values

Often:

    if nums:
        ...

is cleaner than:

    if len(nums) > 0:
        ...

## 21. and / or vs & / |

For booleans:

    and
    or

For bitwise operations:

    &
    |
    ^

Set operations also use:

    a & b
    a | b

## 22. XOR reminder

XOR:

    a ^ b

Useful fact:

    x ^ x = 0
    x ^ 0 = x

That is why Single Number can be solved with:

    result = 0

    for x in nums:
        result ^= x

    return result

## 23. Mutable default argument trap

Avoid:

    def f(items=[]):
        items.append(1)
        return items

Use:

    def f(items=None):
        if items is None:
            items = []

## 24. Shadowing built-ins

Avoid variable names like:

    list = []
    str = "hello"
    sum = 0
    max = 5

They hide Python built-ins.

Prefer:

    nums = []
    text = "hello"
    total = 0
    best = 5

## 25. Indentation matters

Wrong:

    if x > 0:
    return x

Correct:

    if x > 0:
        return x

Python uses indentation as syntax.

## 26. in on dict checks keys

    d = {"a": 10}

    "a" in d      # True
    10 in d       # False

For values:

    10 in d.values()

## 27. enumerate beats manual index sometimes

Instead of:

    for i in range(len(nums)):
        x = nums[i]

Use:

    for i, x in enumerate(nums):
        ...

## 28. Membership speed

List lookup:

    x in nums

is O(n).

Set/dict lookup:

    x in seen
    x in freq

is O(1) average.

## 29. max/min on empty list

This errors:

    max([])

If empty is possible, handle it first:

    if not nums:
        ...

## 30. float infinity

Useful initialization:

    smallest = float("inf")
    largest = float("-inf")

## 31. LeetCode type hint note

Both can appear:

    list[int]

and:

    List[int]

If using List manually outside LeetCode:

    from typing import List

Modern Python usually supports:

    list[int]

## 32. Easy debugging checklist

If LeetCode returns null:
- did your function reach the end without return?
- is return indented correctly?

If Time Limit Exceeded:
- nested loops?
- count/index inside a loop?
- pop(0)?
- repeated sorting?
- could set/dict help?

If Wrong Answer:
- off-by-one in range?
- returning count instead of value?
- using < instead of <=?
- forgot n + 1?
- modified input accidentally?

If KeyError:
- use dict.get()
- use defaultdict()
- check key before access

If IndexError:
- check len(nums)
- verify loop boundaries
- remember last valid index is len(nums) - 1

## 33. A list does not have `.get()`

Wrong:

    fruits = ["apple", "banana"]
    fruits.get("apple", 0)  # AttributeError

`.get()` belongs to a **dictionary**, not a list. Use a dict to remember counts:

    counts = {}
    counts["apple"] = counts.get("apple", 0) + 1

## 34. Dictionary vs integer increment

Wrong:

    counts = {}
    counts += 1  # TypeError

`counts` is a container. Increase the **value under a key**:

    counts["apple"] = counts.get("apple", 0) + 1

If the key already exists:

    counts["apple"] += 1

## 35. String key vs variable key

These are different:

    students = {"Alex": 85}
    "Alex" in students        # True
    alex in students          # NameError unless alex is defined

A variable *containing* the string works:

    name = "Alex"
    name in students          # True
    students[name]            # 85

## 36. Check variable names exactly

Wrong:

    students = {"Alex": 85}
    print(student["Alex"])    # NameError: student is not defined

Correct:

    print(students["Alex"])

Python is case-sensitive and does not guess plural or capitalization.

## 37. Printing in vs after a loop

Prints three times:

    count = {}
    for x in [1, 2, 1]:
        count[x] = count.get(x, 0) + 1
        print(count)

Prints the final result once:

    count = {}
    for x in [1, 2, 1]:
        count[x] = count.get(x, 0) + 1
    print(count)              # {1: 2, 2: 1}

## 38. `print(enumerate(nums))` is not the pairs

    nums = [10, 20]
    print(enumerate(nums))    # prints an enumerate object

To see index + value:

    for i, num in enumerate(nums):
        print(i, num)

Or:

    print(list(enumerate(nums)))  # [(0, 10), (1, 20)]

## 39. `set(num)` when num is an integer

Wrong:

    num = 10
    set(num)                 # TypeError: int isn't iterable

Correct for duplicates in a list:

    nums = [10, 20, 10]
    unique = set(nums)       # {10, 20}

## 40. Return outside a function

Wrong:

    if True:
        return True         # SyntaxError outside a function

At script level, use `print` to display. Inside a function, use `return` to give a result back to the caller.

---

See [CHEATSHEET.md](CHEATSHEET.md) for method lookup, worked examples, and quick Python review.
