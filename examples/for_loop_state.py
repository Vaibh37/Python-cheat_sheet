"""Show how a for loop reuses a changed variable across five iterations."""

w = 3
trace = []
for epoch in range(5):
    before = w
    w = w + 1
    trace.append((before, w))
    print(f"Epoch {epoch + 1}: before={before}, after={w}")

# This statement executes once, after the loop.
print("Final w:", w)
assert trace == [(3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
assert w == 8
