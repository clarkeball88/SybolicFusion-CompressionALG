import unittest
from src.symbolic_encoder import encode_symbolic

class TestSymbolicEncoder(unittest.TestCase):
    def test_basic_encoding(self):
        result = encode_symbolic(["⟦1⟧", "⟦2⟧"])
        expected = "0101"  # Replace with expected symbolic binary
        self.assertEqual(result, expected)

    def test_macro_compression(self):
        result = encode_symbolic(["⟦8,9⟧", "÷", "⟦5,5⟧"])  # symbolic phi
        self.assertTrue(result.startswith("⟦"))  # Just checks structure

if __name__ == "__main__":
    unittest.main()
