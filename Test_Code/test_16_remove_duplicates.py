import importlib.util
import os

file_path = os.path.join(os.path.dirname(__file__), "..", "Code", "16_remove_duplicates.py")

spec = importlib.util.spec_from_file_location("duplicates_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.remove_duplicates([1, 2, 2, 3, 4, 4]) == [1, 2, 3, 4]
assert module.remove_duplicates([5, 5, 5]) == [5]
assert module.remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert module.remove_duplicates([]) == []
assert module.remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]

print("All test cases passed.")