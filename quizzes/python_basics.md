# Python Asoslari — Test

## Savol 1

Quyidagi Python kodini ko'ring:

```python
def greet(name):
    return f"Salom, {name}!"

print(greet("Aziz"))
```

Dastur qanday natija chiqaradi?

- [A] `Salom, name!`
- [B] `Salom, Aziz!`
- [C] `None`
- [D] Xatolik chiqadi

> **To'g'ri javob:** B
> **Tushuntirish:** f-string yordamida `name` o'zgaruvchisi qiymatini satrga qo'shish mumkin. `f"Salom, {name}!"` ifodasi `name` ning qiymatini joylashtiradi.

---

## Savol 2

Quyidagi kodning natijasi nima bo'ladi?

```python
x = [1, 2, 3, 4, 5]
print(x[1:3])
```

- [A] `[1, 2, 3]`
- [B] `[2, 3]`
- [C] `[2, 3, 4]`
- [D] `[1, 2]`

> **To'g'ri javob:** B
> **Tushuntirish:** Python'da slicing `[start:end]` — `start` indeksdan boshlab `end` indeksgacha (lekin `end` o'zi kiritilmaydi). `x[1:3]` — indeks 1 va 2 elementlarini oladi: `[2, 3]`.

---

## Savol 3

`type(3.14)` qanday natija beradi?

- [A] `<class 'int'>`
- [B] `<class 'float'>`
- [C] `<class 'str'>`
- [D] `<class 'decimal'>`

> **To'g'ri javob:** B
> **Tushuntirish:** `3.14` — bu haqiqiy son (float). Python'da kasr sonlar `float` turiga tegishli.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
my_dict = {"a": 1, "b": 2, "c": 3}
print(list(my_dict.keys()))
```

- [A] `[1, 2, 3]`
- [B] `['a', 'b', 'c']`
- [C] `[('a', 1), ('b', 2), ('c', 3)]`
- [D] Xatolik chiqadi

> **To'g'ri javob:** B
> **Tushuntirish:** `.keys()` metodi lug'atning barcha kalitlarini qaytaradi. `list()` bilan o'rashganda `['a', 'b', 'c']` ro'yxati hosil bo'ladi.

---

## Savol 5

Quyidagi kod nima chiqaradi?

```python
for i in range(3):
    print(i, end=" ")
```

- [A] `1 2 3`
- [B] `0 1 2`
- [C] `0 1 2 3`
- [D] `1 2`

> **To'g'ri javob:** B
> **Tushuntirish:** `range(3)` — 0, 1, 2 sonlarini generatsiya qiladi. `end=" "` parametri har bir `print` dan keyin yangi qator o'rniga bo'sh joy qo'yadi.

---

## Savol 6

Quyidagi kodning natijasi nima?

```python
def multiply(a, b=2):
    return a * b

print(multiply(5))
```

- [A] `10`
- [B] `5`
- [C] `7`
- [D] Xatolik chiqadi

> **To'g'ri javob:** A
> **Tushuntirish:** `b=2` default qiymat. `multiply(5)` chaqirilganda `a=5`, `b=2` (default). Natija: `5 * 2 = 10`.
