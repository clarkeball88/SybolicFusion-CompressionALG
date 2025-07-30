import unittest
from src.symbolic_macros import MACRO_PHI, MACRO_SQRT2, MACRO_PI

class TestSymbolicMacros(unittest.TestCase):
    def test_macro_phi(self):
        self.assertEqual(MACRO_PHI, ["⟦8,9⟧", "÷", "⟦5,5⟧"])

    def test_macro_pi(self):
        self.assertEqual(MACRO_PI, ["⟦2,2⟧", "÷", "⟦7⟧"])

if __name__ == "__main__":
    unittest.main()
