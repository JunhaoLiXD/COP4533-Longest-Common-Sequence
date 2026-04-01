import sys
import os

def parse_input(filename):
    """
    Read and parse an input file for the HVLCS problem.

    Args:
        filename (str): Path to the input file.

    Returns:
        tuple[dict[str, int], str, str]:
        A tuple containing:
            - value (dict[str, int]): Mapping from each character to its integer value
            - A (str): The first input string
            - B (str): The second input string
    """
    # Return None if the path is invalid or the file does not exist
    if not os.path.isfile(filename):
        return None

    with open(filename, "r") as f:
        # Remove blank lines and trailing newline characters
        lines = [line.strip() for line in f if line.strip()]

    # First line is the number of characters in the alphabet
    K = int(lines[0])

    # Read each character and its assigned value
    value = {}
    for i in range(1, K + 1):
        parts = lines[i].split()
        ch = parts[0]
        v = int(parts[1])
        value[ch] = v

    # The last two lines are the two input strings
    A = lines[K + 1]
    B = lines[K + 2]

    return value, A, B


def compute_dp(A, B, value):
    """
    Compute the dynamic programming table for the HVLCS problem.

    Args:
        A (str): The first input string.
        B (str): The second input string.
        value (dict[str, int]): Mapping from characters to their values.

    Returns:
        list[list[int]]: A 2D DP table where dp[i][j] is the maximum value of a common subsequence of A[:i] and B[:j].
    """
    n, m = len(A), len(B)

    # dp[i][j] = maximum value of a common subsequence of A[:i] and B[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                # Case 1: The current characters match, either take the match or skip one character from A or B
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1] + value[A[i - 1]]
                )
            else:
                # Case 2: If they do not match, skip one character from either A or B
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


def reconstruct(dp, A, B, value):
    """
    Reconstruct one optimal highest-value common subsequence from the DP table.

    Args:
        dp (list[list[int]]): The completed DP table.
        A (str): The first input string.
        B (str): The second input string.
        value (dict[str, int]): Mapping from characters to their values.

    Returns:
        str: One optimal common subsequence whose total value equals dp[len(A)][len(B)].
    """
    i, j = len(A), len(B)
    res = []

    # Backtrack from the bottom-right corner of the DP table
    while i > 0 and j > 0:
        if A[i - 1] == B [j - 1] and dp[i][j] == dp[i - 1][j - 1] + value[A[i - 1]]:
            # This character is part of one optimal solution
            res.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            # Move up if the optimal value came from dp[i - 1][j]
            i -= 1
        else:
            # Move left if the optimal value came from dp[i][j - 1]
            j -= 1

    # Characters were collected backwards, so reverse them at the end
    res = reversed(res)

    return "".join(res)


def write_output(output_file, max_val, output_seq):
    """
    Write the HVLCS result to an output file.

    Args:
        output_file (str): Path to the output file.
        max_val (int): The maximum value of a common subsequence.
        output_seq (str): One optimal common subsequence.
    """
    with open(output_file, "w") as f:
        f.write(str(max_val) + "\n")
        f.write(output_seq + "\n")


def main():
    """
    One optimal common subsequence.
    """
    if len(sys.argv) < 2:
        print("Usage: python hvlcs.py input_file")
        return

    filename = sys.argv[1]

    # Check whether the input file exists before trying to open it
    if not os.path.isfile(filename):
        print(f"Error: cannot open input file '{filename}'")
        return

    # Paese input
    value, A, B = parse_input(filename)

    # Build the DP table
    dp = compute_dp(A, B, value)

    # Get the final maximum value and reconstruct one optimal subsequence
    max_val = dp[len(A)][len(B)]
    output_seq = reconstruct(dp, A, B, value)

    # Print result to terminal
    print(max_val)
    print(output_seq)

    # Save the result to an output file
    os.makedirs("outputs", exist_ok=True)
    base_name = os.path.splitext(os.path.basename(filename))[0]
    output_file = f"outputs/{base_name}.out"
    write_output(output_file, max_val, output_seq)


if __name__ == "__main__":
    main()
