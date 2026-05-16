#to build a calculator we have to consider the operations we want to perform, such as addtion, subtraction, multiplication, and division. We can create a simple calculator using Python as follows:    

#we create functions for these operations and them we can use a simple user interface to interact with the user and perform the calculations.
#what if there is a general function that can perform all the operations based on user input? we can use a dictionary to map the operation symbols to their corresponding functions.

#if it is a general calulator, why not a class that can perform all the operations? we can create a class called Calculator that has methods for each operation and a method to perform the calculation based on user input.


class Calculator:
    '''
    A simple calculator class that performs basic arithmetic operations such as addition, subtraction, multiplication, division, exponentiation, modulus, square root, and absolute value.
    '''
    def addition(self, a, b):
        return a + b
    #where self is the instance of the class, a and b are the numbers to be added

    #instance simply means an object of the class, it is created when we create an object of the class, it is used to access the methods and attributes of the class

    def subtraction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        if b == 0:
            return ZeroDivisionError("Error: Cannot divide by zero.")
        return a / b
    
    def exponentiation(self, a, b):
        return a ** b
    
    def modulus(self, a, b):
        return a % b
    
    def square_root(self, a):
        if a < 0:
            return ValueError("Error: Cannot take square root of a negative number.")
        return a ** 0.5
    
    def absolute_value(self, a):
        return abs(a)
    

    def calculate(self, operation, a, b):
        operations = {
            "+": self.addition,
            "-": self.subtraction,
            "*": self.multiplication,
            "/": self.division,
            "**": self.exponentiation,
            "%": self.modulus,
            "sqrt": self.square_root,
            "abs": self.absolute_value
        
        }
        if operation in operations:
            # Single-argument operations
            if operation in ["sqrt", "abs"]:
                return operations[operation](a)
            else:
                return operations[operation](a, b)
        else:
            return "Invalid operation"
#we can catch error if the user tries to divide by zero, we can add a check in the division method to return an error message if b is zero.
#we can also add a check if the user should use words instead of numbers, we can add a check in the calculate method to return an error message if a or b is not a number.
#we can create an instance of the Calculator class and use it to perform calculations based on user input.
calculator = Calculator()

# === CALCULATOR ===
# 1. Add (+)
# 2. Subtract (-)
# 3. Multiply (*)
# 4. Divide (/)
# 5. Exit
# Choose: _

print("Welcome to this Basic Calculator!")
print("You can perform the following operations:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Exponentiation (**)")
print("6. Modulus (%)")
print("7. Square Root (sqrt)")
print("8. Absolute Value (abs)")
print("9. Quit (quit)")

history = []

while True:

    operation = input("Enter operation (+, -, *, /, **, %, sqrt, abs, history): ")
    
    if operation == "quit":
        print("Goodbye!")
        break
    
    if operation == "history":
        print("\n=== CALCULATION HISTORY ===")
        if history:
            for i, entry in enumerate(history, 1):
                print(f"{i}. {entry}")
        else:
            print("No calculations yet.")
        print()
        continue
    
    # Single-argument operations
    if operation in ["sqrt", "abs"]:
        try:
            a = float(input("Enter number: "))
            result = calculator.calculate(operation, a, 0)  # b is unused
            print("Result:", result)
            history.append(f"{operation}({a}) = {result}")
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
    else:
        # Two-argument operations
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calculator.calculate(operation, a, b)
            print("Result:", result)
            history.append(f"{a} {operation} {b} = {result}")
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue