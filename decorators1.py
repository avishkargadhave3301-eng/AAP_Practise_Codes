def greeting_decorator(func):
    def wrapper():
        print("----- Program Started -----")
        func()
        print("----- Program Ended -----")
    return wrapper
@greeting_decorator
def greet():
    print("Hello, Welcome to Python Decorators!")
greet()
