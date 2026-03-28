## Savol 1



OOP da 'class' nima?



- [A] O'zgaruvchilar to'plami 
- [B] Funksiyalar to'plami 
- [C] Obyektlarni yaratish uchun qolip (shablon) 
- [D] Python moduli 


> **To'g'ri javob:** C 
> **Tushuntirish:** Class — obyektlar uchun qolip. U atributlar (ma'lumot) va metodlar (xulq-atvor) ni birlashtiradi.


---


## Savol 2



Bir Python faylida nechta class yozish mumkin?



- [A] Faqat bitta 
- [B] Faqat ikkita 
- [C] Istalgancha 
- [D] Faqat 10 ta 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da bir faylda istalgancha class yozish mumkin. Lekin har bir class alohida faylda bo'lishi yaxshi amaliyot.


---


## Savol 3



Quyidagi kodning natijasi nima?

```python
class Nuqta:
    x = 0
    y = 0

n1 = Nuqta()
n2 = Nuqta()
print(n1 is n2)
```



- [A] True 
- [B] False 
- [C] None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Ikki alohida yaratilgan obyekt — boshqa-boshqa xotira joylari. `n1 is n2` → `False`.


---


## Savol 4



Quyidagi kodning natijasi nima?

```python
class Shahar:
    aholi = 0

sh = Shahar()
sh.nomi = 'Toshkent'
sh.aholi = 3000000
print(Shahar.aholi)
print(sh.aholi)
```



- [A] 3000000, 3000000 
- [B] 0, 3000000 
- [C] 3000000, 0 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `sh.aholi = 3000000` — `sh` ga instance atribut. `Shahar.aholi` — class atributi o'zgarmaydi → `0`.


---


## Savol 5



Quyidagi kodning natijasi nima?

```python
class Matn:
    def bosh_harf(self, s):
        return s.upper()
    
    def oxiri(self, s):
        return s[-1]

m = Matn()
print(m.bosh_harf('salom'))
print(m.oxiri('Python'))
```



- [A] SALOM, P 
- [B] salom, n 
- [C] SALOM, n 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `'salom'.upper()` → `'SALOM'`. `'Python'[-1]` → `'n'`.


---


## Savol 6



`__init__` biror qiymat qaytara oladimi?



- [A] Ha, istalgan qiymat 
- [B] Faqat None — boshqa qiymat qaytarsa TypeError 
- [C] Faqat True yoki False 
- [D] Faqat int 


> **To'g'ri javob:** B 
> **Tushuntirish:** `__init__` `None` dan boshqa qiymat qaytarsa `TypeError: __init__() should return None` xatosi chiqadi.


---


## Savol 7



Quyidagi kodning natijasi nima?

```python
class Hisobvar:
    def __init__(self, egasi, balans):
        self.egasi = egasi
        self.balans = balans

    def tolov(self, summa):
        self.balans -= summa

h = Hisobvar('Ali', 100000)
h.tolov(30000)
print(h.balans)
```



- [A] 100000 
- [B] 70000 
- [C] 30000 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `self.balans = 100000`. `tolov(30000)` → `100000 - 30000 = 70000`.


---


## Savol 8



Quyidagi kodning natijasi nima?

```python
class Planeta:
    yulduz = 'Quyosh'

Planeta.yulduz = 'Sirius'
p = Planeta()
print(p.yulduz)
```



- [A] Quyosh 
- [B] Sirius 
- [C] None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `Planeta.yulduz = 'Sirius'` — class atributini o'zgartiradi. Barcha instansiyalar yangi qiymatni oladi.


---


## Savol 9



Quyidagi kodning natijasi nima?

```python
class Shahar:
    davlat = "O'zbekiston"

    def __init__(self, nomi):
        self.nomi = nomi

s = Shahar('Toshkent')
print(s.__dict__)
```



- [A] {'nomi': 'Toshkent', 'davlat': "O'zbekiston"} 
- [B] {'nomi': 'Toshkent'} 
- [C] {'davlat': "O'zbekiston"} 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `s.__dict__` — faqat instance atributlarni qaytaradi: `{'nomi': 'Toshkent'}`.


---


## Savol 10



Name mangling nima?



- [A] Atribut nomini o'chirish 
- [B] Python ning `__x` atributini `_ClassName__x` ga o'zgartirishi 
- [C] Metodlarni yashirish 
- [D] Class nomini o'zgartirish 


> **To'g'ri javob:** B 
> **Tushuntirish:** Name mangling: `self.__x` → Python ichida `_ClassName__x` sifatida saqlanadi. Bu accidental access dan himoya qiladi.


---


## Savol 11



Quyidagi kodning natijasi nima?

```python
class Harorat:
    def __init__(self, celsius):
        self.__celsius = celsius

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, qiymat):
        if qiymat < -273.15:
            print('Xato!')
        else:
            self.__celsius = qiymat

h = Harorat(25)
h.set_celsius(-300)
print(h.get_celsius())
```



- [A] 25 
- [B] -300 
- [C] Xato! va 25 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `-300 < -273.15` → `print('Xato!')`, `self.__celsius` o'zgarmaydi → `25`.


---


## Savol 12



Quyidagi kodning natijasi nima?

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

obj = C()
print(isinstance(obj, A))
print(isinstance(obj, B))
```



- [A] False, False 
- [B] True, False 
- [C] False, True 
- [D] True, True 


> **To'g'ri javob:** D 
> **Tushuntirish:** `C → B → A` meros zanjiri. `isinstance(obj, A)` → `True`. `isinstance(obj, B)` → `True`.


---


## Savol 13



Quyidagi kodning natijasi nima?

```python
class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

class C(B):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

obj = C(1, 2, 3)
print(obj.x, obj.y, obj.z)
```



- [A] Xato beradi 
- [B] None None 3 
- [C] 1 2 3 
- [D] 1 None 3 


> **To'g'ri javob:** C 
> **Tushuntirish:** `C.__init__` → `B.__init__(1,2)` → `A.__init__(1)`. Barcha atributlar o'rnatiladi.


---


## Savol 14



OOP (Object Oriented Programming) nima?



- [A] Faqat funksiyalardan foydalanuvchi dasturlash uslubi 
- [B] Dasturni obyektlar va ularning o'zaro ta'siri asosida quradigan dasturlash paradigmasi 
- [C] Faqat Python ga xos dasturlash usuli 
- [D] Ma'lumotlar bazasi bilan ishlash usuli 


> **To'g'ri javob:** B 
> **Tushuntirish:** OOP — dasturni real dunyodagi obyektlarni modellashtirish orqali quradigan paradigma. Class va obyektlar asosida ishlaydi.


---


## Savol 15



Class nima?



- [A] O'zgaruvchi nomi 
- [B] Obyektlarni yaratish uchun qolip — atributlar va metodlarni o'z ichiga oladi 
- [C] Funksiyalar to'plami 
- [D] Python moduli 


> **To'g'ri javob:** B 
> **Tushuntirish:** Class — obyektlar uchun shablon (qolip). U atributlar (ma'lumot) va metodlar (funksiyalar) ni birlashtiradi.


---


## Savol 16



Obyekt (instance) qanday yaratiladi?



- [A] object.new(ClassName) 
- [B] ClassName.create() 
- [C] o = ClassName() 
- [D] new ClassName() 


> **To'g'ri javob:** C 
> **Tushuntirish:** Obyekt `o = ClassName()` ko'rinishida yaratiladi. Class nomi funksiya kabi chaqiriladi.


---


## Savol 17



Atribut nima?



- [A] Classning funksiyasi 
- [B] Obyekt yoki class ga tegishli ma'lumot (o'zgaruvchi) 
- [C] Python kalit so'zi 
- [D] Modul nomi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Atribut — class yoki obyektga tegishli ma'lumot. Masalan, `mashina.rang`, `mashina.tezlik`.


---


## Savol 18



Metod nima?



- [A] Classning o'zgaruvchisi 
- [B] Class ichida e'lon qilingan funksiya 
- [C] Obyekt nomi 
- [D] Python moduli 


> **To'g'ri javob:** B 
> **Tushuntirish:** Metod — class ichida e'lon qilingan funksiya. U `self` parametrini qabul qiladi.


---


## Savol 19



`__init__()` metodi nima?



- [A] Classni o'chiruvchi metod 
- [B] Obyekt yaratilganda avtomatik chaqiriladigan konstruktor metod 
- [C] Faqat atributlarni chiqaruvchi metod 
- [D] Classni import qiluvchi metod 


> **To'g'ri javob:** B 
> **Tushuntirish:** `__init__()` — konstruktor. Obyekt yaratilganda (`ClassName()`) avtomatik chaqiriladi va atributlarni boshlang'ich qiymat bilan ta'minlaydi.


---


## Savol 20



Instance atribut nima?



- [A] Barcha obyektlarga umumiy atribut 
- [B] Faqat o'sha konkret obyektga xos atribut — __init__ da self orqali yaratiladi 
- [C] Class darajasidagi o'zgaruvchi 
- [D] Yashirin atribut 


> **To'g'ri javob:** B 
> **Tushuntirish:** Instance atribut — har bir obyektga alohida. `self.ism = ism` — instance atribut yaratish.


---


## Savol 21



Class atribut nima?



- [A] Faqat bitta obyektga xos atribut 
- [B] Class darajasida e'lon qilingan, barcha obyektlarga umumiy atribut 
- [C] __init__ ichida yaratilgan atribut 
- [D] Yashirin atribut 


> **To'g'ri javob:** B 
> **Tushuntirish:** Class atribut — class tanasida, metodlar tashqarisida e'lon qilinadi. Barcha instansiyalar uchun umumiy.


---


## Savol 22



Instance va class atributning asosiy farqi nima?



- [A] Hech qanday farq yo'q 
- [B] Instance atribut — har obyektga xos, class atribut — barcha obyektlarga umumiy 
- [C] Class atribut tezroq ishlaydi 
- [D] Instance atribut faqat metodlarda ishlatiladi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Instance atribut `self.x` orqali har obyektga alohida. Class atribut `Klass.x` — umumiy.


---


## Savol 23



Encapsulation (inkapsulyatsiya) nima?



- [A] Bir classdan boshqasiga meros olish 
- [B] Ma'lumotlar va metodlarni bitta classda birlashtirish va tashqaridan kirishni cheklash 
- [C] Funksiyalarni qayta ishlatish 
- [D] Kodlarni qisqartirish usuli 


> **To'g'ri javob:** B 
> **Tushuntirish:** Encapsulation — ma'lumot va metodlarni yashirish, tashqi kirishni cheklash. Private/protected atributlar orqali amalga oshiriladi.


---


## Savol 24



Getter va Setter metodlari nima uchun kerak?



- [A] Faqat chiroyli yozish uchun 
- [B] Private atributlarga nazorat ostida kirish va o'zgartirish imkonini berish uchun 
- [C] Atributlarni o'chirish uchun 
- [D] Class atributlarini boshqarish uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** Getter — qiymatni oladi, Setter — qiymatni tekshirib o'rnatadi. Private atributlarni nazorat ostida boshqaradi.


---


## Savol 25



Inheritance (meros olish) nima?



- [A] Bir xil nomli metodlarni qayta ishlatish 
- [B] Mavjud classning atribut va metodlarini yangi class tomonidan meros qilib olish mexanizmi 
- [C] Ma'lumotlarni yashirish usuli 
- [D] Faqat atributlarni boshqa classga ko'chirish 


> **To'g'ri javob:** B 
> **Tushuntirish:** Inheritance — OOP ning asosiy tamoyillaridan biri. Ota classning xususiyatlarini farzand class meros oladi.


---