def max_average_of_k_elements(arr, k):
    window_sum = sum(arr[:k])  # Calculate the sum of the first k elements
    max_average = window_sum / k  # Initialize the max_average with the average of the first window

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Update the window sum by adding the next element and removing the first element of the window
        average = window_sum / k  # Calculate the average of the current window
        max_average = max(max_average, average)  # Update the max_average if the current average is greater

    return max_average


# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3

max_avg = max_average_of_k_elements(array, k)
print("Maximum average of", k, "elements:", max_avg)
