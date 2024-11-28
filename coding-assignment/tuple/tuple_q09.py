#Generate a tuple of cumulative sums from an input tuple.
def cumulative_sum(tpl):
    result, total = [], 0
    for num in tpl:
        total += num
        result.append(total)
    return tuple(result)

# Example
print(cumulative_sum((1, 2, 3, 4)))  # Output: (1, 3, 6, 10)
