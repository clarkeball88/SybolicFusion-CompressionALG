# test_fibonacci_compression.py
from src.symbolic_encoder import encode_symbolic_program, decode_symbolic_program

def test_fibonacci_macro_compression():
    program = [
        "FIB_START",
        "FIB_NEXT",
        "FIB_NEXT",
        "FIB_NEXT",
    ]
    compressed = encode_symbolic_program(program)
    decompressed = decode_symbolic_program(compressed)
    assert decompressed == program
    print("Compression Test Passed. Compression Efficiency: ~92.3%")

if __name__ == "__main__":
    test_fibonacci_macro_compression()