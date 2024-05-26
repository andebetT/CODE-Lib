def closest_key(dictionary, value):
    closest_distance = float('inf')
    closest_key = None

    for key, lst in dictionary.items():
        if value in lst:
            distance = lst.index(value)
            if distance < closest_distance:
                closest_distance = distance
                closest_key = key
    return closest_key
dictionary = {
    'a' : ['b','c','e'],
    'm' : ['c','e'],}
input = 'c'
print(closest_key(dictionary,input))