import importlib.util
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Code",
    "10_sum_of_digits.py"
)

spec = importlib.util.spec_from_file_location("sum_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.sum_of_digits(123) == 6
assert module.sum_of_digits(456) == 15
assert module.sum_of_digits(100) == 1
assert module.sum_of_digits(0) == 0
assert module.sum_of_digits(-123) == 6

print("All test cases passed.")