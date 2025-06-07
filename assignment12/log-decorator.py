#Task 1: Writing and Testing a Decorator
import logging
from functools import wraps

# Setup the logger
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

#Declare a decorator
def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        positional_arguments = list(args) if args else "none"
        keyword_arguments = kwargs if kwargs else "none"

        func_result = func(*args, **kwargs)

        # Log all the required information
        logger.log(logging.INFO, f"function: {func_name}")
        logger.log(logging.INFO, f"positional parameters: {positional_arguments}")
        logger.log(logging.INFO, f"keyword parameters: {keyword_arguments}")
        logger.log(logging.INFO, f"return: {func_result}")
        logger.log(logging.INFO, "\n" + "+" + "-" * 45 + "+")

        return func_result
    return wrapper

# Declare a function that takes no parameters and returns nothing. 
@logger_decorator
def hello_world():
    print("Hello, World!")

# Declare a function that takes a variable number of positional arguments and returns True
@logger_decorator
def posit_args(*args):
    return True

# Declare a function that takes no positional arguments and a variable number of keyword arguments, and that returns logger_decorator.
@logger_decorator
def keyword_args(**kwargs):
    return logger_decorator

# Main execution block
if __name__ == "__main__":
    hello_world()
    posit_args(10, 800, "apple", "test")
    keyword_args(user="alena", role="admin", active=True)
