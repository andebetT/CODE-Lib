import re



def CodelandUsernameValidation(strParam):
    # Check if the length of the username is between 4 and 25 characters
    if len(strParam) < 4 or len(strParam) > 25:
        return "false"

    # Check if the username starts with a letter
    if not strParam[0].isalpha():
        return "false"

    # Check if the username contains only letters, numbers, and underscores
    if not re.match(r'^[a-zA-Z0-9_]+$', strParam):
        return "false"

    # Check if the username ends with an underscore
    if strParam[-1] == '_':
        return "false"

    # If all checks pass, return "true"
    return "true"