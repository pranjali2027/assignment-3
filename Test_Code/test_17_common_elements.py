import importlib.util
import os

file_path = os.path.join(os.path.dirname(__file__), "..", "Code", "17_common_elements.py")

spec = importlib.util.spec_from_file_location("common_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
assert module.common_elements([1, 2, 3], [4, 5, 6]) == []
assert module.common_elements([5, 6, 7], [5, 7, 9]) == [5, 7]
assert module.common_elements([], [1, 2]) == []
assert module.common_elements([1, 1, 2], [1, 2]) == [1, 2]

print("All test cases passed.")