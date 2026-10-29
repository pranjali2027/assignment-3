
import importlib.util
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Code",
    "06_prime_number.py"
)

spec = importlib.util.spec_from_file_location("prime_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_prime(2) == True
assert module.is_prime(3) == True
assert module.is_prime(5) == True
assert module.is_prime(4) == False
assert module.is_prime(1) == False
assert module.is_prime(0) == False
assert module.is_prime(-7) == False

print("All test cases passed.")
