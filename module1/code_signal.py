import re


def solution(feedback, size):
    # Split the feedback into words
    words = feedback.split()

    # Initialize the result list and the current line
    result = []
    current_line = ''

    # Iterate through the words
    for word in words:
        # If the current line plus the current word is longer than the size,
        # add the current line to the result and start a new line
        if len(current_line + ' ' + word) > size:
            result.append(current_line.strip())
            current_line = word
        # Otherwise, add the current word to the current line
        else:
            current_line += ' ' + word

    # Add the last line to the result
    result.append(current_line.strip())

    return result