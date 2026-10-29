
import importlib.util
import os

program_path = os.path.join(os.path.dirname(__file__), "..", "Code", "03_pos_neg_zero.py")
spec = importlib.util.spec_from_file_location("pos_neg_zero", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.check_number(10) == "Positive"
assert module.check_number(-5) == "Negative"
assert module.check_number(0) == "Zero"
assert module.check_number(1) == "Positive"
assert module.check_number(-1) == "Negative"

print("All test cases passed.")
