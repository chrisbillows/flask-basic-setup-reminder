def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper


@my_decorator
def my_function():
    print("Inside the function.")

my_function()

# def my_decorator(func):
#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrapper
#
# def my_function():
#     print("Inside the function.")
#
# my_function = my_decorator(my_function)
# my_function()