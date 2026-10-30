import importlib.util
import os

file_path = os.path.join(os.path.dirname(__file__), "..", "Code", "14_char_frequency.py")

spec = importlib.util.spec_from_file_location("frequency_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.character_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
assert module.character_frequency("banana") == {"b": 1, "a": 3, "n": 2}
assert module.character_frequency("aaa") == {"a": 3}
assert module.character_frequency("") == {}

print("All test cases passed.")