def rain_days(n):
    # Base cases
    if n == 0:
        return 1.0  # It is raining today
    elif n == 1:
        return 0.2  # It rained today and yesterday

    # Recursive calculation
    p = 0.2 * rain_days(n-1) + 0.6 * rain_days(n-2) + 0.2 * rain_days(n-2)
    return p
print(rain_days(5))