import importlib.util
import os

file_path = os.path.join(os.path.dirname(__file__), "..", "Code", "15_second_largest.py")

spec = importlib.util.spec_from_file_location("second_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.second_largest([10, 20, 30, 40]) == 30
assert module.second_largest([5, 5, 4, 3]) == 4
assert module.second_largest([1, 2]) == 1
assert module.second_largest([100, 100, 90]) == 90
assert module.second_largest([5]) == None

print("All test cases passed.")