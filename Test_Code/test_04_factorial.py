
import importlib.util
import os

program_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "04_factorial.py"
)

spec = importlib.util.spec_from_file_location("factorial", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.factorial(0) == 1
assert module.factorial(1) == 1
assert module.factorial(5) == 120
assert module.factorial(3) == 6
assert module.factorial(7) == 5040

print("All test cases passed.")