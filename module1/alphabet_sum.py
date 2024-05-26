def sum_alphabet(words):
    alphabet_sums = []
    for word in words:
        word_sum = 0
        for char in word:
            word_sum += ord(char) - ord('a') + 1
        alphabet_sums.append(word_sum)

    return alphabet_sums
print(sum_alphabet(["sport","good"]))


def matrix_sum(matrix):
    total=0
    for i in matrix:
        total+=sum(i[:])
    return total
matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
print(matrix_sum(matrix))