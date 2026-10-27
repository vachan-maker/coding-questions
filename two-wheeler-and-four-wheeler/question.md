# Problem: Two-Wheeler and Four-Wheeler Production

## Problem Statement

An automobile company manufactures two types of vehicles: two-wheelers (TW) and four-wheelers (FW). A company manager wants to determine how many of each type should be manufactured based on the following data:

- **First input (`V`):** Total number of vehicles (two-wheelers + four-wheelers).
- **Second input (`W`):** Total number of wheels.

The task is to calculate the number of two-wheelers and four-wheelers that need to be manufactured.

## Example

**Input:**
```text
200
540
```

**Output:**
```text
TW=130 FW=70
```

## Explanation

- Total vehicles: `130 + 70 = 200`
- Total wheels: `(130 × 2) + (70 × 4) = 540`

## Constraints

- `W >= 2`
- `W % 2 == 0`
- `V < W`

Print `INVALID INPUT` if the inputs do not satisfy the given constraints.

## Input Format

The program must accept two positive integers, each on a separate line:

- First line: Value of `V` (total number of vehicles).
- Second line: Value of `W` (total number of wheels).

## Output Format

Print the number of two-wheelers and four-wheelers in the following format, separated by a single space:

```text
TW=<number> FW=<number>
```

If the inputs are invalid, print:

```text
INVALID INPUT
```

**Note:** Do not print any additional messages, as they may cause automated test cases to fail.
