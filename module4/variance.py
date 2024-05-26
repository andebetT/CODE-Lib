def calculate_variance(data):
    n = len(data)
    if n < 2:
        return None  # Variance is undefined for a single data point

    mean = sum(data) / n
    squared_diff_sum = sum((x - mean) ** 2 for x in data)
    variance = squared_diff_sum / (n - 1)
    return variance
print(calculate_variance([1,2,3,4,5,6]))
def number_generator():
    for num in range(1, 11):
        yield num

# Create a generator object
g = number_generator()

# Iterate over the generator to print the numbers
print(next(g))
print(next(g))