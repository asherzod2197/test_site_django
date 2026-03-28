## Savol 1

Obyekt (object) nima?

- [A] Faqat raqamlardan iborat ma'lumot turi  
- [B] Classning aniq bir instansiyasi bo'lib, o'z atributlari va metodlariga ega  
- [C] Dasturning asosiy bloki, classga o'xshash  
- [D] Faqat funksiyalar to'plami  

> **To'g'ri javob:** B  
> **Tushuntirish:** Obyekt — bu classning konkret namunasi (instansiyasi). Class qolip bo'lsa, obyekt o'sha qolipdan yasalgan haqiqiy narsa hisoblanadi. Har bir obyektning o'ziga xos atributlari bo'ladi.

---

## Savol 2

Python'da obyekt qanday yaratiladi?

- [A] `object Mashina()`  
- [B] `new Mashina()`  
- [C] `Mashina()`  
- [D] `create Mashina()`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Python'da obyekt yaratish uchun class nomi yoziladi va qavs ochiladi: `Mashina()`. Bu `__init__` metodini avtomatik chaqiradi.

---

## Savol 3

Quyidagi kodda `ali` nima?

```python
class Talaba:
    def __init__(self, ism):
        self.ism = ism

ali = Talaba("Ali")
```

- [A] Class  
- [B] Funksiya  
- [C] `Talaba` classining obyekti  
- [D] Modul  

> **To'g'ri javob:** C  
> **Tushuntirish:** `ali = Talaba("Ali")` orqali `Talaba` classidan `ali` nomli obyekt yaratildi. `ali` endi `Talaba` classining bir instansiyasi hisoblanadi.

---

## Savol 4

Bir classdan nechta obyekt yaratish mumkin?

- [A] Faqat 1 ta  
- [B] Maksimal 10 ta  
- [C] Cheksiz miqdorda  
- [D] Faqat juft sonda  

> **To'g'ri javob:** C  
> **Tushuntirish:** Bir classdan xohlagan miqdorda obyekt yaratish mumkin. Har bir obyekt mustaqil bo'lib, o'zining atribut qiymatlariga ega bo'ladi.

---

## Savol 5

Quyidagi kodda `t1` va `t2` obyektlari bir xilmi?

```python
class Talaba:
    def __init__(self, ism):
        self.ism = ism

t1 = Talaba("Ali")
t2 = Talaba("Ali")
print(t1 == t2)
```

- [A] Ha, chunki ism qiymatlari bir xil  
- [B] Yo'q, ular xotiraning turli joylarida joylashgan alohida obyektlar  
- [C] Ha, Python avtomatik birlashtiradi  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `t1` va `t2` ism qiymatlari bir xil bo'lsa ham, xotiraning turli joylarida joylashgan alohida obyektlardir. Standart holatda `==` ularning manzillarini solishtiradi va `False` qaytaradi.

---

## Savol 6

Obyekt atributiga qanday murojaat qilinadi?

- [A] `obyekt->atribut`  
- [B] `obyekt::atribut`  
- [C] `obyekt.atribut`  
- [D] `obyekt[atribut]`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Python'da obyekt atributlariga nuqta (`.`) operatori orqali murojaat qilinadi: `obyekt.atribut`. Masalan: `ali.ism` yoki `mashina.rang`.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
class Kitob:
    def __init__(self, nomi, yil):
        self.nomi = nomi
        self.yil = yil

k = Kitob("O'tkan kunlar", 1925)
print(k.yil)
```

- [A] `O'tkan kunlar`  
- [B] `Kitob`  
- [C] `1925`  
- [D] `k`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Kitob("O'tkan kunlar", 1925)` chaqirilganda `self.yil = 1925` qiymati o'rnatiladi. Shuning uchun `k.yil` → `1925` chiqaradi.

---

## Savol 8

Obyektga yangi atribut qo'shish mumkinmi?

- [A] Yo'q, faqat `__init__` da belgilangan atributlar ishlatilishi mumkin  
- [B] Ha, obyekt yaratilgandan keyin ham yangi atribut qo'shish mumkin  
- [C] Faqat class ichida maxsus metod orqali qo'shish mumkin  
- [D] Faqat meros olish orqali mumkin  

> **To'g'ri javob:** B  
> **Tushuntirish:** Python'da obyektga keyin ham yangi atribut qo'shish mumkin: `ali.yosh = 20`. Lekin bu yaxshi amaliyot hisoblanmaydi, chunki boshqa obyektlarda bu atribut bo'lmaydi.

---

## Savol 9

`type()` funksiyasi obyektga nisbatan qanday ishlatiladi?

- [A] Obyektni boshqa turga o'zgartiradi  
- [B] Obyekt qaysi classga mansub ekanligini qaytaradi  
- [C] Obyektdagi metodlar sonini hisoblaydi  
- [D] Obyektni o'chiradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `type(obyekt)` — bu obyekt qaysi classdan yaratilganligini ko'rsatadi. Masalan, `type(ali)` → `<class 'Talaba'>` natijasini beradi.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
class Hisoblagich:
    def __init__(self):
        self.son = 0

    def oshir(self):
        self.son += 1

h = Hisoblagich()
h.oshir()
h.oshir()
h.oshir()
print(h.son)
```

- [A] `0`  
- [B] `1`  
- [C] `2`  
- [D] `3`  

> **To'g'ri javob:** D  
> **Tushuntirish:** `h` obyekti yaratilganda `self.son = 0`. `oshir()` metodi 3 marta chaqirilgani uchun `son` qiymati 3 ga yetadi. Natija `3`.

---

## Savol 11

Quyidagi kodda xato qayerda?

```python
class Uchburchak:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

u = Uchburchak(3, 4)
```

- [A] Class nomi noto'g'ri  
- [B] `__init__` da `self` yo'q  
- [C] Obyekt yaratishda 3 ta argument kerak, lekin 2 ta berilgan  
- [D] Xato yo'q  

> **To'g'ri javob:** C  
> **Tushuntirish:** `__init__` metodi `self` dan tashqari 3 ta parametr (`a`, `b`, `c`) talab qiladi. Lekin `Uchburchak(3, 4)` da faqat 2 ta argument berilgan. Bu `TypeError` xatosini keltirib chiqaradi.

---

## Savol 12

Obyekt metodini chaqirish uchun qaysi sintaksis to'g'ri?

- [A] `metodNomi(obyekt)`  
- [B] `obyekt->metodNomi()`  
- [C] `obyekt.metodNomi()`  
- [D] `call obyekt.metodNomi`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Python'da obyekt metodini chaqirish uchun nuqta operatori ishlatiladi: `obyekt.metodNomi()`. Masalan: `ali.gapir()` yoki `mashina.yur()`.

---

## Savol 13

Quyidagi kodda `id()` funksiyasi nima qaytaradi?

```python
class Nuqta:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n1 = Nuqta(1, 2)
n2 = Nuqta(1, 2)
print(id(n1) == id(n2))
```

- [A] `True`, chunki qiymatlari bir xil  
- [B] `False`, chunki ular xotiraning turli manzillarida  
- [C] Xato beradi  
- [D] `None`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `id()` funksiyasi obyektning xotiradagi manzilini qaytaradi. `n1` va `n2` alohida yaratilgan ikki obyekt bo'lgani uchun ularning manzillari farqli bo'ladi va natija `False` bo'ladi.

---

## Savol 14

Obyektni o'chirish uchun qanday operatordan foydalaniladi?

- [A] `remove(obyekt)`  
- [B] `destroy(obyekt)`  
- [C] `del obyekt`  
- [D] `free(obyekt)`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Python'da obyektni o'chirish (xotiradan bo'shatish) uchun `del` operatori ishlatiladi: `del ali`. Bu `__del__` destruktor metodini chaqiradi va obyektni garbage collector ga topshiradi.

---

## Savol 15

Quyidagi kodning natijasi nima?

```python
class Doira:
    def __init__(self, r):
        self.r = r

    def aylana_uzunligi(self):
        return 2 * 3.14 * self.r

d1 = Doira(10)
d2 = Doira(5)
print(d1.aylana_uzunligi())
print(d2.aylana_uzunligi())
```

- [A] `62.8` va `62.8`  
- [B] `62.8` va `31.400000000000002`  
- [C] `31.4` va `62.8`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `d1` uchun `2 * 3.14 * 10 = 62.8`, `d2` uchun `2 * 3.14 * 5 = 31.400000000000002` (floating point xususiyati). Har bir obyekt o'zining `r` qiymatiga ega bo'lgani uchun natijalar farqli chiqadi.

---