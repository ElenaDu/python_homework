#Task 2: A Decorator that Takes an Argument
from functools import wraps

#Declare a decorator called type_converter. It has one argument called type_of_output. It should convert the return from func to the corresponding type.
def type_converter(type_of_output):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return type_of_output(result)
        return wrapper
    return decorator

#Function return_int() takes no arguments and returns the integer value 5, decorated to convert output to str
@type_converter(str)
def return_int():
    return 5

#Function return_string() takes no arguments and returns the string value "not a number", decorated to convert output to int
@type_converter(int)
def return_string():
    return "not a number"

# Main execution block
if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)

    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")
        