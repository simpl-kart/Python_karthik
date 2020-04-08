#define python user defined exception.
class Error(Exception):
    ###base class for other exceptions
    pass
class ValueSmallError(Error):
    pass
class ValueLargeError(Error):
    pass
number = 10

while True:
    try:
        in_num = int(input("Enter the number:"))
        if in_num < number:
            raise ValueSmallError
        elif in_num > number:
            raise ValueLargeError
        break
    except ValueSmallError:
        print("The value is too small pls try again")
        print()
    except ValueLargeError:
        print("The value is too large pls try again")
        print()
print("Congratulations!! You guessed it correctly")
