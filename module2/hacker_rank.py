def possibleChanges(usernames):
    for i in usernames:
        if i[0] > min(i[1:]):
            return "YES"
    return "NO"
print(possibleChanges("hydra"))