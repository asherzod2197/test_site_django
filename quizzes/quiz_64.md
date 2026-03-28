## Savol 1



Real hayotda OOP qayerda ishlatiladi?



- [A] Faqat o'yinlar yaratishda 
- [B] Faqat veb dasturlashda 
- [C] Veb, o'yinlar, ilova, dasturiy ta'minot — deyarli hamma joyda 
- [D] Faqat ilmiy hisob-kitoblarda 


> **To'g'ri javob:** C 
> **Tushuntirish:** OOP deyarli barcha sohalarda ishlatiladi: veb (Django, Flask), o'yinlar, GUI ilovalar, mobil dasturlar va hokazo.


---


## Savol 2



Quyidagi kodning natijasi nima?

```python
class A:
    x = 10

class B:
    x = 20

print(A.x + B.x)
```



- [A] 10 
- [B] 20 
- [C] 30 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `A.x = 10`, `B.x = 20`. `10 + 20 = 30`.


---


## Savol 3



Quyidagi kodning natijasi nima?

```python
class Raqam:
    qiymat = 10

r = Raqam()
print(type(r))
print(type(Raqam))
```



- [A] <class 'int'>, <class 'int'> 
- [B] <class '__main__.Raqam'>, <class 'type'> 
- [C] <class 'object'>, <class 'type'> 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `type(r)` → `<class '__main__.Raqam'>`. `type(Raqam)` → `<class 'type'>` — class ham obyekt.


---


## Savol 4



Atribut mavjud emasligini tekshirish uchun qaysi funksiya ishlatiladi?



- [A] isset() 
- [B] exists() 
- [C] hasattr() 
- [D] checkattr() 


> **To'g'ri javob:** C 
> **Tushuntirish:** `hasattr(obyekt, 'atribut_nomi')` — atribut mavjud bo'lsa `True`, bo'lmasa `False` qaytaradi.


---


## Savol 5



Bir class ichida nechta metod bo'lishi mumkin?



- [A] Faqat bitta 
- [B] Faqat 10 ta 
- [C] Istalgancha 
- [D] Faqat 5 ta 


> **To'g'ri javob:** C 
> **Tushuntirish:** Class ichida istalgancha metod yozish mumkin.


---


## Savol 6



Quyidagi kodning natijasi nima?

```python
class Kvadrat:
    def __init__(self, tomon):
        self.tomon = tomon
        self.yuza = tomon ** 2

kv = Kvadrat(4)
print(kv.yuza)
```



- [A] 4 
- [B] 8 
- [C] 16 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `__init__` da `self.yuza = 4**2 = 16` hisoblanadi.


---


## Savol 7



Quyidagi kodning natijasi nima?

```python
class Nuqta:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n1 = Nuqta(1, 2)
n2 = Nuqta(3, 4)
n1.x = 99
print(n1.x)
print(n2.x)
```



- [A] 99, 99 
- [B] 1, 3 
- [C] 99, 3 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `n1.x = 99` — faqat `n1` o'zgaradi. `n2.x` mustaqil → `3`.


---


## Savol 8



Class atributiga class orqali va obyekt orqali murojaat qilish mumkinmi?



- [A] Faqat class orqali 
- [B] Faqat obyekt orqali 
- [C] Ikkala usul ham mumkin 
- [D] Hech qaysisi mumkin emas 


> **To'g'ri javob:** C 
> **Tushuntirish:** `Klass.atribut` va `obyekt.atribut` — ikkalasi ham ishlaydi (agar instance atribut ustiga yozilmagan bo'lsa).


---


## Savol 9



Quyidagi kodning natijasi nima?

```python
class Kompaniya:
    xodim_soni = 0

    def __init__(self, nomi):
        self.nomi = nomi
        Kompaniya.xodim_soni += 1

k1 = Kompaniya('Uzum')
k2 = Kompaniya('Payme')
print(k1.xodim_soni)
print(Kompaniya.xodim_soni)
```



- [A] 1, 2 
- [B] 2, 2 
- [C] 0, 2 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Ikki obyekt yaratildi → `Kompaniya.xodim_soni = 2`. `k1.xodim_soni` → class atribut → `2`.


---


## Savol 10



Quyidagi kodning natijasi nima?

```python
class Maxfiy:
    def __init__(self):
        self.__sir = 'yashirin'

    def sir_ol(self):
        return self.__sir

m = Maxfiy()
print(m.sir_ol())
```



- [A] AttributeError 
- [B] None 
- [C] yashirin 
- [D] __sir 


> **To'g'ri javob:** C 
> **Tushuntirish:** `__sir` — private, lekin `sir_ol()` metodi orqali ichkaridan kirish mumkin → `'yashirin'`.


---


## Savol 11



Quyidagi kodning natijasi nima?

```python
class Ism:
    def __init__(self, ism):
        self.__ism = ism

    @property
    def ism(self):
        return self.__ism.title()

    @ism.setter
    def ism(self, yangi):
        if isinstance(yangi, str):
            self.__ism = yangi

i = Ism('ali valiyev')
print(i.ism)
```



- [A] ali valiyev 
- [B] Ali Valiyev 
- [C] None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `@property` `ism` → `'ali valiyev'.title()` → `'Ali Valiyev'`.


---


## Savol 12



Ko'p bosqichli meros (multilevel inheritance) nima?



- [A] Bir class bir nechta classdan meros olishi 
- [B] A → B → C ko'rinishida zanjirsimon meros 
- [C] Bir class ikki marta meros olishi 
- [D] Faqat ikki classdan iborat meros 


> **To'g'ri javob:** B 
> **Tushuntirish:** Multilevel: `A` classdan `B`, `B` dan `C` meros oladi. `C` — `A` va `B` ning xususiyatlariga ega.


---


## Savol 13



Quyidagi kodning natijasi nima?

```python
class Hayvon:
    def ovoz(self):
        return 'Hayvon ovozi'

class Mushuk(Hayvon):
    def ovoz(self):
        ota = super().ovoz()
        return f'{ota} | Miyov!'

m = Mushuk()
print(m.ovoz())
```



- [A] Hayvon ovozi 
- [B] Miyov! 
- [C] Hayvon ovozi | Miyov! 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `super().ovoz()` → `'Hayvon ovozi'`. Keyin `| Miyov!` qo'shiladi.


---


## Savol 14



OOP ning asosiy 4 ta tamoyili qaysilar?



- [A] Funksiya, Tsikl, Shart, O'zgaruvchi 
- [B] Encapsulation, Inheritance, Polymorphism, Abstraction 
- [C] Class, Object, Method, Attribute 
- [D] Import, Module, Package, Library 


> **To'g'ri javob:** B 
> **Tushuntirish:** OOP ning 4 asosiy tamoyili: Encapsulation (yashirish), Inheritance (meros olish), Polymorphism (ko'p shakllilik), Abstraction (mavhumlashtirish).


---


## Savol 15



Python da class qanday e'lon qilinadi?



- [A] class: Nomi 
- [B] class Nomi: 
- [C] Class Nomi() 
- [D] def Nomi(): 


> **To'g'ri javob:** B 
> **Tushuntirish:** Python da class `class Nomi:` ko'rinishida e'lon qilinadi. Nomi odatda CamelCase bilan yoziladi.


---


## Savol 16



Quyidagi kodning natijasi nima?

```python
class It:
    ovoz = 'Vov'

i1 = It()
i2 = It()
print(i1.ovoz)
print(i2.ovoz)
```



- [A] Xato beradi 
- [B] Vov, Vov 
- [C] None, None 
- [D] Vov, None 


> **To'g'ri javob:** B 
> **Tushuntirish:** `i1` va `i2` — `It` classining ikki obyekti. Ikkalasi ham `ovoz` atributini meros oladi → `Vov`.


---


## Savol 17



Quyidagi kodning natijasi nima?

```python
class Talaba:
    maktab = 'INHA'

t = Talaba()
t.ism = 'Ali'
print(t.maktab)
print(t.ism)
```



- [A] Xato beradi 
- [B] INHA, Ali 
- [C] None, Ali 
- [D] INHA, None 


> **To'g'ri javob:** B 
> **Tushuntirish:** `t.maktab` — class atributi → `'INHA'`. `t.ism` — instance atributi → `'Ali'`.


---


## Savol 18



Instance metodning birinchi parametri nima bo'lishi shart?



- [A] cls 
- [B] this 
- [C] self 
- [D] object 


> **To'g'ri javob:** C 
> **Tushuntirish:** `self` — instance metodining birinchi parametri. U chaqirilayotgan obyektni ko'rsatadi.


---


## Savol 19



Quyidagi kodning natijasi nima?

```python
class Inson:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

i = Inson('Sarvar', 25)
print(i.ism)
print(i.yosh)
```



- [A] Xato beradi 
- [B] None, None 
- [C] Sarvar, 25 
- [D] ism, yosh 


> **To'g'ri javob:** C 
> **Tushuntirish:** `__init__` da `self.ism = 'Sarvar'`, `self.yosh = 25` o'rnatiladi.


---


## Savol 20



Quyidagi kodning natijasi nima?

```python
class Mashina:
    def __init__(self, rang, tezlik):
        self.rang = rang
        self.tezlik = tezlik

m1 = Mashina('qizil', 200)
m2 = Mashina('yashil', 150)
print(m1.rang)
print(m2.tezlik)
```



- [A] qizil, 200 
- [B] qizil, 150 
- [C] yashil, 150 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `m1.rang` → `'qizil'`. `m2.tezlik` → `150`.


---


## Savol 21



Quyidagi kodning natijasi nima?

```python
class Sayyora:
    galaktika = 'Somon yoli'

s1 = Sayyora()
s2 = Sayyora()
print(s1.galaktika)
print(s2.galaktika)
print(Sayyora.galaktika)
```



- [A] None, None, None 
- [B] Somon yoli, Somon yoli, Somon yoli 
- [C] Xato beradi 
- [D] Somon yoli, None, Somon yoli 


> **To'g'ri javob:** B 
> **Tushuntirish:** Class atribut barcha instansiyalarga umumiy. Uchala ham `'Somon yoli'` qaytaradi.


---


## Savol 22



Quyidagi kodning natijasi nima?

```python
class Test:
    umumiy = 'class'

    def __init__(self):
        self.shaxsiy = 'instance'

t = Test()
print(t.umumiy)
print(t.shaxsiy)
print(Test.umumiy)
```



- [A] class, instance, class 
- [B] instance, instance, class 
- [C] class, class, class 
- [D] Xato beradi 


> **To'g'ri javob:** A 
> **Tushuntirish:** `t.umumiy` → class atribut: `'class'`. `t.shaxsiy` → instance atribut: `'instance'`. `Test.umumiy` → `'class'`.


---


## Savol 23



Python da private atribut qanday e'lon qilinadi?



- [A] private self.x = 5 
- [B] self.x = 5 
- [C] self.__x = 5 
- [D] self._private_x = 5 


> **To'g'ri javob:** C 
> **Tushuntirish:** Ikki pastki chiziq `__` — private atribut: `self.__x`. Tashqaridan to'g'ridan-to'g'ri kirish mumkin emas.


---


## Savol 24



Quyidagi kodning natijasi nima?

```python
class Talaba:
    def __init__(self, ball):
        self.__ball = ball

    def get_ball(self):
        return self.__ball

    def set_ball(self, yangi):
        if 0 <= yangi <= 100:
            self.__ball = yangi

t = Talaba(75)
t.set_ball(90)
print(t.get_ball())
```



- [A] 75 
- [B] 90 
- [C] None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `set_ball(90)` — `0 <= 90 <= 100` → to'g'ri → `self.__ball = 90`. `get_ball()` → `90`.


---


## Savol 25



Python da meros olish qanday yoziladi?



- [A] class Farzand extends Ota: 
- [B] class Farzand inherits Ota: 
- [C] class Farzand(Ota): 
- [D] class Farzand -> Ota: 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da meros olish: `class FarzandClass(OtaClass):`. Qavs ichiga ota class nomi yoziladi.


---