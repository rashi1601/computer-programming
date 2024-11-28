def compose(f, g):
    return lambda x: f(g(x))

# Example
square = lambda x: x**2
increment = lambda x: x + 1
h = compose(square, increment)
print(h(2))  # Output: 9
