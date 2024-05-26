from collections import defaultdict
def find_max_balloon(string):
    counter=defaultdict(int)
    balloon="balloon"
    for i in string:
        if i in counter:
            counter[i]+=1
    if any(c not in counter for c in balloon):
        return 0
    else:
        return min(counter["b"],counter["a"],counter["l"]//2,counter["o"]//2,counter["n"])
print(find_max_balloon("balloon"))