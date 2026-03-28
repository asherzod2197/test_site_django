## Savol 1



OOP da 'instance' nima?



- [A] Class ning o'zi 
- [B] Class asosida yaratilgan konkret obyekt 
- [C] Metod nomi 
- [D] Atribut qiymati 


> **To'g'ri javob:** B 
> **Tushuntirish:** Instance — classdan yaratilgan konkret obyekt. Masalan, `it = It()` — `it` bu `It` classining instansiyasi.


---


## Savol 2



Quyidagi kodning natijasi nima?

```python
class Kitob:
    janr = 'Roman'

k1 = Kitob()
k2 = Kitob()
print(k1.janr == k2.janr)
```



- [A] False 
- [B] True 
- [C] None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Ikkalasi ham `Kitob` classining `janr` atributini meros oladi: `'Roman' == 'Roman'` → `True`.


---


## Savol 3



Quyidagi kodning natijasi nima?

```python
class Qush:
    qanotlar = 2

q1 = Qush()
q2 = Qush()
q1.qanotlar = 0
print(q1.qanotlar)
print(q2.qanotlar)
```



- [A] 0, 0 
- [B] 2, 2 
- [C] 0, 2 
- [D] 2, 0 


> **To'g'ri javob:** C 
> **Tushuntirish:** `q1.qanotlar = 0` — `q1` ga instance atribut qo'shiladi, class atributini yopmaydi. `q2` class atributidan oladi → `2`.


---


## Savol 4



`delattr()` funksiyasi nima qiladi?



- [A] Class ni o'chiradi 
- [B] Obyektdan atributni o'chiradi 
- [C] Atribut qiymatini nolga tenglashtiradi 
- [D] Atributni yashiradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `delattr(obyekt, 'atribut')` — obyektdan atributni o'chiradi. `del obyekt.atribut` bilan bir xil.


---


## Savol 5



Quyidagi kodning natijasi nima?

```python
class Shakllar:
    def yuza(self, a, b):
        return a * b

    def perimetr(self, a, b):
        return 2 * (a + b)

s = Shakllar()
print(s.yuza(4, 5))
print(s.perimetr(4, 5))
```



- [A] 20, 18 
- [B] 9, 18 
- [C] 20, 9 
- [D] Xato beradi 


> **To'g'ri javob:** A 
> **Tushuntirish:** `yuza(4,5)` → `4*5=20`. `perimetr(4,5)` → `2*(4+5)=18`.


---


## Savol 6



Quyidagi kodning natijasi nima?

```python
class Uchburchak:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.perimetr = a + b + c

ut = Uchburchak(3, 4, 5)
print(ut.perimetr)
```



- [A] 3 
- [B] 5 
- [C] 12 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `self.perimetr = 3 + 4 + 5 = 12`.


---


## Savol 7



Quyidagi kodning natijasi nima?

```python
class Tovar:
    def __init__(self, nomi, narx):
        self.nomi = nomi
        self.narx = narx

    def chegirma(self, foiz):
        self.narx *= (1 - foiz / 100)
        return self.narx

t = Tovar('Telefon', 2000000)
print(t.chegirma(10))
print(t.narx)
```



- [A] 200000, 2000000 
- [B] 1800000.0, 1800000.0 
- [C] 1800000.0, 2000000 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `chegirma(10)` → `2000000 * 0.9 = 1800000.0` va `self.narx` yangilanadi.


---


## Savol 8



Quyidagi kodning natijasi nima?

```python
class Mahsulot:
    soliq = 15

    def jami_narx(self, narx):
        return narx * (1 + self.soliq / 100)

m = Mahsulot()
print(m.jami_narx(10000))
```



- [A] 10000 
- [B] 11500.0 
- [C] 1500.0 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `self.soliq` → class atribut `15`. `10000 * (1 + 15/100) = 10000 * 1.15 = 11500.0`.


---


## Savol 9



Quyidagi kodning natijasi nima?

```python
class Narx:
    qqs = 12

    def __init__(self, asos):
        self.asos = asos

    def jami(self):
        return self.asos * (1 + self.qqs / 100)

n = Narx(50000)
print(n.jami())
```



- [A] 50000 
- [B] 56000.0 
- [C] 6000.0 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `self.qqs` → class atribut `12`. `50000 * (1 + 12/100) = 50000 * 1.12 = 56000.0`.


---


## Savol 10



Quyidagi kodning natijasi nima?

```python
class Hisobvar:
    def __init__(self, balans):
        self.__balans = balans

    def balans_korsatish(self):
        return self.__balans

h = Hisobvar(500000)
print(h.balans_korsatish())
print(h._Hisobvar__balans)
```



- [A] 500000, AttributeError 
- [B] 500000, 500000 
- [C] AttributeError, 500000 
- [D] None, None 


> **To'g'ri javob:** B 
> **Tushuntirish:** `balans_korsatish()` → `500000`. `_Hisobvar__balans` → name mangling orqali kirish → `500000`.


---


## Savol 11



Quyidagi kodning natijasi nima?

```python
class Balans:
    def __init__(self):
        self.__summa = 0

    @property
    def summa(self):
        return self.__summa

    @summa.setter
    def summa(self, qiymat):
        if qiymat >= 0:
            self.__summa = qiymat

b = Balans()
b.summa = 50000
b.summa = -1000
print(b.summa)
```



- [A] -1000 
- [B] 0 
- [C] 50000 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `b.summa = 50000` → `50000 >= 0` → qabul. `b.summa = -1000` → `-1000 < 0` → rad. `b.summa` → `50000`.


---


## Savol 12



`issubclass()` funksiyasi nima qaytaradi?



- [A] Obyektning classini 
- [B] Bir classning boshqasidan meros olgan-olmaganini — True/False 
- [C] Class metodlari ro'yxatini 
- [D] Class atributlarini 


> **To'g'ri javob:** B 
> **Tushuntirish:** `issubclass(Farzand, Ota)` → `True` yoki `False`. Classlar bilan ishlaydi, obyektlar bilan emas.


---


## Savol 13



Quyidagi kodning natijasi nima?

```python
class Narx:
    def __init__(self, asos):
        self.asos = asos

    def jami(self):
        return self.asos

class SoliqliNarx(Narx):
    def __init__(self, asos, soliq):
        super().__init__(asos)
        self.soliq = soliq

    def jami(self):
        return super().jami() * (1 + self.soliq/100)

n = SoliqliNarx(100000, 15)
print(n.jami())
```



- [A] 100000 
- [B] 115000.0 
- [C] 15000.0 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `super().jami()` → `100000`. `100000 * (1 + 15/100) = 115000.0`.


---


## Savol 14



Python da OOP qo'llab-quvvatlanadimi?



- [A] Yo'q, Python faqat funksional dasturlashni qo'llab-quvvatlaydi 
- [B] Ha, Python to'liq OOP ni qo'llab-quvvatlaydi 
- [C] Faqat qisman 
- [D] Faqat Python 3 da 


> **To'g'ri javob:** B 
> **Tushuntirish:** Python to'liq OOP ni qo'llab-quvvatlaydi. Class, meros olish, polimorfizm, enkapsulatsiya — barchasi mavjud.


---


## Savol 15



Quyidagi kodning natijasi nima?

```python
class Kafe:
    nomi = 'Bahor'

print(Kafe.nomi)
```



- [A] Xato beradi 
- [B] None 
- [C] 'Bahor' 
- [D] Kafe 


> **To'g'ri javob:** C 
> **Tushuntirish:** `Kafe.nomi` — class atributiga to'g'ridan-to'g'ri class orqali murojaat: `'Bahor'`.


---


## Savol 16



Quyidagi kodning natijasi nima?

```python
class Doira:
    pass

d = Doira()
print(isinstance(d, Doira))
```



- [A] False 
- [B] None 
- [C] True 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `isinstance(d, Doira)` — `d` `Doira` classining instansiyasimi → `True`.


---


## Savol 17



Quyidagi kodning natijasi nima?

```python
class Avtomobil:
    davlat = "O'zbekiston"

a1 = Avtomobil()
a2 = Avtomobil()
a1.davlat = 'Rossiya'
print(a1.davlat)
print(a2.davlat)
```



- [A] O'zbekiston, O'zbekiston 
- [B] Rossiya, Rossiya 
- [C] Rossiya, O'zbekiston 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** `a1.davlat = 'Rossiya'` — `a1` ga instance atribut qo'shiladi. `a2` hali class atributidan → `O'zbekiston`.


---


## Savol 18



`self` parametri nima uchun ishlatiladi?



- [A] Faqat __init__ uchun 
- [B] Metodda obyektning o'z atributlari va metodlariga murojaat qilish uchun 
- [C] Class atributiga murojaat uchun 
- [D] Parametrlarni o'tkazish uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** `self` — chaqirilayotgan obyektning o'zi. `self.ism`, `self.run()` kabi murojaat qilish uchun.


---


## Savol 19



Quyidagi kodning natijasi nima?

```python
class Kitob:
    def __init__(self, nomi, narx=10000):
        self.nomi = nomi
        self.narx = narx

k1 = Kitob('Python')
k2 = Kitob('Java', 15000)
print(k1.narx)
print(k2.narx)
```



- [A] 10000, 15000 
- [B] None, 15000 
- [C] 10000, 10000 
- [D] Xato beradi 


> **To'g'ri javob:** A 
> **Tushuntirish:** `k1` → `narx` standart `10000`. `k2` → `narx=15000`.


---


## Savol 20



Quyidagi kodning natijasi nima?

```python
class Talaba:
    def __init__(self, ism, ball):
        self.ism = ism
        self.ball = ball

t = Talaba('Kamola', 85)
print(t.__dict__)
```



- [A] Xato beradi 
- [B] {'ism': 'Kamola', 'ball': 85} 
- [C] ['ism', 'ball'] 
- [D] None 


> **To'g'ri javob:** B 
> **Tushuntirish:** `t.__dict__` → `{'ism': 'Kamola', 'ball': 85}` — instance atributlar dictionary.


---


## Savol 21



Quyidagi kodning natijasi nima?

```python
class Firma:
    xodimlar = 0

    def __init__(self, ism):
        self.ism = ism
        Firma.xodimlar += 1

f1 = Firma('Ali')
f2 = Firma('Vali')
f3 = Firma('Gali')
print(Firma.xodimlar)
```



- [A] 0 
- [B] 1 
- [C] 3 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** Har `__init__` da `Firma.xodimlar += 1`. 3 ta obyekt → `3`.


---


## Savol 22



Quyidagi kodning natijasi nima?

```python
class Rang:
    asosiy = 'qizil'

r1 = Rang()
r2 = Rang()
r1.asosiy = 'ko\'k'
print(Rang.asosiy)
print(r1.asosiy)
print(r2.asosiy)
```



- [A] ko'k, ko'k, ko'k 
- [B] qizil, ko'k, qizil 
- [C] qizil, qizil, qizil 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** `r1.asosiy = 'ko'k'` — `r1` ga instance atribut. `Rang.asosiy` va `r2.asosiy` o'zgarmaydi.


---


## Savol 23



Protected atribut qanday e'lon qilinadi?



- [A] protect self.x = 5 
- [B] self.__x = 5 
- [C] self._x = 5 
- [D] self.x = private(5) 


> **To'g'ri javob:** C 
> **Tushuntirish:** Bitta pastki chiziq `_` — konventsiya bo'yicha protected: `self._x`. Texnik jihatdan tashqaridan kirish mumkin, lekin qo'llamaslik tavsiya etiladi.


---


## Savol 24



Quyidagi kodning natijasi nima?

```python
class Doira:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

d = Doira(5)
print(d.radius)
```



- [A] Xato beradi 
- [B] None 
- [C] 5 
- [D] __radius 


> **To'g'ri javob:** C 
> **Tushuntirish:** `@property` — `d.radius` (qavsiz) metodni chaqiradi → `self.__radius` → `5`.


---


## Savol 25



Farzand class ota classning metodini bekor qilishi nima deyiladi?



- [A] Overloading 
- [B] Encapsulation 
- [C] Method overriding 
- [D] Abstraction 


> **To'g'ri javob:** C 
> **Tushuntirish:** Method overriding — farzand classda ota class metodini qayta e'lon qilib, xatti-harakatini o'zgartirish.


---