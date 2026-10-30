import importlib.util
import os

file_path = os.path.join(os.path.dirname(__file__), "..", "Code", "13_palindrome_string.py")

spec = importlib.util.spec_from_file_location("palindrome_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome_string("madam") == True
assert module.is_palindrome_string("level") == True
assert module.is_palindrome_string("hello") == False
assert module.is_palindrome_string("Python") == False
assert module.is_palindrome_string("A") == True

print("All test cases passed.")