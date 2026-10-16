# Python for Loops, Variable Updates and Final Output — A Worked Trace

**Practiced 16 October 2026.** Use this when you forget **how a for loop keeps an updated value** or why printing outside the loop displays only the final result.

## 1. What range(5) means

~~~python
for epoch in range(5):
    print(epoch)
~~~

Output:

~~~text
0
1
2
3
4
~~~

Five iterations, indexed **0 through 4**. The stop value (5) is excluded. To display human-friendly numbering, print epoch + 1.

## 2. Variables do not reset on each iteration

~~~python
w = 3  # executes once, before the loop

for epoch in range(5):
    w = w + 1
    print(w)
~~~

Output:

~~~text
4
5
6
7
8
~~~

Trace:

| Iteration | w at the start | Assignment performed | w after |
| --- | ---: | --- | ---: |
| 1 (epoch=0) | 3 | 3 + 1 | 4 |
| 2 (epoch=1) | 4 | 4 + 1 | 5 |
| 3 (epoch=2) | 5 | 5 + 1 | 6 |
| 4 (epoch=3) | 6 | 6 + 1 | 7 |
| 5 (epoch=4) | 7 | 7 + 1 | 8 |

The assignment on the right-hand side is calculated using the **current** w. The new value then replaces the old w. The initialization before the loop is not executed again.

A for loop does **not automatically create a local scope** in Python, unlike a function. The loop reuses the same variable.

## 3. Does a for loop return the final result?

No. A Python **for statement** runs a body repeatedly. It does not return a value. The values assigned to variables remain available after it completes.

~~~python
w = 3
for epoch in range(5):
    w = w + 1

print(w)  # 8; runs after all 5 updates
~~~

Compare indentation:

~~~python
w = 3
for epoch in range(5):
    w = w + 1
    print(w)  # runs 5 times; each iteration

print("Final:", w)  # runs once after the loop
~~~

**The indentation decides** which statements repeat. A print statement does not trigger, control or calculate the loop's final result; it only reads a value and displays it when Python executes that line.

## 4. The gradient descent example we coded

Initial values: x=2, target y=10, w=3, b=1, learning rate=0.05.

~~~python
x = 2
y = 10
w = 3
b = 1
learning_rate = 0.05

for epoch in range(5):
    pred_y = w * x + b
    loss_before = (pred_y - y) ** 2

    dw = 2 * (pred_y - y) * x
    db = 2 * (pred_y - y)

    w = w - learning_rate * dw  # overwrites old w
    b = b - learning_rate * db  # overwrites old b

    pred_y = w * x + b         # predict using NEW w and b
    loss = (pred_y - y) ** 2  # loss after the update

print(pred_y)
print(loss)
~~~

Output:

~~~text
9.90625
0.0087890625
~~~

This is five consecutive **updates**, not one repeated update from the original w=3 and b=1.

| End of iteration | w | b | Prediction | Loss |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 3.6 | 1.3 | 8.5 | 2.25 |
| 2 | 3.9 | 1.45 | 9.25 | 0.5625 |
| 3 | 4.05 | 1.525 | 9.625 | 0.140625 |
| 4 | 4.125 | 1.5625 | 9.8125 | 0.03515625 |
| 5 | 4.1625 | 1.58125 | 9.90625 | 0.0087890625 |

**Why the calculation appears twice:** The first prediction is used to find gradients with the old parameters. The second prediction evaluates the new parameters immediately after updating. At the start of the *next* iteration, the first prediction is recalculated using those updated parameters.

## 5. Frequent mistakes

- Thinking each iteration goes back to the initializer before the loop. It does not.
- Thinking w inside a for loop is automatically a separate variable. It is not.
- Thinking a loop returns a final result. It does not; reassigned variables remain available.
- Printing outside the loop but expecting all intermediate values. Put print inside the body to show every iteration.
- Confusing **target y = 10**, **predicted y-hat**, and **squared loss**. They measure different things.
- Mistaking 5 epochs for five independent runs that start with the same parameters.

## 6. Tiny runnable reminder

~~~python
w = 3
for epoch in range(5):
    old_w = w
    w = w + 1
    print(f"epoch={epoch + 1}, before={old_w}, after={w}")

print("Final weight:", w)
~~~

To run a checked script, see [examples/for_loop_state.py](examples/for_loop_state.py).

For model training mathematics and a runnable example, see [Neural-Network lesson](https://github.com/Vaibh37/Neural-Network/blob/main/notes/06-first-gradient-descent-training-loop.md) and [script](https://github.com/Vaibh37/Neural-Network/blob/main/examples/train_single_neuron.py).
