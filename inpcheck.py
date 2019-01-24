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
    The entered string can be arbitrary.
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
    The 'space' character is don't accept.
    Therefore, only one word can be the string you type.
    """
    y = False
    while y != True:
        s = input(">?: ")
        y = str.isalpha(s)
    return s

def range_check(a,b):
    """
    Checks your choice between two numbers.
    Usage:
    range_check(1,10)
    Return rating value.
    """
    y = 0
    while y != 1:
        try:
            i = int(input("?>: "))
            if i in range(a,b+1):
               y = 1
               pass
            else:
               print("The number is in out of range!")
               y = 0
        except ValueError:
            print ("This is not a number, or not an integer value!")
            y = 0
    return i

def float_check():
    """
    Check the input field.
    Return only float number.
    """
    y = False
    while y != True:
        f = input("?>: ")
        if len(f) == 0:
            print("This is something else.")
            y = False
        else:
            print("This is", end=" ")
            try:
                int(f)
                print("Integer.")
                y = False
            except:
                try:
                    float(f)
                    y = True
                except:
                    print("String.")

    return f