## Savol 1



Quyidagi kodning natijasi nima?

```python
r = [1, [2, 3], 4]
print(len(r))
```



- [A] 4 
- [B] 3 
- [C] 2 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `len` birinchi darajali elementlarni sanaydi: `1`, `[2, 3]`, `4` — jami `3`.


---


## Savol 2



Quyidagi kodning natijasi nima?

```python
asl = [1, 2, 3]
nusxa = asl[:]
nusxa.append(4)
print(asl)
```



- [A] [1, 2, 3, 4] 
- [B] [1, 2, 3] 
- [C] [1, 2, 3, 4, 4] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `asl[:]` — mustaqil nusxa yaratadi. `nusxa.append(4)` faqat nusxani o'zgartiradi, asl o'zgarmaydi.


---


## Savol 3



Quyidagi kodning natijasi nima?

```python
r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(r[::3])
```



- [A] [0, 3, 6, 9] 
- [B] [0, 1, 2] 
- [C] [3, 6, 9] 
- [D] [0, 3, 6] 


> **To'g'ri javob:** A 
> **Tushuntirish:** `r[::3]` — 0 dan boshlab, 3 qadam: indeks 0, 3, 6, 9 → `[0, 3, 6, 9]`.


---


## Savol 4



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 2, 1]
r.remove(2)
print(r)
```



- [A] [1, 3, 2, 1] 
- [B] [1, 2, 3, 1] 
- [C] [1, 3, 1] 
- [D] Xato beradi 


> **To'g'ri javob:** A 
> **Tushuntirish:** `remove(2)` — birinchi uchraydigan `2` ni o'chiradi (indeks 1). Natija: `[1, 3, 2, 1]`.


---


## Savol 5



Quyidagi kodning natijasi nima?

```python
r = [2, 4, 6, 8, 10]
print(len(r))
print(8 in r)
```



- [A] 5, True 
- [B] 5, False 
- [C] 4, True 
- [D] 5, 8 


> **To'g'ri javob:** A 
> **Tushuntirish:** `len=5`. `8 in r` → `True`.


---


## Savol 6



Quyidagi kodning natijasi nima?

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(type(t1 + t2))
print(len(t1 + t2))
```



- [A] <class 'list'>, 6 
- [B] <class 'tuple'>, 6 
- [C] <class 'tuple'>, 3 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Tuple `+` → yangi tuple qaytaradi: `(1,2,3,4,5,6)`. `type` → `tuple`. `len` → `6`.


---


## Savol 7



`sorted(tuple)` nima qaytaradi?



- [A] Tartiblangan tuple 
- [B] Tartiblangan list 
- [C] None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `sorted()` har doim **list** qaytaradi, tuple emas.


---


## Savol 8



Quyidagi kodning natijasi nima?

```python
d = {}
d[(1, 2)] = 'tuple kalit'
d[[1, 2]] = 'list kalit'
```



- [A] Ikkalasi ham ishlaydi 
- [B] Birinchi ishlaydi, ikkinchisi TypeError 
- [C] Ikkalasi ham TypeError 
- [D] List ustun turadi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Tuple hashable → kalit bo'la oladi. List mutable → `TypeError: unhashable type: 'list'`.


---


## Savol 9



Quyidagi kodning natijasi nima?

```python
d = {'ism': 'Sarvar', 'yosh': 22}
d['ball'] = 95
del d['yosh']
print(len(d))
```



- [A] 3 
- [B] 2 
- [C] 1 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `ball` qo'shiladi → 3 ta. `del d['yosh']` → o'chiriladi → `2`.


---


## Savol 10



Quyidagi kodning natijasi nima?

```python
d = dict.fromkeys(['a', 'b', 'c'])
print(d)
```



- [A] {'a':0,'b':0,'c':0} 
- [B] {'a':None,'b':None,'c':None} 
- [C] {} 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `fromkeys` standart qiymat ko'rsatilmasa `None` bo'ladi.


---


## Savol 11



Quyidagi kodning natijasi nima?

```python
d = {'a': 1, 'b': 2}
olindi = d.pop('b')
print(olindi)
print('b' in d)
```



- [A] 2, True 
- [B] 2, False 
- [C] None, False 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `pop('b')` — `'b'` o'chiriladi, `2` qaytaradi. `'b' in d` → yo'q → `False`.


---


## Savol 12



`return` va `print()` ning asosiy farqi nima?



- [A] Hech qanday farq yo'q 
- [B] `print()` ekranga chiqaradi; `return` qiymat qaytaradi, ekranga chiqarmaydi 
- [C] `return` faqat raqam qaytaradi 
- [D] `print()` qiymat qaytaradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `print(x)` — `x` ni ekranda ko'rsatadi. `return x` — `x` ni chaqirgan joyga qaytaradi.


---


## Savol 13



Standart qiymatli parametr qayerda yozilishi kerak?



- [A] Istalgan joyda 
- [B] Majburiy (standart qiymatsiz) parametrlardan oldin 
- [C] Majburiy (standart qiymatsiz) parametrlardan keyin 
- [D] Faqat bitta standart parametr bo'lishi mumkin 


> **To'g'ri javob:** C 
> **Tushuntirish:** `def f(a, b=2):` — to'g'ri. `def f(a=1, b):` — `SyntaxError`. Standart parametrlar majburiylardan keyin keladi.


---


## Savol 14



Pozitsion va kalit so'z argumentlari aralashtirilganda qaysi qoida?



- [A] Kalit so'z argumentlari har doim oldin kelishi kerak 
- [B] Pozitsion argumentlar kalit so'z argumentlaridan oldin kelishi shart 
- [C] Tartib umuman muhim emas 
- [D] Aralashtirib bo'lmaydi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `f(1, b=2)` — to'g'ri. `f(a=1, 2)` — `SyntaxError`. Pozitsionlar avval kelishi shart.


---


## Savol 15



Quyidagi kodning natijasi nima?

```python
def f(x):
    print(x)

x = f(42)
print(x)
```



- [A] 42, 42 
- [B] 42, None 
- [C] None, 42 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `f(42)` → `print(42)` chiqaradi, `None` qaytaradi. `x = None`. `print(x)` → `None`.


---


## Savol 16



Quyidagi kodning natijasi nima?

```python
r = [5, 10, 15]
print(15 in r)
print(7 in r)
```



- [A] True, True 
- [B] True, False 
- [C] False, True 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `15` listda bor → `True`. `7` listda yo'q → `False`.


---


## Savol 17



Quyidagi kodning natijasi nima?

```python
r = list(range(2, 10, 2))
print(r)
```



- [A] [2, 4, 6, 8, 10] 
- [B] [2, 4, 6, 8] 
- [C] [0, 2, 4, 6, 8] 
- [D] [2, 3, 4, 5, 6, 7, 8, 9] 


> **To'g'ri javob:** B 
> **Tushuntirish:** `range(2, 10, 2)` — 2 dan 8 gacha, 2 qadam: `2, 4, 6, 8`.


---


## Savol 18



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(r[1::3])
```



- [A] [1, 4, 7, 10] 
- [B] [2, 5, 8] 
- [C] [2, 4, 6, 8, 10] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `r[1::3]` — 1-indeksdan boshlab, 3 qadam: indeks 1, 4, 7 → `[2, 5, 8]`.


---


## Savol 19



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 6, 5, 4]
natija = sorted(r)
print(r)
print(natija)
```



- [A] [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6] 
- [B] [1, 2, 3, 6, 5, 4], [1, 2, 3, 4, 5, 6] 
- [C] [1, 2, 3, 4, 5, 6], [1, 2, 3, 6, 5, 4] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `sorted()` — yangi tartibli list qaytaradi, asl listni o'zgartirmaydi.


---


## Savol 20



Quyidagi kodning natijasi nima?

```python
r = ['a', 'b', 'c']
for i, x in enumerate(r, start=1):
    print(i, x)
```



- [A] 0 a, 1 b, 2 c 
- [B] 1 a, 2 b, 3 c 
- [C] a 1, b 2, c 3 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `enumerate(r, start=1)` — indeks `1` dan boshlanadi.


---


## Savol 21



Quyidagi kodning natijasi nima?

```python
t = (3, 1, 4, 1, 5)
print(t.count(1))
```



- [A] 1 
- [B] 2 
- [C] True 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `count(1)` — `1` necha marta uchragani: indeks 1 va 3 → `2`.


---


## Savol 22



Quyidagi kodning natijasi nima?

```python
ismlar = ('Ali', 'Vali', 'Gali')
balllar = (85, 92, 78)
for ism, ball in zip(ismlar, balllar):
    if ball > 88:
        print(ism)
```



- [A] Faqat Ali 
- [B] Faqat Vali 
- [C] Ali, Vali 
- [D] Hech narsa 


> **To'g'ri javob:** B 
> **Tushuntirish:** `85>88` → yo'q. `92>88` → `Vali`. `78>88` → yo'q. Faqat `Vali` chiqadi.


---


## Savol 23



Quyidagi kodning natijasi nima?

```python
t = (1, 2, 3)
r = list(t)
print(t is r)
print(t == r)
```



- [A] True, True 
- [B] False, False 
- [C] False, True 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** Boshqa-boshqa obyektlar → `is` → `False`. Qiymatlari teng → `==` → `True`.


---


## Savol 24



Quyidagi kodning natijasi nima?

```python
d = {}
for i in range(1, 4):
    d[i] = i * i
print(d[3])
```



- [A] 3 
- [B] 6 
- [C] 9 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `for` → `{1:1, 2:4, 3:9}`. `d[3]` → `9`.


---


## Savol 25



Quyidagi kodning natijasi nima?

```python
d = dict(zip('abc', [1, 2, 3]))
print(d)
```



- [A] {'a':1,'b':2,'c':3} 
- [B] {'abc':[1,2,3]} 
- [C] [('a',1),('b',2),('c',3)] 
- [D] Xato beradi 


> **To'g'ri javob:** A 
> **Tushuntirish:** `zip('abc', [1,2,3])` → `('a',1),('b',2),('c',3)`. `dict()` → `{'a':1,'b':2,'c':3}`.


---