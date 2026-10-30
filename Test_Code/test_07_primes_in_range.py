import importlib.util
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Code",
    "07_primes_in_range.py"
)

spec = importlib.util.spec_from_file_location("prime_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.primes_in_range(1, 10) == [2, 3, 5, 7]
assert module.primes_in_range(10, 20) == [11, 13, 17, 19]
assert module.primes_in_range(1, 5) == [2, 3, 5]
assert module.primes_in_range(14, 16) == []
assert module.primes_in_range(2, 2) == [2]

print("All test cases passed.")