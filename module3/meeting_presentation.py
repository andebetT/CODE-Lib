def maxPresentations(scheduleStart, scheduleEnd):
    # Combine the start and end times into a list of tuples
    schedule = list(zip(scheduleStart, scheduleEnd))

    # Sort the schedule based on the end times in ascending order
    schedule.sort(key=lambda x: x[1])

    # Initialize variables
    max_presentations = 0
    current_end_time = float('-inf')

    # Iterate through the sorted schedule
    for start, end in schedule:
        # If the start time is after the current end time,
        # increment the max_presentations count and update
        # the current_end_time to the end time of the current presentation
        if start >= current_end_time:
            max_presentations += 1
            current_end_time = end

    return max_presentations
scheduleStart = [1, 1, 2]
scheduleEnd = [3, 2, 4]

print(maxPresentations(scheduleStart, scheduleEnd))
mylist=[1,2,3,4,5,6]
for i in range(1,6):
    mylist[i-1]=mylist[i]
for i in range(0,6):
    print(mylist[i],end=" ")