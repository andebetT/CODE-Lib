def most_tips(user_ids, tips):
    tip_counts = {}
    for user_id, tip in zip(user_ids, tips):
        if user_id not in tip_counts:
            tip_counts[user_id] = tip
        tip_counts[user_id] += tip
    max_tips = 0
    max_user_id = None
    for user_id, tip_count in tip_counts.items():
        if tip_count > max_tips:
            max_tips = tip_count
            max_user_id = user_id
    return max_user_id
user_ids = [103, 105, 105, 107, 106, 103, 102, 108, 107, 103, 102]
tips = [2, 5, 1, 0, 2, 1, 1, 0, 0, 2, 2]
print(most_tips(user_ids, tips))  # Output: 105