# Python for LeetCode / DSA

This file contains the Python tools that show up constantly in problems.

## 1. Frequency counting

Manual dict:

    freq = {}

    for x in nums:
        freq[x] = freq.get(x, 0) + 1

Using Counter:

    from collections import Counter

    freq = Counter(nums)

    freq[x]
    freq.most_common(1)

Example:

    Counter([1, 1, 2, 3, 3, 3])

behaves roughly like:

    {1: 2, 2: 1, 3: 3}

## 2. defaultdict

Avoid checking if key exists:

    from collections import defaultdict

    graph = defaultdict(list)

    graph[1].append(2)

Frequency:

    count = defaultdict(int)

    for x in nums:
        count[x] += 1

Sets:

    groups = defaultdict(set)

## 3. deque — real queue

Do NOT use list.pop(0) repeatedly for a queue.

Use:

    from collections import deque

    q = deque()

    q.append(10)
    q.append(20)

    q.popleft()   # remove front
    q.pop()       # remove right
    q.appendleft(5)

Peek:

    q[0]
    q[-1]

Useful for:
- BFS
- queues
- sliding window

## 4. Stack

A list is perfect as a stack:

    stack = []

    stack.append(10)  # push
    stack.append(20)

    top = stack[-1]   # peek
    x = stack.pop()   # pop

Check empty:

    if stack:
        ...

## 5. Heap / priority queue

Python heap is a min-heap:

    import heapq

    heap = []

    heapq.heappush(heap, 5)
    heapq.heappush(heap, 2)
    heapq.heappush(heap, 8)

    smallest = heapq.heappop(heap)

Turn list into heap:

    heapq.heapify(nums)

Peek min:

    heap[0]

Push then pop:

    heapq.heappushpop(heap, x)

Pop then push:

    heapq.heapreplace(heap, x)

Get smallest/largest:

    heapq.nsmallest(k, nums)
    heapq.nlargest(k, nums)

Max-heap trick:

    heapq.heappush(heap, -x)
    largest = -heapq.heappop(heap)

## 6. Binary search

Manual pattern:

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

Built-in helpers:

    import bisect

    i = bisect.bisect_left(nums, target)
    j = bisect.bisect_right(nums, target)

Insert while keeping sorted:

    bisect.insort(nums, target)

## 7. Two pointers

Common pattern:

    left = 0
    right = len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            ...
        elif current < target:
            left += 1
        else:
            right -= 1

Used for:
- sorted arrays
- pair sum
- palindrome
- container problems

## 8. Sliding window

Fixed/variable window idea:

    left = 0

    for right in range(len(nums)):
        # include nums[right]

        while window_is_invalid:
            # remove nums[left]
            left += 1

        # update answer

## 9. Prefix sum

Build:

    prefix = [0]

    for x in nums:
        prefix.append(prefix[-1] + x)

Range sum from left to right inclusive:

    range_sum = prefix[right + 1] - prefix[left]

Alternative:

    from itertools import accumulate

    prefix = [0] + list(accumulate(nums))

## 10. Hash set lookup

Classic duplicate detection:

    seen = set()

    for x in nums:
        if x in seen:
            return True
        seen.add(x)

Set lookup is O(1) average.

## 11. Hash map lookup

Classic complement pattern:

    seen = {}

    for i, x in enumerate(nums):
        need = target - x

        if need in seen:
            return [seen[need], i]

        seen[x] = i

## 12. Sorting tricks

Sort intervals/pairs by first value:

    intervals.sort(key=lambda x: x[0])

Second value:

    intervals.sort(key=lambda x: x[1])

Descending:

    nums.sort(reverse=True)

Multiple keys:

    items.sort(key=lambda x: (x[0], x[1]))

First ascending, second descending:

    items.sort(key=lambda x: (x[0], -x[1]))

## 13. Strings for LeetCode

Reverse:

    s[::-1]

Palindrome:

    s == s[::-1]

Lowercase:

    s.lower()

Only alphanumeric:

    cleaned = "".join(c.lower() for c in s if c.isalnum())

Character frequency:

    from collections import Counter
    Counter(s)

## 14. Matrix / grid

Rows:

    rows = len(grid)

Columns:

    cols = len(grid[0])

Loop:

    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]

Directions:

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

Neighbor:

    nr = r + dr
    nc = c + dc

Bounds:

    if 0 <= nr < rows and 0 <= nc < cols:
        ...

Create matrix:

    grid = [[0] * cols for _ in range(rows)]

IMPORTANT — avoid:

    grid = [[0] * cols] * rows

because every row references the same inner list.

## 15. Recursion template

    def dfs(node):
        if base_case:
            return

        # work
        dfs(next_node)

Python recursion depth can be limited, so large DFS may need iterative logic.

## 16. DFS graph

    def dfs(node):
        if node in visited:
            return

        visited.add(node)

        for nei in graph[node]:
            dfs(nei)

## 17. BFS graph

    from collections import deque

    q = deque([start])
    visited = {start}

    while q:
        node = q.popleft()

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

## 18. Graph adjacency list

    from collections import defaultdict

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

Directed graph:

    graph[u].append(v)

## 19. Linked list reminders

Typical LeetCode node:

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

Traverse:

    curr = head

    while curr:
        print(curr.val)
        curr = curr.next

Dummy node pattern:

    dummy = ListNode(0)
    tail = dummy

Return:

    return dummy.next

## 20. Trees

Typical node:

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

DFS recursion:

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        dfs(node.right)

BFS:

    from collections import deque

    q = deque([root])

    while q:
        node = q.popleft()

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

## 21. Math helpers

    import math

    math.sqrt(x)
    math.isqrt(x)      # integer square root
    math.ceil(x)
    math.floor(x)
    math.gcd(a, b)
    math.lcm(a, b)
    math.factorial(n)

Infinity:

    math.inf
    -math.inf

Or:

    float("inf")

## 22. Combinations / permutations

    from itertools import combinations, permutations

Pairs:

    combinations(nums, 2)

Permutations:

    permutations(nums)

Example:

    for a, b in combinations(nums, 2):
        ...

Cartesian product:

    from itertools import product

    product(a, b)

## 23. Memoization for DP

Modern Python:

    from functools import cache

    @cache
    def dp(i):
        ...

Older/common:

    from functools import lru_cache

    @lru_cache(None)
    def dp(i):
        ...

## 24. Basic DP array

    dp = [0] * (n + 1)

Example Fibonacci-style:

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

Often you can optimize space:

    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

## 25. Useful itertools

Running sum:

    from itertools import accumulate

    list(accumulate(nums))

Combinations:

    from itertools import combinations

Permutations:

    from itertools import permutations

Product:

    from itertools import product

## 26. Useful collections

    from collections import Counter
    from collections import defaultdict
    from collections import deque

Counter:
- frequencies

defaultdict:
- auto-create missing values

deque:
- queue / BFS

## 27. Complexity traps

This is O(n):

    for x in nums:
        ...

This is O(n²):

    for x in nums:
        nums.count(x)

because count scans the list every time.

Also O(n²):

    for i in range(n):
        for j in range(n):
            ...

Prefer set/dict when repeated lookup/counting is needed.

## 28. Common operation complexities

| Structure | Operation | Average |
|---|---|---:|
| list | append | O(1) |
| list | pop() | O(1) |
| list | pop(0) | O(n) |
| list | x in list | O(n) |
| list | count | O(n) |
| list | index | O(n) |
| list | sort | O(n log n) |
| set | x in set | O(1) |
| set | add | O(1) |
| set | remove/discard | O(1) |
| dict | get/set | O(1) |
| dict | membership | O(1) |
| deque | append/popleft | O(1) |
| heap | push/pop | O(log n) |

## 29. Very common one-liners

Maximum index:

    i = max(range(len(nums)), key=nums.__getitem__)

Minimum index:

    i = min(range(len(nums)), key=nums.__getitem__)

Count True values:

    count = sum(condition(x) for x in nums)

Flatten one level:

    flat = [x for row in matrix for x in row]

Unique while ignoring order:

    unique = list(set(nums))

Unique while preserving order:

    unique = list(dict.fromkeys(nums))

Pair with index:

    for i, x in enumerate(nums):
        ...

Two lists together:

    for x, y in zip(a, b):
        ...

## 30. LeetCode return reminders

Return VALUE:

    return num

Not its count unless the question asks for count:

    return count

Return indices:

    return [i, j]

Boolean:

    return True
    return False

No explicit return means Python returns None.
