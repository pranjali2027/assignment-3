
import importlib.util
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Code",
    "05_fibonacci_series.py"
)

spec = importlib.util.spec_from_file_location(
    "fibonacci_module", file_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.fibonacci_series(0) == []
assert module.fibonacci_series(1) == [0]
assert module.fibonacci_series(2) == [0, 1]
assert module.fibonacci_series(5) == [0, 1, 1, 2, 3]
assert module.fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]

print("All test cases passed.")