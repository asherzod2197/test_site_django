## Savol 1

Tuple qanday yaratiladi?

- [A] `t = [1, 2, 3]`
- [B] `t = (1, 2, 3)`
- [C] `t = {1, 2, 3}`
- [D] `t = <1, 2, 3>`

> **To'g'ri javob:** B
> **Tushuntirish:** Tuple dumaloq qavslar `(...)` ichiga elementlarni vergul bilan yozib yaratiladi. `[]` — list, `{}` — set yoki dict yaratadi.

---

## Savol 2

Bo'sh tuple qanday yaratiladi?

- [A] `t = (,)`
- [B] `t = ( )`
- [C] `t = ()`
- [D] `t = tuple`

> **To'g'ri javob:** C
> **Tushuntirish:** Bo'sh tuple `()` yoki `tuple()` konstruktori bilan yaratiladi. `( )` (ichida bo'sh joy) ham ishlaydi, lekin `()` to'g'riroq yozuv.

---

## Savol 3

Bitta elementli tuple qanday yaratiladi?

- [A] `t = (5)`
- [B] `t = (5,)`
- [C] `t = tuple(5)`
- [D] `t = [5]`

> **To'g'ri javob:** B
> **Tushuntirish:** `(5)` — bu shunchaki `5` soni (matematik qavs). Bitta elementli tuple uchun vergul **shart**: `(5,)`. `type((5))` → `int`, `type((5,))` → `tuple`.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
a = (5)
b = (5,)
print(type(a))
print(type(b))
```

- [A] `<class 'tuple'>`, `<class 'tuple'>`
- [B] `<class 'int'>`, `<class 'tuple'>`
- [C] `<class 'int'>`, `<class 'int'>`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `(5)` → qavs matematik, `int`. `(5,)` → vergul tufayli `tuple`. Shuning uchun bitta elementli tuple yaratishda vergul unutilmaydi.

---

## Savol 5

`tuple()` konstruktori bilan qanday tuple yaratiladi?

- [A] Faqat bo'sh tuple yaratadi
- [B] Istalgan iterableni (list, string, range) tuple ga aylantiradi
- [C] Faqat raqamli qiymatlardan tuple yaratadi
- [D] Faqat listdan tuple yaratadi

> **To'g'ri javob:** B
> **Tushuntirish:** `tuple(iterable)` — istalgan iterableni tuple ga aylantiradi. `tuple([1,2,3])` → `(1,2,3)`. `tuple("salom")` → `("s","a","l","o","m")`. `tuple(range(3))` → `(0,1,2)`.

---

## Savol 6

Quyidagi kodning natijasi nima?

```python
t = tuple("Python")
print(t)
print(len(t))
```

- [A] `("Python",)`, `1`
- [B] `("P","y","t","h","o","n")`, `6`
- [C] `["P","y","t","h","o","n"]`, `6`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `tuple(string)` — stringdagi har bir belgi alohida element bo'ladi. `"Python"` → 6 ta harf → `("P","y","t","h","o","n")`. `len` → `6`.

---

## Savol 7

Tuple o'zgarmas (immutable) ekanligi nimani anglatadi?

- [A] Tuple elementlarini o'qib bo'lmaydi
- [B] Tuple yaratilgandan keyin elementlarini o'zgartirish, qo'shish yoki o'chirish mumkin emas
- [C] Tuple faqat bir marta ishlatiladi
- [D] Tuple da faqat bir xil turdagi elementlar bo'lishi kerak

> **To'g'ri javob:** B
> **Tushuntirish:** Immutable — o'zgarmas. `t[0] = 99` yoki `t.append(4)` kabi amallar `TypeError` beradi. Tuple ni qayta belgilash mumkin: `t = (1,2)` → `t = (3,4)`, lekin bu yangi tuple yaratish.

---

## Savol 8

Quyidagi kodda nima sodir bo'ladi?

```python
t = (10, 20, 30)
t[1] = 99
print(t)
```

- [A] `(10, 99, 30)` chiqadi
- [B] `TypeError` — tuple o'zgarmas
- [C] `(10, 20, 30)` — o'zgarmaydi
- [D] `ValueError` beradi

> **To'g'ri javob:** B
> **Tushuntirish:** Tuple immutable. `t[1] = 99` → `TypeError: 'tuple' object does not support item assignment`. Elementni o'zgartirish uchun tuple ni listga aylantirish kerak.

---

## Savol 9

Quyidagi kodning natijasi nima?

```python
t = (10, 20, 30, 40, 50)
print(t[0])
print(t[-1])
print(t[1:4])
```

- [A] `10`, `40`, `(20, 30, 40, 50)`
- [B] `10`, `50`, `(20, 30, 40)`
- [C] `20`, `50`, `(10, 20, 30)`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `t[0]` → `10`. `t[-1]` → oxirgi: `50`. `t[1:4]` → indeks 1 dan 3 gacha: `(20, 30, 40)`.

---

## Savol 10

Tuple unpacking (qadoqdan chiqarish) nima?

- [A] Tuple ni listga aylantirish
- [B] Tuple elementlarini alohida o'zgaruvchilarga biriktirish
- [C] Tuple ni o'chirish
- [D] Tuple dan nusxa olish

> **To'g'ri javob:** B
> **Tushuntirish:** `a, b, c = (1, 2, 3)` — tuple elementlari `a`, `b`, `c` ga biriktiriladi. O'zgaruvchilar soni tuple uzunligiga teng bo'lishi shart, aks holda `ValueError`.

---

## Savol 11

Quyidagi kodning natijasi nima?

```python
t = ("Ali", 25, "Toshkent")
ism, yosh, shahar = t
print(ism)
print(shahar)
```

- [A] `"Ali"`, `25`
- [B] `"Ali"`, `"Toshkent"`
- [C] `25`, `"Toshkent"`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `ism, yosh, shahar = ("Ali", 25, "Toshkent")` → `ism="Ali"`, `yosh=25`, `shahar="Toshkent"`. `print(ism)` → `"Ali"`, `print(shahar)` → `"Toshkent"`.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
a, *b, c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
```

- [A] `1`, `(2, 3, 4)`, `5`
- [B] `1`, `[2, 3, 4]`, `5`
- [C] `1`, `[2, 3, 4, 5]`, xato
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `*b` — o'rtadagi qolgan elementlarni **list** sifatida oladi. `a=1`, `b=[2,3,4]` (list), `c=5`.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
t4 = t1 * 2
print(t3)
print(t4)
```

- [A] `(5, 7, 9)`, `(2, 4, 6)`
- [B] `(1,2,3,4,5,6)`, `(1,2,3,1,2,3)`
- [C] `[1,2,3,4,5,6]`, `[1,2,3,1,2,3]`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `+` — ikkala tuple ni birlashtiradi, yangi tuple qaytaradi. `*` — takrorlaydi, yangi tuple qaytaradi. Natijalar tuple bo'ladi.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
t = (3, 1, 4, 1, 5, 9, 2, 6)
print(t.count(1))
print(t.index(5))
print(len(t))
```

- [A] `2`, `4`, `8`
- [B] `1`, `5`, `8`
- [C] `2`, `5`, `7`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `count(1)` → `1` ikkita (indeks 1 va 3) → `2`. `index(5)` → `5` ning indeksi → `4`. `len(t)` → `8`.

---

## Savol 15

Tuple ni listga va listni tuple ga aylantirish qanday?

- [A] `tuple.to_list()` va `list.to_tuple()`
- [B] `list(tuple_nomi)` va `tuple(list_nomi)`
- [C] `tuple[:]` va `list[:]`
- [D] Aylantirish mumkin emas

> **To'g'ri javob:** B
> **Tushuntirish:** `list((1,2,3))` → `[1,2,3]`. `tuple([1,2,3])` → `(1,2,3)`. Tuple o'zgarmas bo'lgani uchun uni listga aylantirib, o'zgartirib, qaytadan tuple qilish mumkin.

---

## Savol 16

Quyidagi kodning natijasi nima?

```python
t = (5, 3, 8, 1, 9)
r = list(t)
r.sort()
t2 = tuple(r)
print(t)
print(t2)
```

- [A] `(1,3,5,8,9)`, `(1,3,5,8,9)`
- [B] `(5,3,8,1,9)`, `(1,3,5,8,9)`
- [C] `(5,3,8,1,9)`, `[1,3,5,8,9]`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** Asl `t` o'zgarmaydi. `list(t)` → `[5,3,8,1,9]`. `sort()` → `[1,3,5,8,9]`. `tuple(r)` → `(1,3,5,8,9)`.

---

## Savol 17

Quyidagi kodning natijasi nima?

```python
t = (10, [20, 30], 40)
t[1].append(99)
print(t)
```

- [A] `(10, [20, 30], 40)` — o'zgarmadi
- [B] `TypeError` beradi
- [C] `(10, [20, 30, 99], 40)`
- [D] `(10, 99, 40)`

> **To'g'ri javob:** C
> **Tushuntirish:** Tuple immutable — lekin ichidagi **list** mutable. `t[1]` bu list, unga `append(99)` qilish mumkin. Tuple ning o'zi (list havolasi) o'zgarmadi, faqat list ichiga element qo'shildi.

---

## Savol 18

`in` operatori tuple da qanday ishlaydi?

```python
t = ("olma", "banan", "gilos")
print("banan" in t)
print("anor" in t)
print("anor" not in t)
```

- [A] `True`, `True`, `False`
- [B] `True`, `False`, `True`
- [C] `False`, `True`, `True`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `"banan" in t` → `True`. `"anor" in t` → `False`. `"anor" not in t` → `True`. `in` operatori tuple da listdek ishlaydi.

---

## Savol 19

Quyidagi kodning natijasi nima?

```python
koordinatalar = ((1, 2), (3, 4), (5, 6))
for x, y in koordinatalar:
    print(f"x={x}, y={y}")
```

- [A] `x=(1,2)`, `x=(3,4)`, `x=(5,6)`
- [B] `x=1, y=2` / `x=3, y=4` / `x=5, y=6`
- [C] `x=1` / `x=3` / `x=5`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `for x, y in koordinatalar` — har tuple `x` va `y` ga unpackinglanadi. `(1,2)` → `x=1, y=2`, `(3,4)` → `x=3, y=4`, `(5,6)` → `x=5, y=6`.

---

## Savol 20

Quyidagi to'liq kodning natijasi nima?

```python
talabalar = (
    ("Ali", 85),
    ("Vali", 92),
    ("Gali", 78),
    ("Zulfiya", 95)
)

eng_yaxshi_ism = ""
eng_yaxshi_ball = 0

for ism, ball in talabalar:
    if ball > eng_yaxshi_ball:
        eng_yaxshi_ball = ball
        eng_yaxshi_ism = ism

print(eng_yaxshi_ism)
print(eng_yaxshi_ball)
print(len(talabalar))
```

- [A] `"Ali"`, `85`, `4`
- [B] `"Zulfiya"`, `95`, `4`
- [C] `"Vali"`, `92`, `3`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `for` tsikli har tuple ni `ism` va `ball` ga unpackinglaydi. Eng katta ball: `95` → `"Zulfiya"`. `len(talabalar)` → `4` ta tuple.

---