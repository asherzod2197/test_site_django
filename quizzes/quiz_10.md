## Savol 1

Instance attribute (instansiya atributi) nima?

- [A] Barcha obyektlar uchun umumiy bo'lgan o'zgaruvchi  
- [B] Har bir obyektga alohida tegishli bo'lgan va o'sha obyektning o'ziga xos qiymatini saqlovchi o'zgaruvchi  
- [C] Faqat class ichidagi funksiya  
- [D] Dastur ishlash davomida o'zgarmaydigan konstantа  

> **To'g'ri javob:** B  
> **Tushuntirish:** Instance attribute — bu har bir obyektga alohida tegishli o'zgaruvchi. Bir classdan yaratilgan turli obyektlarning instansiya atributlari bir-biridan mustaqil va har xil qiymatga ega bo'lishi mumkin.

---

## Savol 2

Instance attribute qayerda e'lon qilinadi?

- [A] Class tanasida, metodlardan tashqarida  
- [B] Alohida fayl ichida  
- [C] `__init__` yoki boshqa metodlar ichida `self.atribut_nomi = qiymat` shaklida  
- [D] Faqat class nomi orqali  

> **To'g'ri javob:** C  
> **Tushuntirish:** Instance atributlar odatda `__init__` ichida `self.atribut_nomi = qiymat` shaklida e'lon qilinadi. Shuningdek, boshqa metodlar ichida ham `self` orqali yangi atribut qo'shish mumkin.

---

## Savol 3

Quyidagi kodda qaysi atributlar instance atribut hisoblanadi?

```python
class Mashina:
    marka = "Toyota"

    def __init__(self, rang, tezlik):
        self.rang = rang
        self.tezlik = tezlik
```

- [A] Faqat `marka`  
- [B] `marka`, `rang`, `tezlik` — hammasi  
- [C] Faqat `rang` va `tezlik`  
- [D] Hech biri  

> **To'g'ri javob:** C  
> **Tushuntirish:** `rang` va `tezlik` — `self` orqali `__init__` ichida e'lon qilingan, shuning uchun instance atributlar. `marka` esa class tanasida e'lon qilingan class atribut hisoblanadi.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
class Talaba:
    def __init__(self, ism, ball):
        self.ism = ism
        self.ball = ball

t1 = Talaba("Ali", 85)
t2 = Talaba("Vali", 92)
print(t1.ball, t2.ball)
```

- [A] `85 85`  
- [B] `92 92`  
- [C] `85 92`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `t1` va `t2` — alohida obyektlar. Har birining `ball` instance atributi mustaqil: `t1.ball = 85`, `t2.ball = 92`. Natija: `85 92`.

---

## Savol 5

Instance atributni obyekt yaratilgandan keyin o'zgartirish mumkinmi?

- [A] Yo'q, bir marta belgilangan qiymat o'zgarmaydi  
- [B] Faqat `__init__` ichida o'zgartirish mumkin  
- [C] Ha, `obyekt.atribut = yangi_qiymat` orqali istalgan vaqtda o'zgartirish mumkin  
- [D] Faqat maxsus metod orqali o'zgartirish mumkin  

> **To'g'ri javob:** C  
> **Tushuntirish:** Instance atributlar istalgan vaqtda to'g'ridan-to'g'ri `obyekt.atribut = yangi_qiymat` orqali o'zgartirilishi mumkin. Bu Python'ning moslashuvchan xususiyatlaridan biri.

---

## Savol 6

Quyidagi kodning natijasi nima?

```python
class Hisob:
    def __init__(self, egasi, balans):
        self.egasi = egasi
        self.balans = balans

h = Hisob("Nodira", 500000)
h.balans += 200000
print(h.balans)
```

- [A] `500000`  
- [B] `200000`  
- [C] `700000`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `h.balans` dastlab `500000`. `h.balans += 200000` → `500000 + 200000 = 700000`. Instance atribut yangilandi. Natija: `700000`.

---

## Savol 7

Instance atributni obyektdan o'chirish uchun qaysi operator ishlatiladi?

- [A] `remove(obyekt.atribut)`  
- [B] `obyekt.atribut = None`  
- [C] `del obyekt.atribut`  
- [D] `clear(obyekt.atribut)`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `del obyekt.atribut` — bu instance atributni o'chiradi. O'chirilgandan so'ng unga murojaat qilinsa `AttributeError` xatosi yuzaga keladi.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
class Shaxs:
    def __init__(self, ism):
        self.ism = ism

s = Shaxs("Kamol")
del s.ism
print(s.ism)
```

- [A] `None`  
- [B] `Kamol`  
- [C] `AttributeError` xatosi  
- [D] Bo'sh satr  

> **To'g'ri javob:** C  
> **Tushuntirish:** `del s.ism` orqali `ism` instance atributi o'chirildi. Keyin `s.ism` ga murojaat qilinganda `AttributeError: 'Shaxs' object has no attribute 'ism'` xatosi yuzaga keladi.

---

## Savol 9

`__dict__` atributi nimani qaytaradi?

- [A] Classning barcha metodlari ro'yxatini  
- [B] Obyektning barcha instance atributlarini `{kalit: qiymat}` ko'rinishida  
- [C] Faqat `__init__` parametrlarini  
- [D] Class atributlarini  

> **To'g'ri javob:** B  
> **Tushuntirish:** `obyekt.__dict__` — bu obyektga tegishli barcha instance atributlarni lug'at ko'rinishida qaytaradi. Masalan: `{'ism': 'Ali', 'yosh': 20}`. Class atributlari bu lug'atga kirmaydi.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
class Tovar:
    def __init__(self, nomi, narx):
        self.nomi = nomi
        self.narx = narx

t = Tovar("Olma", 5000)
print(t.__dict__)
```

- [A] `{'Tovar': 'Tovar'}`  
- [B] `{'nomi': 'Olma', 'narx': 5000}`  
- [C] `['nomi', 'narx']`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `t.__dict__` obyektning instance atributlarini lug'at ko'rinishida qaytaradi. `nomi = "Olma"` va `narx = 5000` atributlari `__init__` da o'rnatilgani uchun natija: `{'nomi': 'Olma', 'narx': 5000}`.

---

## Savol 11

Instance atribut va class atribut bir xil nomga ega bo'lsa nima bo'ladi?

- [A] Xato beradi  
- [B] Class atributi instance atributni yopadi  
- [C] Instance atributi o'sha obyekt uchun class atributini yopadi (ustunlik qiladi)  
- [D] Ikkalasi bir vaqtda ko'rinadi  

> **To'g'ri javob:** C  
> **Tushuntirish:** Bir xil nomli instance atribut yaratilsa, Python avval instance atributni topadi va uni ishlatadi. Class atributi faqat instance atribut yo'q bo'lganda ko'rinadi. Bu "shadowing" deb ataladi.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
class Mahsulot:
    chegirma = 10

    def __init__(self, nomi):
        self.nomi = nomi

m1 = Mahsulot("Noutbuk")
m1.chegirma = 25
m2 = Mahsulot("Telefon")

print(m1.chegirma, m2.chegirma)
```

- [A] `25 25`  
- [B] `10 10`  
- [C] `25 10`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `m1.chegirma = 25` — `m1` uchun yangi instance atribut yaratildi va class atributini yopdi. `m2` da esa instance atribut yo'q, shuning uchun class atributi `10` ko'rinadi. Natija: `25 10`.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
class Kurs:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []

    def qosh(self, talaba):
        self.talabalar.append(talaba)

k1 = Kurs("Python")
k2 = Kurs("Java")
k1.qosh("Ali")
k1.qosh("Vali")
print(len(k1.talabalar), len(k2.talabalar))
```

- [A] `2 2`  
- [B] `2 0`  
- [C] `0 2`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `self.talabalar = []` — har bir obyekt uchun alohida instance atribut yaratiladi. `k1` ga 2 ta talaba qo'shildi, `k2` ga hech narsa qo'shilmadi. Natija: `2 0`.

---

## Savol 14

Obyektga `__init__` dan tashqarida yangi instance atribut qo'shish mumkinmi?

- [A] Yo'q, faqat `__init__` ichida qo'shish mumkin  
- [B] Ha, `obyekt.yangi_atribut = qiymat` orqali istalgan joyda qo'shish mumkin  
- [C] Faqat `setattr()` funksiyasi orqali  
- [D] Faqat metod ichida `self` orqali  

> **To'g'ri javob:** B  
> **Tushuntirish:** Python'da obyektga istalgan vaqtda yangi atribut qo'shish mumkin: `obyekt.yangi_atribut = qiymat`. Lekin bu barcha instansiyalarda emas, faqat shu obyektda paydo bo'ladi.

---

## Savol 15

Quyidagi kodning natijasi nima?

```python
class Robot:
    def __init__(self, ism):
        self.ism = ism

r = Robot("R2D2")
r.batareya = 100
print(r.ism, r.batareya)
```

- [A] Xato beradi, `batareya` `__init__` da yo'q  
- [B] `R2D2 None`  
- [C] `R2D2 100`  
- [D] `None 100`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `r.batareya = 100` orqali `r` obyektiga yangi instance atribut qo'shildi. Bu to'liq ruxsat etiladi. `r.ism` → `"R2D2"`, `r.batareya` → `100`. Natija: `R2D2 100`.

---

## Savol 16

`hasattr()` funksiyasi instance atribut bilan qanday ishlaydi?

- [A] Atributni o'chiradi  
- [B] Atribut qiymatini qaytaradi  
- [C] Obyektda ko'rsatilgan atribut mavjud yoki yo'qligini `True`/`False` ko'rinishida qaytaradi  
- [D] Atributni yangilaydi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `hasattr(obyekt, 'atribut_nomi')` — instance atributning mavjudligini tekshiradi. Mavjud bo'lsa `True`, bo'lmasa `False` qaytaradi. Xatoga yo'l qo'ymasdan tekshirish uchun qulay.

---

## Savol 17

Quyidagi kodning natijasi nima?

```python
class Uy:
    def __init__(self, xonalar):
        self.xonalar = xonalar

u = Uy(3)
print(hasattr(u, 'xonalar'))
print(hasattr(u, 'baho'))
```

- [A] `False` va `True`  
- [B] `True` va `True`  
- [C] `True` va `False`  
- [D] `False` va `False`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `u.xonalar` mavjud → `hasattr(u, 'xonalar')` → `True`. `u.baho` esa e'lon qilinmagan → `hasattr(u, 'baho')` → `False`. Natija: `True`, `False`.

---

## Savol 18

Quyidagi kodda instance atributlarning mustaqilligini ko'rsating:

```python
class Oydin:
    def __init__(self, qiymat):
        self.qiymat = qiymat

a = Oydin(10)
b = Oydin(10)
a.qiymat = 99
print(a.qiymat, b.qiymat)
```

- [A] `99 99`  
- [B] `10 10`  
- [C] `99 10`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `a` va `b` — alohida obyektlar. `a.qiymat = 99` faqat `a` obyektining instance atributini o'zgartiradi. `b.qiymat` esa o'zgarmagan holda `10` qoladi. Natija: `99 10`.

---

## Savol 19

Quyidagi kodning natijasi nima?

```python
class Kompyuter:
    def __init__(self, model):
        self.model = model
        self.dasturlar = []

    def install(self, dastur):
        self.dasturlar.append(dastur)
        return f"{dastur} o'rnatildi"

pc = Kompyuter("Dell")
pc.install("Python")
pc.install("VSCode")
print(pc.__dict__)
```

- [A] `{'model': 'Dell'}`  
- [B] `{'dasturlar': ['Python', 'VSCode']}`  
- [C] `{'model': 'Dell', 'dasturlar': ['Python', 'VSCode']}`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `__init__` da `self.model = "Dell"` va `self.dasturlar = []` o'rnatildi. `install()` chaqiruvlaridan so'ng `dasturlar` ro'yxatiga ikki element qo'shildi. `__dict__` barcha instance atributlarni ko'rsatadi.

---

## Savol 20

Instance atributlarning class atributlaridan asosiy ustunligi nima?

- [A] Instance atributlar tezroq ishlaydi  
- [B] Instance atributlar kamroq xotira oladi  
- [C] Har bir obyekt o'ziga xos qiymatlar saqlashi mumkin — bu OOP ning encapsulation tamoyilini ta'minlaydi  
- [D] Instance atributlarni o'chirish mumkin emas  

> **To'g'ri javob:** C  
> **Tushuntirish:** Instance atributlarning asosiy ustunligi — har bir obyekt o'ziga xos holat (state) saqlaydi. Bu OOP ning inkapsulyatsiya tamoyilini amalga oshiradi va har bir obyektni mustaqil, o'ziga xos birlik sifatida ifodalash imkonini beradi.

---