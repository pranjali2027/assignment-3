import importlib.util
import os

file_path = os.path.join(os.path.dirname(__file__), "..", "Code", "11_vowels_consonants.py")

spec = importlib.util.spec_from_file_location("vowels_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.count_vowels_consonants("hello") == (2, 3)
assert module.count_vowels_consonants("Python") == (1, 5)
assert module.count_vowels_consonants("AEIOU") == (5, 0)
assert module.count_vowels_consonants("123 !") == (0, 0)
assert module.count_vowels_consonants("") == (0, 0)

print("All test cases passed.")