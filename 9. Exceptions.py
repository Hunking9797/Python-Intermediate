# Errors and Exceptions
# Types of error -> Syntax error, Type error, ModuleNotFoundError, Name error(variable not yet defined)
# FileNotFoundError, Value error

try:
    a = 5 / 0   # will raise zerodivision error
    b = a + 4   # will raise type error
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else: # will execute if no exception were raised in try block
    print('everything is fine')
finally: # will always execute even if exception occurs
    print('cleaning up...\n')

# user defined exceptions
class ValueTooSmallError(Exception):
    message = ''
    value = 0
    def __init__(self, message, value):
        self.message = message
        self.value = value

def check_value(x):
    if x < 5:
        raise ValueTooSmallError('too low value', x) 
try:
    check_value(1)
except ValueTooSmallError as e:
    print(e.message, e.value)
finally:
    print('final block.')
