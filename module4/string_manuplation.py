def string_manuplation(string):
    positive_key_word=["happy","joyful","pleased"]
    negative_key_word=["sad","angry","upset"]
    positive_count=0
    negtaive_count=0
    for i in string:
        if i in positive_key_word:
            positive_count+=1
        if i in negative_key_word:
            negtaive_count+=1
    if negtaive_count>positive_count:
        return "Negative"
    if negtaive_count<positive_count:
        return "Positve"
    return "Natural"

