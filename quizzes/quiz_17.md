## Savol 1

Python'da list (ro'yxat) nima?

- [A] Faqat sonlarni saqlaydigan ma'lumot turi  
- [B] Tartib saqlangan, o'zgaruvchan va turli xil elementlarni o'z ichiga oluvchi to'plam  
- [C] Faqat o'zgarmas elementlar to'plami  
- [D] Kalit-qiymat juftliklarini saqlaydigan tuzilma  

> **To'g'ri javob:** B  
> **Tushuntirish:** List — bu tartibli (ordered), o'zgaruvchan (mutable) va bir xil yoki turli xil turdagi elementlarni saqlashi mumkin bo'lgan Python ma'lumot turi. Elementlarga indeks orqali murojaat qilish mumkin.

---

## Savol 2

Quyidagi kodning natijasi nima?

```python
meva = ["olma", "banan", "uzum"]
print(meva[1])
```

- [A] `olma`  
- [B] `banan`  
- [C] `uzum`  
- [D] `IndexError`  

> **To'g'ri javob:** B  
> **Tushuntirish:** Listda indekslash `0` dan boshlanadi. `meva[0]` → `"olma"`, `meva[1]` → `"banan"`, `meva[2]` → `"uzum"`.

---

## Savol 3

Bo'sh list qanday yaratiladi?

- [A] `list = {}`  
- [B] `list = ()`  
- [C] `list = []`  
- [D] `list = ""`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Bo'sh list ikki usulda yaratiladi: `[]` yoki `list()`. `{}` — dict, `()` — tuple, `""` — string yaratadi.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
sonlar = [10, 20, 30, 40, 50]
print(sonlar[-1])
```

- [A] `10`  
- [B] `50`  
- [C] `40`  
- [D] `IndexError`  

> **To'g'ri javob:** B  
> **Tushuntirish:** Manfiy indeks listning oxiridan hisoblaydi. `-1` — oxirgi element, `-2` — oxiridan ikkinchi, va hokazo. `sonlar[-1]` → `50`.

---

## Savol 5

`append()` metodi nima qiladi?

- [A] Listning boshiga element qo'shadi  
- [B] Listning oxiriga element qo'shadi  
- [C] Listdagi elementni o'chiradi  
- [D] Listni tartiblaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `append(element)` — berilgan elementni listning eng oxiriga qo'shadi. Faqat bitta argument qabul qiladi.

---

## Savol 6

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3]
r.append(4)
r.append(5)
print(r)
```

- [A] `[5, 4, 1, 2, 3]`  
- [B] `[1, 2, 3, 4, 5]`  
- [C] `[1, 2, 3]`  
- [D] `[4, 5]`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `append(4)` → `[1, 2, 3, 4]`. `append(5)` → `[1, 2, 3, 4, 5]`. Har bir `append` oxiriga element qo'shadi.

---

## Savol 7

`insert()` metodi qanday ishlaydi?

- [A] `insert(element)` — oxiriga qo'shadi  
- [B] `insert(indeks, element)` — ko'rsatilgan indeks o'rniga element qo'shadi  
- [C] `insert(element, indeks)` — elementni indeks bilan almashtiradi  
- [D] Faqat raqamli elementlar uchun ishlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `insert(i, x)` — `i` indeksga `x` elementni joylashtiradi, qolgan elementlar o'ngga suriladi. Masalan: `[1,2,3]` ga `insert(1, 10)` → `[1, 10, 2, 3]`.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
r = ["a", "b", "d"]
r.insert(2, "c")
print(r)
```

- [A] `["a", "b", "c"]`  
- [B] `["a", "c", "b", "d"]`  
- [C] `["a", "b", "c", "d"]`  
- [D] `["c", "a", "b", "d"]`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `insert(2, "c")` — 2-indeksga `"c"` qo'yiladi: `["a", "b", "c", "d"]`. `"d"` bir o'rindan o'ngga suriladi.

---

## Savol 9

`remove()` va `pop()` metodlarining farqi nima?

- [A] Hech qanday farq yo'q  
- [B] `remove(qiymat)` — qiymat bo'yicha o'chiradi; `pop(indeks)` — indeks bo'yicha o'chirib, elementni qaytaradi  
- [C] `pop()` — qiymat bo'yicha, `remove()` — indeks bo'yicha o'chiradi  
- [D] `remove()` faqat birinchi elementni, `pop()` faqat oxirgi elementni o'chiradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `remove(x)` — `x` qiymatiga teng birinchi elementni o'chiradi. `pop(i)` — `i` indeksidagi elementni o'chirib, uni qaytaradi. `pop()` (indekssiz) oxirgi elementni o'chiradi.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40, 50]
olingan = r.pop(2)
print(olingan)
print(r)
```

- [A] `20`, `[10, 30, 40, 50]`  
- [B] `30`, `[10, 20, 40, 50]`  
- [C] `50`, `[10, 20, 30, 40]`  
- [D] `10`, `[20, 30, 40, 50]`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `pop(2)` — 2-indeksdagi element (`30`) ni o'chirib qaytaradi. `olingan = 30`. Listda `[10, 20, 40, 50]` qoladi.

---

## Savol 11

List slicing (kesish) qanday ishlaydi?

- [A] `list[bosh:oxir]` — `bosh` dan `oxir` gacha (oxiri kirmaydi) elementlarni qaytaradi  
- [B] `list[bosh:oxir]` — `bosh` dan `oxir` gacha (ikkalasi ham kiradi) elementlarni qaytaradi  
- [C] `list[bosh:oxir]` — faqat `bosh` va `oxir` indeksdagi elementlarni qaytaradi  
- [D] Slice listni o'zgartirib yuboradi  

> **To'g'ri javob:** A  
> **Tushuntirish:** `list[a:b]` — `a` indeksdan `b` indeksgacha, lekin `b` kirmasdan elementlarni oladi. Masalan: `[0,1,2,3,4][1:4]` → `[1,2,3]`.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(r[2:7])
print(r[:4])
print(r[6:])
```

- [A] `[2,3,4,5,6]`, `[0,1,2,3,4]`, `[6,7,8,9]`  
- [B] `[2,3,4,5,6]`, `[0,1,2,3]`, `[6,7,8,9]`  
- [C] `[2,3,4,5,6,7]`, `[0,1,2,3]`, `[6,7,8,9]`  
- [D] `[2,7]`, `[4]`, `[6]`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `r[2:7]` → indeks 2 dan 6 gacha: `[2,3,4,5,6]`. `r[:4]` → boshdan 3 gacha: `[0,1,2,3]`. `r[6:]` → 6 dan oxirigacha: `[6,7,8,9]`.

---

## Savol 13

`len()` funksiyasi listda nima qaytaradi?

- [A] Listdagi eng katta elementni  
- [B] Listdagi elementlar sonini  
- [C] Listdagi oxirgi elementning indeksini  
- [D] Listni matn ko'rinishida qaytaradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `len(list)` — listdagi elementlarning umumiy sonini qaytaradi. Masalan: `len([10, 20, 30])` → `3`.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
r = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(r))
print(max(r))
print(min(r))
```

- [A] `8`, `9`, `1`  
- [B] `7`, `9`, `1`  
- [C] `8`, `6`, `2`  
- [D] `8`, `9`, `2`  

> **To'g'ri javob:** A  
> **Tushuntirish:** `len(r)` → `8` ta element. `max(r)` → `9`. `min(r)` → `1` (ikki marta bor, lekin `min` birinchi topilgan minimumni qaytaradi → `1`).

---

## Savol 15

`sort()` va `sorted()` funksiyalarining farqi nima?

- [A] Hech qanday farq yo'q  
- [B] `sort()` — listni o'zini o'zgartiradi (in-place), `sorted()` — yangi tartiblangan list qaytaradi  
- [C] `sorted()` — faqat raqamlar uchun, `sort()` — matnlar uchun  
- [D] `sort()` — yangi list, `sorted()` — o'zini o'zgartiradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `list.sort()` — listni bevosita o'zgartiradi, `None` qaytaradi. `sorted(list)` — asl listni o'zgartirmay, yangi tartiblangan list qaytaradi.

---

## Savol 16

Quyidagi kodning natijasi nima?

```python
r = [5, 2, 8, 1, 9, 3]
r.sort()
print(r)
r.sort(reverse=True)
print(r)
```

- [A] `[1,2,3,5,8,9]`, `[9,8,5,3,2,1]`  
- [B] `[5,2,8,1,9,3]`, `[5,2,8,1,9,3]`  
- [C] `[1,2,3,5,8,9]`, `[1,2,3,5,8,9]`  
- [D] Xato beradi  

> **To'g'ri javob:** A  
> **Tushuntirish:** `sort()` — o'sish tartibida: `[1,2,3,5,8,9]`. `sort(reverse=True)` — kamayish tartibida: `[9,8,5,3,2,1]`.

---

## Savol 17

`in` operatori listda qanday ishlatiladi?

- [A] Listni indeksga bo'ladi  
- [B] Element listda bor-yo'qligini tekshiradi, `True` yoki `False` qaytaradi  
- [C] Elementni listga qo'shadi  
- [D] Listni boshqa list bilan birlashtiradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `element in list` — agar element listda mavjud bo'lsa `True`, aks holda `False` qaytaradi. `not in` esa teskarisini tekshiradi.

---

## Savol 18

Quyidagi kodning natijasi nima?

```python
mevalar = ["olma", "banan", "gilos", "nok"]
print("banan" in mevalar)
print("anor" in mevalar)
print("gilos" not in mevalar)
```

- [A] `True`, `True`, `True`  
- [B] `True`, `False`, `False`  
- [C] `False`, `True`, `False`  
- [D] `True`, `False`, `True`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `"banan" in mevalar` → `True`. `"anor" in mevalar` → `False`. `"gilos" not in mevalar` → `"gilos"` listda bor, shuning uchun `not in` → `False`.

---

## Savol 19

List ustida `for` tsikli qanday ishlaydi?

- [A] Faqat raqamli listlarda ishlaydi  
- [B] Har bir elementni ketma-ket o'tib chiqadi  
- [C] Faqat indekslarni chiqaradi  
- [D] Listni teskaridan o'tadi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `for element in list:` — listning har bir elementini `element` o'zgaruvchisiga biriktirib ketma-ket o'tib chiqadi. `enumerate()` bilan ham indeks va qiymatni birgalikda olish mumkin.

---

## Savol 20

Quyidagi kodning natijasi nima?

```python
sonlar = [1, 2, 3, 4, 5]
jami = 0
for son in sonlar:
    jami += son
print(jami)
```

- [A] `12345`  
- [B] `15`  
- [C] `5`  
- [D] `[1, 2, 3, 4, 5]`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `for` tsikli har bir elementni `jami` ga qo'shadi: `0+1+2+3+4+5 = 15`. Xuddi shu natijani `sum(sonlar)` ham beradi.

---

## Savol 21

List comprehension nima?

- [A] Listni nusxalash usuli  
- [B] `for` va shart bilan yangi list yaratishning qisqa, Pythonic usuli  
- [C] Listni tartiblash usuli  
- [D] Faqat `filter()` funksiyasining muqobili  

> **To'g'ri javob:** B  
> **Tushuntirish:** List comprehension: `[ifoda for element in iterable if shart]` — `for` tsiklini bir qatorda yozish imkonini beradi va yangi list qaytaradi. Kodni qisqa va o'qilishi oson qiladi.

---

## Savol 22

Quyidagi kodning natijasi nima?

```python
kvadratlar = [x**2 for x in range(1, 6)]
print(kvadratlar)
```

- [A] `[1, 2, 3, 4, 5]`  
- [B] `[2, 4, 6, 8, 10]`  
- [C] `[1, 4, 9, 16, 25]`  
- [D] `[0, 1, 4, 9, 16]`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `range(1, 6)` → `1, 2, 3, 4, 5`. Har birining kvadrati: `1, 4, 9, 16, 25`. Natija: `[1, 4, 9, 16, 25]`.

---

## Savol 23

Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
juft = [x for x in r if x % 2 == 0]
print(juft)
```

- [A] `[1, 3, 5, 7, 9]`  
- [B] `[2, 4, 6, 8, 10]`  
- [C] `[0, 2, 4, 6, 8, 10]`  
- [D] `[1, 2, 3, 4, 5]`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `x % 2 == 0` — juft sonlarni filtrlaydi: `2, 4, 6, 8, 10`. Natija: `[2, 4, 6, 8, 10]`.

---

## Savol 24

`extend()` metodi nima qiladi?

- [A] Listning oxiriga bitta element qo'shadi  
- [B] Boshqa iterablening barcha elementlarini listga qo'shadi  
- [C] Ikkita listni birlashtiradi va yangi list qaytaradi  
- [D] Listni kengaytiradi (o'lchamini oshiradi)  

> **To'g'ri javob:** B  
> **Tushuntirish:** `list1.extend(list2)` — `list2` ning har bir elementini `list1` ga qo'shadi (in-place). `append([1,2])` esa butun listni bitta element sifatida qo'shgan bo'lardi.

---

## Savol 25

Quyidagi kodning natijasi nima?

```python
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
print(b)
```

- [A] `[1, 2, 3, [4, 5, 6]]`, `[4, 5, 6]`  
- [B] `[1, 2, 3, 4, 5, 6]`, `[4, 5, 6]`  
- [C] `[1, 2, 3, 4, 5, 6]`, `[]`  
- [D] `[[1,2,3], [4,5,6]]`, `[4, 5, 6]`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `a.extend(b)` — `b` ning elementlari `a` ga bitta-bitta qo'shiladi. `a` → `[1,2,3,4,5,6]`. `b` o'zgarmaydi → `[4,5,6]`.

---

## Savol 26

`count()` va `index()` metodlari nima qiladi?

- [A] `count()` — listni tartiblaydi, `index()` — qidiradi  
- [B] `count(x)` — `x` elementining necha marta uchrashini, `index(x)` — birinchi marta qaysi indeksda ekanini qaytaradi  
- [C] `count()` — elementlar sonini, `index()` — oxirgi indeksini qaytaradi  
- [D] Ikkalasi ham elementni o'chiradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `list.count(x)` → `x` necha marta bor. `list.index(x)` → `x` ning birinchi uchraydigan indeksi. Agar `x` listda bo'lmasa, `index()` `ValueError` beradi.

---

## Savol 27

Quyidagi kodning natijasi nima?

```python
r = [1, 3, 5, 3, 7, 3, 9]
print(r.count(3))
print(r.index(7))
```

- [A] `2`, `4`  
- [B] `3`, `4`  
- [C] `3`, `3`  
- [D] `2`, `3`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `r.count(3)` → `3` qiymati `[1,3,5,3,7,3,9]` da 3 marta uchraydi. `r.index(7)` → `7` qiymati 4-indeksda (0: 1, 1: 3, 2: 5, 3: 3, 4: 7) → `4`.

---

## Savol 28

Ichma-ich (nested) list nima?

- [A] Juda uzun list  
- [B] Elementlari ham list bo'lgan list — ko'p o'lchovli ma'lumotlarni ifodalaydi  
- [C] Faqat butun sonlardan iborat list  
- [D] Tartiblangan list  

> **To'g'ri javob:** B  
> **Tushuntirish:** Nested list — elementlaridan biri yoki bir nechtasi o'zi ham list bo'lgan list. Masalan: `[[1,2],[3,4],[5,6]]`. Matritsalar va 2D jadvallar shu tarzda ifodalanadi.

---

## Savol 29

Quyidagi kodning natijasi nima?

```python
matritsa = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

print(matritsa[1][2])
print(matritsa[0][0])

jami = sum(matritsa[i][i] for i in range(3))
print(jami)
```

- [A] `5`, `1`, `15`  
- [B] `6`, `1`, `15`  
- [C] `6`, `1`, `12`  
- [D] `5`, `0`, `12`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `matritsa[1][2]` → 1-qator, 2-ustun → `6`. `matritsa[0][0]` → `1`. Diagonal: `matritsa[0][0]=1`, `matritsa[1][1]=5`, `matritsa[2][2]=9` → `1+5+9=15`.

---

## Savol 30

Quyidagi to'liq kodning natijasi nima?

```python
def top_n(r, n):
    tartiblangan = sorted(r, reverse=True)
    return tartiblangan[:n]

def statistika(r):
    return {
        "soni": len(r),
        "jami": sum(r),
        "ortacha": round(sum(r) / len(r), 2),
        "max": max(r),
        "min": min(r)
    }

balllar = [85, 92, 78, 95, 88, 72, 90, 65, 88, 76]
eng_yaxshi = top_n(balllar, 3)
stat = statistika(balllar)

print(eng_yaxshi)
print(stat["ortacha"])
print(stat["max"] - stat["min"])
```

- [A] `[95, 92, 90]`, `82.9`, `30`  
- [B] `[95, 92, 88]`, `82.9`, `30`  
- [C] `[95, 92, 90]`, `83.0`, `30`  
- [D] `[95, 92, 90]`, `82.9`, `25`  

> **To'g'ri javob:** A  
> **Tushuntirish:** `sorted(balllar, reverse=True)` → `[95, 92, 90, 88, 88, 85, 78, 76, 72, 65]`. `[:3]` → `[95, 92, 90]`. `sum = 829`, `len = 10` → `ortacha = 82.9`. `max=95`, `min=65` → `95-65=30`.

---