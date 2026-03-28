## Savol 1



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3]
print(r * 2)
```



- [A] [2, 4, 6] 
- [B] [1, 2, 3, 1, 2, 3] 
- [C] 6 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `r * 2` — listni 2 marta takrorlaydi: `[1, 2, 3, 1, 2, 3]`.


---


## Savol 2



Quyidagi kodning natijasi nima?

```python
r = list(range(5, 0, -1))
print(r)
```



- [A] [0, 1, 2, 3, 4] 
- [B] [5, 4, 3, 2, 1, 0] 
- [C] [5, 4, 3, 2, 1] 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `range(5, 0, -1)` — 5 dan 1 gacha (0 kirmaydi), -1 qadam: `5, 4, 3, 2, 1`.


---


## Savol 3



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
r[1] = 99
print(r)
```



- [A] [1, 2, 3, 4, 5] 
- [B] [99, 2, 3, 4, 5] 
- [C] [1, 99, 3, 4, 5] 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `r[1] = 99` — 1-indeksdagi element almashtiriladi. Natija: `[1, 99, 3, 4, 5]`.


---


## Savol 4



Quyidagi kodning natijasi nima?

```python
r = ['a', 'b', 'c']
r.insert(1, 'X')
print(r)
```



- [A] ['X', 'a', 'b', 'c'] 
- [B] ['a', 'X', 'b', 'c'] 
- [C] ['a', 'b', 'X', 'c'] 
- [D] ['a', 'b', 'c', 'X'] 


> **To'g'ri javob:** B 
> **Tushuntirish:** `insert(1, 'X')` — 1-indeksga `'X'` qo'shiladi, qolganlar o'ngga suriladi.


---


## Savol 5



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
for i, x in enumerate(r):
    print(i, x)
```



- [A] 0 1, 1 2, 2 3, 3 4, 4 5 
- [B] 1 1, 2 2, 3 3, 4 4, 5 5 
- [C] 1, 2, 3, 4, 5 
- [D] Xato beradi 


> **To'g'ri javob:** A 
> **Tushuntirish:** `enumerate(r)` — `(indeks, element)` juftliklari. Indeks `0` dan boshlanadi.


---


## Savol 6



Tuple nechta o'z metodiga ega?



- [A] 0 ta — hech qanday metod yo'q 
- [B] 2 ta — `count()` va `index()` 
- [C] Listdagi kabi ko'p 
- [D] 5 ta 


> **To'g'ri javob:** B 
> **Tushuntirish:** Tuple faqat 2 ta metod: `count()` va `index()`. O'zgartiruvchi metodlar listda bor, tupled yo'q.


---


## Savol 7



Quyidagi kodning natijasi nima?

```python
t = (3, 1, 4, 1, 5)
print(t.index(1))
```



- [A] 0 
- [B] 1 
- [C] 3 
- [D] [1, 3] 


> **To'g'ri javob:** B 
> **Tushuntirish:** `index(1)` — `1` ning birinchi uchraydigan indeksi: `1`.


---


## Savol 8



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3]
t = (1, 2, 3)
print(r[1:])
print(t[1:])
```



- [A] [2, 3], [2, 3] 
- [B] [2, 3], (2, 3) 
- [C] (2, 3), (2, 3) 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** List slicing → list qaytaradi: `[2, 3]`. Tuple slicing → tuple qaytaradi: `(2, 3)`.


---


## Savol 9



Dictionary da kalitlar takrorlanishi mumkinmi?



- [A] Ha, bir kalit bir necha qiymatga ega bo'ladi 
- [B] Yo'q, kalitlar noyob — oxirgisi saqlanadi 
- [C] Faqat string kalitlar takrorlanishi mumkin 
- [D] Python xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `{'a':1, 'a':2}` → `{'a':2}`. Bir xil kalit bo'lsa oxirgisi saqlanadi.


---


## Savol 10



Quyidagi kodning natijasi nima?

```python
d = dict.fromkeys(['a', 'b', 'c'], 0)
print(d['b'])
```



- [A] None 
- [B] 'b' 
- [C] 0 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `fromkeys(kalitlar, 0)` — barcha kalitlarga `0` qiymat beradi. `d['b']` → `0`.


---


## Savol 11



`setdefault()` va `get()` ning farqi nima?



- [A] Hech qanday farq yo'q 
- [B] `setdefault` kalit yo'q bo'lsa dictionaryga qo'shadi, `get` qo'shmaydi 
- [C] `get` qo'shadi, `setdefault` qo'shmaydi 
- [D] Ikkalasi ham qo'shadi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `get('k', v)` — topilmasa standart qaytaradi, qo'shmaydi. `setdefault('k', v)` — qo'shib qaytaradi.


---


## Savol 12



Funksiya e'lon qilinganda (`def`) darhol ishlaydimi?



- [A] Ha, darhol ishlaydi 
- [B] Yo'q, faqat chaqirilganda ishlaydi 
- [C] Faqat birinchi marta ishlaydi 
- [D] Faqat `if` ichida ishlaydi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `def f():` — faqat e'lon qiladi. `f()` deb chaqirilgandagina ishlaydi.


---


## Savol 13



Quyidagi kodning natijasi nima?

```python
def salom(ism):
    print(f'Salom, {ism}!')

salom('Kamol')
```



- [A] Salom, ism! 
- [B] Salom, Kamol! 
- [C] None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `ism` parametriga `'Kamol'` beriladi. `f-string` da `{ism}` → `'Kamol'`.


---


## Savol 14



Quyidagi kodning natijasi nima?

```python
def tanishtir(ism, yosh, shahar):
    print(f'{ism}, {yosh}, {shahar}')

tanishtir(yosh=22, shahar='Samarqand', ism='Dilnoza')
```



- [A] Xato beradi — tartib noto'g'ri 
- [B] Dilnoza, 22, Samarqand 
- [C] yosh, ism, shahar 
- [D] 22, Dilnoza, Samarqand 


> **To'g'ri javob:** B 
> **Tushuntirish:** Kalit so'z argumentlarida tartib muhim emas — har biri nomi bilan mos parametrga birikadi.


---


## Savol 15



`return` dan keyin yozilgan kod ishlaydimi?



- [A] Ha, har doim ishlaydi 
- [B] Yo'q — `return` funksiyani to'xtatadi, undan keyingi kod hech qachon ishlamaydi 
- [C] Faqat `return None` dan keyin ishlaydi 
- [D] Faqat `try` blokida ishlaydi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `return` — funksiyani darhol tugatadi. Undan keyingi kod **unreachable** hisoblanadi.


---


## Savol 16



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
print(r[-3])
```



- [A] 1 
- [B] 2 
- [C] 3 
- [D] 4 


> **To'g'ri javob:** C 
> **Tushuntirish:** Manfiy indeks oxirdan hisoblaydi: `r[-1]=5`, `r[-2]=4`, `r[-3]=3`.


---


## Savol 17



Quyidagi kodning natijasi nima?

```python
asl = [1, 2, 3]
n1 = asl.copy()
n2 = asl[:]
n1.append(10)
n2.append(20)
print(asl)
```



- [A] [1, 2, 3, 10, 20] 
- [B] [1, 2, 3, 10] 
- [C] [1, 2, 3] 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `copy()` va `[:]` — mustaqil nusxalar. Ularni o'zgartirish asl listga ta'sir qilmaydi.


---


## Savol 18



Quyidagi kodning natijasi nima?

```python
r = [5, 10, 15, 20, 25]
r[1:4] = [0]
print(r)
```



- [A] [5, 0, 20, 25] 
- [B] [5, 0, 25] 
- [C] [5, 10, 0, 20, 25] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `r[1:4]` — `[10, 15, 20]` o'rniga `[0]` qo'yiladi. Natija: `[5, 0, 25]`.


---


## Savol 19



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
r.reverse()
print(r)
print(r.reverse())
```



- [A] [5, 4, 3, 2, 1], [1, 2, 3, 4, 5] 
- [B] [5, 4, 3, 2, 1], None 
- [C] [1, 2, 3, 4, 5], None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Birinchi `reverse()` → `[5,4,3,2,1]`. `print(r.reverse())` — yana teskari, `None` qaytaradi → `None`.


---


## Savol 20



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
hisoblagich = 0
for x in r:
    if x % 2 == 0:
        hisoblagich += 1
print(hisoblagich)
```



- [A] 5 
- [B] 3 
- [C] 2 
- [D] None 


> **To'g'ri javob:** C 
> **Tushuntirish:** Juft sonlar: `2`, `4` — jami `2` ta.


---


## Savol 21



Quyidagi kodning natijasi nima?

```python
t = (1, [2, 3], 4)
t[1].append(99)
print(t)
```



- [A] (1, [2, 3], 4) — o'zgarmadi 
- [B] TypeError 
- [C] (1, [2, 3, 99], 4) 
- [D] (1, 99, 4) 


> **To'g'ri javob:** C 
> **Tushuntirish:** Tuple immutable, lekin ichidagi list mutable. `t[1].append(99)` — listga element qo'shiladi, tuple tuzilmasi o'zgarmaydi.


---


## Savol 22



Quyidagi kodning natijasi nima?

```python
t = (1, 2, 3)
r = list(t)
r[0] = 99
t2 = tuple(r)
print(t)
print(t2)
```



- [A] (99, 2, 3), (99, 2, 3) 
- [B] (1, 2, 3), (99, 2, 3) 
- [C] (1, 2, 3), (1, 2, 3) 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `list(t)` mustaqil nusxa. `r[0]=99`. `tuple(r)` → `(99,2,3)`. Asl `t` o'zgarmaydi.


---


## Savol 23



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3]
t = (1, 2, 3)
print(type(r[1:]))
print(type(t[1:]))
```



- [A] list, list 
- [B] tuple, tuple 
- [C] list, tuple 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** List slicing → `list`. Tuple slicing → `tuple`.


---


## Savol 24



`update()` metodi nima qiladi?



- [A] Faqat yangi kalitlar qo'shadi 
- [B] Faqat mavjud kalitlarni yangilaydi 
- [C] Yangi kalitlar qo'shadi va mavjudlarini yangilaydi 
- [D] Barcha elementlarni o'chiradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `d.update(boshqa)` — mavjud kalit bo'lsa yangilaydi, bo'lmasa qo'shadi.


---


## Savol 25



Quyidagi kodning natijasi nima?

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 99, 'c': 3}
d3 = {**d1, **d2}
print(len(d3))
```



- [A] 2 
- [B] 3 
- [C] 4 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Noyob kalitlar: `a`, `b`, `c` → `3` ta.


---