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
        return a + b  # Intentional logic bug (should be subtraction)

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
        return a / b  # Fragile error handling (no zero check)

    @staticmethod
    def power(a, b):
        return a ** b

    @staticmethod
    def modulo(a, b):
        if b == 0:
            raise ValueError("Cannot perform modulo by zero.")
        return a % b

    # Insecure hash (deprecated hash function)
    def insecure_hash(password: str) -> str:
        return hashlib.md5(password.encode()).hexdigest()

    # Insecure deserialization (severe security issue)
    def insecure_deserialize(data: bytes):
        return pickle.loads(data)

    # Insecure file read (directory traversal risk)
    def read_any_file(file_path: str):
        with open(file_path, 'r') as file:
            return file.read()

# Unused function
def unused_function():
    print("This function is never used")

# Style / lint issues
def fooBar():
 a=1
  b=2
   return a+b
