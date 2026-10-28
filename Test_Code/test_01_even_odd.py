
import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Code"))
)

from importlib.util import spec_from_file_location, module_from_spec

spec = spec_from_file_location(
    "even_odd",
    os.path.join(os.path.dirname(__file__), "..", "Code", "01_even_odd.py")
)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.check_even_odd(4) == "Even"
assert module.check_even_odd(7) == "Odd"
assert module.check_even_odd(0) == "Even"
assert module.check_even_odd(-3) == "Odd"

print("All test cases passed.")