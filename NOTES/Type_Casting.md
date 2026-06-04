````md
# Type Casting

## What is Type Casting?

Converting one data type into another.

---

## int()

Convert to integer.

```python
num = int("10")
````

---

## float()

Convert to float.

```python id="jlwm8z"
price = float("99.5")
```

---

## str()

Convert to string.

```python id="jlwm3a"
age = str(20)
```

---

## bool()

Convert to boolean.

```python id="jlwm6b"
value = bool(1)
```

---

## Integer Input

```python id="jlwm0c"
age = int(input("Enter Age : "))
```

---

## Float Input

```python id="jlwm9d"
price = float(input("Enter Price : "))
```

---

## Example

```python id="jlwm5e"
num1 = int(input("Enter Number : "))
num2 = int(input("Enter Number : "))

print(num1 + num2)
```

---

## Important Notes

* input() gives string by default
* Use int() for number input
* Wrong conversion gives error

---

## Invalid Conversion Example

```python id="jlwm2f"
int("hello")
```

This causes ValueError.

```id="jlwm7g"
```
