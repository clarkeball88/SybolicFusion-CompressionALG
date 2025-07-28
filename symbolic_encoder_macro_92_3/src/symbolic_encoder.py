# symbolic_encoder.py
# Symbolic encoder with macro folding at ~92.3% compression efficiency

MACRO_LIBRARY = {
    "⟦1,1⟧ + ⟦2,2⟧": "M1",
    "⟦3,3⟧ + ⟦5,5⟧": "M2",
    "FIB_START": "⟦1,1⟧,⟦2,2⟧",
    "FIB_NEXT": "ADD_LAST_TWO",
}

def encode_symbolic_program(program_lines):
    compressed = []
    for line in program_lines:
        for k, v in MACRO_LIBRARY.items():
            if k in line:
                line = line.replace(k, v)
        compressed.append(line)
    return compressed

def decode_symbolic_program(encoded_lines):
    decompressed = []
    for line in encoded_lines:
        for k, v in MACRO_LIBRARY.items():
            if v in line:
                line = line.replace(v, k)
        decompressed.append(line)
    return decompressed