## Savol 1



Quyidagi kodning natijasi nima?

```python
r = ['a', 'b', 'c']
print(r[0], r[-1])
```



- [A] 'b', 'b' 
- [B] 'a', 'a' 
- [C] 'a', 'c' 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `r[0]` — birinchi element: `'a'`. `r[-1]` — oxirgi element: `'c'`.


---


## Savol 2



`[5] * 3` ifodasi qanday natija beradi?



- [A] [15] 
- [B] [5, 5, 5] 
- [C] [5, 3] 
- [D] [1, 2, 3, 4, 5] 


> **To'g'ri javob:** B 
> **Tushuntirish:** `[5] * 3` — `5` elementini 3 marta takrorlaydi: `[5, 5, 5]`.


---


## Savol 3



Quyidagi kodning natijasi nima?

```python
r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(r[2:7])
```



- [A] [2, 3, 4, 5, 6, 7] 
- [B] [2, 3, 4, 5, 6] 
- [C] [1, 2, 3, 4, 5, 6] 
- [D] [2, 7] 


> **To'g'ri javob:** B 
> **Tushuntirish:** `r[2:7]` — indeks 2 dan 6 gacha (7 kirmaydi): `[2, 3, 4, 5, 6]`.


---


## Savol 4



Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40]
olindi = r.pop(1)
print(olindi)
print(r)
```



- [A] 10, [20, 30, 40] 
- [B] 20, [10, 30, 40] 
- [C] 30, [10, 20, 40] 
- [D] 40, [10, 20, 30] 


> **To'g'ri javob:** B 
> **Tushuntirish:** `pop(1)` — 1-indeksdagi `20` ni o'chirib, qaytaradi. `r` → `[10, 30, 40]`.


---


## Savol 5



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
jami = 0
for x in r:
    jami += x
print(jami)
```



- [A] 12345 
- [B] 15 
- [C] 5 
- [D] None 


> **To'g'ri javob:** B 
> **Tushuntirish:** `1+2+3+4+5 = 15`.


---


## Savol 6



Quyidagi kod nima natija beradi?

```python
t = (1, 2, 3)
t[0] = 99
```



- [A] (99, 2, 3) 
- [B] (1, 2, 3) 
- [C] TypeError 
- [D] None 


> **To'g'ri javob:** C 
> **Tushuntirish:** Tuple immutable. `t[0] = 99` → `TypeError: 'tuple' object does not support item assignment`.


---


## Savol 7



Quyidagi kodning natijasi nima?

```python
t = (10, 20, 30)
a, b, c = t
print(b)
```



- [A] 10 
- [B] 20 
- [C] 30 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Tuple unpacking: `a=10`, `b=20`, `c=30`. `print(b)` → `20`.


---


## Savol 8



Tuple dict kaliti sifatida ishlatila oladimi?



- [A] Yo'q, hech qachon 
- [B] Ha, chunki tuple o'zgarmas (hashable) 
- [C] Faqat raqamli tuple 
- [D] Faqat string tuple 


> **To'g'ri javob:** B 
> **Tushuntirish:** Dict kaliti hashable bo'lishi shart. Tuple immutable → hashable → kalit bo'la oladi. List esa bo'la olmaydi.


---


## Savol 9



Dictionary kaliti qanday bo'lishi kerak?



- [A] Faqat string 
- [B] Faqat raqam 
- [C] O'zgarmas (immutable) — string, int, tuple bo'lishi mumkin 
- [D] Istalgan turdagi 


> **To'g'ri javob:** C 
> **Tushuntirish:** Kalit hashable bo'lishi shart: `str`, `int`, `tuple` — bo'la oladi. `list`, `dict` — bo'la olmaydi.


---


## Savol 10



Bo'sh dictionary qanday yaratiladi?



- [A] Faqat {} 
- [B] Faqat dict() 
- [C] {} yoki dict() — ikkalasi ham 
- [D] {:} 


> **To'g'ri javob:** C 
> **Tushuntirish:** `{}` va `dict()` — ikkalasi ham bo'sh dictionary yaratadi.


---


## Savol 11



`pop()` metodi nima qiladi?



- [A] Oxirgi elementni o'chiradi 
- [B] Ko'rsatilgan kalitni o'chirib, uning qiymatini qaytaradi 
- [C] Tasodifiy elementni o'chiradi 
- [D] Barcha elementlarni o'chiradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `d.pop('kalit')` — kalitni o'chirib, faqat **qiymatini** qaytaradi.


---


## Savol 12



Funksiyadan foydalanishning asosiy sababi nima?



- [A] Kodni sekinlashtirish 
- [B] Kodni takrorlamaslik (DRY) va tartibli yozish 
- [C] Faqat raqamli hisob-kitoblar uchun 
- [D] Xotira tejash 


> **To'g'ri javob:** B 
> **Tushuntirish:** DRY — Don't Repeat Yourself. Funksiya bir marta yozilib, kerak joyda chaqiriladi.


---


## Savol 13



Funksiya tanasi qanday belgilanadi?



- [A] `{}` qavslar bilan 
- [B] `begin...end` kalit so'zlari bilan 
- [C] Indentatsiya (4 bo'sh joy yoki 1 tab) bilan 
- [D] `()` qavslar bilan 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da kod bloklari indentatsiya bilan belgilanadi. Funksiya tanasi 4 bo'sh joy ichkariga yoziladi.


---


## Savol 14



Quyidagi kodning natijasi nima?

```python
def ayirma(a, b):
    return a - b

print(ayirma(10, 3))
print(ayirma(3, 10))
```



- [A] 7, 7 
- [B] 7, -7 
- [C] -7, 7 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `ayirma(10, 3)` → `10-3=7`. `ayirma(3, 10)` → `3-10=-7`. Tartib natijaga ta'sir qiladi.


---


## Savol 15



Quyidagi kodning natijasi nima?

```python
def salom():
    print('Salom!')

natija = salom()
print(natija)
```



- [A] Salom!, Salom! 
- [B] Salom!, None 
- [C] None, Salom! 
- [D] None, None 


> **To'g'ri javob:** B 
> **Tushuntirish:** `salom()` → `print('Salom!')` chiqaradi, `None` qaytaradi. `natija = None`. `print(None)` → `None`.


---


## Savol 16



Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30]
print(r.index(20))
print(r.count(10))
```



- [A] 2, 1 
- [B] 1, 1 
- [C] 20, 10 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `index(20)` — `20` ning indeksi: `1`. `count(10)` — `10` necha marta: `1`.


---


## Savol 17



Quyidagi kodning natijasi nima?

```python
a = [1, 2, 3]
b = a
b.append(99)
print(a)
```



- [A] [1, 2, 3] 
- [B] [1, 2, 3, 99] 
- [C] [99] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `b = a` — reference (havola). `b.append(99)` asl listni o'zgartiradi. `a` va `b` bir xil obyekt.


---


## Savol 18



Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40, 50]
print(r[1:4])
print(r[-3:-1])
```



- [A] [20, 30, 40], [30, 40] 
- [B] [20, 30, 40], [30, 40, 50] 
- [C] [10, 20, 30], [30, 40] 
- [D] Xato beradi 


> **To'g'ri javob:** A 
> **Tushuntirish:** `r[1:4]` → `[20, 30, 40]`. `r[-3:-1]` → indeks -3, -2 → `[30, 40]`.


---


## Savol 19



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3]
r.extend([4, 5])
r.append(6)
print(r)
```



- [A] [1, 2, 3, [4, 5], 6] 
- [B] [1, 2, 3, 4, 5, 6] 
- [C] [1, 2, 3, 4, 5, [6]] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `extend([4,5])` — har elementni alohida qo'shadi. `append(6)` — bitta element. Natija: `[1, 2, 3, 4, 5, 6]`.


---


## Savol 20



Quyidagi kodning natijasi nima?

```python
r = [3, 1, 4, 1, 5, 9, 2, 6]
print(max(r))
print(min(r))
```



- [A] 6, 1 
- [B] 9, 1 
- [C] 9, 2 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `max=9`, `min=1`.


---


## Savol 21



Quyidagi kodning natijasi nima?

```python
t = ('a', 'b', 'c')
print('b' in t)
print('d' not in t)
```



- [A] True, False 
- [B] False, True 
- [C] True, True 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `'b' in t` → `True`. `'d' not in t` → `'d'` yo'q, shuning uchun `not in` → `True`.


---


## Savol 22



Quyidagi kodning natijasi nima?

```python
t = (1, 2, 3)
r = list(t)
r.append(4)
print(t)
print(r)
```



- [A] (1, 2, 3, 4), [1, 2, 3, 4] 
- [B] (1, 2, 3), [1, 2, 3, 4] 
- [C] (1, 2, 3), [1, 2, 3] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `list(t)` — mustaqil nusxa. `r.append(4)` faqat `r` ni o'zgartiradi. Asl `t` o'zgarmaydi.


---


## Savol 23



Qaysi holda tuple listdan afzal?



- [A] Ko'p element saqlashda 
- [B] O'zgarmaydigan ma'lumotlar, dict kaliti, tezlik muhim bo'lganda 
- [C] Har doim list afzal 
- [D] Elementlarni tartiblashda 


> **To'g'ri javob:** B 
> **Tushuntirish:** Tuple — doimiy ma'lumotlar, koordinatalar, dict kaliti uchun. List — o'zgaruvchan to'plamlar uchun.


---


## Savol 24



Quyidagi kodning natijasi nima?

```python
d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
    print(k)
```



- [A] Qiymatlar chiqadi 
- [B] Kalitlar: a, b, c 
- [C] (a,1), (b,2), (c,3) 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `for k in d` — standart dictionary iteratsiyasi kalitlarni beradi.


---


## Savol 25



`{**d1, **d2}` sintaksisi nima qiladi?



- [A] Ikki dictionaryni solishtiради 
- [B] Ikki dictionaryni birlashtirib yangi dict yaratadi 
- [C] Faqat d1 ni nusxalaydi 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `**` — dict ni yoyadi. `{**d1, **d2}` — ikkisini birlashtirib yangi dictionary yaratadi.


---