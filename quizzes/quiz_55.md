## Savol 1



Bo'sh list qanday yaratiladi?



- [A] list = {} 
- [B] list = () 
- [C] list = [] 
- [D] list = '' 


> **To'g'ri javob:** C 
> **Tushuntirish:** `[]` yoki `list()` — bo'sh list yaratadi. `{}` — dict/set, `()` — tuple.


---


## Savol 2



Quyidagi kodning natijasi nima?

```python
r = [0] * 3 + [1] * 3
print(r)
```



- [A] [0, 1, 0, 1, 0, 1] 
- [B] [0, 0, 0, 1, 1, 1] 
- [C] [0, 3, 1, 3] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `[0]*3` → `[0, 0, 0]`. `[1]*3` → `[1, 1, 1]`. Birlashtirish: `[0, 0, 0, 1, 1, 1]`.


---


## Savol 3



Quyidagi kodning natijasi nima?

```python
r = [10, 20, 30, 40]
print(r[100:])
```



- [A] IndexError 
- [B] [40] 
- [C] [] 
- [D] None 


> **To'g'ri javob:** C 
> **Tushuntirish:** Slicingda chegaradan tashqari indeks xato bermaydi — bo'sh list qaytaradi.


---


## Savol 4



Quyidagi kodning natijasi nima?

```python
r = [3, 1, 4, 1, 5]
natija = r.sort()
print(r)
print(natija)
```



- [A] [1, 1, 3, 4, 5], [1, 1, 3, 4, 5] 
- [B] [3, 1, 4, 1, 5], None 
- [C] [1, 1, 3, 4, 5], None 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `sort()` — in-place o'zgartiradi va `None` qaytaradi. `r` tartiblanadi, `natija = None`.


---


## Savol 5



Quyidagi kodning natijasi nima?

```python
r = [1, 2, 3, 4, 5]
for x in r:
    if x == 3:
        break
    print(x)
```



- [A] 1, 2, 3 
- [B] 1, 2 
- [C] 3, 4, 5 
- [D] 1, 2, 3, 4, 5 


> **To'g'ri javob:** B 
> **Tushuntirish:** `break` — `x==3` bo'lganda tsiklni to'xtatadi. `1`, `2` chiqadi, `3` chiqmaydi.


---


## Savol 6



Tuple e'lon qilishning to'g'ri sintaksisi qaysi?



- [A] t = [1, 2, 3] 
- [B] t = {1, 2, 3} 
- [C] t = (1, 2, 3) 
- [D] t = <1, 2, 3> 


> **To'g'ri javob:** C 
> **Tushuntirish:** Tuple dumaloq qavslar `()` bilan yaratiladi. `[]` — list, `{}` — set/dict.


---


## Savol 7



Quyidagi kodning natijasi nima?

```python
t = (10, 20, 30, 40, 50)
print(t[1:4])
print(type(t[1:4]))
```



- [A] [20, 30, 40], list 
- [B] (20, 30, 40), tuple 
- [C] (10, 20, 30), tuple 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Tuple slicing → tuple qaytaradi: `(20, 30, 40)`, `type` → `tuple`.


---


## Savol 8



`b = a` bilan nusxa olish listda qanday muammo tug'diradi?



- [A] Hech qanday muammo yo'q 
- [B] Yangi mustaqil list yaratadi 
- [C] Havola (reference) yaratadi — biri o'zgarganda ikkinchisi ham o'zgaradi 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `b = a` — reference. `b.append(x)` → `a` ham o'zgaradi. Mustaqil nusxa: `b = a.copy()`.


---


## Savol 9



Quyidagi kodning natijasi nima?

```python
d = {'a': 1, 'b': 2}
print('a' in d)
print(1 in d)
```



- [A] True, True 
- [B] True, False 
- [C] False, True 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `in` dictionary da faqat **kalitlarni** tekshiradi. `'a'` kalit → `True`. `1` kalit emas → `False`.


---


## Savol 10



Quyidagi kodning natijasi nima?

```python
d = {'a': 1}
d.update(b=2, c=3)
print(len(d))
```



- [A] 1 
- [B] 2 
- [C] 3 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `update(b=2, c=3)` — `'b'` va `'c'` qo'shiladi → jami `3` ta.


---


## Savol 11



Quyidagi kodning natijasi nima?

```python
d = {'a': 1, 'b': 2, 'c': 3}
d.clear()
print(d)
```



- [A] None 
- [B] {} 
- [C] Xato beradi 
- [D] {'a':1,'b':2,'c':3} 


> **To'g'ri javob:** B 
> **Tushuntirish:** `clear()` — barcha elementlarni o'chiradi, dictionary saqlanadi. `d = {}`.


---


## Savol 12



Quyidagi kodning natijasi nima?

```python
def f(x):
    return x + 1

print(f(f(f(1))))
```



- [A] 2 
- [B] 3 
- [C] 4 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `f(1)=2`, `f(2)=3`, `f(3)=4`.


---


## Savol 13



Quyidagi kodning natijasi nima?

```python
def kopaytir(a, b=2):
    return a * b

print(kopaytir(5))
print(kopaytir(3, 4))
```



- [A] 10, 12 
- [B] 5, 12 
- [C] 10, 7 
- [D] Xato beradi 


> **To'g'ri javob:** A 
> **Tushuntirish:** `kopaytir(5)` → `b=2` standart → `10`. `kopaytir(3, 4)` → `b=4` → `12`.


---


## Savol 14



Quyidagi kodning natijasi nima?

```python
def f(a, b=5, c=10):
    print(a, b, c)

f(1)
f(1, 2)
f(1, c=3)
```



- [A] 1 5 10, 1 2 10, 1 5 3 
- [B] 1 5 10, 1 2 5, 1 5 3 
- [C] 1 5 10, 1 2 10, 1 3 10 
- [D] Xato beradi 


> **To'g'ri javob:** A 
> **Tushuntirish:** `f(1)` → standartlar. `f(1,2)` → `b=2`. `f(1, c=3)` → `b=5` standart, `c=3`.


---


## Savol 15



Returnsiz funksiya natijasini raqamli amallarda ishlatsa nima bo'ladi?



- [A] Avtomatik `0` ga aylanadi 
- [B] `None + son` → `TypeError` 
- [C] Bo'sh string sifatida ishlaydi 
- [D] Hech narsa bo'lmaydi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `None + 5` → `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`.


---


## Savol 16



Listda indekslash qaysi raqamdan boshlanadi?



- [A] 1 
- [B] -1 
- [C] 0 
- [D] Listning uzunligidan 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da indekslash `0` dan boshlanadi. Birinchi element `[0]`, ikkinchisi `[1]`.


---


## Savol 17



Quyidagi kodning natijasi nima?

```python
a = [1, 2, 3]
b = [4, 5]
print(a + b)
```



- [A] [1, 2, 3, 4, 5] 
- [B] [[1, 2, 3], [4, 5]] 
- [C] [5, 7] 
- [D] Xato beradi 


> **To'g'ri javob:** A 
> **Tushuntirish:** `+` operatori ikkala listni birlashtiradi: `[1, 2, 3, 4, 5]`.


---


## Savol 18



Quyidagi kodning natijasi nima?

```python
r = ['a', 'b', 'c', 'd', 'e']
print(r[::-1])
```



- [A] ['a', 'b', 'c', 'd', 'e'] 
- [B] ['e', 'd', 'c', 'b', 'a'] 
- [C] ['e', 'd'] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `[::-1]` — qadam `-1`, ya'ni teskari tartibda o'qiydi.


---


## Savol 19



Quyidagi kodning natijasi nima?

```python
r = [3, 1, 4, 1, 5, 9]
r.sort()
print(r[0], r[-1])
```



- [A] 3, 9 
- [B] 1, 9 
- [C] 9, 1 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `sort()` — o'sish tartibida: `[1, 1, 3, 4, 5, 9]`. `r[0]=1`, `r[-1]=9`.


---


## Savol 20



`in` operatori listda nima tekshiradi?



- [A] Elementning indeksini 
- [B] Element listda mavjud yoki yo'qligini — True/False qaytaradi 
- [C] Elementlar sonini 
- [D] Faqat raqamli elementlar uchun ishlaydi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `x in list` → `x` listda bo'lsa `True`, bo'lmasa `False` qaytaradi.


---


## Savol 21



Quyidagi kodning natijasi nima?

```python
t = ()
print(type(t))
print(len(t))
```



- [A] <class 'set'>, 0 
- [B] <class 'tuple'>, 0 
- [C] <class 'tuple'>, 1 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `()` — bo'sh tuple. `type` → `tuple`. `len` → `0`.


---


## Savol 22



`tuple('Python')` natijasi nima?



- [A] ('Python',) 
- [B] ('P', 'y', 't', 'h', 'o', 'n') 
- [C] TypeError 
- [D] ['P', 'y', 't', 'h', 'o', 'n'] 


> **To'g'ri javob:** B 
> **Tushuntirish:** `tuple(iterable)` — har bir belgini alohida element qiladi: 6 elementli tuple.


---


## Savol 23



Qaysi metodlar faqat listda bor, tupled emas?



- [A] count(), index() 
- [B] len(), in 
- [C] append(), remove(), sort(), pop() 
- [D] +, * 


> **To'g'ri javob:** C 
> **Tushuntirish:** O'zgartiruvchi metodlar faqat mutable listda bor. Tuple o'zgarmaydi, shuning uchun bu metodlar unga qo'shilmagan.


---


## Savol 24



Quyidagi kodning natijasi nima?

```python
d = {'a': 1, 'b': 2}
print(d.get('c', 0))
```



- [A] KeyError 
- [B] None 
- [C] 0 
- [D] 'c' 


> **To'g'ri javob:** C 
> **Tushuntirish:** `get('c', 0)` — `'c'` kalit yo'q, standart qiymat `0` qaytaradi.


---


## Savol 25



Quyidagi kodning natijasi nima?

```python
k = ['x', 'y', 'z']
v = [1, 2, 3]
d = dict(zip(k, v))
print(d['y'])
```



- [A] 1 
- [B] 2 
- [C] 3 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `zip(k, v)` → `[('x',1),('y',2),('z',3)]`. `dict()` → `{'x':1,'y':2,'z':3}`. `d['y']` → `2`.


---