import importlib.util
import os

file_path = os.path.join(os.path.dirname(__file__), "..", "Code", "20_word_frequency.py")
spec = importlib.util.spec_from_file_location("frequency_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.word_frequency("Hello, world! Hello") == {
    "hello": 2,
    "world": 1
}

assert module.word_frequency("Python is fun and Python is easy") == {
    "python": 2,
    "is": 2,
    "fun": 1,
    "and": 1,
    "easy": 1
}

assert module.word_frequency("") == {}

print("All test cases passed.")