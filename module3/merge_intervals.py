def merge(intervals):
    if not intervals:
        return []

    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])
    print(intervals)

    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            # No overlap, add interval to merged
            merged.append(interval)
        else:
            # Overlap, merge intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]]))
print(merge(intervals))