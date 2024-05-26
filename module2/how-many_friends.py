def how_many_friends(friends):
    friend_counts = {}
    # Iterate over each group of friends
    for group in friends:
        for person in group:
            if person not in friend_counts:
                friend_counts[person] = 0  # Initialize friend count for new person
            friend_counts[person] += 1  # Increment friend count

    # Convert the friend counts into a list of tuples
    result = [(person, friend_counts.get(person, 0)) for person in range(1, max(friend_counts.keys()) + 1)]

    return result
friends = [[1, 3], [2, 3], [3, 5], [4]]
print(how_many_friends(friends))
# Output: [(1, 1), (2, 1), (3, 3), (4, 0), (5, 1)]

friends = [[1], [2], [3], [4]]
print(how_many_friends(friends))
# Output: [(1, 0), (2, 0), (3, 0), (4, 0)]