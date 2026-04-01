import os
import time
import subprocess
import matplotlib.pyplot as plt

# make sure outputs folder exists
os.makedirs("outputs", exist_ok=True)

input_files = [f"inputs/test{i}.in" for i in range(1, 11)]
runtimes = []

for input_file in input_files:
    start = time.perf_counter()

    result = subprocess.run(
        ["python3", "hvlcs.py", input_file],
        capture_output=True,
        text=True
    )

    end = time.perf_counter()

    if result.returncode != 0:
        print(f"Error running {input_file}:")
        print(result.stderr)
        continue

    runtimes.append(end - start)

# plot runtime graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(runtimes) + 1), runtimes, marker='o')
plt.xlabel("Test File Number")
plt.ylabel("Runtime (seconds)")
plt.title("HVLCS Runtime on 10 Input Files")
plt.grid(True)
plt.savefig("outputs/runtime_graph.png")

print("Runtime graph saved to outputs/runtime_graph.png")
print("Runtimes:", runtimes)