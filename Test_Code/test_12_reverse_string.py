import importlib.util
import os

file_path = os.path.join(os.path.dirname(__file__), "..", "Code", "12_reverse_string.py")

spec = importlib.util.spec_from_file_location("reverse_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.reverse_string("hello") == "olleh"
assert module.reverse_string("Python") == "nohtyP"
assert module.reverse_string("12345") == "54321"
assert module.reverse_string("a") == "a"
assert module.reverse_string("") == ""

print("All test cases passed.")