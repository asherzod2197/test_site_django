## Savol 1

To'g'ridan-to'g'ri (literal) usulda list qanday yaratiladi?

- [A] `list(1, 2, 3)`  
- [B] `[1, 2, 3]`  
- [C] `{1, 2, 3}`  
- [D] `(1, 2, 3)`  

> **To'g'ri javob:** B  
> **Tushuntirish:** Kvadrat qavslar `[...]` ichiga elementlarni vergul bilan yozish — listni to'g'ridan-to'g'ri (literal) yaratish usuli. `{}` — set yoki dict, `()` — tuple, `list(...)` — konstruktor usuli.

---

## Savol 2

`list()` konstruktori bilan bo'sh list qanday yaratiladi?

- [A] `list(0)`  
- [B] `list{}`  
- [C] `list()`  
- [D] `list("")`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `list()` — argumentsiz chaqirilganda bo'sh list qaytaradi. `[]` ham xuddi shunday bo'sh list yaratadi. `list(0)` — xato, chunki `0` iterable emas.

---

## Savol 3

Quyidagi kodning natijasi nima?

```python
a = []
b = list()
print(a == b)
print(type(a) == type(b))
```

- [A] `False`, `False`  
- [B] `True`, `False`  
- [C] `True`, `True`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `[]` va `list()` ikkalasi ham bo'sh list yaratadi. Teng qiymat: `True`. Ikkalasi ham `list` turi: `True`.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40, 50]
print(r[0])
print(r[-1])
print(r[2])
```

- [A] `10`, `40`, `30`  
- [B] `20`, `50`, `30`  
- [C] `10`, `50`, `30`  
- [D] `10`, `50`, `40`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `r[0]` → birinchi element: `10`. `r[-1]` → oxirgi element: `50`. `r[2]` → 2-indeks: `30`.

---

## Savol 5

Quyidagi kodning natijasi nima?

```python
r = [True, 3.14, "salom", 42]
print(type(r))
print(len(r))
```

- [A] `<class 'tuple'>`, `4`  
- [B] `<class 'list'>`, `3`  
- [C] `<class 'list'>`, `4`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** List turli xil turdagi elementlarni saqlashi mumkin. `type(r)` → `<class 'list'>`. `len(r)` → `4` ta element.

---

## Savol 6

`range()` funksiyasi yordamida list yaratish uchun qaysi usul to'g'ri?

- [A] `range(1, 10)`  
- [B] `list[range(1, 10)]`  
- [C] `list(range(1, 10))`  
- [D] `[range(1, 10)]`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `range(1, 10)` o'zi list emas — bu range obyekti. Uni listga aylantirish uchun `list(range(1, 10))` ishlatiladi. `[range(1, 10)]` esa range obyektini bitta elementli listga joylashtiradi.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
r = list(range(1, 6))
print(r)
```

- [A] `[0, 1, 2, 3, 4, 5]`  
- [B] `[1, 2, 3, 4, 5, 6]`  
- [C] `[1, 2, 3, 4, 5]`  
- [D] `range(1, 6)`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `range(1, 6)` → `1` dan `6` gacha, `6` kirmaydi: `1, 2, 3, 4, 5`. `list()` → `[1, 2, 3, 4, 5]`.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
r = list(range(0, 10, 2))
print(r)
```

- [A] `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`  
- [B] `[2, 4, 6, 8, 10]`  
- [C] `[0, 2, 4, 6, 8]`  
- [D] `[1, 3, 5, 7, 9]`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `range(0, 10, 2)` — `0` dan `10` gacha (kirmaydi), `2` qadam bilan: `0, 2, 4, 6, 8`. Natija: `[0, 2, 4, 6, 8]`.

---

## Savol 9

Quyidagi kodning natijasi nima?

```python
r = list(range(10, 0, -1))
print(r)
```

- [A] `[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]`  
- [B] `[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`  
- [C] `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `range(10, 0, -1)` — `10` dan `0` gacha (kirmaydi), `-1` qadam: `10, 9, ..., 1`. `0` kirmaydi. Natija: `[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
r = list(range(5))
print(r)
print(r[3])
```

- [A] `[1, 2, 3, 4, 5]`, `4`  
- [B] `[0, 1, 2, 3, 4]`, `3`  
- [C] `[0, 1, 2, 3, 4]`, `4`  
- [D] `[0, 1, 2, 3, 4, 5]`, `3`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `range(5)` → `range(0, 5)` → `[0, 1, 2, 3, 4]`. `r[3]` → 3-indeksdagi element: `3`.

---

## Savol 11

`*` (yulduzcha) operatori listda nima qiladi?

- [A] Listning barcha elementlarini ko'paytiradi  
- [B] Listni berilgan songa ko'ra takrorlab yangi list yaratadi  
- [C] Ikkita listni birlashtiradi  
- [D] Listdagi elementlarni o'chiradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `[element] * n` — elementni `n` marta takrorlab yangi list yaratadi. Masalan: `[0] * 4` → `[0, 0, 0, 0]`. Asl list o'zgarmaydi.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
r = [0] * 5
print(r)

s = ["ha"] * 3
print(s)
```

- [A] `[0, 0, 0, 0, 0]`, `["ha", "ha", "ha"]`  
- [B] `[0, 5]`, `["ha", 3]`  
- [C] `[0, 1, 2, 3, 4]`, `["ha"]`  
- [D] Xato beradi  

> **To'g'ri javob:** A  
> **Tushuntirish:** `[0] * 5` → `0` ni 5 marta: `[0, 0, 0, 0, 0]`. `["ha"] * 3` → `"ha"` ni 3 marta: `["ha", "ha", "ha"]`.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3] * 3
print(r)
print(len(r))
```

- [A] `[[1,2,3], [1,2,3], [1,2,3]]`, `3`  
- [B] `[1, 2, 3, 1, 2, 3, 1, 2, 3]`, `9`  
- [C] `[3, 6, 9]`, `3`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `[1, 2, 3] * 3` — butun listni 3 marta takrorlaydi: `[1, 2, 3, 1, 2, 3, 1, 2, 3]`. `len()` → `9`.

---

## Savol 14

`+` operatori listlarda qanday ishlaydi?

- [A] Listlarning mos elementlarini qo'shadi  
- [B] Ikkala listni birlashtirgan yangi list qaytaradi, asl listlar o'zgarmaydi  
- [C] Birinchi listni o'zgartirib, ikkinchisini unga qo'shadi  
- [D] Faqat raqamli listlarda ishlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `list1 + list2` — ikkala listni birlashtirgan yangi list yaratadi. Asl `list1` va `list2` o'zgarmaydi. `extend()` esa `list1` ni bevosita o'zgartiradi.

---

## Savol 15

Quyidagi kodning natijasi nima?

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)
print(b)
```

- [A] `[1,2,3,4,5,6]`, `[1,2,3,4,5,6]`, `[4,5,6]`  
- [B] `[1,2,3,4,5,6]`, `[1,2,3]`, `[4,5,6]`  
- [C] `[[1,2,3],[4,5,6]]`, `[1,2,3]`, `[4,5,6]`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `a + b` → yangi `c` list yaratiladi: `[1,2,3,4,5,6]`. `a` va `b` o'zgarmaydi.

---

## Savol 16

Quyidagi kodning natijasi nima?

```python
a = [1, 2]
b = [3, 4]
c = [5, 6]
r = a + b + c
print(r)
print(len(r))
```

- [A] `[[1,2],[3,4],[5,6]]`, `3`  
- [B] `[1, 2, 3, 4, 5, 6]`, `6`  
- [C] `[1, 2, 3, 4, 5, 6]`, `3`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `a + b + c` — ketma-ket birlashtirish: `[1,2,3,4,5,6]`. `len()` → `6`.

---

## Savol 17

Quyidagi kodning natijasi nima?

```python
r = [0] * 3 + [1] * 3 + [2] * 3
print(r)
```

- [A] `[0, 1, 2]`  
- [B] `[0, 0, 0, 1, 1, 1, 2, 2, 2]`  
- [C] `[[0,0,0], [1,1,1], [2,2,2]]`  
- [D] `[0, 3, 1, 3, 2, 3]`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `[0]*3` → `[0,0,0]`, `[1]*3` → `[1,1,1]`, `[2]*3` → `[2,2,2]`. `+` bilan birlashtirish: `[0,0,0,1,1,1,2,2,2]`.

---

## Savol 18

`*` va `+` operatorlari o'rtasidagi farq nima?

- [A] Hech qanday farq yo'q  
- [B] `*` — listni n marta takrorlaydi; `+` — ikkita listni birlashtiradi  
- [C] `+` — listni n marta takrorlaydi; `*` — birlashtiradi  
- [D] `*` faqat raqamli, `+` faqat matnli listlarda ishlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `[1,2] * 3` → `[1,2,1,2,1,2]` (takrorlash). `[1,2] + [3,4]` → `[1,2,3,4]` (birlashtirish). Ikkalasi ham yangi list yaratadi.

---

## Savol 19

`list` nusxasini `=` operatori bilan yaratsa nima bo'ladi?

- [A] Yangi mustaqil list yaratiladi  
- [B] Bir xil listga ikki xil nom (reference) beriladi — biri o'zgarsa ikkinchisi ham o'zgaradi  
- [C] List avtomatik nusxalanadi  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `b = a` — `b` yangi list emas, `a` bilan bir xil obyektga ko'rsatadi (reference). `a` o'zgarsa `b` ham o'zgaradi. Mustaqil nusxa olish uchun `b = a.copy()` yoki `b = a[:]` ishlatish kerak.

---

## Savol 20

Quyidagi kodning natijasi nima?

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
print(a is b)
```

- [A] `[1,2,3]`, `[1,2,3,4]`, `False`  
- [B] `[1,2,3,4]`, `[1,2,3,4]`, `True`  
- [C] `[1,2,3]`, `[1,2,3,4]`, `True`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `b = a` — reference. `b.append(4)` asl listni ham o'zgartiradi. `a` va `b` bir xil obyekt: `a is b` → `True`. Ikkalasi ham `[1,2,3,4]`.

---

## Savol 21

`copy()` metodi qanday nusxa yaratadi?

- [A] Chuqur nusxa (deep copy) — barcha ichki listlar ham yangi yaratiladi  
- [B] Sirtqi nusxa (shallow copy) — faqat birinchi daraja elementlar yangi, ichki listlar baham ko'riladi  
- [C] Reference (havola) qaytaradi  
- [D] Faqat raqamli listlar uchun ishlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `list.copy()` — sirtqi (shallow) nusxa yaratadi. Oddiy elementlar mustaqil bo'ladi, lekin ichki (nested) listlar hali baham ko'riladi. Chuqur nusxa uchun `copy.deepcopy()` kerak.

---

## Savol 22

Quyidagi kodning natijasi nima?

```python
asl = [1, 2, 3, 4, 5]
nusxa = asl.copy()
nusxa.append(6)
print(asl)
print(nusxa)
```

- [A] `[1,2,3,4,5,6]`, `[1,2,3,4,5,6]`  
- [B] `[1,2,3,4,5]`, `[1,2,3,4,5,6]`  
- [C] `[1,2,3,4,5]`, `[1,2,3,4,5]`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `copy()` mustaqil nusxa yaratadi. `nusxa.append(6)` faqat nusxani o'zgartiradi. `asl` → `[1,2,3,4,5]` (o'zgarmagan).

---

## Savol 23

`[:]` slice yordamida nusxa olish `copy()` dan farq qiladimi?

- [A] Ha, `[:]` chuqur nusxa, `copy()` sirtqi nusxa yaratadi  
- [B] Yo'q, ikkalasi ham sirtqi nusxa (shallow copy) yaratadi  
- [C] Ha, `copy()` tezroq ishlaydi  
- [D] `[:]` faqat raqamli listlarda ishlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `a[:]` va `a.copy()` — ikkalasi ham sirtqi nusxa (shallow copy) yaratadi. Natija bir xil: oddiy elementlar mustaqil, ichki listlar baham ko'riladi.

---

## Savol 24

Quyidagi kodning natijasi nima?

```python
asl = [10, 20, 30]
nusxa = asl[:]
nusxa[0] = 999
print(asl)
print(nusxa)
```

- [A] `[999, 20, 30]`, `[999, 20, 30]`  
- [B] `[10, 20, 30]`, `[999, 20, 30]`  
- [C] `[999, 20, 30]`, `[10, 20, 30]`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `asl[:]` — mustaqil nusxa. `nusxa[0] = 999` faqat nusxani o'zgartiradi. `asl` → `[10, 20, 30]` o'zgarmagan. `nusxa` → `[999, 20, 30]`.

---

## Savol 25

Quyidagi kodda `=`, `copy()` va `[:]` dan qaysi biri mustaqil nusxa yaratadi?

```python
a = [1, 2, 3]
b = a
c = a.copy()
d = a[:]
a.append(99)
print(b)
print(c)
print(d)
```

- [A] `[1,2,3,99]`, `[1,2,3,99]`, `[1,2,3,99]`  
- [B] `[1,2,3,99]`, `[1,2,3]`, `[1,2,3]`  
- [C] `[1,2,3]`, `[1,2,3]`, `[1,2,3]`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `b = a` — reference, `a` o'zgarganda `b` ham o'zgaradi → `[1,2,3,99]`. `c = a.copy()` va `d = a[:]` — mustaqil nusxa, o'zgarmaydi → `[1,2,3]`.

---

## Savol 26

Quyidagi kodning natijasi nima?

```python
r = list(range(1, 11))
juft = r[1::2]
print(juft)
```

- [A] `[1, 3, 5, 7, 9]`  
- [B] `[2, 4, 6, 8, 10]`  
- [C] `[1, 2, 3, 4, 5]`  
- [D] `[2, 4, 6, 8]`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `list(range(1,11))` → `[1,2,3,4,5,6,7,8,9,10]`. `r[1::2]` — 1-indeksdan boshlab, 2 qadam: `2, 4, 6, 8, 10`. Natija: `[2, 4, 6, 8, 10]`.

---

## Savol 27

Quyidagi kodning natijasi nima?

```python
a = [1, 2, 3]
b = a * 2 + [0]
print(b)
print(len(b))
```

- [A] `[1,2,3,1,2,3,0]`, `7`  
- [B] `[2,4,6,0]`, `4`  
- [C] `[1,2,3,0,1,2,3,0]`, `8`  
- [D] Xato beradi  

> **To'g'ri javob:** A  
> **Tushuntirish:** `a * 2` → `[1,2,3,1,2,3]`. `+ [0]` → `[1,2,3,1,2,3,0]`. `len()` → `7`.

---

## Savol 28

Quyidagi kodning natijasi nima?

```python
import copy
asl = [[1, 2], [3, 4]]
sirtqi = asl.copy()
chuqur = copy.deepcopy(asl)

asl[0].append(99)
print(sirtqi[0])
print(chuqur[0])
```

- [A] `[1, 2, 99]`, `[1, 2, 99]`  
- [B] `[1, 2, 99]`, `[1, 2]`  
- [C] `[1, 2]`, `[1, 2]`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `copy()` sirtqi nusxa — ichki listlar baham ko'riladi. `asl[0].append(99)` → `sirtqi[0]` ham `[1,2,99]`. `deepcopy()` to'liq mustaqil — `chuqur[0]` → `[1,2]` o'zgarmagan.

---

## Savol 29

Quyidagi kodning natijasi nima?

```python
r1 = list(range(1, 6))
r2 = r1[::-1]
r3 = r1 + r2
print(r3)
print(r3[4])
```

- [A] `[1,2,3,4,5,5,4,3,2,1]`, `5`  
- [B] `[1,2,3,4,5,4,3,2,1]`, `5`  
- [C] `[5,4,3,2,1,1,2,3,4,5]`, `1`  
- [D] Xato beradi  

> **To'g'ri javob:** A  
> **Tushuntirish:** `r1` → `[1,2,3,4,5]`. `r1[::-1]` → teskari: `[5,4,3,2,1]`. `r1 + r2` → `[1,2,3,4,5,5,4,3,2,1]`. `r3[4]` → 4-indeks: `5`.

---

## Savol 30

Quyidagi to'liq kodning natijasi nima?

```python
boshlang_ich = list(range(1, 6))
takror = boshlang_ich * 2
birlashtir = takror + [0] * 3
nusxa = birlashtir[:]
nusxa[0] = 999

print(birlashtir[:5])
print(nusxa[:5])
print(len(birlashtir) == len(nusxa))
print(birlashtir[0] == nusxa[0])
```

- [A] `[1,2,3,4,5]`, `[999,2,3,4,5]`, `True`, `True`  
- [B] `[1,2,3,4,5]`, `[999,2,3,4,5]`, `True`, `False`  
- [C] `[999,2,3,4,5]`, `[999,2,3,4,5]`, `True`, `True`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `boshlang_ich` → `[1,2,3,4,5]`. `takror` → `[1,2,3,4,5,1,2,3,4,5]`. `birlashtir` → `[1,2,3,4,5,1,2,3,4,5,0,0,0]` (13 ta). `nusxa = birlashtir[:]` — mustaqil nusxa. `nusxa[0] = 999` faqat nusxani o'zgartiradi. `birlashtir[:5]` → `[1,2,3,4,5]`. `nusxa[:5]` → `[999,2,3,4,5]`. `len` teng: `True`. `birlashtir[0]=1`, `nusxa[0]=999` → `False`.

---