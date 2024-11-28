#Find the product of all elements in a list.
from functools import reduce

def product_of_elements(lst):
    return reduce(lambda x, y: x * y, lst)

# Example
print(product_of_elements([1, 2, 3, 4]))  # Output: 24
