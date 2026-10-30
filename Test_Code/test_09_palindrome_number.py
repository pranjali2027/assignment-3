import importlib.util
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Code",
    "09_palindrome_number.py"
)

spec = importlib.util.spec_from_file_location("palindrome_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome(121) == True
assert module.is_palindrome(10) == False
assert module.is_palindrome(12321) == True
assert module.is_palindrome(123) == False
assert module.is_palindrome(0) == True
assert module.is_palindrome(-121) == False

print("All test cases passed.")