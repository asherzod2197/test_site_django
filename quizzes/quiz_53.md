## Savol 1



Listda qanday turdagi elementlar saqlanishi mumkin?



- [A] Faqat raqamlar 
- [B] Faqat matnlar 
- [C] Faqat bir xil turdagi 
- [D] Turli xil turdagi (int, str, list va boshqalar) 


> **To'g'ri javob:** D 
> **Tushuntirish:** List har qanday turdagi elementlarni saqlashi mumkin: `[1, 'salom', True, [2,3]]`.


---


## Savol 2



Quyidagi kodning natijasi nima?

```python
r = list('abc')
print(r)
```



- [A] ['abc'] 
- [B] ['a', 'b', 'c'] 
- [C] ['a, b, c'] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `list(string)` — har bir belgini alohida element qiladi.


---


## Savol 3



Quyidagi kodning natijasi nima?

```python
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(m[1][2])
```



- [A] 5 
- [B] 6 
- [C] 8 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `m[1]` → 2-qator: `[4, 5, 6]`. `[2]` → `6`.


---


## Savol 4



Quyidagi kodning natijasi nima?

```python
r = [5, 2, 8, 1, 9]
r.sort(reverse=True)
print(r)
```



- [A] [1, 2, 5, 8, 9] 
- [B] [9, 8, 5, 2, 1] 
- [C] [5, 2, 8, 1, 9] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `sort(reverse=True)` — kamayish tartibida saralaydi: `[9, 8, 5, 2, 1]`.


---


## Savol 5



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5, 6]
toq = []
for x in r:
    if x % 2 != 0:
        toq.append(x)
print(toq)
```



- [A] [2, 4, 6] 
- [B] [1, 3, 5] 
- [C] [1, 2, 3] 
- [D] [4, 5, 6] 


> **To'g'ri javob:** B 
> **Tushuntirish:** Toq sonlar: `1, 3, 5`. Ular `toq` listga qo'shiladi.


---


## Savol 6



Tuple immutable degani nima?



- [A] Elementlarini o'qib bo'lmaydi 
- [B] Yaratilgandan keyin element qo'shish, o'chirish yoki o'zgartirish mumkin emas 
- [C] Faqat bir marta ishlatiladi 
- [D] Faqat bir xil turdagi element saqlaydi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Immutable — o'zgarmas. `t[0] = x` → `TypeError`. Lekin tuple o'zgaruvchisini qayta belgilash mumkin.


---


## Savol 7



Quyidagi kodning natijasi nima?

```python
t = (1, 2, 3, 4, 5)
a, *b, c = t
print(b)
```



- [A] (2, 3, 4) 
- [B] [2, 3, 4] 
- [C] [1, 2, 3, 4, 5] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `*b` — o'rtadagi elementlarni **list** sifatida oladi: `[2, 3, 4]`.


---


## Savol 8



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3]
t = (1, 2, 3)
r2 = r.copy()
t2 = t
print(r2 is r)
print(t2 is t)
```



- [A] False, False 
- [B] True, True 
- [C] False, True 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `r.copy()` — yangi obyekt → `is` → `False`. `t2 = t` — reference → bir xil obyekt → `True`.


---


## Savol 9



Quyidagi kodning natijasi nima?

```python
d = {'x': 10, 'y': 20, 'x': 30}
print(len(d))
print(d['x'])
```



- [A] 3, 10 
- [B] 2, 30 
- [C] 3, 30 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `'x'` ikki marta — oxirgisi `30` saqlanadi. Noyob kalitlar: `'x'`, `'y'` → `len=2`.


---


## Savol 10



Quyidagi kodning natijasi nima?

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 99, 'c': 3}
d3 = {**d1, **d2}
print(d3['b'])
```



- [A] 1 
- [B] 99 
- [C] [1, 99] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `d2` keyinroq yoyiladi → `'b':99` ustun turadi.


---


## Savol 11



Quyidagi kodning natijasi nima?

```python
d = {'a': 1, 'b': 2, 'c': 3}
print(list(d.values()))
```



- [A] ['a', 'b', 'c'] 
- [B] [1, 2, 3] 
- [C] [('a',1), ('b',2), ('c',3)] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `d.values()` — qiymatlarni qaytaradi. `list(...)` → `[1, 2, 3]`.


---


## Savol 12



Lokal o'zgaruvchi nima?



- [A] Butun dasturda ko'rinadigan o'zgaruvchi 
- [B] Faqat funksiya ichida yaratilgan va ko'rinadigan o'zgaruvchi 
- [C] Modul darajasidagi o'zgaruvchi 
- [D] Faqat `global` bilan e'lon qilingan o'zgaruvchi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Lokal — funksiya ichida yaratiladi, funksiya tugagach yo'q bo'ladi. Global — hamma joydan ko'rinadi.


---


## Savol 13



Quyidagi kodning natijasi nima?

```python
def f(x):
    return x * x
    print('Bu ishlamaydi')

print(f(4))
```



- [A] 16, Bu ishlamaydi 
- [B] 16 
- [C] Bu ishlamaydi, 16 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `return` dan keyin kod ishlamaydi — unreachable code. Faqat `16` chiqadi.


---


## Savol 14



Quyidagi kodning natijasi nima?

```python
def f(a, b, c):
    print(a, b, c)

f(1, c=3, b=2)
```



- [A] 1 2 3 
- [B] 1 3 2 
- [C] Xato beradi 
- [D] c b a 


> **To'g'ri javob:** A 
> **Tushuntirish:** `a=1` pozitsion, `c=3`, `b=2` kalit so'z. `print(a, b, c)` → `1 2 3`.


---


## Savol 15



Quyidagi kodning natijasi nima?

```python
def f():
    return

def g():
    pass

print(f() is None)
print(g() is None)
```



- [A] False, False 
- [B] True, True 
- [C] True, False 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `f()` va `g()` — ikkalasi ham `None` qaytaradi. `None is None` → `True`.


---


## Savol 16



List nima?



- [A] Kalit-qiymat juftliklarini saqlaydigan tuzilma 
- [B] Tartibli, o'zgaruvchan, turli xil elementli to'plam 
- [C] O'zgarmas elementlar to'plami 
- [D] Faqat raqamlarni saqlaydigan tuzilma 


> **To'g'ri javob:** B 
> **Tushuntirish:** List — tartibli (ordered), o'zgaruvchan (mutable), turli turdagi elementlarni saqlashi mumkin bo'lgan to'plam.


---


## Savol 17



Quyidagi kodning natijasi nima?

```python
r = list(range(1, 6))
print(r)
```



- [A] [0, 1, 2, 3, 4] 
- [B] [1, 2, 3, 4, 5, 6] 
- [C] [1, 2, 3, 4, 5] 
- [D] range(1, 6) 


> **To'g'ri javob:** C 
> **Tushuntirish:** `range(1, 6)` — 1 dan 5 gacha (6 kirmaydi). `list()` → `[1, 2, 3, 4, 5]`.


---


## Savol 18



Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40, 50]
print(r[-2])
```



- [A] 20 
- [B] 30 
- [C] 40 
- [D] 50 


> **To'g'ri javob:** C 
> **Tushuntirish:** `r[-1]=50`, `r[-2]=40`.


---


## Savol 19



`append()` va `extend()` ning farqi nima?



- [A] Hech qanday farq yo'q 
- [B] `append` butun obyektni, `extend` iterablening har bir elementini qo'shadi 
- [C] `extend` tezroq ishlaydi 
- [D] `append` faqat raqamlar uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** `append([1,2])` → `[..., [1, 2]]`. `extend([1,2])` → `[..., 1, 2]`. Farqi: `append` bitta element, `extend` ko'p element qo'shadi.


---


## Savol 20



Quyidagi kodning natijasi nima?

```python
r = [3, 1, 4, 1, 5]
print(len(r))
print(1 in r)
```



- [A] 5, False 
- [B] 4, True 
- [C] 5, True 
- [D] 5, 1 


> **To'g'ri javob:** C 
> **Tushuntirish:** `len(r)` → 5 ta element. `1 in r` → `1` listda bor → `True`.


---


## Savol 21



Tuple va listning asosiy farqi nima?



- [A] Tuple faqat raqam saqlaydi 
- [B] List o'zgarmas, tuple o'zgaruvchan 
- [C] Tuple o'zgarmas (immutable), list o'zgaruvchan (mutable) 
- [D] Hech qanday farq yo'q 


> **To'g'ri javob:** C 
> **Tushuntirish:** Tuple immutable — yaratilgandan keyin o'zgartirib bo'lmaydi. List mutable — istalgan vaqt o'zgartiriladi.


---


## Savol 22



Bitta elementli tuple qanday yaratiladi?



- [A] t = (5) 
- [B] t = [5] 
- [C] t = (5,) 
- [D] t = tuple(5) 


> **To'g'ri javob:** C 
> **Tushuntirish:** `(5)` — bu shunchaki `5` soni. Bitta elementli tuple uchun vergul shart: `(5,)`.


---


## Savol 23



Quyidagi kodda qaysi satr `TypeError` beradi?

```python
r = [1, 2, 3]
t = (1, 2, 3)
r[0] = 99   # 1-satr
t[0] = 99   # 2-satr
```



- [A] 1-satr 
- [B] 2-satr 
- [C] Ikkalasi ham 
- [D] Hech biri 


> **To'g'ri javob:** B 
> **Tushuntirish:** List mutable — `r[0]=99` ishlaydi. Tuple immutable — `t[0]=99` → `TypeError`.


---


## Savol 24



Dictionary da mavjud bo'lmagan kalitga `d[kalit]` bilan murojaat qilsa nima bo'ladi?



- [A] None qaytaradi 
- [B] False qaytaradi 
- [C] KeyError beradi 
- [D] 0 qaytaradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `d['mavjud_emas']` → `KeyError`. Xavfsiz murojaat uchun `d.get('kalit')` ishlatiladi.


---


## Savol 25



Quyidagi kodning natijasi nima?

```python
d = dict(ism='Ali', yosh=20)
print(d['ism'])
```



- [A] 'ism' 
- [B] 'Ali' 
- [C] KeyError 
- [D] None 


> **To'g'ri javob:** B 
> **Tushuntirish:** `dict(kalit=qiymat)` — kalitlar string sifatida saqlanadi. `d['ism']` → `'Ali'`.


---