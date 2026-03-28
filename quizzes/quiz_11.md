## Savol 1

Class attribute (class atributi) nima?

- [A] Faqat bitta obyektga tegishli o'zgaruvchi  
- [B] Class tanasida e'lon qilinib, o'sha classdan yaratilgan barcha obyektlar tomonidan umumiy ishlatiladigan o'zgaruvchi  
- [C] Faqat `__init__` ichida `self` orqali yaratilgan o'zgaruvchi  
- [D] Maxsus metodlar ichidagi lokal o'zgaruvchi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Class atributi class tanasida, metodlardan tashqarida e'lon qilinadi. U classdan yaratilgan barcha obyektlar tomonidan umumiy ishlatiladi — ya'ni bitta umumiy qiymatni saqlaydi.

---

## Savol 2

Class atributi qayerda e'lon qilinadi?

- [A] `__init__` metodi ichida `self` orqali  
- [B] Class tanasida, metodlardan tashqarida to'g'ridan-to'g'ri  
- [C] Faqat `@classmethod` dekoratori ichida  
- [D] Class tashqarisida, global darajada  

> **To'g'ri javob:** B  
> **Tushuntirish:** Class atributlari class tanasida, lekin har qanday metoddan tashqarida e'lon qilinadi. Masalan: `class Mashina:` bloki ichida `tur = "Avtomobil"` deb yozilsa — bu class atribut.

---

## Savol 3

Quyidagi kodda qaysi atribut class atributi hisoblanadi?

```python
class Hayvon:
    oyoq_soni = 4

    def __init__(self, ism):
        self.ism = ism
```

- [A] `ism`  
- [B] `self`  
- [C] `oyoq_soni`  
- [D] Ikkalasi ham  

> **To'g'ri javob:** C  
> **Tushuntirish:** `oyoq_soni = 4` class tanasida, `__init__` dan tashqarida e'lon qilingan — bu class atribut. `self.ism` esa `__init__` ichida `self` orqali e'lon qilingan instance atribut hisoblanadi.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
class Talaba:
    maktab = "Najot Ta'lim"

t1 = Talaba()
t2 = Talaba()
print(t1.maktab, t2.maktab)
```

- [A] `None None`  
- [B] Xato beradi  
- [C] `Najot Ta'lim Najot Ta'lim`  
- [D] `maktab maktab`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `maktab` — class atribut bo'lgani uchun barcha instansiyalar uchun umumiy. `t1.maktab` va `t2.maktab` ikkalasi ham class atributidan `"Najot Ta'lim"` ni o'qiydi. Natija: `Najot Ta'lim Najot Ta'lim`.

---

## Savol 5

Class atributiga class nomi orqali murojaat qilish mumkinmi?

- [A] Yo'q, faqat obyekt orqali mumkin  
- [B] Ha, `ClassName.atribut_nomi` orqali to'g'ridan-to'g'ri murojaat qilish mumkin  
- [C] Faqat `@classmethod` ichida mumkin  
- [D] Faqat `super()` orqali mumkin  

> **To'g'ri javob:** B  
> **Tushuntirish:** Class atributlariga ham class nomi, ham obyekt orqali murojaat qilish mumkin. `Talaba.maktab` yoki `t1.maktab` — ikkalasi ham ishlaydi. Lekin class nomi orqali murojaat qilish aniqroq va tavsiya etiladi.

---

## Savol 6

Quyidagi kodning natijasi nima?

```python
class Kompaniya:
    xodimlar_soni = 0

    def __init__(self, ism):
        self.ism = ism
        Kompaniya.xodimlar_soni += 1

k1 = Kompaniya("Ali")
k2 = Kompaniya("Vali")
k3 = Kompaniya("Gani")
print(Kompaniya.xodimlar_soni)
```

- [A] `0`  
- [B] `1`  
- [C] `2`  
- [D] `3`  

> **To'g'ri javob:** D  
> **Tushuntirish:** Har bir yangi obyekt yaratilganda `Kompaniya.xodimlar_soni += 1` bajariladi. 3 ta obyekt yaratilgani uchun `xodimlar_soni` → `3` bo'ladi. Bu class atributini umumiy hisoblagich sifatida ishlatishning klassik usuli.

---

## Savol 7

Class atributi o'zgartirilsa, barcha instansiyalarga ta'sir qiladimi?

- [A] Yo'q, faqat o'zgartirilgan instansiyaga ta'sir qiladi  
- [B] Ha, agar `ClassName.atribut = yangi_qiymat` orqali o'zgartirilsa — instansiya atributi bo'lmagan barcha obyektlarga ta'sir qiladi  
- [C] Faqat yangi yaratilgan obyektlarga ta'sir qiladi  
- [D] Hech qanday ta'sir qilmaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `ClassName.atribut = yangi_qiymat` orqali class atributi o'zgartirilsa, o'sha atribut uchun instansiya atributi bo'lmagan barcha obyektlar yangi qiymatni ko'radi. Instansiya atributi bo'lgan obyektlar esa o'z qiymatini saqlab qoladi.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
class Narx:
    soliq = 12

n1 = Narx()
n2 = Narx()
Narx.soliq = 20
print(n1.soliq, n2.soliq)
```

- [A] `12 12`  
- [B] `20 12`  
- [C] `12 20`  
- [D] `20 20`  

> **To'g'ri javob:** D  
> **Tushuntirish:** `Narx.soliq = 20` class atributini o'zgartirdi. `n1` va `n2` da instansiya atributi yo'q, shuning uchun ikkalasi ham yangilangan class atributini ko'radi. Natija: `20 20`.

---

## Savol 9

Instansiya orqali class atributi o'zgartirilsa nima bo'ladi?

- [A] Class atributi o'zgaradi va barcha instansiyalarga ta'sir qiladi  
- [B] Faqat o'sha instansiya uchun yangi instance atribut yaratiladi, class atributi o'zgarmaydi  
- [C] Xato beradi  
- [D] Barcha instansiyalar o'chib ketadi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `obyekt.class_atribut = yangi_qiymat` orqali class atributi o'zgarmaydi — buning o'rniga faqat shu obyekt uchun yangi instance atribut yaratiladi. Boshqa obyektlar class atributini ko'rishda davom etadi.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
class Daraxt:
    tur = "Ignabargli"

d1 = Daraxt()
d2 = Daraxt()
d1.tur = "Keng bargli"
print(d1.tur, d2.tur)
print(Daraxt.tur)
```

- [A] `Keng bargli Keng bargli` va `Keng bargli`  
- [B] `Keng bargli Ignabargli` va `Ignabargli`  
- [C] `Ignabargli Ignabargli` va `Ignabargli`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `d1.tur = "Keng bargli"` — `d1` uchun instance atribut yaratildi. `d2` va `Daraxt.tur` esa o'zgarmagan. Natija: `d1.tur` → `"Keng bargli"`, `d2.tur` → `"Ignabargli"`, `Daraxt.tur` → `"Ignabargli"`.

---

## Savol 11

Class atributlari qanday holatda foydali?

- [A] Har bir obyekt uchun alohida qiymat saqlanishi kerak bo'lganda  
- [B] Barcha instansiyalar uchun umumiy bo'lgan konstantalar, hisoblagichlar yoki standart qiymatlarni saqlashda  
- [C] Faqat yopiq (private) ma'lumotlarni saqlashda  
- [D] Faqat meros olishda  

> **To'g'ri javob:** B  
> **Tushuntirish:** Class atributlari barcha instansiyalar uchun umumiy bo'lgan qiymatlarni saqlashda qulay: konstantalar (masalan, PI = 3.14), umumiy hisoblagichlar, standart sozlamalar va h.k.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
class Doira:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return Doira.PI * self.radius ** 2

d = Doira(7)
print(round(d.yuza(), 2))
```

- [A] `21.99`  
- [B] `153.94`  
- [C] `43.98`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `Doira.PI * 7 ** 2` = `3.14159 * 49` = `153.93791`. `round(..., 2)` → `153.94`. `PI` — class atribut sifatida barcha metodlarda ishlatilishi mumkin.

---

## Savol 13

Meros olishda farzand class class atributiga qanday murojaat qiladi?

- [A] Farzand class ota classning class atributlariga murojaaat qila olmaydi  
- [B] Faqat `super()` orqali  
- [C] Farzand class ota classning class atributlarini meros oladi va to'g'ridan-to'g'ri ishlata oladi  
- [D] Faqat `@classmethod` orqali  

> **To'g'ri javob:** C  
> **Tushuntirish:** Meros olishda farzand class ota classning class atributlarini avtomatik meros oladi. Farzand class nomi orqali ham, instansiya orqali ham o'sha atributlarga murojaat qilish mumkin.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
class Transport:
    harakat_turi = "Quruqlik"

class Avtomobil(Transport):
    pass

class Samolyot(Transport):
    harakat_turi = "Havo"

print(Avtomobil.harakat_turi)
print(Samolyot.harakat_turi)
```

- [A] `Quruqlik` va `Quruqlik`  
- [B] `Havo` va `Havo`  
- [C] `Quruqlik` va `Havo`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Avtomobil` o'z class atributini e'lon qilmagan, shuning uchun ota classdan `"Quruqlik"` ni meros oldi. `Samolyot` esa o'zining `harakat_turi = "Havo"` ni e'lon qilgan. Natija: `Quruqlik`, `Havo`.

---

## Savol 15

Quyidagi kodning natijasi nima?

```python
class Hisoblagich:
    son = 0

    def __init__(self):
        Hisoblagich.son += 1
        self.id = Hisoblagich.son

h1 = Hisoblagich()
h2 = Hisoblagich()
h3 = Hisoblagich()
print(h1.id, h2.id, h3.id)
```

- [A] `3 3 3`  
- [B] `0 0 0`  
- [C] `1 2 3`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** Har obyekt yaratilganda `Hisoblagich.son` bittaga oshadi, so'ng joriy qiymat `self.id` ga o'rnatiladi. `h1.id = 1`, `h2.id = 2`, `h3.id = 3`. Natija: `1 2 3`.

---

## Savol 16

`vars()` funksiyasi class atributlari uchun qanday ishlaydi?

- [A] Faqat instance atributlarni qaytaradi  
- [B] Class uchun `vars(ClassName)` barcha class atributlari va metodlarini o'z ichiga olgan `mappingproxy` qaytaradi  
- [C] Xato beradi  
- [D] Faqat `None` qaytaradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `vars(ClassName)` class uchun barcha atributlar va metodlarini o'z ichiga olgan `mappingproxy` obyektini qaytaradi. `vars(obyekt)` esa faqat instance atributlarni lug'at ko'rinishida beradi.

---

## Savol 17

Quyidagi kodning natijasi nima?

```python
class Limit:
    max_son = 100

    def tekshir(self, son):
        if son > Limit.max_son:
            return "Limitdan oshdi"
        return "Limit doirasida"

Limit.max_son = 50
l = Limit()
print(l.tekshir(75))
```

- [A] `Limit doirasida`  
- [B] `Limitdan oshdi`  
- [C] `100`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `Limit.max_son = 50` orqali class atributi `50` ga o'zgartirildi. `tekshir(75)` da `75 > 50` shart bajariladi va `"Limitdan oshdi"` qaytariladi.

---

## Savol 18

Class atributini `@classmethod` ichida o'zgartirish to'g'ri usulmi?

- [A] Yo'q, `@classmethod` faqat o'qish uchun  
- [B] Ha, `cls.atribut = yangi_qiymat` orqali class atributini `@classmethod` ichida o'zgartirish to'g'ri va tavsiya etilgan usul  
- [C] Faqat `@staticmethod` ichida o'zgartirish mumkin  
- [D] Faqat `__init__` ichida o'zgartirish mumkin  

> **To'g'ri javob:** B  
> **Tushuntirish:** `@classmethod` ichida `cls` orqali class atributini o'qish va o'zgartirish mumkin. `cls.atribut = yangi_qiymat` — bu classni meros olishda ham to'g'ri ishlaydi, chunki `cls` farzand classni ham ifodalashi mumkin.

---

## Savol 19

Quyidagi kodning natijasi nima?

```python
class Sozlama:
    til = "O'zbek"

    @classmethod
    def tilni_ozgartir(cls, yangi_til):
        cls.til = yangi_til

Sozlama.tilni_ozgartir("Ingliz")
s = Sozlama()
print(s.til)
print(Sozlama.til)
```

- [A] `O'zbek` va `O'zbek`  
- [B] `Ingliz` va `O'zbek`  
- [C] `Ingliz` va `Ingliz`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `cls.til = "Ingliz"` orqali class atributi o'zgartirildi. `s` da instance atribut yo'q, shuning uchun class atributini ko'radi. Ham `s.til`, ham `Sozlama.til` → `"Ingliz"`. Natija: `Ingliz`, `Ingliz`.

---

## Savol 20

Instance atribut va class atribut o'rtasidagi asosiy farqni to'g'ri ifodalagan javobni toping:

- [A] Class atributlari tezroq ishlaydi, instance atributlar sekinroq  
- [B] Instance atribut har bir obyektga xos alohida qiymat saqlaydi; class atribut esa barcha obyektlar uchun umumiy bitta qiymatni saqlaydi  
- [C] Class atributlarini o'zgartirish mumkin emas, instance atributlarni mumkin  
- [D] Instance atributlar `__init__` dan tashqarida ishlatib bo'lmaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Asosiy farq: instance atribut `self` orqali har bir obyektga alohida tegishli bo'lib, mustaqil qiymat saqlaydi. Class atribut esa class darajasida e'lon qilinib, barcha instansiyalar tomonidan umumiy ishlatiladi. Birini o'zgartirish ikkinchisiga ta'sir qilmaydi.

---