import os
import random


os.makedirs("inputs", exist_ok=True)
random.seed(42)

values = {
    'a': 2,
    'b': 4,
    'c': 5,
    'd': 3,
    'e': 1
}

alphabet = list(values.keys())

lengths = [25, 30, 35, 40, 45, 50, 55, 60, 70, 80]

for idx, length in enumerate(lengths, start=1):
    A = ''.join(random.choice(alphabet) for _ in range(length))
    B = ''.join(random.choice(alphabet) for _ in range(length))

    filename = f"inputs/test{idx}.in"
    with open(filename, "w") as f:
        f.write(f"{len(values)}\n")
        for ch, val in values.items():
            f.write(f"{ch} {val}\n")
        f.write(A + "\n")
        f.write(B + "\n")

print("Generated 10 test files in the inputs/ folder.")