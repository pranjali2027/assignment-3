import importlib.util
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Code",
    "08_reverse_number.py"
)

spec = importlib.util.spec_from_file_location("reverse_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.reverse_number(123) == 321
assert module.reverse_number(4567) == 7654
assert module.reverse_number(100) == 1
assert module.reverse_number(0) == 0
assert module.reverse_number(-123) == -321

print("All test cases passed.")