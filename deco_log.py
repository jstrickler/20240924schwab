import logging
from functools import wraps

logging.basicConfig(
    level=logging.DEBUG,
    filename="LOGS/deco.log",
    datefmt="%x-%X",
    format='%(levelname)s %(name)s %(asctime)s %(filename)s %(lineno)d %(module)s %(message)s',
)

def log_call(original_function):

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.debug("function is %s args are %s kwargs are %s", original_function.__name__, args, kwargs)
        result = original_function(*args, **kwargs)
        return result
    
    return wrapper

@log_call
def spam(m):
    print("SPAM SPAM SPAM")
    return 2 * m
# spam = log_call(spam)

x = spam(50)
x = spam("mint")
x = spam([1, 2, 3])
print(f"{x = }")
print(f"{spam.__name__ = }")

@log_call
def ham(x, y, **kwargs):
    return x + y

r = ham(1, 2, animal="wombat")
r = ham(10, 99, ocean="Pacific")