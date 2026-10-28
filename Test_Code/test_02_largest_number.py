
import os
import importlib.util

program_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "02_largest_number.py"
)

spec = importlib.util.spec_from_file_location("largest_number", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.largest_number(10, 25, 15) == 25
assert module.largest_number(5, 2, 1) == 5
assert module.largest_number(-1, -5, -3) == -1
assert module.largest_number(7, 7, 2) == 7

print("All test cases passed.")