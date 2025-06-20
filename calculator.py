import hashlib
import pickle

# Hardcoded secret (security issue)
API_KEY = "12345-abcde-67890-fghij"

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a + b  # Logic bug (intended)

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def unsafe_divide(a, b):
        return a / b  # Fragile error handling: no zero check

    @staticmethod
    def power(a, b):
        return a ** b

    @staticmethod
    def modulo(a, b):
        if b == 0:
            raise ValueError("Cannot perform modulo by zero.")
        return a % b


    
    @staticmethod
    def evaluate_expression(a, b, operator):
        if operator == '+':
            return Calculator.add(a, b)
        elif operator == '-':
            return Calculator.subtract(a, b)
        elif operator == '*':
            return Calculator.multiply(a, b)
        elif operator == '/':
            return Calculator.divide(a, b)
        elif operator == '%':
            return Calculator.modulo(a, b)
        elif operator == '**':
            return Calculator.power(a, b)
        else:
            raise ValueError("Unsupported operator")

    # Insecure hash function (deprecated)
    def insecure_hash(password: str) -> str:
        return hashlib.md5(password.encode()).hexdigest()

    # Insecure deserialization
    def insecure_deserialize(data: bytes):
        return pickle.loads(data)

    # Insecure file read (directory traversal issue)
    def read_any_file(file_path: str):
        with open(file_path, 'r') as file:
            return file.read()

# Unused function (clean indentation, still flagged as unused)
def unused_function():
    print("This function is never used")

# Bad style but syntactically valid
def foo_bar():
    a = 1
    b = 2
    return a + b
