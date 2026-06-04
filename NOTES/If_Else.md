````md
# If Else

## Syntax

```python
if condition:
    # code

else:
    # code
````

---

## Example

```python
age = int(input("Enter Age : "))

if age >= 18:
    print("Adult")

else:
    print("Minor")
```

---

## elif

Used for multiple conditions.

```python
marks = 75

if marks >= 90:
    print("A")

elif marks >= 70:
    print("B")

else:
    print("C")
```

---

## Comparison Operators Used in Conditions

| Operator | Meaning          |
| -------- | ---------------- |
| ==       | Equal            |
| !=       | Not Equal        |
| >        | Greater Than     |
| <        | Less Than        |
| >=       | Greater or Equal |
| <=       | Less or Equal    |

---

## Logical Operators

| Operator | Meaning                     |
| -------- | --------------------------- |
| and      | Both conditions True        |
| or       | At least one condition True |
| not      | Reverse condition           |

---

## Nested If

```python
age = 20

if age >= 18:

    if age <= 60:
        print("Valid")

    else:
        print("Senior")
```

---

## Important Notes

* Python uses indentation
* Condition must return True or False
* elif means "else if"

```
```
