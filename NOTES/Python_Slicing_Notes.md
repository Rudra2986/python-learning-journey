# Python Slicing Notes

A quick reference for Python string slicing with examples.

## Basic Syntax

``` python
string[start:stop:step]
```

-   **start** → Starting index (inclusive)
-   **stop** → Ending index (exclusive)
-   **step** → Number of positions to move

Defaults: - start = 0 - stop = len(string) - step = 1

## Slicing Cheat Sheet

  Slice       Meaning                  Example (`python`)   Result
  ----------- ------------------------ -------------------- ----------
  `s[:]`      Copy entire string       `s[:]`               `python`
  `s[1:]`     From index 1             `s[1:]`              `ython`
  `s[:3]`     First 3 characters       `s[:3]`              `pyt`
  `s[:-1]`    Remove last character    `s[:-1]`             `pytho`
  `s[-1]`     Last character           `s[-1]`              `n`
  `s[::-1]`   Reverse                  `s[::-1]`            `nohtyp`
  `s[::2]`    Every 2nd character      `s[::2]`             `pto`
  `s[1::2]`   Every 2nd from index 1   `s[1::2]`            `yhn`
  `s[::-2]`   Reverse with step 2      `s[::-2]`            `nhy`
  `s[2:5]`    Index 2 to 4             `s[2:5]`             `tho`

## Examples

### Reverse a String

``` python
s = "python"
print(s[::-1])
```

### Rotate Left

``` python
s = "abcdef"
k = 2
print(s[k:] + s[:k])
```

### Rotate Right

``` python
s = "abcdef"
k = 2
print(s[-k:] + s[:-k])
```

### Remove Middle Character

``` python
s = "python"
mid = len(s)//2
print(s[:mid] + s[mid+1:])
```

### Swap First and Last Character

``` python
s = "python"
print(s[-1] + s[1:-1] + s[0])
```

### Check Palindrome

``` python
s = "madam"
print(s == s[::-1])
```

## Practice

Predict the output before running:

``` python
s = "abcdefgh"

print(s[2:])
print(s[:-2])
print(s[2:-2])
print(s[-4:-1])
print(s[::-3])
```
