## Savol 1

`len()` funksiyasi listda nima qaytaradi?

- [A] Listdagi eng katta elementni
- [B] Listdagi elementlarning umumiy sonini
- [C] Listning oxirgi elementining indeksini
- [D] Listdagi noyob elementlar sonini

> **To'g'ri javob:** B
> **Tushuntirish:** `len(list)` — listdagi elementlarning umumiy sonini qaytaradi. Ichki (nested) listlar bitta element hisoblanadi. Masalan: `len([1, [2, 3], 4])` → `3`.

---

## Savol 2

Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40, 50]
print(len(r))
print(len(r) - 1)
print(r[len(r) - 1])
```

- [A] `5`, `4`, `50`
- [B] `5`, `4`, `40`
- [C] `4`, `3`, `50`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `len(r)` → `5`. `len(r)-1` → `4`. `r[len(r)-1]` → `r[4]` → oxirgi element: `50`.

---

## Savol 3

Quyidagi kodning natijasi nima?

```python
r = [[1, 2, 3], [4, 5], [6]]
print(len(r))
print(len(r[0]))
print(len(r[2]))
```

- [A] `6`, `3`, `1`
- [B] `3`, `3`, `1`
- [C] `3`, `2`, `1`
- [D] `6`, `2`, `1`

> **To'g'ri javob:** B
> **Tushuntirish:** `len(r)` → 3 ta ichki list → `3`. `len(r[0])` → `[1,2,3]` ning uzunligi → `3`. `len(r[2])` → `[6]` ning uzunligi → `1`.

---

## Savol 4

`len()` funksiyasi bo'sh listda nima qaytaradi?

- [A] `None`
- [B] `ValueError` beradi
- [C] `0`
- [D] `-1`

> **To'g'ri javob:** C
> **Tushuntirish:** Bo'sh list `[]` uchun `len([])` → `0`. Bu listning bo'sh-bo'lmasligini tekshirishda ishlatiladi: `if len(r) == 0:` yoki qisqacha `if not r:`.

---

## Savol 5

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
o'rta_indeks = len(r) // 2
print(o'rta_indeks)
print(r[o'rta_indeks])
```

- [A] `5`, `5`
- [B] `5`, `6`
- [C] `4`, `5`
- [D] `10`, `10`

> **To'g'ri javob:** B
> **Tushuntirish:** `len(r)//2` → `10//2 = 5`. `r[5]` → `6`.

---

## Savol 6

`in` operatori listda nima tekshiradi?

- [A] Element listning necha marta uchraganini
- [B] Element listda mavjud yoki yo'qligini — `True` yoki `False` qaytaradi
- [C] Elementning indeksini
- [D] Faqat raqamli elementlar uchun ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `x in list` — `x` listda bo'lsa `True`, bo'lmasa `False`. `x not in list` — teskarisi. `in` operatori faqat birinchi darajali elementlarni tekshiradi.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
print(3 in r)
print(6 in r)
print(6 not in r)
print(0 not in r)
```

- [A] `True`, `False`, `True`, `True`
- [B] `True`, `False`, `False`, `True`
- [C] `True`, `True`, `False`, `False`
- [D] `False`, `True`, `True`, `False`

> **To'g'ri javob:** A
> **Tushuntirish:** `3 in r` → `True`. `6 in r` → `False`. `6 not in r` → `True`. `0 not in r` → `0` listda yo'q → `True`.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
r = [[1, 2], [3, 4], [5, 6]]
print([1, 2] in r)
print(1 in r)
```

- [A] `True`, `True`
- [B] `False`, `True`
- [C] `True`, `False`
- [D] `False`, `False`

> **To'g'ri javob:** C
> **Tushuntirish:** `in` faqat birinchi darajali elementlarni tekshiradi. `[1,2] in r` → `[1,2]` listda bor → `True`. `1 in r` → `1` emas, `[1,2]` bor → `False`.

---

## Savol 9

`in` operatori `if` shart bilan qanday ishlatiladi?

```python
ruxsat_etilgan = ["admin", "moderator", "editor"]
foydalanuvchi = "moderator"

if foydalanuvchi in ruxsat_etilgan:
    print("Kirish ruxsat etildi")
else:
    print("Kirish taqiqlandi")
```

- [A] `Kirish taqiqlandi`
- [B] `Kirish ruxsat etildi`
- [C] Xato beradi
- [D] Hech narsa chiqmaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `"moderator" in ruxsat_etilgan` → `True` → `if` bloki ishlaydi → `"Kirish ruxsat etildi"`.

---

## Savol 10

`for` tsikli bilan list elementlari qanday o'tiladi?

- [A] `for i in range(list):`
- [B] `for element in list:`
- [C] `for list.element:`
- [D] `foreach element in list:`

> **To'g'ri javob:** B
> **Tushuntirish:** `for element in list:` — listning har bir elementini ketma-ket `element` o'zgaruvchisiga beradi. Bu eng Pythonic va qulay usul.

---

## Savol 11

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
jami = 0
for x in r:
    jami += x
print(jami)
```

- [A] `12345`
- [B] `15`
- [C] `5`
- [D] `[1, 2, 3, 4, 5]`

> **To'g'ri javob:** B
> **Tushuntirish:** `for` har bir elementni `jami` ga qo'shadi: `0+1+2+3+4+5 = 15`. Xuddi shu natijani `sum(r)` ham beradi.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
mevalar = ["olma", "banan", "gilos"]
for i in range(len(mevalar)):
    print(i, mevalar[i])
```

- [A] `0 olma`, `1 banan`, `2 gilos`
- [B] `1 olma`, `2 banan`, `3 gilos`
- [C] `olma`, `banan`, `gilos`
- [D] `0`, `1`, `2`

> **To'g'ri javob:** A
> **Tushuntirish:** `range(len(mevalar))` → `range(3)` → `0,1,2`. Har iteratsiyada indeks va element chiqariladi. `0 olma`, `1 banan`, `2 gilos`.

---

## Savol 13

`enumerate()` funksiyasi `for` tsikli bilan qanday ishlaydi?

- [A] Faqat indekslarni qaytaradi
- [B] `(indeks, element)` juftliklarini qaytaradi — indeks va qiymatni birgalikda olish imkonini beradi
- [C] Listni tartiblaydi
- [D] Faqat raqamli listlarda ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `for i, x in enumerate(list):` — `i` indeks, `x` qiymat. `enumerate(list, start=1)` — indekslash 1 dan boshlanadi. `range(len(list))` ga qaraganda Pythonic usul.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
r = ["a", "b", "c", "d"]
for i, harf in enumerate(r, start=1):
    print(f"{i}. {harf}")
```

- [A] `0. a`, `1. b`, `2. c`, `3. d`
- [B] `1. a`, `2. b`, `3. c`, `4. d`
- [C] `a. 1`, `b. 2`, `c. 3`, `d. 4`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `enumerate(r, start=1)` — indekslash `1` dan boshlanadi: `(1,"a"), (2,"b"), (3,"c"), (4,"d")`. Natija: `1. a`, `2. b`, `3. c`, `4. d`.

---

## Savol 15

Quyidagi kodning natijasi nima?

```python
sonlar = [3, 7, 2, 8, 1, 9, 4]
eng_katta = sonlar[0]
for son in sonlar:
    if son > eng_katta:
        eng_katta = son
print(eng_katta)
```

- [A] `3`
- [B] `4`
- [C] `9`
- [D] `1`

> **To'g'ri javob:** C
> **Tushuntirish:** Har bir elementni `eng_katta` bilan solishtiriladi. Ketma-ket: `3→7→7→8→8→9→9`. Oxirida `eng_katta = 9`. Xuddi shu natijani `max(sonlar)` beradi.

---

## Savol 16

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hisoblagich = 0
for x in r:
    if x % 2 == 0:
        hisoblagich += 1
print(hisoblagich)
```

- [A] `5`
- [B] `10`
- [C] `25`
- [D] `30`

> **To'g'ri javob:** A
> **Tushuntirish:** `x % 2 == 0` — juft sonlar: `2, 4, 6, 8, 10` → 5 ta. `hisoblagich = 5`.

---

## Savol 17

`for` tsiklida `break` qanday ishlaydi?

- [A] Joriy iteratsiyani o'tkazib yuboradi
- [B] Tsiklni to'liq to'xtatadi
- [C] Listdan elementni o'chiradi
- [D] Tsiklni boshiga qaytaradi

> **To'g'ri javob:** B
> **Tushuntirish:** `break` — tsiklni darhol to'xtatadi va tsikldan keyingi kodga o'tadi. `continue` esa faqat joriy iteratsiyani o'tkazib, tsikl davom etadi.

---

## Savol 18

Quyidagi kodning natijasi nima?

```python
r = [4, 7, 2, 9, 1, 5, 8]
topildi = False
for i, x in enumerate(r):
    if x > 8:
        print(f"Topildi: {x}, indeks: {i}")
        topildi = True
        break
if not topildi:
    print("Topilmadi")
```

- [A] `Topildi: 9, indeks: 3`
- [B] `Topildi: 8, indeks: 6`
- [C] `Topilmadi`
- [D] `Topildi: 9, indeks: 4`

> **To'g'ri javob:** A
> **Tushuntirish:** `4>8` → yo'q. `7>8` → yo'q. `2>8` → yo'q. `9>8` → ha → `indeks=3`, `x=9` → chiqaradi va `break`.

---

## Savol 19

`for` tsiklida `continue` qanday ishlaydi?

- [A] Tsiklni to'xtatadi
- [B] Joriy iteratsiyaning qolgan qismini o'tkazib yuboradi, keyingi elementga o'tadi
- [C] Listni tozalaydi
- [D] Tsikl boshiga qaytaradi va elementni qayta ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `continue` — joriy iteratsiyani tugatib, keyingi elementga o'tadi. Masalan, manfiy sonlarni o'tkazib, faqat musbatlarni chiqarish uchun ishlatiladi.

---

## Savol 20

Quyidagi kodning natijasi nima?

```python
r = [1, -2, 3, -4, 5, -6]
musbat_jami = 0
for x in r:
    if x < 0:
        continue
    musbat_jami += x
print(musbat_jami)
```

- [A] `-3`
- [B] `3`
- [C] `9`
- [D] `-12`

> **To'g'ri javob:** C
> **Tushuntirish:** Manfiy sonlarda `continue` — o'tkazib yuboriladi. Musbatlar qo'shiladi: `1 + 3 + 5 = 9`.

---

## Savol 21

Ichma-ich `for` tsikli (nested loop) listda qanday ishlaydi?

```python
matritsa = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
jami = 0
for qator in matritsa:
    for element in qator:
        jami += element
print(jami)
```

- [A] `15`
- [B] `45`
- [C] `[1,2,3,4,5,6,7,8,9]`
- [D] `9`

> **To'g'ri javob:** B
> **Tushuntirish:** Tashqi tsikl har bir qatorni, ichki tsikl qatordagi har bir elementni o'tadi. `1+2+3+4+5+6+7+8+9 = 45`.

---

## Savol 22

Quyidagi kodning natijasi nima?

```python
r = ["olma", "banan", "gilos", "nok", "anor"]
uzun_so_zlar = []
for meva in r:
    if len(meva) >= 5:
        uzun_so_zlar.append(meva)
print(uzun_so_zlar)
print(len(uzun_so_zlar))
```

- [A] `["banan","gilos","anor"]`, `3`
- [B] `["banan","gilos"]`, `2`
- [C] `["olma","nok"]`, `2`
- [D] `["banan","gilos","anor"]`, `4`

> **To'g'ri javob:** A
> **Tushuntirish:** Uzunliklari: `olma`=4✗, `banan`=5✓, `gilos`=5✓, `nok`=3✗, `anor`=4... `anor` = 4✗... Aslida `anor` 4 ta harf, lekin `anor` → a,n,o,r = 4. `banan`=5✓, `gilos`=5✓. Natija: `["banan","gilos"]`, `2`.

> **To'g'ri javob (to'g'irlangan):** B — `["banan", "gilos"]`, `2`

---

## Savol 23

Quyidagi kodning natijasi nima?

```python
r = [2, 4, 6, 8, 10]
for i in range(len(r)):
    r[i] = r[i] ** 2
print(r)
```

- [A] `[2, 4, 6, 8, 10]`
- [B] `[4, 8, 12, 16, 20]`
- [C] `[4, 16, 36, 64, 100]`
- [D] Xato beradi

> **To'g'ri javob:** C
> **Tushuntirish:** `range(len(r))` — indeks orqali o'tiladi va har element o'zining kvadratiga almashtiriladi: `2²=4, 4²=16, 6²=36, 8²=64, 10²=100`.

---

## Savol 24

`len()`, `in` va `for` ni birgalikda qanday ishlatish mumkin?

```python
r = [1, 3, 5, 7, 9]
natija = []
for i in range(len(r)):
    if r[i] in r[i+1:]:
        natija.append(r[i])
print(natija)
```

- [A] `[1, 3, 5, 7, 9]`
- [B] `[]`
- [C] `[9]`
- [D] `IndexError`

> **To'g'ri javob:** B
> **Tushuntirish:** Har bir element o'zidan keyingisida qidiradi. Listda takrorlanuvchi element yo'q → hech biri topilmaydi → `natija = []`.

---

## Savol 25

Quyidagi kodning natijasi nima?

```python
so'zlar = ["python", "java", "c", "javascript", "go"]
for so'z in so'zlar:
    if len(so'z) > 4:
        print(so'z.upper())
```

- [A] `PYTHON`, `JAVASCRIPT`
- [B] `PYTHON`, `JAVA`, `JAVASCRIPT`
- [C] `JAVA`, `JAVASCRIPT`
- [D] `PYTHON`, `JAVA`, `C`, `JAVASCRIPT`, `GO`

> **To'g'ri javob:** B
> **Tushuntirish:** `python`=6>4✓, `java`=4 — 4>4 yo'q✗, `c`=1✗, `javascript`=10>4✓, `go`=2✗. Faqat `python` va `javascript` chiqadi → `PYTHON`, `JAVASCRIPT`.

> **To'g'ri javob (to'g'irlangan):** A — `PYTHON`, `JAVASCRIPT`

---

## Savol 26

Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40, 50]
print(len(r))

kamaytir = []
for x in r:
    if x not in kamaytir:
        kamaytir.append(x * 2)

print(len(kamaytir))
print(20 in kamaytir)
```

- [A] `5`, `5`, `True`
- [B] `5`, `5`, `False`
- [C] `5`, `10`, `True`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `kamaytir` — har element 2 ga ko'paytiriladi: `[20,40,60,80,100]`. Barchasi noyob → `len = 5`. `20 in kamaytir` → `True`.

---

## Savol 27

Quyidagi kodning natijasi nima?

```python
juft = []
toq = []
r = list(range(1, 11))

for x in r:
    if x % 2 == 0:
        juft.append(x)
    else:
        toq.append(x)

print(len(juft), len(toq))
print(juft[-1] in toq)
```

- [A] `5 5`, `True`
- [B] `5 5`, `False`
- [C] `4 6`, `False`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `juft` → `[2,4,6,8,10]`, `toq` → `[1,3,5,7,9]`. `len` ikkalasi `5`. `juft[-1]` → `10`. `10 in toq` → yo'q → `False`.

---

## Savol 28

Quyidagi kodning natijasi nima?

```python
r = [5, 3, 8, 1, 9, 2, 7, 4, 6]
chegarа = 5
katta = [x for x in r if x > chegarа]
print(len(katta))
print(chegarа in katta)
print(max(katta))
```

- [A] `4`, `False`, `9`
- [B] `5`, `True`, `9`
- [C] `4`, `True`, `9`
- [D] `3`, `False`, `9`

> **To'g'ri javob:** A
> **Tushuntirish:** `x > 5`: `8✓, 9✓, 7✓, 6✓` → 4 ta. `chegarа=5`, `5 > 5` → yo'q → `5 in katta` → `False`. `max([8,9,7,6])` → `9`.

---

## Savol 29

Quyidagi kodning natijasi nima?

```python
r = ["a", "b", "c", "a", "d", "b", "a"]
takrorlar = {}
for element in r:
    if element in takrorlar:
        takrorlar[element] += 1
    else:
        takrorlar[element] = 1

eng_ko'p = max(takrorlar, key=takrorlar.get)
print(eng_ko'p, takrorlar[eng_ko'p])
```

- [A] `b 2`
- [B] `a 2`
- [C] `a 3`
- [D] Xato beradi

> **To'g'ri javob:** C
> **Tushuntirish:** `a` → 3 marta, `b` → 2 marta, `c` → 1, `d` → 1. `max(key=get)` → eng ko'p: `"a"`. `takrorlar["a"]` → `3`.

---

## Savol 30

Quyidagi to'liq kodning natijasi nima?

```python
r = [4, 7, 2, 9, 1, 5, 8, 3, 6, 10]

jami = 0
hisoblagich = 0
eng_katta = r[0]

for i, x in enumerate(r):
    if x % 2 != 0:
        jami += x
        hisoblagich += 1
        if x > eng_katta:
            eng_katta = x

print(hisoblagich)
print(jami)
print(eng_katta in r)
print(r.index(eng_katta))
```

- [A] `5`, `25`, `True`, `3`
- [B] `4`, `20`, `True`, `1`
- [C] `5`, `25`, `True`, `1`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** Toq sonlar: `7,9,1,5,3` → 5 ta. `jami = 7+9+1+5+3 = 25`. Ulardan eng kattasi: `9`. `eng_katta` `r[0]=4` dan boshlanadi, keyin `7→9`. `9 in r` → `True`. `r.index(9)` → indeks `3`.

---