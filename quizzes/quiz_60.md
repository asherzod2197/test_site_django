## Savol 1



OOP dan foydalanishning asosiy sababi nima?



- [A] Kodni qisqartirish 
- [B] Kodni qayta ishlatish, tartibli va kengaytiriladigan qilish 
- [C] Faqat grafik interfeyslar yaratish 
- [D] Dasturni tezlashtirish 


> **To'g'ri javob:** B 
> **Tushuntirish:** OOP — kodni qayta ishlatish (reusability), tartiblilik (modularity) va kengaytirish (scalability) imkonini beradi.


---


## Savol 2



Quyidagi kodda xato bormi?

```python
class Hayvon:
    pass
```



- [A] Ha, `pass` ishlatib bo'lmaydi 
- [B] Ha, atribut bo'lishi shart 
- [C] Yo'q — `pass` bo'sh class uchun to'g'ri 
- [D] Ha, `class` kichik harf bilan yozilishi kerak 


> **To'g'ri javob:** C 
> **Tushuntirish:** `pass` — hozircha bo'sh class yaratish uchun ishlatiladi. Bu to'liq to'g'ri sintaksis.


---


## Savol 3



Bir classdan nechta obyekt yaratish mumkin?



- [A] Faqat bitta 
- [B] Faqat ikkita 
- [C] Istalgancha 
- [D] Faqat 100 ta 


> **To'g'ri javob:** C 
> **Tushuntirish:** Bir classdan istalgancha obyekt yaratish mumkin. Har bir obyekt mustaqil.


---


## Savol 4



Instance atribut va class atributning farqi nima?



- [A] Hech qanday farq yo'q 
- [B] Instance atribut — har obyektga xos, class atribut — barcha obyektlar uchun umumiy 
- [C] Class atribut tezroq ishlaydi 
- [D] Instance atribut faqat `__init__` da bo'ladi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Class atribut — barcha instansiyalarga umumiy. Instance atribut — faqat o'sha obyektga xos.


---


## Savol 5



Quyidagi kodning natijasi nima?

```python
class Salom:
    def ayt(self):
        return 'Assalomu alaykum!'

s = Salom()
print(s.ayt())
```



- [A] Xato beradi 
- [B] None 
- [C] Assalomu alaykum! 
- [D] ayt 


> **To'g'ri javob:** C 
> **Tushuntirish:** `s.ayt()` — `Salom` classining `ayt` metodini chaqiradi → `'Assalomu alaykum!'`.


---


## Savol 6



`__init__` ning `self` dan keyin qo'shimcha parametrlari bo'lishi shartmi?



- [A] Ha, har doim kerak 
- [B] Yo'q, ixtiyoriy — kerak bo'lsa qo'shiladi 
- [C] Faqat bitta parametr bo'lishi mumkin 
- [D] Faqat standart qiymatli parametrlar 


> **To'g'ri javob:** B 
> **Tushuntirish:** `__init__(self)` — to'liq to'g'ri. Qo'shimcha parametrlar ixtiyoriy.


---


## Savol 7



Instance atributlarni `__dict__` bilan ko'rish mumkinmi?



- [A] Yo'q 
- [B] Ha, `obyekt.__dict__` — instance atributlar lug'atini qaytaradi 
- [C] Faqat maxsus metod orqali 
- [D] Faqat `dir()` bilan 


> **To'g'ri javob:** B 
> **Tushuntirish:** `obyekt.__dict__` → `{'ism': 'Ali', 'yosh': 25}` ko'rinishida instance atributlarni qaytaradi.


---


## Savol 8



Class atributini qanday o'zgartirish kerak?



- [A] Istalgan obyekt orqali 
- [B] Class nomi orqali: `ClassName.atribut = yangi_qiymat` 
- [C] Faqat __init__ ichida 
- [D] Faqat classni qayta e'lon qilib 


> **To'g'ri javob:** B 
> **Tushuntirish:** `ClassName.atribut = yangi` — to'g'ri usul. Obyekt orqali o'zgartirish faqat o'sha obyekt uchun instance atribut yaratadi.


---


## Savol 9



Obyekt orqali class atributini o'zgartirsak nima bo'ladi?



- [A] Class atributi o'zgaradi 
- [B] Faqat o'sha obyektga instance atribut yaratiladi, class atribut o'zgarmaydi 
- [C] Xato beradi 
- [D] Barcha obyektlar uchun o'zgaradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `obj.class_attr = yangi` — faqat `obj` ga instance atribut yaratadi. Class atribut o'zgarmaydi.


---


## Savol 10



Quyidagi kodning natijasi nima?

```python
class Bank:
    def __init__(self, balans):
        self.__balans = balans

b = Bank(100000)
print(b.__balans)
```



- [A] 100000 
- [B] None 
- [C] AttributeError 
- [D] 0 


> **To'g'ri javob:** C 
> **Tushuntirish:** `__balans` — private. Tashqaridan `b.__balans` → `AttributeError`. Python uni `_Bank__balans` ga o'zgartiradi.


---


## Savol 11



Python da `@property` dekoratori nima uchun ishlatiladi?



- [A] Metodni o'chirish uchun 
- [B] Metodga atribut kabi murojaat qilish imkonini beruvchi getter yaratadi 
- [C] Faqat class metodlari uchun 
- [D] Atributlarni yashirish uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** `@property` — metodga `obyekt.metod` (qavsiz) murojaat qilish imkonini beradi. Getter uchun ishlatiladi.


---


## Savol 12



Quyidagi kodning natijasi nima?

```python
class Hayvon:
    def nafas_ol(self):
        return 'Nafas olmoqda'

class It(Hayvon):
    def vov(self):
        return 'Vov-vov!'

i = It()
print(i.nafas_ol())
print(i.vov())
```



- [A] Xato beradi 
- [B] Nafas olmoqda, Vov-vov! 
- [C] None, Vov-vov! 
- [D] Nafas olmoqda, None 


> **To'g'ri javob:** B 
> **Tushuntirish:** `It` classi `Hayvon` dan meros olgan → `nafas_ol()` ham ishlaydi. `'Nafas olmoqda'`, `'Vov-vov!'`.


---


## Savol 13



`super()` ishlatmasak `__init__` da nima muammo bo'ladi?



- [A] Hech qanday muammo yo'q 
- [B] Ota classning `__init__` chaqirilmaydi → ota class atributlari o'rnatilmaydi 
- [C] Farzand class ishlashni to'xtatadi 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `super().__init__()` chaqirilmasa, ota classning atributlari yaratilmaydi → keyin ularni ishlatmoqchi bo'lsak `AttributeError`.


---


## Savol 14



Quyidagi qaysi misol OOP konsepsiyasini eng yaxshi ifodalaydi?



- [A] Raqamlar ro'yxati 
- [B] Avtomobil — rangi, tezligi bor (atributlar), yuradi, to'xtaydi (metodlar) 
- [C] Matematik formula 
- [D] Fayl o'qish funksiyasi 


> **To'g'ri javob:** B 
> **Tushuntirish:** OOP real dunyo obyektlarini modellashtiradi. Avtomobil — atributlari (rang, tezlik) va metodlari (yur, to'xta) bor.


---


## Savol 15



Class va funksiya o'rtasidagi asosiy farq nima?



- [A] Hech qanday farq yo'q 
- [B] Class — atributlar va metodlarni birlashtiruvchi tuzilma, funksiya — faqat amallar bajaradi 
- [C] Funksiya tezroq ishlaydi 
- [D] Class faqat raqamlar bilan ishlaydi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Class — ma'lumot (atributlar) va xulq-atvor (metodlar) ni birlashtiradi. Funksiya — faqat amallar bajaradi.


---


## Savol 16



Quyidagi kodning natijasi nima?

```python
class Kalit:
    pass

k = Kalit()
k.rang = 'sariq'
print(k.rang)
```



- [A] Xato beradi 
- [B] None 
- [C] sariq 
- [D] '' 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da obyektga dinamik atribut qo'shish mumkin: `k.rang = 'sariq'`. `print(k.rang)` → `'sariq'`.


---


## Savol 17



Quyidagi kodning natijasi nima?

```python
class Mehmon:
    pass

m = Mehmon()
m.ism = 'Zulfiya'
m.yosh = 25
print(hasattr(m, 'ism'))
print(hasattr(m, 'manzil'))
```



- [A] True, True 
- [B] True, False 
- [C] False, True 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `ism` atributi bor → `True`. `manzil` atributi yo'q → `False`.


---


## Savol 18



Quyidagi kodning natijasi nima?

```python
class Hisoblagich:
    soni = 0

    def oshir(self):
        self.soni += 1

h = Hisoblagich()
h.oshir()
h.oshir()
h.oshir()
print(h.soni)
```



- [A] 0 
- [B] 1 
- [C] 3 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `oshir()` har chaqirilganda `h.soni` ga 1 qo'shadi. 3 marta → `3`.


---


## Savol 19



Quyidagi kodning natijasi nima?

```python
class Sanoq:
    umumiy = 0

    def __init__(self, ism):
        self.ism = ism
        Sanoq.umumiy += 1

a = Sanoq('Ali')
b = Sanoq('Vali')
c = Sanoq('Gali')
print(Sanoq.umumiy)
```



- [A] 0 
- [B] 1 
- [C] 3 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** Har `__init__` chaqirilganda `Sanoq.umumiy` 1 ga oshadi. 3 ta obyekt → `3`.


---


## Savol 20



`self` orqali yaratilmagan o'zgaruvchi instance atributmi?



- [A] Ha, class ichidagi har bir o'zgaruvchi 
- [B] Yo'q — `self.nom = qiymat` ko'rinishida yaratilganlargina instance atribut 
- [C] Faqat __init__ ichidagilar 
- [D] Faqat public o'zgaruvchilar 


> **To'g'ri javob:** B 
> **Tushuntirish:** `self.x = 5` — instance atribut. `x = 5` — lokal o'zgaruvchi yoki class atribut.


---


## Savol 21



Quyidagi kodning natijasi nima?

```python
class Til:
    versiya = 3.11

t1 = Til()
t2 = Til()
Til.versiya = 3.12
print(t1.versiya)
print(t2.versiya)
```



- [A] 3.11, 3.11 
- [B] 3.12, 3.12 
- [C] 3.11, 3.12 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `Til.versiya = 3.12` — class atributini o'zgartiradi. Barcha instansiyalar yangi qiymatni oladi.


---


## Savol 22



Class atribut mutable (list, dict) bo'lsa qanday muammo chiqishi mumkin?



- [A] Hech qanday muammo yo'q 
- [B] Barcha instansiyalar bir xil mutable obyektga reference bo'ladi — biri o'zgartirsa hammasi o'zgaradi 
- [C] Faqat birinchi instansiya o'zgartira oladi 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Class atribut list bo'lsa: `obj.list.append(x)` — barcha instansiyalar uchun o'zgaradi. Har obyektga alohida list uchun `__init__` da `self.list = []` kerak.


---


## Savol 23



Encapsulation nimani ta'minlaydi?



- [A] Kodni qisqartiradi 
- [B] Ma'lumotlarning yaxlitligini va xavfsizligini ta'minlaydi 
- [C] Dasturni tezlashtiradi 
- [D] Faqat xatoliklarni kamaytiradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Encapsulation — ma'lumotlarni yashirish orqali to'g'ridan-to'g'ri o'zgartirishdan himoya qiladi.


---


## Savol 24



Quyidagi kodda `@property` va `@x.setter` to'g'ri tartibda yozilganmi?

```python
class A:
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val
```



- [A] Yo'q, setter oldin kelishi kerak 
- [B] Ha, to'g'ri tartib — avval @property, keyin @nom.setter 
- [C] Yo'q, ikkalasi bir funksiya bo'lishi kerak 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** To'g'ri tartib: avval `@property` (getter), keyin `@property_nomi.setter`. Aks holda `AttributeError`.


---


## Savol 25



Quyidagi kodning natijasi nima?

```python
class Ota:
    def kim(self):
        return 'Ota'

class Farzand(Ota):
    pass

f = Farzand()
print(f.kim())
```



- [A] Xato beradi 
- [B] None 
- [C] Farzand 
- [D] Ota 


> **To'g'ri javob:** D 
> **Tushuntirish:** `Farzand` classida `kim()` yo'q → ota classdan qidiradi → `'Ota'`.


---