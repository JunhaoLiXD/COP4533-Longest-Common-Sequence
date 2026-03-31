# COP4533–Highest-Value-Longest-Common-Subsequence

This repository contains the implementation for a COP4533 dynamic programming programming assignment. The project solves the Highest Value Longest Common Subsequence (HVLCS) problem by computing the maximum total value of a common subsequence of two strings and reconstructing one optimal subsequence.

## Team Members
- Name: Yuyang Sun, UFID: 38133550  
- Name: Junhao Li, UFID: 51521823

## Requirements / Dependencies
- Python **3.x**
- No external libraries are required.

## Project Structure
- `hvlcs.py` : Main program file containing:
  - input parsing
  - dynamic programming table construction
  - subsequence reconstruction
  - output writing

- `inputs/` : Example input files for testing the HVLCS solver
  - `example.in` : Sample HVLCS input file

- `outputs/` : Generated program outputs
  - `example.out` : Output produced for `example.in`

- `README.md` : Project documentation and usage instructions.

## Input Format

The program reads an HVLCS input file describing the alphabet values and two input strings.

The input file format is:

1. First line: one integer `K`
   - `K` : number of characters in the alphabet

2. Next `K` lines:
   - each line contains one character and its assigned value

3. Next line:
   - string `A`

4. Next line:
   - string `B`

### Example Input

    3
    a 2
    b 4
    c 5
    aacb
    caab

This means:
- `a` has value `2`
- `b` has value `4`
- `c` has value `5`
- the two input strings are `A = aacb` and `B = caab`

## Output Format

The program writes the result to an output file and also prints it to the terminal.

The output contains:

1. First line:
   - the maximum value of a common subsequence

2. Second line:
   - one optimal common subsequence achieving that value

### Example Output

    9
    cb

Explanation:
- `cb` is a common subsequence of both strings
- `Val(cb) = 5 + 4 = 9`

## How to Run

The program is executed from the repository root directory and requires one command-line argument:

    python hvlcs.py <input_file>

Where:

- `<input_file>` : path to the HVLCS input file

### Step-by-step Instructions

1. Open a terminal.
2. Navigate to the project root directory.
3. Run the program using Python with an input file.

### Example

Suppose the repository contains the following file:

    inputs/example.in

Run the program using:

    python hvlcs.py inputs/example.in

The program will:
- print the result to the terminal
- write the result to:

    outputs/example.out

## Written Component

### Question 1:


### Question 2:


### Question 3:
