from datetime import datetime, timedelta

def count_business_days(date1, date2):
    start_date = datetime.strptime(date1, "%Y-%m-%d")
    end_date = datetime.strptime(date2, "%Y-%m-%d")

    # Define a set of weekdays (Monday to Friday)
    weekdays = {0, 1, 2, 3, 4}

    # Initialize a counter for business days
    business_days = 0

    # Iterate over each date in the range
    current_date = start_date
    while current_date <= end_date:
        # Check if the current date is a weekday (Monday to Friday)
        if current_date.weekday() in weekdays:
            business_days += 1

        # Move to the next day
        current_date += timedelta(days=1)

    return business_days
date1 = "2021-01-31"
date2 = "2021-02-18"
print(count_business_days(date1,date2))