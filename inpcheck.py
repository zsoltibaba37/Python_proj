def integer_check():
    """
    Check the input field.
    Return the integer, if all characters in the string are digits,
    and there is at least one character.
    """
    x = False
    while x != True:
        i = input(">?: ")
        x = str.isdigit(i)
    ii = int(i)
    return ii

def name_check():
    """
    Check the input field.
    Return the string if all character is string.
    Include 'space' character check.
    """
    while True:
        try:
            s = input(">?: ")
            f = float(s)
        except ValueError:
            break
    return s

def string_check():
    """
    Check the input field.
    Return the string, if all characters in the string are alphabetic,
    and there is at least one character.
    """
    y = False
    while y != True:
        s = input(">?: ")
        y = str.isalpha(s)
    return s