# Function Decorators
# Write a decorator function log_function_call that prints "Function is being called" 
# before a function executes. Apply it to a function say_hello().

def log_function_call(func):
    def wrapper():
        print("Function is being called")  # Function call hone se pehle yeh message print hoga

        # Actual function call hoga
        func()
    return wrapper


# say_hello function par decorator apply kar rahe hain
@log_function_call
def say_hello():
    print("Hello!")

# Function call
say_hello()