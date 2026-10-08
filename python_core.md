# Python Core Cheat Sheet

## 1. Variables and basic types

    x = 10
    price = 19.99
    name = "vaibhav"
    active = True
    nothing = None

Common types:

    int
    float
    str
    bool
    list
    tuple
    set
    dict
    None

Check type:

    type(x)

Convert types:

    int("42")       # 42
    float("3.14")   # 3.14
    str(123)        # "123"
    list("abc")     # ['a', 'b', 'c']
    set([1, 1, 2])  # {1, 2}

## 2. Operators

Arithmetic:

    +   addition
    -   subtraction
    *   multiplication
    /   normal division
    //  floor/integer division
    %   remainder/modulo
    **  power

Examples:

    7 / 2    # 3.5
    7 // 2   # 3
    7 % 2    # 1
    2 ** 4   # 16

Comparison:

    ==  equal
    !=  not equal
    >   greater
    <   smaller
    >=  greater or equal
    <=  smaller or equal

Logical:

    and
    or
    not

Membership:

    x in nums
    x not in nums

Identity:

    a is None
    a is not None

## 3. if / elif / else

    if x > 10:
        print("big")
    elif x == 10:
        print("ten")
    else:
        print("small")

Truthy/falsy values:

Falsy:
- False
- None
- 0
- 0.0
- ""
- []
- {}
- set()

So this works:

    if nums:
        print("not empty")

## 4. Loops

Loop values:

    for x in nums:
        print(x)

Loop indices:

    for i in range(len(nums)):
        print(i, nums[i])

Index + value:

    for i, x in enumerate(nums):
        print(i, x)

while:

    i = 0
    while i < len(nums):
        i += 1

break:

    for x in nums:
        if x == target:
            break

continue:

    for x in nums:
        if x < 0:
            continue
        print(x)

## 5. range()

    range(5)          # 0..4
    range(2, 6)       # 2..5
    range(1, 10, 2)   # 1,3,5,7,9
    range(5, 0, -1)   # 5,4,3,2,1

Convert to list if you want to see values:

    list(range(5))

## 6. Useful built-ins

    len(nums)
    sum(nums)
    min(nums)
    max(nums)
    abs(-7)           # 7
    round(3.14159, 2) # 3.14
    sorted(nums)
    reversed(nums)
    any(values)
    all(values)
    enumerate(nums)
    zip(a, b)

ASCII / characters:

    ord("a")          # 97
    chr(97)           # 'a'

Quotient + remainder:

    divmod(7, 3)      # (2, 1)

Binary / hex:

    bin(10)           # '0b1010'
    hex(255)          # '0xff'
    int("1010", 2)    # 10

## 7. Strings

    s = "hello"

Indexing:

    s[0]      # 'h'
    s[-1]     # 'o'

Slicing:

    s[1:4]
    s[:3]
    s[2:]
    s[::-1]   # reverse

Length:

    len(s)

Common string methods:

    s.lower()
    s.upper()
    s.capitalize()
    s.title()

    s.strip()         # remove outer whitespace
    s.lstrip()
    s.rstrip()

    s.startswith("he")
    s.endswith("lo")

    s.find("ll")      # index or -1
    s.index("ll")     # index, error if missing

    s.count("l")

    s.replace("l", "x")

    s.split()         # split by whitespace
    s.split(",")

Join:

    words = ["i", "love", "python"]
    " ".join(words)   # "i love python"

Character checks:

    s.isalpha()
    s.isdigit()
    s.isalnum()
    s.islower()
    s.isupper()
    s.isspace()

Important: strings are immutable.

    s[0] = "H"        # ERROR

Instead:

    s = "H" + s[1:]

## 8. f-strings

    name = "vaibhav"
    age = 18

    print(f"{name} is {age}")

Formatting:

    pi = 3.14159
    print(f"{pi:.2f}")    # 3.14

## 9. Lists

Create:

    nums = [10, 20, 30]

Index:

    nums[0]
    nums[-1]

Slice:

    nums[1:3]
    nums[::-1]

Add:

    nums.append(40)
    nums.extend([50, 60])
    nums.insert(1, 15)

Remove:

    nums.pop()        # remove + return last
    nums.pop(0)       # remove + return at index
    nums.remove(20)   # remove first matching value
    nums.clear()

Search/count:

    nums.index(30)
    nums.count(30)
    30 in nums

Sort:

    nums.sort()
    nums.sort(reverse=True)

New sorted list:

    new_nums = sorted(nums)
    new_nums = sorted(nums, reverse=True)

Reverse original:

    nums.reverse()

Copy:

    copy1 = nums.copy()
    copy2 = nums[:]

Useful:

    len(nums)
    sum(nums)
    min(nums)
    max(nums)

List unpacking:

    a, b, c = [1, 2, 3]

    first, *middle, last = [1, 2, 3, 4, 5]

## 10. Tuples

Immutable ordered container:

    point = (3, 5)

    x, y = point

Useful as dict/set keys because tuples can be hashable.

Single-item tuple:

    x = (5,)

## 11. Sets

Create:

    seen = set()
    values = {1, 2, 3}

Add:

    seen.add(5)

Remove:

    seen.remove(5)    # error if missing
    seen.discard(5)   # safe if missing

Check:

    5 in seen
    5 not in seen

Other:

    len(seen)
    seen.clear()

Set operations:

    a | b             # union
    a & b             # intersection
    a - b             # difference
    a ^ b             # symmetric difference

Methods:

    a.union(b)
    a.intersection(b)
    a.difference(b)

Subset/superset:

    a <= b
    a >= b

Remove duplicates:

    unique = list(set(nums))

Note: set order should not be relied on.

## 12. Dictionaries

Create:

    d = {}
    age = {"alice": 20, "bob": 25}

Read:

    age["alice"]
    age.get("alice")
    age.get("missing", 0)

Set/update:

    age["charlie"] = 30
    age["alice"] = 21

Delete:

    del age["bob"]
    age.pop("bob", None)

Membership checks keys:

    "alice" in age

Loop keys:

    for key in age:
        print(key)

Loop values:

    for value in age.values():
        print(value)

Loop key + value:

    for key, value in age.items():
        print(key, value)

Get keys:

    age.keys()

Get values:

    age.values()

Get pairs:

    age.items()

Frequency pattern:

    freq = {}

    for x in nums:
        freq[x] = freq.get(x, 0) + 1

## 13. Comprehensions

List:

    squares = [x * x for x in nums]

With condition:

    evens = [x for x in nums if x % 2 == 0]

Set:

    unique_squares = {x * x for x in nums}

Dict:

    square_map = {x: x * x for x in nums}

Nested:

    flat = [x for row in matrix for x in row]

## 14. Functions

    def add(a, b):
        return a + b

Default argument:

    def greet(name="bro"):
        return f"hi {name}"

Multiple returns actually create a tuple:

    def values():
        return 1, 2

    a, b = values()

Type hints:

    def add(a: int, b: int) -> int:
        return a + b

Variable arguments:

    def total(*args):
        return sum(args)

Keyword arguments:

    def show(**kwargs):
        print(kwargs)

## 15. lambda

Small anonymous function:

    square = lambda x: x * x

Common with sorting:

    pairs = [(1, 5), (2, 3), (4, 1)]
    pairs.sort(key=lambda x: x[1])

## 16. map / filter

Map:

    nums = [1, 2, 3]
    doubled = list(map(lambda x: x * 2, nums))

Filter:

    evens = list(filter(lambda x: x % 2 == 0, nums))

For LeetCode, comprehensions are often clearer:

    doubled = [x * 2 for x in nums]
    evens = [x for x in nums if x % 2 == 0]

## 17. enumerate()

Instead of:

    for i in range(len(nums)):
        x = nums[i]

Use:

    for i, x in enumerate(nums):
        ...

Start from 1:

    for i, x in enumerate(nums, start=1):
        ...

## 18. zip()

Loop two lists together:

    for x, y in zip(a, b):
        print(x, y)

Create pairs:

    pairs = list(zip(a, b))

Make dict:

    d = dict(zip(keys, values))

## 19. Sorting

Numbers:

    sorted(nums)

Descending:

    sorted(nums, reverse=True)

Strings by length:

    sorted(words, key=len)

Pairs by second value:

    sorted(pairs, key=lambda x: x[1])

Sort by first ascending, second descending:

    sorted(pairs, key=lambda x: (x[0], -x[1]))

Important:

    sorted(nums)   # returns a NEW list
    nums.sort()    # changes nums, returns None

## 20. Input / output

Read string:

    name = input()

Read integer:

    n = int(input())

Read list of ints:

    nums = list(map(int, input().split()))

Print:

    print(nums)

Without newline:

    print("hello", end="")

Custom separator:

    print(1, 2, 3, sep="-")

## 21. Exceptions

    try:
        x = int(input())
    except ValueError:
        print("invalid number")

Multiple:

    try:
        ...
    except (ValueError, TypeError):
        ...

Finally:

    try:
        ...
    finally:
        ...

## 22. Classes

    class Player:
        def __init__(self, name, score=0):
            self.name = name
            self.score = score

        def add_score(self, amount):
            self.score += amount

    p = Player("vaibhav")
    p.add_score(10)

## 23. Handy patterns

Swap:

    a, b = b, a

Clamp-like idea:

    x = max(low, min(x, high))

Infinity:

    inf = float("inf")
    neg_inf = float("-inf")

Check even:

    x % 2 == 0

Check odd:

    x % 2 != 0

Last item:

    nums[-1]

Reverse iteration:

    for x in reversed(nums):
        ...

Reverse indices:

    for i in range(len(nums) - 1, -1, -1):
        ...

Check empty:

    if not nums:
        ...

Ternary:

    result = "even" if x % 2 == 0 else "odd"
