# Count Elements Greater Than All Previous Elements

## Problem Statement

Given an integer array `Arr` of size `N`, find the count of elements whose value is strictly greater than all the elements that appear before them.

The first element is always counted because it has no preceding elements.

## Example 1

**Input:**
```python
Arr = [4, 2, 7, 5, 9]
```

**Output:**
```text
3
```

**Explanation:**

- `4` is counted because it is the first element.
- `2` is not counted because `2 < 4`.
- `7` is counted because `7 > 4` and `7 > 2`.
- `5` is not counted because `5 < 7`.
- `9` is counted because it is greater than all the preceding elements.

Therefore, the count is `3`.

## Example 2

**Input:**
```python
Arr = [3, 3, 5, 2, 8, 6, 9]
```

**Output:**
```text
4
```

**Explanation:**

The qualifying elements are `3`, `5`, `8`, and `9`.

Therefore, the count is `4`.

## Constraints

- `1 <= N <= 10^5`
- `-10^9 <= Arr[i] <= 10^9`

## Task

Implement the function:

```python
def countPriorGreaterElements(Arr):
    # Your code here
```

Return the count of elements that are strictly greater than all their preceding elements.

**Expected time complexity:** `O(N)`

**Expected auxiliary space complexity:** `O(1)`