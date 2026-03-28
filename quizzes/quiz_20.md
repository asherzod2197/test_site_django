## Savol 1

`append()` metodi qanday ishlaydi?

- [A] Listning boshiga bitta element qo'shadi
- [B] Listning oxiriga bitta element qo'shadi
- [C] Listga bir nechta element qo'shadi
- [D] Boshqa listni joriy listga birlashtiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `list.append(x)` — `x` elementini listning eng oxiriga qo'shadi. Faqat bitta argument qabul qiladi. Qaytarish qiymati `None`.

---

## Savol 2

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3]
r.append(4)
r.append([5, 6])
print(r)
print(len(r))
```

- [A] `[1, 2, 3, 4, 5, 6]`, `6`
- [B] `[1, 2, 3, 4, [5, 6]]`, `5`
- [C] `[1, 2, 3, 4, [5, 6]]`, `6`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `append(4)` → `[1,2,3,4]`. `append([5,6])` — `[5,6]` butun holda bitta element sifatida qo'shiladi → `[1,2,3,4,[5,6]]`. `len()` → `5`.

---

## Savol 3

`extend()` metodi `append()` dan qanday farq qiladi?

- [A] Hech qanday farq yo'q
- [B] `extend(iterable)` — iterablening har bir elementini alohida qo'shadi; `append` esa butun obyektni bitta element sifatida qo'shadi
- [C] `extend()` yangi list qaytaradi
- [D] `extend()` faqat raqamli listlarda ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `append([1,2])` → `[..., [1,2]]` (bitta element). `extend([1,2])` → `[..., 1, 2]` (ikkita alohida element). `extend()` istalgan iterableni qabul qiladi.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
print(b)
```

- [A] `[1,2,3,[4,5,6]]`, `[4,5,6]`
- [B] `[1,2,3,4,5,6]`, `[]`
- [C] `[1,2,3,4,5,6]`, `[4,5,6]`
- [D] Xato beradi

> **To'g'ri javob:** C
> **Tushuntirish:** `extend(b)` — `b` ning elementlari `a` ga bitta-bitta qo'shiladi. `a` → `[1,2,3,4,5,6]`. `b` o'zgarmaydi → `[4,5,6]`.

---

## Savol 5

`insert()` metodi qanday ishlaydi?

- [A] `insert(element)` — oxiriga qo'shadi
- [B] `insert(indeks, element)` — ko'rsatilgan indeksga element kiritadi, qolganlar o'ngga suriladi
- [C] `insert(element, indeks)` — elementni indeks bilan almashtiradi
- [D] Faqat bo'sh listlarda ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `list.insert(i, x)` — `i` indeksga `x` ni joylashtiradi. `i` listdan katta bo'lsa oxiriga, manfiy bo'lsa boshiga qo'shadi. Hech narsa qaytarmaydi (`None`).

---

## Savol 6

Quyidagi kodning natijasi nima?

```python
r = [10, 20, 40, 50]
r.insert(2, 30)
print(r)
r.insert(0, 0)
print(r)
```

- [A] `[10,20,30,40,50]`, `[0,10,20,30,40,50]`
- [B] `[10,30,20,40,50]`, `[0,10,30,20,40,50]`
- [C] `[10,20,40,30,50]`, `[0,10,20,40,30,50]`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `insert(2, 30)` → 2-indeksga `30` → `[10,20,30,40,50]`. `insert(0, 0)` → boshiga `0` → `[0,10,20,30,40,50]`.

---

## Savol 7

`remove()` metodi qanday ishlaydi?

- [A] Indeks bo'yicha elementni o'chiradi
- [B] Berilgan qiymatga teng birinchi elementni o'chiradi
- [C] Barcha mos keluvchi elementlarni o'chiradi
- [D] Oxirgi elementni o'chiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `list.remove(x)` — `x` qiymatiga teng birinchi elementni topib o'chiradi. Element topilmasa `ValueError`. Faqat birinchi uchraganini o'chiradi.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
r = [1, 3, 5, 3, 7, 3]
r.remove(3)
print(r)
r.remove(3)
print(r)
```

- [A] `[1,5,7]`, `[1,5,7]`
- [B] `[1,5,3,7,3]`, `[1,5,7,3]`
- [C] `[1,5,3,7,3]`, `[1,5,3,7]`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** Birinchi `remove(3)` — 1-indeksdagi `3` ni o'chiradi → `[1,5,3,7,3]`. Ikkinchi `remove(3)` — yana birinchi `3` ni o'chiradi → `[1,5,7,3]`.

---

## Savol 9

`pop()` metodi qanday ishlaydi?

- [A] Elementni o'chiradi, lekin qaytarmaydi
- [B] Ko'rsatilgan indeksdagi (yoki oxirgi) elementni o'chirib, uni qaytaradi
- [C] Faqat oxirgi elementni o'chiradi
- [D] Barcha elementlarni o'chiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `list.pop(i)` — `i` indeksdagi elementni o'chirib qaytaradi. `pop()` (indekssiz) — oxirgi elementni o'chirib qaytaradi. Indeks noto'g'ri bo'lsa `IndexError`.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40, 50]
a = r.pop()
b = r.pop(1)
print(a, b)
print(r)
```

- [A] `50`, `20`, `[10, 30, 40]`
- [B] `50`, `30`, `[10, 20, 40]`
- [C] `10`, `20`, `[30, 40, 50]`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `pop()` → oxirgi: `50`. `r` → `[10,20,30,40]`. `pop(1)` → 1-indeks: `20`. `r` → `[10,30,40]`. Natija: `a=50`, `b=20`.

---

## Savol 11

`clear()` metodi nima qiladi?

- [A] Listni o'chirib, xotirani bo'shatadi
- [B] Listning barcha elementlarini o'chirib, bo'sh list qoldiradi
- [C] Faqat birinchi elementni o'chiradi
- [D] Listni boshlang'ich holatga qaytaradi

> **To'g'ri javob:** B
> **Tushuntirish:** `list.clear()` — listning barcha elementlarini o'chiradi, lekin list obyekti saqlanib qoladi (`[]`). `del list` esa o'zgaruvchini to'liq o'chiradi.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
r.clear()
print(r)
print(type(r))
print(len(r))
```

- [A] `None`, `<class 'NoneType'>`, `0`
- [B] `[]`, `<class 'list'>`, `0`
- [C] Xato beradi
- [D] `[1,2,3,4,5]`, `<class 'list'>`, `5`

> **To'g'ri javob:** B
> **Tushuntirish:** `clear()` elementlarni o'chiradi, list obyekti qoladi. `r` → `[]`. `type(r)` → `<class 'list'>`. `len(r)` → `0`.

---

## Savol 13

`index()` metodi nima qaytaradi?

- [A] Elementning necha marta uchraganini
- [B] Berilgan qiymatning birinchi uchraydigan indeksini
- [C] Oxirgi uchraydigan indeksini
- [D] Barcha indekslar ro'yxatini

> **To'g'ri javob:** B
> **Tushuntirish:** `list.index(x)` — `x` qiymatining birinchi uchraydigan indeksini qaytaradi. `list.index(x, bosh, oxir)` — qidiruv diapazonini cheklash mumkin. Element yo'q bo'lsa `ValueError`.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
r = [5, 10, 15, 10, 20, 10]
print(r.index(10))
print(r.index(10, 2))
print(r.index(10, 4, 6))
```

- [A] `1`, `3`, `5`
- [B] `1`, `2`, `5`
- [C] `0`, `3`, `5`
- [D] `1`, `3`, `ValueError`

> **To'g'ri javob:** A
> **Tushuntirish:** `index(10)` → birinchi `10`: indeks `1`. `index(10, 2)` → 2-indeksdan qidirish: `3`. `index(10, 4, 6)` → 4 dan 5 gacha: indeks `5`. Natija: `1`, `3`, `5`.

---

## Savol 15

`count()` metodi nima qaytaradi?

- [A] Listdagi elementlar umumiy sonini
- [B] Berilgan qiymat listda necha marta uchraganini
- [C] Listdagi noyob elementlar sonini
- [D] Listdagi maksimal qiymatni

> **To'g'ri javob:** B
> **Tushuntirish:** `list.count(x)` — `x` qiymati listda necha marta uchraganini qaytaradi. Element yo'q bo'lsa `0` qaytaradi (xato bermaydi).

---

## Savol 16

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 2, 1, 2, 4, 2]
print(r.count(2))
print(r.count(5))
print(r.count(1))
```

- [A] `4`, `0`, `2`
- [B] `3`, `0`, `2`
- [C] `4`, `ValueError`, `2`
- [D] `4`, `0`, `1`

> **To'g'ri javob:** A
> **Tushuntirish:** `count(2)` → `2` qiymati: 4 marta (indeks 1,3,5,7). `count(5)` → `5` yo'q → `0`. `count(1)` → 2 marta (indeks 0,4).

---

## Savol 17

`sort()` metodi qanday ishlaydi?

- [A] Yangi tartiblangan list qaytaradi
- [B] Listni o'zini o'sish tartibida tartiblaydi, `None` qaytaradi
- [C] Listni nusxalab, tartiblangan nusxani qaytaradi
- [D] Faqat raqamli listlarni tartiblaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `list.sort()` — listni bevosita (in-place) o'zgartiradi, `None` qaytaradi. `key` va `reverse` parametrlarini qabul qiladi. `sorted()` esa yangi list qaytaradi.

---

## Savol 18

Quyidagi kodning natijasi nima?

```python
r = [3, 1, 4, 1, 5, 9, 2, 6]
natija = r.sort()
print(r)
print(natija)
```

- [A] `[3,1,4,1,5,9,2,6]`, `[1,1,2,3,4,5,6,9]`
- [B] `[1,1,2,3,4,5,6,9]`, `None`
- [C] `[1,1,2,3,4,5,6,9]`, `[1,1,2,3,4,5,6,9]`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `sort()` listni o'zini o'zgartiradi, `None` qaytaradi. `r` → `[1,1,2,3,4,5,6,9]`. `natija = r.sort()` → `natija = None`.

---

## Savol 19

`sort()` metodida `key` parametri qanday ishlatiladi?

- [A] Tartiblash tartibini o'zgartiradi
- [B] Har bir elementga qo'llaniladigan funksiyani belgilaydi — funksiya natijasi bo'yicha tartiblanadi
- [C] Faqat `reverse=True` bilan birgalikda ishlaydi
- [D] Tartiblash boshlanadigan indeksni belgilaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `sort(key=funksiya)` — har bir element `funksiya` ga beriladi va qaytarilgan qiymat bo'yicha tartiblanadi. Masalan: `sort(key=len)` — uzunlik bo'yicha, `sort(key=str.lower)` — kichik harfga o'girib tartiblaydi.

---

## Savol 20

Quyidagi kodning natijasi nima?

```python
so_zlar = ["banan", "olma", "o'rik", "gilos", "nok"]
so_zlar.sort(key=len)
print(so_zlar)
so_zlar.sort(key=len, reverse=True)
print(so_zlar)
```

- [A] `["nok","olma","banan","gilos","o'rik"]`, `["banan","gilos","o'rik","olma","nok"]`
- [B] `["nok","olma","banan","gilos","o'rik"]`, `["o'rik","gilos","banan","olma","nok"]`
- [C] `["olma","nok","banan","gilos","o'rik"]`, `["banan","gilos","o'rik","olma","nok"]`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** Uzunliklari: `banan`=5, `olma`=4, `o'rik`=5, `gilos`=5, `nok`=3. `sort(key=len)` → `["nok","olma","banan","gilos","o'rik"]`. `reverse=True` → uzundan qisqaga: `["banan","gilos","o'rik","olma","nok"]`.

---

## Savol 21

`reverse()` metodi qanday ishlaydi?

- [A] Tartiblangan listni qaytaradi
- [B] Listni teskari tartibda yangi list qaytaradi
- [C] Listni o'zini teskari tartibga o'tkazadi, `None` qaytaradi
- [D] Faqat tartiblangan listlarda ishlaydi

> **To'g'ri javob:** C
> **Tushuntirish:** `list.reverse()` — listni o'zini in-place teskari tartibga o'tkazadi, `None` qaytaradi. `list[::-1]` esa yangi teskari list qaytaradi.

---

## Savol 22

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
r.reverse()
print(r)
natija = r.reverse()
print(r)
print(natija)
```

- [A] `[5,4,3,2,1]`, `[1,2,3,4,5]`, `None`
- [B] `[5,4,3,2,1]`, `[5,4,3,2,1]`, `None`
- [C] `[5,4,3,2,1]`, `[1,2,3,4,5]`, `[1,2,3,4,5]`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `r.reverse()` → `[5,4,3,2,1]`. `natija = r.reverse()` → yana teskariga: `[1,2,3,4,5]`. `natija` → `None` (reverse qaytarmaydi).

---

## Savol 23

`copy()` metodi qanday nusxa yaratadi?

- [A] Chuqur nusxa (deep copy)
- [B] Sirtqi nusxa (shallow copy) — ichki listlar baham ko'riladi
- [C] Reference (havola) qaytaradi
- [D] `deepcopy()` bilan bir xil ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `list.copy()` — sirtqi (shallow) nusxa. Oddiy elementlar mustaqil, ichki (nested) listlar hali baham ko'riladi. Chuqur nusxa uchun `copy.deepcopy()` kerak.

---

## Savol 24

Quyidagi kodning natijasi nima?

```python
asl = [1, 2, 3]
nusxa = asl.copy()
nusxa.append(99)
asl[0] = 100
print(asl)
print(nusxa)
```

- [A] `[100, 2, 3, 99]`, `[100, 2, 3, 99]`
- [B] `[100, 2, 3]`, `[1, 2, 3, 99]`
- [C] `[1, 2, 3]`, `[1, 2, 3, 99]`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `nusxa = asl.copy()` — mustaqil nusxa. `nusxa.append(99)` faqat nusxaga ta'sir qiladi. `asl[0] = 100` faqat asliga. `asl` → `[100,2,3]`, `nusxa` → `[1,2,3,99]`.

---

## Savol 25

`index()` va `count()` metodlarini birgalikda qo'llash qanday natija beradi?

```python
r = [4, 7, 2, 7, 9, 7, 1]
x = 7
print(r.count(x))
print(r.index(x))
```

- [A] `2`, `1`
- [B] `3`, `1`
- [C] `3`, `0`
- [D] `2`, `3`

> **To'g'ri javob:** B
> **Tushuntirish:** `count(7)` → `7` uchta: indeks 1, 3, 5 → `3`. `index(7)` → birinchi `7` ning indeksi → `1`.

---

## Savol 26

Quyidagi kodning natijasi nima?

```python
r = [5, 3, 8, 1, 9, 2, 7]
r.sort()
print(r[0], r[-1])
r.reverse()
print(r[0], r[-1])
```

- [A] `1 9`, `9 1`
- [B] `5 7`, `9 1`
- [C] `1 9`, `7 5`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `sort()` → `[1,2,3,5,7,8,9]`. `r[0]=1`, `r[-1]=9`. `reverse()` → `[9,8,7,5,3,2,1]`. `r[0]=9`, `r[-1]=1`.

---

## Savol 27

`extend()` metodi qaysi turdagi argumentlarni qabul qiladi?

- [A] Faqat listlarni
- [B] Faqat raqamli qiymatlarni
- [C] Istalgan iterableni: list, tuple, string, range va boshqalar
- [D] Faqat bitta elementni

> **To'g'ri javob:** C
> **Tushuntirish:** `extend(iterable)` — istalgan iterable qabul qiladi. `extend("abc")` → `["a","b","c"]` qo'shadi. `extend((1,2))` → tuple dan qo'shadi. `extend(range(3))` → `[0,1,2]` qo'shadi.

---

## Savol 28

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3]
r.extend("xyz")
print(r)
r.extend(range(3))
print(r)
```

- [A] `[1,2,3,"xyz"]`, `[1,2,3,"xyz",range(3)]`
- [B] `[1,2,3,"x","y","z"]`, `[1,2,3,"x","y","z",0,1,2]`
- [C] Xato beradi
- [D] `[1,2,3,"xyz",0,1,2]`, xato

> **To'g'ri javob:** B
> **Tushuntirish:** `extend("xyz")` — stringdagi har bir harf alohida qo'shiladi: `"x","y","z"`. `extend(range(3))` → `0,1,2` qo'shiladi. Natija: `[1,2,3,"x","y","z",0,1,2]`.

---

## Savol 29

`remove()` metodi element topilmasa nima bo'ladi?

- [A] `None` qaytaradi
- [B] `False` qaytaradi
- [C] `ValueError` beradi
- [D] Listni o'zgartirmay qaytaradi

> **To'g'ri javob:** C
> **Tushuntirish:** `list.remove(x)` — `x` topilmasa `ValueError: list.remove(x): x not in list` xatosi chiqadi. Avval `in` operator bilan tekshirish yoki `try-except` ishlatish tavsiya etiladi.

---

## Savol 30

Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40]
try:
    r.remove(99)
except ValueError as e:
    print("Xato:", e)
print(r)
```

- [A] `Xato: list.remove(x): x not in list`, `[10, 20, 30, 40]`
- [B] `Xato: 99 topilmadi`, `[]`
- [C] `None`, `[10, 20, 30, 40]`
- [D] Dastur to'xtab qoladi

> **To'g'ri javob:** A
> **Tushuntirish:** `remove(99)` → `99` listda yo'q → `ValueError`. `except` bloki xabar chiqaradi. List o'zgarmaydi → `[10,20,30,40]`.

---

## Savol 31

`sort()` va `sorted()` o'rtasidagi asosiy farq nima?

- [A] `sort()` faqat raqamlar, `sorted()` matnlar uchun
- [B] `sort()` — in-place, `None` qaytaradi; `sorted()` — yangi tartiblangan list qaytaradi, asl o'zgarmaydi
- [C] `sorted()` tezroq ishlaydi
- [D] Hech qanday farq yo'q

> **To'g'ri javob:** B
> **Tushuntirish:** `r.sort()` — `r` ni o'zgartiradi, `None` qaytaradi. `sorted(r)` — `r` ni o'zgartirmaydi, yangi tartiblangan list qaytaradi. `sorted()` har qanday iterabledan ishlaydi.

---

## Savol 32

Quyidagi kodning natijasi nima?

```python
r = [3, 1, 4, 1, 5]
a = sorted(r)
b = sorted(r, reverse=True)
print(r)
print(a)
print(b)
```

- [A] `[1,1,3,4,5]`, `[1,1,3,4,5]`, `[5,4,3,1,1]`
- [B] `[3,1,4,1,5]`, `[1,1,3,4,5]`, `[5,4,3,1,1]`
- [C] `[3,1,4,1,5]`, `[5,4,3,1,1]`, `[1,1,3,4,5]`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `sorted()` asl listni o'zgartirmaydi. `r` → `[3,1,4,1,5]`. `a` → `[1,1,3,4,5]`. `b` → `[5,4,3,1,1]`.

---

## Savol 33

Quyidagi kodning natijasi nima?

```python
talabalar = [
    ("Ali", 85),
    ("Vali", 92),
    ("Gali", 78),
    ("Zulfiya", 95)
]
talabalar.sort(key=lambda x: x[1])
print(talabalar[0][0])
print(talabalar[-1][0])
```

- [A] `Ali`, `Zulfiya`
- [B] `Gali`, `Zulfiya`
- [C] `Zulfiya`, `Gali`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `key=lambda x: x[1]` — ball bo'yicha tartiblaydi: `78(Gali), 85(Ali), 92(Vali), 95(Zulfiya)`. `[0][0]` → eng kichik ball: `"Gali"`. `[-1][0]` → eng katta: `"Zulfiya"`.

---

## Savol 34

`append()`, `insert()`, `extend()` metodlaridan qaysi biri `None` qaytarmaydi?

- [A] `append()`
- [B] `insert()`
- [C] `extend()`
- [D] Uchkalasi ham `None` qaytaradi

> **To'g'ri javob:** D
> **Tushuntirish:** `append()`, `insert()`, `extend()` — barchasi listni o'zgartiradigan (mutating) metodlar va `None` qaytaradi. Bu Python'ning "in-place o'zgartiruvchi metodlar `None` qaytaradi" qoidasiga mos.

---

## Savol 35

Quyidagi kodda xato bormi?

```python
r = [1, 2, 3, 4, 5]
r2 = r.append(6).append(7)
print(r2)
```

- [A] Xato yo'q, `[1,2,3,4,5,6,7]` chiqadi
- [B] `AttributeError` — `append()` `None` qaytaradi, `None.append()` xato
- [C] `[6, 7]` chiqadi
- [D] `r2 = None` chiqadi

> **To'g'ri javob:** B
> **Tushuntirish:** `r.append(6)` → `None` qaytaradi. `None.append(7)` → `AttributeError: 'NoneType' object has no attribute 'append'`. Metodlarni zanjirlab chaqirib bo'lmaydi.

---

## Savol 36

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 2, 1]
while 2 in r:
    r.remove(2)
print(r)
```

- [A] `[1, 3, 1]`
- [B] `[1, 2, 3, 1]`
- [C] `[1, 1]`
- [D] Cheksiz tsikl

> **To'g'ri javob:** A
> **Tushuntirish:** `remove(2)` har safar birinchi `2` ni o'chiradi. Birinchi: `[1,3,2,1]`. Ikkinchi: `[1,3,1]`. `while` tekshiradi: `2` yo'q → to'xtaydi. Natija: `[1,3,1]`.

---

## Savol 37

Quyidagi kodning natijasi nima?

```python
r = [5, 2, 8, 1, 9, 3, 7]
r.sort()
o'rta = r[len(r) // 2]
print(o'rta)
```

- [A] `5`
- [B] `3`
- [C] `8`
- [D] `1`

> **To'g'ri javob:** A
> **Tushuntirish:** `sort()` → `[1,2,3,5,7,8,9]`. `len(r)//2` → `7//2 = 3`. `r[3]` → `5` (o'rta element).

---

## Savol 38

Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40, 50]
r.insert(len(r), 60)
r.insert(-1, 45)
print(r)
```

- [A] `[10,20,30,40,50,60,45]`
- [B] `[10,20,30,40,45,50,60]`
- [C] `[45,10,20,30,40,50,60]`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `insert(len(r), 60)` → `insert(5, 60)` → oxiriga: `[10,20,30,40,50,60]`. `insert(-1, 45)` → `-1` indeks, ya'ni oxirgi elementdan oldin: `[10,20,30,40,50,45,60]`. Natija: `[10,20,30,40,50,45,60]`.

> **To'g'ri javob (to'liqroq):** B — `[10,20,30,40,50,45,60]`

---

## Savol 39

Quyidagi kodning natijasi nima?

```python
r = [3, 6, 1, 8, 2, 9, 4, 7, 5]
r.sort(reverse=True)
top3 = r[:3]
r.clear()
print(top3)
print(r)
```

- [A] `[]`, `[]`
- [B] `[9, 8, 7]`, `[]`
- [C] `[9, 8, 7]`, `[3,6,1,8,2,9,4,7,5]`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `sort(reverse=True)` → `[9,8,7,6,5,4,3,2,1]`. `top3 = r[:3]` → `[9,8,7]` (mustaqil nusxa). `r.clear()` → `r = []`. `top3` o'zgarmaydi: `[9,8,7]`.

---

## Savol 40

Quyidagi to'liq kodning natijasi nima?

```python
class Navbat:
    def __init__(self):
        self.__data = []

    def qosh(self, element):
        self.__data.append(element)

    def chiqar(self):
        if self.__data:
            return self.__data.pop(0)
        return None

    def ko_rsat(self):
        return self.__data.copy()

    def soni(self):
        return len(self.__data)

n = Navbat()
n.qosh("Ali")
n.qosh("Vali")
n.qosh("Gali")
print(n.chiqar())
n.qosh("Zulfiya")
print(n.soni())
print(n.ko_rsat())
```

- [A] `"Ali"`, `3`, `["Vali", "Gali", "Zulfiya"]`
- [B] `"Gali"`, `3`, `["Ali", "Vali", "Zulfiya"]`
- [C] `"Ali"`, `2`, `["Vali", "Gali"]`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `qosh` uch marta: `["Ali","Vali","Gali"]`. `chiqar()` → `pop(0)` → birinchi element: `"Ali"`, `["Vali","Gali"]`. `qosh("Zulfiya")` → `["Vali","Gali","Zulfiya"]`. `soni()` → `3`. `ko'rsat()` → `["Vali","Gali","Zulfiya"]`.

---