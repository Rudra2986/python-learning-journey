````md
# Functions

## What is Function?

Reusable block of code.

Functions help:
- reuse code
- organize logic
- reduce repetition

---

## Create Function

```python
def greet():
    print("Hello")
````

---

## Call Function

```python id="jlwm7k"
greet()
```

---

## Function With Parameters

```python id="jlwm5l"
def add(a, b):
    print(a + b)
```

---

## Function With Return

```python id="jlwm2m"
def square(n):
    return n * n
```

---

## Example

```python id="jlwm8n"
def even_or_odd(num):

    if num % 2 == 0:
        print("Even")

    else:
        print("Odd")
```

---

## Return Example

```python id="jlwm1o"
def add(a, b):

    return a + b

result = add(5, 3)

print(result)
```

---

## Local Variable

Variable created inside function.

```python id="jlwm4p"
def test():

    x = 10
```

---

## Global Variable

Variable created outside function.

```python id="jlwm6q"
x = 100

def test():
    print(x)
```

---

## Important Keywords

| Keyword | Meaning         |
| ------- | --------------- |
| def     | create function |
| return  | send value back |

---

## Important Notes

* Function runs only when called
* Parameters receive values
* return stores/output value

```
```
