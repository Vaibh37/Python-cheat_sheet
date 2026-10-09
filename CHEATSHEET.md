# Python for LeetCode — FAST CHEATSHEET 🐍⚡

**Use this page when you forget syntax.** Examples first, short explanations, no full LeetCode solutions.

> **Rule of thumb:** Understand the data type, select the operation, then write the loop.  
> Want deeper detail? [Python core](python_core.md) · [DSA patterns](leetcode_dsa.md) · [Mistakes](common_gotchas.md).

## 0. What do I use?

| I want to... | Use | Example |
|---|---|---|
| Add to end of list | `.append(x)` | `nums.append(9)` |
| Remove last list item | `.pop()` | `nums.pop()` |
| Remove a specific value | `.remove(x)` | `nums.remove(20)` |
| Sort a list in place | `.sort()` | `nums.sort()` |
| Get a new sorted list | `sorted(...)` | `copy = sorted(nums)` |
| Reverse a list copy | slicing | `nums[::-1]` |
| Find list length | `len(...)` | `len(nums)` |
| Count list occurrences | `.count(x)` | `nums.count(2)` |
| Remove duplicates | `set(...)` | `set(nums)` |
| Check whether a key exists | `in` | `"Sam" in scores` |
| Read a dict key safely | `.get(key, default)` | `count.get("cat", 0)` |
| Add/update dictionary entry | `d[key] = value` | `scores["Sam"] = 90` |
| Loop with indices + values | `enumerate(...)` | `for i, x in enumerate(nums):` |
| Pair two iterables | `zip(...)` | `zip(names, scores)` |
| Split text into words | `.split()` | `"a b".split()` |
| Join a list of words | `separator.join(...)` | `" ".join(words)` |
| Get character frequency | `Counter` | `Counter("aaba")` |

**Method vs function:** `nums.append(4)` is a **list method**. `len(nums)` and `set(nums)` are **built-in functions**. A list has no `.get()`; a dict does.

## 1. Choose the right container

```python
nums = [10, 20, 20]       # list: ordered, allows duplicates
coords = (2, 5)           # tuple: ordered, immutable
seen = {10, 20}           # set: unique elements
scores = {"Sam": 90}      # dict: key -> value

empty_list = []
empty_set = set()         # {} is an empty DICT, not a set
empty_dict = {}
```

| Container | Access | Best for |
|---|---|---|
| `list` | `nums[0]` | Ordered elements, stack, two pointers |
| `str` | `s[0]` | Text, character scans |
| `set` | `x in seen` | Membership / duplicates |
| `dict` | `d[key]` | Mapping values, indices, frequencies |

## 2. Loops, `range`, `enumerate`, `zip`

```python
nums = [10, 20, 30]

for x in nums:                 # values only
    print(x)                   # 10, then 20, then 30

for i in range(len(nums)):     # indices: 0, 1, 2
    print(i, nums[i])

for i, x in enumerate(nums):   # index AND value
    print(i, x)                # 0 10 / 1 20 / 2 30

for i, x in enumerate(nums, start=1):
    print(i, x)                # 1 10 / 2 20 / 3 30

for i in range(3):             # 0, 1, 2 (stop excluded)
    print(i)

for i in range(4, -1, -1):     # 4, 3, 2, 1, 0
    print(i)

names = ["Ram", "Sam", "Alex"]
marks = [80, 75, 95]
for name, mark in zip(names, marks):
    print(name, mark)          # Ram 80 / Sam 75 / Alex 95
```

**Remember:** `zip()` stops at the **shorter** input. `print(enumerate(nums))` doesn't print all the pairs; iterate over it or use `list(enumerate(nums))`.

## 3. Lists — most-used methods

```python
nums = [10, 20, 30]
nums.append(40)           # [10, 20, 30, 40]
nums.extend([50, 60])     # [10, 20, 30, 40, 50, 60]
nums.insert(1, 15)        # insert at index 1
nums.remove(20)           # remove first occurrence of VALUE 20
last = nums.pop()         # remove + return last item (60)
item = nums.pop(0)        # remove + return element at INDEX 0

nums = [5, 2, 8, 1]
nums.sort()               # [1, 2, 5, 8] (changes nums)
nums.sort(reverse=True)   # [8, 5, 2, 1]
new_nums = sorted(nums)   # [1, 2, 5, 8] (new list)
nums.reverse()            # reverse nums in place
backwards = nums[::-1]    # NEW reversed list

nums = [5, 2, 5, 1]
nums.count(5)             # 2
nums.index(2)             # 1 (raises ValueError if missing)
5 in nums                # True
len(nums)                # 4
sum(nums)                # 13
min(nums), max(nums)     # (1, 5)
nums[-1]                 # 1 (last element)
nums[1:3]                # [2, 5] (stop excluded)
```

**Do not write** `nums = nums.sort()`: `.sort()` changes the original list and returns `None`.  
`pop(index)` removes by **position**; `remove(value)` removes by **value**.

## 4. Dictionaries — READ, WRITE, CHECK

```python
scores = {"Ram": 80, "Sam": 70}

scores["Ram"] = 95        # UPDATE existing key
scores["Alex"] = 85       # ADD new key
print(scores["Alex"])     # 85; KeyError if missing

print(scores.get("Bob", 0))   # 0; no KeyError
print("Sam" in scores)        # True (checks KEYS)

name = "Sam"
print(scores[name])           # 70; same as scores["Sam"]

for name in scores:           # loop over keys
    print(name, scores[name])

for name, mark in scores.items():  # loop over key-value pairs
    print(name, mark)

scores.keys()                 # dict_keys(...)
scores.values()               # dict_values(...)
scores.items()                # dict_items(...)
scores.pop("Alex", None)      # remove key, safe if missing
```

**Variable key vs literal string:**

```python
key = "cat"
d = {"cat": 3}
d[key]        # 3, because key contains "cat"
d["cat"]      # 3, literal key
# d[cat]      # NameError, unless a variable cat exists
```

**`.get(key, default)`** reads a value or supplies a default if the key is absent. It **does not automatically insert** a new key.

## 5. Frequency counting — most important current concept

```python
fruits = ["apple", "banana", "apple"]
count = {}

for fruit in fruits:
    count[fruit] = count.get(fruit, 0) + 1

print(count)  # {'apple': 2, 'banana': 1}
```

| Iteration | `fruit` | `count.get(fruit, 0)` | After `+ 1` |
|---|---|---:|---:|
| 1 | apple | 0 (missing) | apple: 1 |
| 2 | banana | 0 (missing) | banana: 1 |
| 3 | apple | 1 (existing) | apple: 2 |

Read this line **right to left**:

```python
count[fruit] = count.get(fruit, 0) + 1
#             ^ find existing or 0     ^ add 1
# ^ store result at THIS fruit's key
```

When the key is *already present*, shorter:

```python
scores = {"Ram": 5}
scores["Ram"] += 1        # 6
```

Later, `Counter` is shorthand for frequencies:

```python
from collections import Counter
counts = Counter(["a", "b", "a"])
print(counts["a"])        # 2
print(counts["missing"])  # 0
```

## 6. Sets — unique items and fast checks

```python
nums = [1, 2, 2, 3]
unique = set(nums)        # {1, 2, 3}; do not rely on set order
len(unique)               # 3

seen = set()
seen.add(10)
10 in seen                # True
seen.discard(99)          # safe if 99 does not exist
seen.remove(10)           # KeyError if missing

a = {1, 2, 3}
b = {3, 4}
a | b                     # union: {1, 2, 3, 4}
a & b                     # intersection: {3}
a - b                     # difference: {1, 2}
```

**Important:** `set(nums)` takes an iterable/list. `set(num)` fails when `num` is an integer.

## 7. Strings — methods you will use

```python
s = "  Hello Python  "
s.strip()                 # "Hello Python"
s.lower()                 # "  hello python  "
s.upper()                 # "  HELLO PYTHON  "
s.strip().lower().split() # ['hello', 'python']

text = "banana"
text.count("a")           # 3
text.find("na")           # 2; -1 if not found
text.replace("a", "o")    # "bonono"
text.startswith("ba")    # True
text.endswith("na")      # True
text[0], text[-1]        # ('b', 'a')
text[::-1]               # "ananab"

"ab12".isalnum()          # True
"abc".isalpha()           # True
"123".isdigit()           # True
"-".join(["a", "b"])      # "a-b"
"a,b,c".split(",")        # ['a', 'b', 'c']
```

Strings cannot be changed by `s[0] = "x"`. Build a new string or convert to a list first.

## 8. Functions, conditions, returns

```python
def increment(x):
    return x + 1         # send result to caller

value = increment(4)    # 5

if value == 5:          # comparison: ==
    print("five")       # print is for display
elif value > 5:
    print("big")
else:
    print("small")
```

- `=`: assign; `==`: compare.
- `return`: only inside a function; stops it and sends back a value.
- `print`: displays; does not return the result to LeetCode.
- Indentation controls whether `print` runs **each loop** or **once after the loop**.

```python
for x in [1, 2, 3]:
    print(x)      # inside loop: 3 prints

print("done")     # outside loop: 1 print
```

## 9. Built-ins and operators

```python
len([1, 2, 3])         # 3
sum([1, 2, 3])         # 6
min([4, 2]), max([4, 2])  # (2, 4)
abs(-7)                # 7
sorted([3, 1, 2])      # [1, 2, 3]
list(reversed([1, 2])) # [2, 1]

7 / 2                  # 3.5 (true division)
7 // 2                 # 3   (floor division)
7 % 2                  # 1   (remainder)
2 ** 3                 # 8   (power)
```

## 10. Which tool is faster?

| Operation | Typical cost |
|---|---:|
| `x in list`, `list.count(x)` | O(n) |
| `x in set`, `key in dict`, `dict.get` | O(1) average |
| `list.append`, `list.pop()` at end | O(1) amortized / O(1) |
| `list.pop(0)`, `list.insert(0,x)` | O(n) |
| `sorted(...)`, `list.sort()` | O(n log n) |
| One pass through `n` items | O(n) |

## 11. Error-to-fix lookup

| Symptom / attempt | Why it fails | Fix |
|---|---|---|
| `fruits.get("apple", 0)` when fruits is a list | `.get()` is for dicts | `count.get("apple", 0)` |
| `count += 1` when count is `{}` | Cannot add integer to dict | `count[key] = count.get(key, 0) + 1` |
| `if alex in students:` | `alex` is a variable, not text | `if "Alex" in students:` |
| `print(student["Alex"])` | Variable was named `students` | Use exact variable name |
| `return True` outside a function | `return` only works in functions | Use `print(...)` at top level |
| `print(enumerate(nums))` | Prints iterator representation | Loop or `list(enumerate(nums))` |
| `nums = nums.sort()` | `sort()` returns None | Call `nums.sort()` alone |
| `print(count)` indented inside counting loop | Prints intermediate states | Dedent to print final result |

## 12. Study order (from our current sessions)

- [x] List `append`, `remove`, sorting basics
- [x] Dict read, write, check membership
- [x] Dict `.get()` and dynamic keys
- [x] Frequency counting with a loop
- [x] `enumerate()`: index + value
- [ ] `zip()`: two iterables together **(next lesson)**
- [ ] `Counter`, `defaultdict`, `deque` (after syntax practice)
- [ ] Comprehensions, sorting with `key=`, pattern-building

**Learning rule:** Study the idea → trace the variables → write a tiny example yourself → only then use it in LeetCode. This page is a reference, not a substitute for reasoning.
