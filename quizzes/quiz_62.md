## Savol 1



Protsedural va OOP dasturlashning farqi nima?



- [A] Hech qanday farq yo'q 
- [B] Protsedural — funksiyalar ketma-ketligi, OOP — obyektlar va ularning o'zaro ta'siri 
- [C] OOP faqat raqamlar bilan ishlaydi 
- [D] Protsedural yangi, OOP eski paradigma 


> **To'g'ri javob:** B 
> **Tushuntirish:** Protsedural — kod funksiyalar ketma-ketligi. OOP — ma'lumot va xulq-atvor bitta obyektda birlashadi.


---


## Savol 2



Class nomini yozishda qaysi uslub tavsiya etiladi?



- [A] kichik_harf_bilan 
- [B] KATTA_HARF_BILAN 
- [C] CamelCase (har so'z bosh harf) 
- [D] camelCase 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da class nomlari CamelCase bilan yoziladi: `Mashina`, `BankHisobi`, `OnlineDokon`.


---


## Savol 3



Obyektlarning identifikatori (id) bir xil bo'ladimi?



- [A] Ha, barcha obyektlar bir xil id ga ega 
- [B] Yo'q, har bir obyektning o'z unique id si bor 
- [C] Faqat bir xil qiymatli obyektlar 
- [D] Id degan tushuncha yo'q 


> **To'g'ri javob:** B 
> **Tushuntirish:** Har bir obyektning o'z `id()` si bor — xotira manzili. Har safar yangi obyekt yaratilganda yangi id beriladi.


---


## Savol 4



Atributga qanday murojaat qilinadi?



- [A] obyekt->atribut 
- [B] obyekt::atribut 
- [C] obyekt.atribut 
- [D] obyekt[atribut] 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da atributga nuqta `.` orqali murojaat qilinadi: `obyekt.atribut`.


---


## Savol 5



Quyidagi kodning natijasi nima?

```python
class Kalkulyator:
    def qoshish(self, a, b):
        return a + b

k = Kalkulyator()
print(k.qoshish(3, 7))
```



- [A] None 
- [B] 37 
- [C] 10 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `k.qoshish(3, 7)` — `self=k`, `a=3`, `b=7`. `3 + 7 = 10`.


---


## Savol 6



Quyidagi kodning natijasi nima?

```python
class Toifa:
    def __init__(self):
        self.elementlar = []

t1 = Toifa()
t2 = Toifa()
t1.elementlar.append('a')
print(len(t1.elementlar))
print(len(t2.elementlar))
```



- [A] 1, 1 
- [B] 1, 0 
- [C] 0, 0 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Har obyekt uchun `__init__` da yangi `[]` yaratiladi. `t1.elementlar` va `t2.elementlar` — mustaqil listlar.


---


## Savol 7



Ikki obyektning instance atributlari bir-biriga ta'sir qiladimi?



- [A] Ha, har doim 
- [B] Yo'q, har bir obyekt o'zining mustaqil instance atributlariga ega 
- [C] Faqat mutable atributlar 
- [D] Faqat __init__ dan keyin 


> **To'g'ri javob:** B 
> **Tushuntirish:** Instance atributlar mustaqil. `m1.rang = 'ko'k'` → `m2.rang` o'zgarmaydi.


---


## Savol 8



Class atribut qayerda e'lon qilinadi?



- [A] Faqat __init__ ichida 
- [B] Class tanasida, metodlardan tashqarida 
- [C] Faqat class tashqarisida 
- [D] Istalgan joyda 


> **To'g'ri javob:** B 
> **Tushuntirish:** Class atribut class tanasida, lekin metodlar tashqarisida e'lon qilinadi.


---


## Savol 9



Atributni qidirishda Python qanday tartibda izlaydi?



- [A] Class atributdan, keyin instance atributdan 
- [B] Instance atributdan, keyin class atributdan 
- [C] Ikkisi bir vaqtda 
- [D] Istalgan tartibda 


> **To'g'ri javob:** B 
> **Tushuntirish:** Python avval instance atributini, topilmasa class atributini izlaydi (MRO — Method Resolution Order).


---


## Savol 10



Quyidagi kodning natijasi nima?

```python
class Konteyner:
    def __init__(self):
        self._qiymat = 42

k = Konteyner()
print(k._qiymat)
```



- [A] AttributeError 
- [B] None 
- [C] 42 
- [D] 0 


> **To'g'ri javob:** C 
> **Tushuntirish:** `_qiymat` — protected (konventsiya). Texnik jihatdan tashqaridan kirish mumkin: `k._qiymat` → `42`.


---


## Savol 11



Setter da tekshiruv (validation) nima uchun muhim?



- [A] Kodni qisqartirish uchun 
- [B] Noto'g'ri qiymatlar kiritilishini oldini olish uchun 
- [C] Atributni tezlashtirish uchun 
- [D] Faqat estetik sabab 


> **To'g'ri javob:** B 
> **Tushuntirish:** Setter da tekshiruv — noto'g'ri qiymatlar (manfiy yosh, noto'g'ri format) kiritilishini oldini oladi.


---


## Savol 12



Quyidagi kodning natijasi nima?

```python
class Shakl:
    def yuza(self):
        return 'Hisoblanmadi'

class Kvadrat(Shakl):
    def __init__(self, t):
        self.t = t

    def yuza(self):
        return self.t ** 2

k = Kvadrat(5)
print(k.yuza())
```



- [A] Hisoblanmadi 
- [B] 5 
- [C] 25 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `Kvadrat` classi `yuza()` ni override qilgan. `k.yuza()` → `5**2 = 25`.


---


## Savol 13



`super()` faqat `__init__` da ishlatilishi mumkinmi?



- [A] Ha, faqat __init__ da 
- [B] Yo'q — istalgan metodda ota classning metodini chaqirish uchun ishlatiladi 
- [C] Faqat override qilingan metodlarda 
- [D] Faqat ko'p merosda 


> **To'g'ri javob:** B 
> **Tushuntirish:** `super()` istalgan metodda ishlatilishi mumkin: `super().method_name()`.


---


## Savol 14



Quyidagi kodning natijasi nima?

```python
class Mashina:
    pass

m = Mashina()
print(type(m))
```



- [A] <class 'type'> 
- [B] <class '__main__.Mashina'> 
- [C] <class 'object'> 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `type(m)` — `m` ning classi: `<class '__main__.Mashina'>`.


---


## Savol 15



Quyidagi kodning natijasi nima?

```python
class Test:
    qiymat = 5

print(Test.qiymat)
Test.qiymat = 99
print(Test.qiymat)
```



- [A] 5, 5 
- [B] 5, 99 
- [C] 99, 99 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Class atributini o'zgartirish mumkin: birinchi `5`, keyin `99`.


---


## Savol 16



Quyidagi kodning natijasi nima?

```python
class Box:
    count = 0

b1 = Box()
b2 = Box()
b3 = Box()
print(Box.count)
```



- [A] 3 
- [B] 0 
- [C] 1 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `count = 0` — class atributi, obyekt yaratish uni o'zgartirmaydi. `Box.count` → `0`.


---


## Savol 17



Quyidagi kodning natijasi nima?

```python
class Tovar:
    kategoriya = 'Oziq-ovqat'

t1 = Tovar()
t2 = Tovar()
t1.kategoriya = 'Kiyim'
print(Tovar.kategoriya)
print(t1.kategoriya)
print(t2.kategoriya)
```



- [A] Kiyim, Kiyim, Kiyim 
- [B] Oziq-ovqat, Kiyim, Oziq-ovqat 
- [C] Oziq-ovqat, Oziq-ovqat, Oziq-ovqat 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `t1.kategoriya = 'Kiyim'` — faqat `t1` ga instance atribut. `Tovar` va `t2` o'zgarmaydi.


---


## Savol 18



Metod ichidan boshqa metodini chaqirish uchun nima yoziladi?



- [A] method_nomi() 
- [B] self->method_nomi() 
- [C] self.method_nomi() 
- [D] this.method_nomi() 


> **To'g'ri javob:** C 
> **Tushuntirish:** Metod ichidan boshqa metodga `self.method_nomi()` orqali murojaat qilinadi.


---


## Savol 19



Quyidagi kodning natijasi nima?

```python
class Parol:
    def __init__(self, uzunlik=8):
        self.uzunlik = uzunlik
        self.kuchli = uzunlik >= 12

p1 = Parol()
p2 = Parol(16)
print(p1.kuchli)
print(p2.kuchli)
```



- [A] True, True 
- [B] False, True 
- [C] True, False 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `p1`: `uzunlik=8` → `8>=12` → `False`. `p2`: `uzunlik=16` → `16>=12` → `True`.


---


## Savol 20



Quyidagi kodning natijasi nima?

```python
class Yozuvchi:
    def __init__(self, ism):
        self.ism = ism
        self.asarlar = []

    def yoz(self, asar):
        self.asarlar.append(asar)

y = Yozuvchi('Navoiy')
y.yoz('Xamsa')
y.yoz('Farhod va Shirin')
print(len(y.asarlar))
```



- [A] 0 
- [B] 1 
- [C] 2 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `yoz` metodi `self.asarlar` ga element qo'shadi. 2 marta chaqirildi → `len = 2`.


---


## Savol 21



Quyidagi kodning natijasi nima?

```python
class Config:
    debug = False
    versiya = '1.0'

print(Config.__dict__['debug'])
print(Config.__dict__['versiya'])
```



- [A] True, 1.0 
- [B] False, '1.0' 
- [C] None, None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `Config.__dict__` class atributlarini dict sifatida qaytaradi. `debug` → `False`, `versiya` → `'1.0'`.


---


## Savol 22



Quyidagi kodning natijasi nima?

```python
class Sozlama:
    til = 'uz'

s1 = Sozlama()
s2 = Sozlama()
Sozlama.til = 'en'
print(s1.til)
print(s2.til)
```



- [A] uz, uz 
- [B] en, en 
- [C] uz, en 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `Sozlama.til = 'en'` — class atributini o'zgartiradi. Barcha instansiyalar yangi qiymat `'en'` ni oladi.


---


## Savol 23



Quyidagi kodning natijasi nima?

```python
class Karta:
    def __init__(self, raqam):
        self.__raqam = raqam

    def __str__(self):
        return f'**** **** **** {self.__raqam[-4:]}'

k = Karta('1234567890123456')
print(k)
```



- [A] 1234567890123456 
- [B] **** **** **** 3456 
- [C] AttributeError 
- [D] None 


> **To'g'ri javob:** B 
> **Tushuntirish:** `__str__` — `print(k)` chaqirilganda ishlaydi. `self.__raqam[-4:]` → `'3456'`.


---


## Savol 24



Quyidagi kodning natijasi nima?

```python
class Mahsulot:
    def __init__(self, narx):
        self._narx = narx

    def get_narx(self):
        return f'{self._narx:,} so\'m'

m = Mahsulot(150000)
print(m.get_narx())
```



- [A] 150000 
- [B] 150,000 so'm 
- [C] None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `f'{150000:,}'` → `'150,000'`. Natija: `'150,000 so'm'`.


---


## Savol 25



Quyidagi kodning natijasi nima?

```python
class Transport:
    def __init__(self, nomi, tezlik):
        self.nomi = nomi
        self.tezlik = tezlik

class Velosiped(Transport):
    def __init__(self, nomi, tezlik, g_soni):
        super().__init__(nomi, tezlik)
        self.g_soni = g_soni

v = Velosiped('Trek', 30, 21)
print(v.nomi, v.tezlik, v.g_soni)
```



- [A] Xato beradi 
- [B] Trek 30 21 
- [C] None None 21 
- [D] Trek None 21 


> **To'g'ri javob:** B 
> **Tushuntirish:** `super().__init__(nomi, tezlik)` ota classni chaqiradi. Barcha atributlar o'rnatiladi.


---