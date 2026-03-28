## Savol 1

Attribute (atribut) nima?

- [A] Class ichidagi funksiya  
- [B] Obyekt yoki classning xususiyatini ifodalovchi o'zgaruvchi  
- [C] Dasturni tezlashtirish vositasi  
- [D] Faqat raqamli qiymatlarni saqlovchi katak  

> **To'g'ri javob:** B  
> **Tushuntirish:** Atribut — bu obyekt yoki classga tegishli ma'lumotni saqlovchi o'zgaruvchi. Masalan, `self.ism`, `self.yosh` — bular instansiya atributlari hisoblanadi.

---

## Savol 2

Instansiya atributi (instance attribute) qayerda e'lon qilinadi?

- [A] Class tanasida, metodlardan tashqarida  
- [B] `__init__` metodi ichida `self` orqali  
- [C] Faqat class nomi orqali  
- [D] Alohida fayl ichida  

> **To'g'ri javob:** B  
> **Tushuntirish:** Instansiya atributlari odatda `__init__` metodi ichida `self.atribut_nomi = qiymat` shaklida e'lon qilinadi va har bir obyektga alohida tegishli bo'ladi.

---

## Savol 3

Class atributi (class attribute) qayerda e'lon qilinadi?

- [A] `__init__` ichida `self` orqali  
- [B] Class tanasida, metodlardan tashqarida to'g'ridan-to'g'ri  
- [C] Faqat `@classmethod` dekoratori bilan  
- [D] Obyekt yaratilgandan keyin  

> **To'g'ri javob:** B  
> **Tushuntirish:** Class atributlari class tanasida, lekin metodlardan tashqarida e'lon qilinadi. Ular classning barcha instansiyalari tomonidan umumiy ishlatiladi.

---

## Savol 4

Quyidagi kodda `tur` qaysi turdagi atribut?

```python
class Hayvon:
    tur = "Sut emizuvchi"

    def __init__(self, ism):
        self.ism = ism
```

- [A] Instansiya atributi  
- [B] Mahalliy o'zgaruvchi  
- [C] Class atributi  
- [D] Global o'zgaruvchi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `tur` class tanasida, `__init__` dan tashqarida e'lon qilingan. Shuning uchun u class atributi hisoblanadi va `Hayvon.tur` yoki har qanday instansiya orqali murojaat qilish mumkin.

---

## Savol 5

Quyidagi kodning natijasi nima?

```python
class Mashina:
    tepalik = 4

    def __init__(self, rang):
        self.rang = rang

m1 = Mashina("qizil")
m2 = Mashina("ko'k")
print(m1.tepalik, m2.tepalik)
```

- [A] `4 4`  
- [B] `qizil ko'k`  
- [C] Xato beradi  
- [D] `None None`  

> **To'g'ri javob:** A  
> **Tushuntirish:** `tepalik` — class atributi bo'lib, barcha instansiyalar uchun umumiy. `m1.tepalik` va `m2.tepalik` ikkalasi ham `4` qiymatini qaytaradi.

---

## Savol 6

Instansiya atributi class atributini yopa oladimi (override)?

- [A] Yo'q, bu imkonsiz  
- [B] Ha, instansiyada bir xil nomdagi atribut yaratilsa, u class atributini o'sha obyekt uchun yopadi  
- [C] Faqat `super()` orqali mumkin  
- [D] Faqat `__init__` ichida mumkin emas  

> **To'g'ri javob:** B  
> **Tushuntirish:** Agar instansiyaga class atributi bilan bir xil nomdagi atribut berilsa, o'sha obyekt uchun instansiya atributi ustunlik qiladi. Boshqa obyektlar esa class atributini ko'rishda davom etadi.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
class Talaba:
    ball = 0

t1 = Talaba()
t1.ball = 95
t2 = Talaba()
print(t1.ball, t2.ball)
```

- [A] `95 95`  
- [B] `0 0`  
- [C] `95 0`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `t1.ball = 95` orqali faqat `t1` uchun instansiya atributi yaratildi va class atributini yopdi. `t2` uchun hali instansiya atributi yo'q, shuning uchun class atributi `0` qaytariladi.

---

## Savol 8

`__dict__` atributi nima qaytaradi?

- [A] Classning barcha metodlari ro'yxatini  
- [B] Obyektning barcha instansiya atributlarini lug'at (dict) ko'rinishida  
- [C] Class atributlarini o'chiradi  
- [D] Faqat `__init__` parametrlarini  

> **To'g'ri javob:** B  
> **Tushuntirish:** `obyekt.__dict__` — bu obyektning instansiya atributlarini `{atribut: qiymat}` ko'rinishida qaytaradi. Masalan: `{'ism': 'Ali', 'yosh': 20}`.

---

## Savol 9

`hasattr()` funksiyasi nima uchun ishlatiladi?

- [A] Atributni o'chirish uchun  
- [B] Atribut qiymatini o'zgartirish uchun  
- [C] Obyektda ma'lum atribut mavjud yoki yo'qligini tekshirish uchun  
- [D] Yangi atribut yaratish uchun  

> **To'g'ri javob:** C  
> **Tushuntirish:** `hasattr(obyekt, 'atribut_nomi')` — bu obyektda ko'rsatilgan atribut mavjud bo'lsa `True`, bo'lmasa `False` qaytaradi. Xato yuzaga kelmasdan tekshirish imkonini beradi.

---

## Savol 10

`getattr()` funksiyasi qanday ishlaydi?

```python
class Odam:
    def __init__(self, ism):
        self.ism = ism

o = Odam("Zara")
print(getattr(o, "ism"))
```

- [A] Xato beradi  
- [B] `ism`  
- [C] `Zara`  
- [D] `None`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `getattr(obyekt, 'atribut_nomi')` — bu `obyekt.atribut_nomi` ga teng. `getattr(o, "ism")` → `o.ism` → `"Zara"` qaytaradi.

---

## Savol 11

`setattr()` funksiyasi nima qiladi?

- [A] Atributni o'chiradi  
- [B] Atributning turini o'zgartiradi  
- [C] Obyektga yangi atribut qo'shadi yoki mavjudini yangilaydi  
- [D] Faqat class atributlarini yangilaydi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `setattr(obyekt, 'atribut_nomi', qiymat)` — bu `obyekt.atribut_nomi = qiymat` ga teng. Dinamik ravishda atribut qo'shish yoki o'zgartirish imkonini beradi.

---

## Savol 12

`delattr()` funksiyasi nima uchun ishlatiladi?

- [A] Butun classni o'chirish uchun  
- [B] Obyektdan ma'lum atributni o'chirish uchun  
- [C] Atribut qiymatini nolga tenglashtirish uchun  
- [D] Atributni yashirish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `delattr(obyekt, 'atribut_nomi')` — bu `del obyekt.atribut_nomi` ga teng va obyektdan ko'rsatilgan atributni butunlay o'chiradi.

---

## Savol 13

Yopiq (private) atribut qanday e'lon qilinadi?

- [A] `atribut` — oddiy nom bilan  
- [B] `_atribut` — bir ta pastki chiziq bilan  
- [C] `__atribut` — ikki ta pastki chiziq bilan  
- [D] `#atribut` — xesh belgisi bilan  

> **To'g'ri javob:** C  
> **Tushuntirish:** `__atribut` (ikki pastki chiziq) bilan boshlangan atribut yopiq (private) hisoblanadi. Python bu atributga nom o'zgartirish (name mangling) qo'llab, tashqaridan bevosita murojaat qilishni qiyinlashtiradi.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
class Telefon:
    def __init__(self, model, narx):
        self.model = model
        self.__narx = narx

t = Telefon("iPhone", 12000000)
print(t.model)
print(t.__narx)
```

- [A] `iPhone` va `12000000`  
- [B] `iPhone` chiqadi, keyin `AttributeError` xatosi  
- [C] Ikkala qator ham xato beradi  
- [D] `None` va `12000000`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `t.model` → `"iPhone"` muvaffaqiyatli chiqadi. Lekin `t.__narx` yopiq atribut bo'lgani uchun `AttributeError` xatosi beradi. Unga `t._Telefon__narx` orqali murojaat qilish mumkin.

---

## Savol 15

Quyidagi kodda class atributi qiymatini o'zgartirish barcha instansiyalarga ta'sir qiladimi?

```python
class Kompaniya:
    xodim_soni = 100

k1 = Kompaniya()
k2 = Kompaniya()
Kompaniya.xodim_soni = 200
print(k1.xodim_soni, k2.xodim_soni)
```

- [A] `100 100`  
- [B] `200 100`  
- [C] `200 200`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Kompaniya.xodim_soni = 200` orqali class atributi to'g'ridan-to'g'ri o'zgartirildi. `k1` va `k2` da instansiya atributi bo'lmagani uchun ikkalasi ham yangilangan class atributini ko'radi: `200 200`.

---