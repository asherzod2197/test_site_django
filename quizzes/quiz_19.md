## Savol 1

Listda indekslash qaysi raqamdan boshlanadi?

- [A] `1`
- [B] `-1`
- [C] `0`
- [D] Listning uzunligidan

> **To'g'ri javob:** C
> **Tushuntirish:** Python'da indekslash `0` dan boshlanadi. Birinchi element `[0]`, ikkinchi `[1]`, va hokazo. `[-1]` esa oxirgi elementni bildiradi.

---

## Savol 2

Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40, 50]
print(r[0])
print(r[4])
```

- [A] `10`, `40`
- [B] `20`, `50`
- [C] `10`, `50`
- [D] `IndexError`

> **To'g'ri javob:** C
> **Tushuntirish:** `r[0]` → birinchi element: `10`. `r[4]` → beshinchi (oxirgi) element: `50`. Indeks `0` dan `4` gacha (5 ta element).

---

## Savol 3

Manfiy indekslash qanday ishlaydi?

- [A] Xato beradi
- [B] Listning boshidan hisoblaydi
- [C] Listning oxiridan hisoblaydi: `-1` oxirgi, `-2` oxiridan ikkinchi
- [D] Faqat `-1` ishlatish mumkin

> **To'g'ri javob:** C
> **Tushuntirish:** Manfiy indeks listning oxiridan hisoblaydi. `-1` — oxirgi element, `-2` — oxiridan ikkinchi, `-n` — boshidan `n`-element.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
r = ["a", "b", "c", "d", "e"]
print(r[-1])
print(r[-3])
print(r[-5])
```

- [A] `"e"`, `"c"`, `"a"`
- [B] `"e"`, `"b"`, `"a"`
- [C] `"d"`, `"c"`, `"b"`
- [D] `IndexError`

> **To'g'ri javob:** A
> **Tushuntirish:** `r[-1]` → `"e"` (oxirgi). `r[-3]` → `"c"` (oxiridan 3-chi). `r[-5]` → `"a"` (oxiridan 5-chi = birinchi).

---

## Savol 5

Quyidagi kodda xato bormi?

```python
r = [1, 2, 3, 4, 5]
print(r[5])
```

- [A] Xato yo'q, `5` chiqadi
- [B] Xato yo'q, `None` chiqadi
- [C] `IndexError` — indeks chegaradan tashqarida
- [D] `0` chiqadi

> **To'g'ri javob:** C
> **Tushuntirish:** 5 ta elementli listda indekslar `0` dan `4` gacha. `r[5]` mavjud emas → `IndexError: list index out of range`.

---

## Savol 6

Slicing (kesish) sintaksisi qanday?

- [A] `list{bosh:oxir}`
- [B] `list(bosh, oxir)`
- [C] `list[bosh:oxir]`
- [D] `list[bosh, oxir]`

> **To'g'ri javob:** C
> **Tushuntirish:** `list[bosh:oxir]` — `bosh` indeksdan `oxir` indeksgacha (oxiri kirmaydi) elementlarni oladi. `bosh` yoki `oxir` tushirib qoldirilsa, mos ravishda listning boshi yoki oxirigacha ketadi.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(r[2:6])
print(r[:4])
print(r[7:])
```

- [A] `[2,3,4,5,6]`, `[0,1,2,3,4]`, `[7,8,9]`
- [B] `[2,3,4,5]`, `[0,1,2,3]`, `[7,8,9]`
- [C] `[2,3,4,5,6]`, `[0,1,2,3]`, `[8,9]`
- [D] `[2,6]`, `[4]`, `[7]`

> **To'g'ri javob:** B
> **Tushuntirish:** `r[2:6]` → indeks 2 dan 5 gacha: `[2,3,4,5]`. `r[:4]` → boshdan 3 gacha: `[0,1,2,3]`. `r[7:]` → 7 dan oxirigacha: `[7,8,9]`.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40, 50]
print(r[-3:-1])
print(r[-4:])
```

- [A] `[30, 40]`, `[20, 30, 40, 50]`
- [B] `[30, 40, 50]`, `[20, 30, 40, 50]`
- [C] `[20, 30]`, `[10, 20, 30, 40]`
- [D] `IndexError`

> **To'g'ri javob:** A
> **Tushuntirish:** `r[-3:-1]` → `-3` dan `-1` gacha (kirmaydi): `[30, 40]`. `r[-4:]` → `-4` dan oxirigacha: `[20, 30, 40, 50]`.

---

## Savol 9

Slicingda qadam (step) parametri qanday ishlatiladi?

- [A] `list[bosh:oxir, qadam]`
- [B] `list[bosh:oxir:qadam]`
- [C] `list[bosh, oxir, qadam]`
- [D] `list.step(bosh, oxir, qadam)`

> **To'g'ri javob:** B
> **Tushuntirish:** `list[bosh:oxir:qadam]` — `qadam` orqali necha tashlab olishni belgilaydi. `[::2]` — har ikkinchi element, `[::-1]` — teskari tartib.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(r[::2])
print(r[1::2])
print(r[::-1])
```

- [A] `[0,2,4,6,8]`, `[1,3,5,7,9]`, `[9,8,7,6,5,4,3,2,1,0]`
- [B] `[0,2,4,6,8,10]`, `[1,3,5,7,9]`, `[9,8,7,6,5,4,3,2,1]`
- [C] `[0,2,4,6,8]`, `[0,2,4,6,8]`, `[9,8,7,6,5,4,3,2,1,0]`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `r[::2]` → juft indekslar: `[0,2,4,6,8]`. `r[1::2]` → toq indekslar: `[1,3,5,7,9]`. `r[::-1]` → teskari: `[9,8,...,0]`.

---

## Savol 11

Ichma-ich (nested) listda elementga qanday murojaat qilinadi?

- [A] `r[i, j]`
- [B] `r[i][j]`
- [C] `r[i:j]`
- [D] `r.get(i, j)`

> **To'g'ri javob:** B
> **Tushuntirish:** `r[i][j]` — avval `i`-indeksdagi ichki listni oladi, keyin undan `j`-elementni. Masalan: `[[1,2],[3,4]][1][0]` → `3`.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
matritsa = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
print(matritsa[0][2])
print(matritsa[2][0])
print(matritsa[1][1])
```

- [A] `3`, `7`, `5`
- [B] `2`, `8`, `5`
- [C] `3`, `8`, `6`
- [D] `IndexError`

> **To'g'ri javob:** A
> **Tushuntirish:** `matritsa[0][2]` → 0-qator, 2-ustun: `3`. `matritsa[2][0]` → 2-qator, 0-ustun: `7`. `matritsa[1][1]` → 1-qator, 1-ustun: `5`.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
r[2] = 99
print(r)
```

- [A] `[1, 2, 3, 4, 5]`
- [B] `[1, 99, 3, 4, 5]`
- [C] `[1, 2, 99, 4, 5]`
- [D] `[99, 2, 3, 4, 5]`

> **To'g'ri javob:** C
> **Tushuntirish:** `r[2] = 99` — 2-indeksdagi elementni `99` bilan almashtiradi. `[1, 2, 99, 4, 5]`.

---

## Savol 14

Slicing orqali bir nechta elementni o'zgartirish mumkinmi?

- [A] Yo'q, faqat bitta elementni o'zgartirish mumkin
- [B] Ha, `r[bosh:oxir] = yangi_list` orqali bir nechta elementni almashtirish mumkin
- [C] Faqat `replace()` metodi bilan
- [D] Faqat `insert()` metodi bilan

> **To'g'ri javob:** B
> **Tushuntirish:** `r[1:3] = [10, 20]` — 1 va 2-indeksdagi elementlarni `10` va `20` bilan almashtiradi. Yangi list uzunligi farqli bo'lishi ham mumkin.

---

## Savol 15

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
r[1:4] = [20, 30]
print(r)
```

- [A] `[1, 20, 30, 4, 5]`
- [B] `[1, 20, 30, 5]`
- [C] `[20, 30, 3, 4, 5]`
- [D] `IndexError`

> **To'g'ri javob:** B
> **Tushuntirish:** `r[1:4]` — 1, 2, 3-indeksdagi `[2, 3, 4]` → `[20, 30]` bilan almashtiriladi (3 element o'rniga 2 element). Natija: `[1, 20, 30, 5]`.

---

## Savol 16

Quyidagi kodning natijasi nima?

```python
r = ["a", "b", "c", "d", "e"]
print(r[1:4:2])
```

- [A] `["b", "c", "d"]`
- [B] `["b", "d"]`
- [C] `["a", "c", "e"]`
- [D] `["b", "c"]`

> **To'g'ri javob:** B
> **Tushuntirish:** `r[1:4:2]` — 1-indeksdan 3-indeksgacha, 2 qadam bilan: indeks `1` (`"b"`) va indeks `3` (`"d"`). Natija: `["b", "d"]`.

---

## Savol 17

Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40, 50]
a = r[1]
b = r[-2]
c = r[len(r) - 1]
print(a, b, c)
```

- [A] `20`, `30`, `50`
- [B] `20`, `40`, `50`
- [C] `10`, `40`, `40`
- [D] `20`, `40`, `40`

> **To'g'ri javob:** B
> **Tushuntirish:** `r[1]` → `20`. `r[-2]` → oxiridan ikkinchi: `40`. `r[len(r)-1]` → `r[4]` → oxirgi: `50`.

---

## Savol 18

`for` tsikli va `enumerate()` bilan listga murojaat qanday farq qiladi?

- [A] Hech qanday farq yo'q
- [B] `for x in r` — faqat qiymatni beradi; `for i, x in enumerate(r)` — indeks va qiymatni birga beradi
- [C] `enumerate()` faqat raqamli listlarda ishlaydi
- [D] `for x in r` — indeksni, `enumerate()` — qiymatni beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `for x in r` — har bir elementni `x` ga beradi. `for i, x in enumerate(r)` — `i` indeks, `x` qiymat. Indeks kerak bo'lganda `enumerate()` qulayroq.

---

## Savol 19

Quyidagi kodning natijasi nima?

```python
r = [5, 10, 15, 20, 25]
for i, qiymat in enumerate(r):
    if qiymat > 12:
        print(i, qiymat)
        break
```

- [A] `1 10`
- [B] `2 15`
- [C] `3 20`
- [D] `0 5`

> **To'g'ri javob:** B
> **Tushuntirish:** `5 > 12` → yo'q. `10 > 12` → yo'q. `15 > 12` → ha → `i=2, qiymat=15`. `break` → to'xtaydi. Natija: `2 15`.

---

## Savol 20

Quyidagi kodning natijasi nima?

```python
r = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
natija = []
for qator in r:
    natija.append(qator[0])
print(natija)
```

- [A] `[1, 2, 3]`
- [B] `[3, 6, 9]`
- [C] `[1, 4, 7]`
- [D] `[[1], [4], [7]]`

> **To'g'ri javob:** C
> **Tushuntirish:** Har bir qatorning `[0]`-elementi: `[1,2,3][0]=1`, `[4,5,6][0]=4`, `[7,8,9][0]=7`. Natija: `[1, 4, 7]` — matritsa birinchi ustuni.

---

## Savol 21

Quyidagi kodning natijasi nima?

```python
r = [3, 1, 4, 1, 5, 9, 2, 6]
print(r[2:5])
print(r[-4:-1])
print(r[::3])
```

- [A] `[4,1,5]`, `[5,9,2]`, `[3,1,2]`
- [B] `[4,1,5]`, `[5,9,2]`, `[3,1,9]`
- [C] `[1,4,1]`, `[9,2,6]`, `[3,9,6]`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `r[2:5]` → `[4,1,5]`. `r[-4:-1]` → indeks 4 dan 6 gacha: `[5,9,2]`. `r[::3]` → 0, 3, 6-indekslar: `r[0]=3, r[3]=1, r[6]=2` → `[3,1,2]`.

---

## Savol 22

Quyidagi kodning natijasi nima?

```python
r = list(range(10))
r[::2] = [0] * 5
print(r)
```

- [A] `[0, 1, 0, 3, 0, 5, 0, 7, 0, 9]`
- [B] `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- [C] `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- [D] `ValueError`

> **To'g'ri javob:** A
> **Tushuntirish:** `r[::2]` — juft indekslar (0,2,4,6,8) — 5 ta element. `= [0]*5` → ularni `0` bilan almashtiradi. Toq indekslar o'zgarmaydi. Natija: `[0,1,0,3,0,5,0,7,0,9]`.

---

## Savol 23

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
print(r[10:20])
print(r[-10:-6])
```

- [A] `IndexError`, `IndexError`
- [B] `[]`, `[]`
- [C] `[1,2,3,4,5]`, `[]`
- [D] `None`, `None`

> **To'g'ri javob:** B
> **Tushuntirish:** Slicingda chegaradan tashqari indekslar xato bermaydi — bo'sh list qaytaradi. `r[10:20]` → `[]`. `r[-10:-6]` → -10 dan -6 gacha: 5 elementli listda bu diapazon bo'sh → `[]`.

---

## Savol 24

Quyidagi kodning natijasi nima?

```python
r = ["olma", "banan", "gilos", "nok", "anor"]
oxirgi_uch = r[-3:]
birinchi_ikki = r[:2]
print(oxirgi_uch)
print(birinchi_ikki)
print(oxirgi_uch[0])
```

- [A] `["gilos","nok","anor"]`, `["olma","banan"]`, `"gilos"`
- [B] `["nok","anor"]`, `["olma","banan","gilos"]`, `"nok"`
- [C] `["gilos","nok"]`, `["olma","banan"]`, `"gilos"`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `r[-3:]` → oxirgi 3 ta: `["gilos","nok","anor"]`. `r[:2]` → birinchi 2 ta: `["olma","banan"]`. `oxirgi_uch[0]` → `"gilos"`.

---

## Savol 25

Quyidagi to'liq kodning natijasi nima?

```python
r = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

a = r[2]
b = r[-3]
c = r[1:6:2]
d = r[::-2]

print(a)
print(b)
print(c)
print(d)
```

- [A] `6`, `16`, `[4,8,12]`, `[20,16,12,8,4]`
- [B] `6`, `18`, `[4,8,12]`, `[20,16,12,8,4]`
- [C] `6`, `16`, `[4,8,12]`, `[18,14,10,6,2]`
- [D] `4`, `16`, `[4,8,12]`, `[20,16,12,8,4]`

> **To'g'ri javob:** A
> **Tushuntirish:** `r[2]` → `6`. `r[-3]` → oxiridan 3-chi: `16` (indeks 7). `r[1:6:2]` → indeks 1,3,5: `4,8,12`. `r[::-2]` → oxiridan 2 qadam: `20,16,12,8,4`. Natija: `[20,16,12,8,4]`.

---