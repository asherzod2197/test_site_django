## Savol 1

Tuple va listning sintaktik farqi nima?

- [A] Tuple `{}`, list `[]` bilan yoziladi
- [B] Tuple `()`, list `[]` bilan yoziladi
- [C] Tuple `[]`, list `()` bilan yoziladi
- [D] Ikkalasi ham `[]` bilan yoziladi

> **To'g'ri javob:** B
> **Tushuntirish:** List kvadrat qavslar `[1, 2, 3]`, tuple esa dumaloq qavslar `(1, 2, 3)` bilan yoziladi. Lekin tuple qavsini tushirib ham yozish mumkin: `t = 1, 2, 3`.

---

## Savol 2

Tuple va listning asosiy farqi nima?

- [A] Tuple faqat raqam saqlaydi, list har qanday ma'lumot
- [B] List o'zgarmas, tuple o'zgaruvchan
- [C] Tuple o'zgarmas (immutable), list o'zgaruvchan (mutable)
- [D] Hech qanday farq yo'q, faqat yozilishi boshqa

> **To'g'ri javob:** C
> **Tushuntirish:** Eng asosiy farq: `list` mutable — elementlarini o'zgartirish, qo'shish, o'chirish mumkin. `tuple` immutable — yaratilgandan keyin o'zgartirib bo'lmaydi. Bu farq xotira, tezlik va xavfsizlikka ta'sir qiladi.

---

## Savol 3

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3]
t = (1, 2, 3)

r[0] = 99
print(r)

t[0] = 99
print(t)
```

- [A] `[99, 2, 3]`, `(99, 2, 3)`
- [B] `[99, 2, 3]`, so'ng `TypeError`
- [C] `[1, 2, 3]`, `(1, 2, 3)`
- [D] Ikkalasi ham `TypeError` beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `r[0] = 99` — list mutable, ishlaydi → `[99, 2, 3]`. `t[0] = 99` — tuple immutable → `TypeError: 'tuple' object does not support item assignment`.

---

## Savol 4

Qaysi metodlar faqat listda bor, tupled emas?

- [A] `count()`, `index()`
- [B] `append()`, `remove()`, `sort()`, `pop()`
- [C] `len()`, `in`
- [D] `+`, `*`

> **To'g'ri javob:** B
> **Tushuntirish:** `append()`, `remove()`, `sort()`, `pop()`, `insert()`, `extend()`, `clear()`, `reverse()` — faqat listda. Tuple faqat `count()` va `index()` metodlariga ega, chunki u o'zgarmas.

---

## Savol 5

Quyidagi kodning natijasi nima?

```python
t = (3, 1, 4, 1, 5)
r = [3, 1, 4, 1, 5]

print(t.count(1))
print(r.count(1))
print(t.index(4))
print(r.index(4))
```

- [A] `2`, `2`, `2`, `2`
- [B] `1`, `2`, `2`, `2`
- [C] `2`, `2`, `2`, `3`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `count()` va `index()` — ikkala turda ham bor. `count(1)` → ikkala turda ham `2`. `index(4)` → ikkala turda ham indeks `2`.

---

## Savol 6

Tuple dict (lug'at) kaliti sifatida ishlatila oladimi?

- [A] Yo'q, faqat list kalit bo'la oladi
- [B] Ha, chunki tuple o'zgarmas (hashable)
- [C] Faqat raqamli tuple kalit bo'la oladi
- [D] Hech qaysi biri kalit bo'la olmaydi

> **To'g'ri javob:** B
> **Tushuntirish:** Dict kaliti hashable bo'lishi shart. Tuple immutable → hashable → kalit bo'la oladi. List mutable → not hashable → `TypeError` beradi.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
joylashuvlar = {}
joylashuvlar[(40.37, 71.80)] = "Toshkent"
joylashuvlar[(41.29, 69.24)] = "Samarqand"
print(joylashuvlar[(40.37, 71.80)])
```

- [A] `TypeError` — tuple kalit bo'la olmaydi
- [B] `"Toshkent"`
- [C] `"Samarqand"`
- [D] `(40.37, 71.80)`

> **To'g'ri javob:** B
> **Tushuntirish:** Tuple hashable bo'lgani uchun dict kaliti sifatida ishlatiladi. `(40.37, 71.80)` kalitiga mos qiymat `"Toshkent"`.

---

## Savol 8

Tezlik va xotira jihatidan qaysi biri samaraliroq?

- [A] List har doim tezroq
- [B] Tuple bir oz tezroq va kam xotira oladi, chunki o'zgarmas
- [C] Ikkalasi bir xil
- [D] Bu dastur turiga bog'liq emas

> **To'g'ri javob:** B
> **Tushuntirish:** Tuple immutable bo'lgani uchun Python uni optimallashtirib saqlaydi — list ga qaraganda biroz tezroq yaratiladi va kamroq xotira oladi. Ko'p o'qiladigan, o'zgarmaydigan ma'lumotlar uchun tuple afzal.

---

## Savol 9

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3]
t = (1, 2, 3)

r.append(4)
print(r)

t.append(4)
print(t)
```

- [A] `[1,2,3,4]`, `(1,2,3,4)`
- [B] `[1,2,3,4]`, so'ng `AttributeError`
- [C] Ikkalasi ham xato beradi
- [D] `[1,2,3]`, `(1,2,3,4)`

> **To'g'ri javob:** B
> **Tushuntirish:** `r.append(4)` → list mutable → `[1,2,3,4]`. `t.append(4)` → tuple da `append` metodi yo'q → `AttributeError: 'tuple' object has no attribute 'append'`.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30]
t = (10, 20, 30)

print(type(r))
print(type(t))
print(isinstance(r, list))
print(isinstance(t, tuple))
```

- [A] `list`, `tuple`, `False`, `False`
- [B] `list`, `tuple`, `True`, `True`
- [C] `<class 'list'>`, `<class 'tuple'>`, `True`, `True`
- [D] Xato beradi

> **To'g'ri javob:** C
> **Tushuntirish:** `type(r)` → `<class 'list'>`. `type(t)` → `<class 'tuple'>`. `isinstance(r, list)` → `True`. `isinstance(t, tuple)` → `True`.

---

## Savol 11

Qachon list, qachon tuple ishlatish to'g'ri?

- [A] Har doim list ishlatgan ma'qul
- [B] O'zgarmaydigan ma'lumotlar uchun tuple, o'zgaruvchi to'plamlar uchun list
- [C] Har doim tuple ishlatgan ma'qul
- [D] Katta ma'lumotlar uchun list, kichik uchun tuple

> **To'g'ri javob:** B
> **Tushuntirish:** Tuple — doimiy ma'lumotlar: koordinatalar, RGB ranglar, sanalar, dict kalitlari. List — o'zgaruvchan to'plamlar: foydalanuvchilar ro'yxati, savatcha, natijalar. To'g'ri tanlash kodni xavfsizroq va tushunarliroq qiladi.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3]
t = (1, 2, 3)

r2 = r
r2.append(99)
print(r)

t2 = t
t2 += (99,)
print(t)
print(t2)
```

- [A] `[1,2,3,99]`, `(1,2,3,99)`, `(1,2,3,99)`
- [B] `[1,2,3,99]`, `(1,2,3)`, `(1,2,3,99)`
- [C] `[1,2,3]`, `(1,2,3)`, `(1,2,3,99)`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `r2 = r` — bir xil listga havola. `r2.append(99)` → `r` ham o'zgaradi: `[1,2,3,99]`. `t2 += (99,)` — yangi tuple yaratadi, `t` o'zgarmaydi: `(1,2,3)`. `t2` → `(1,2,3,99)`.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5)

print(2 in r)
print(2 in t)
print(r[2:4])
print(t[2:4])
```

- [A] `True`, `True`, `[3, 4]`, `(3, 4)`
- [B] `True`, `False`, `[3, 4]`, `(3, 4)`
- [C] `True`, `True`, `[3, 4]`, `[3, 4]`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `in` operatori ikkala turda ham ishlaydi. Slicing ham ishlaydi, lekin **list slicing — list, tuple slicing — tuple** qaytaradi.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
r = [("Ali", 90), ("Vali", 85), ("Gali", 92)]

for ism, ball in r:
    if ball > 88:
        print(ism)
```

- [A] `Ali`, `Vali`, `Gali`
- [B] `Ali`, `Gali`
- [C] `Vali`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** List ichida tuplelar bor. `for ism, ball in r` — har tuple unpackinglanadi. `90 > 88` → `Ali` ✓. `85 > 88` → yo'q. `92 > 88` → `Gali` ✓.

---

## Savol 15

Quyidagi to'liq kodning natijasi nima?

```python
r = ["Python", "Java", "C++"]
t = ("Python", "Java", "C++")

r.append("JavaScript")
print(len(r), len(t))

r_nusxa = r.copy()
r_nusxa[0] = "Go"
print(r[0], r_nusxa[0])

print(t[0], t[-1])
print(type(r[1:]), type(t[1:]))
```

- [A] `4 3`, `Python Go`, `Python C++`, `<class 'list'>` `<class 'tuple'>`
- [B] `4 4`, `Python Go`, `Python C++`, `<class 'list'>` `<class 'list'>`
- [C] `3 3`, `Go Go`, `Python C++`, `<class 'list'>` `<class 'tuple'>`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `r.append` → `r` 4 ta, `t` o'zgarmadi → 3 ta. `r_nusxa[0]="Go"` → `r[0]` hali `"Python"`. `t[0]="Python"`, `t[-1]="C++"`. `r[1:]` → list slice → `list`. `t[1:]` → tuple slice → `tuple`.

---