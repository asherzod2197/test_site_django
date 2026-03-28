## Savol 1

Method (metod) nima?

- [A] Classda saqlanadigan o'zgaruvchi  
- [B] Class ichida e'lon qilingan va obyekt bilan ishlaydigan funksiya  
- [C] Faqat matematik amallar bajaruvchi operator  
- [D] Alohida faylda saqlangan kod bloki  

> **To'g'ri javob:** B  
> **Tushuntirish:** Metod — bu class ichida e'lon qilingan funksiya bo'lib, obyektning xatti-harakatini (behavior) ifodalaydi. Oddiy funksiyadan farqi — u classga tegishli va birinchi parametri sifatida `self` ni qabul qiladi.

---

## Savol 2

OOP da metodlarning asosiy 3 turi qaysilar?

- [A] Kiruvchi, chiquvchi va aralash metodlar  
- [B] Instansiya metodi, class metodi va statik metod  
- [C] Ochiq, yopiq va himoyalangan metodlar  
- [D] Asosiy, yordamchi va zaxira metodlar  

> **To'g'ri javob:** B  
> **Tushuntirish:** Python OOP da metodlarning 3 asosiy turi bor: **instansiya metodi** (`self` oladi), **class metodi** (`@classmethod`, `cls` oladi) va **statik metod** (`@staticmethod`, hech narsa olmaydi).

---

## Savol 3

Instansiya metodi qanday farqlanadi?

- [A] `@staticmethod` dekoratori bilan belgilanadi  
- [B] Birinchi parametri `cls` bo'ladi  
- [C] Birinchi parametri `self` bo'lib, joriy obyektga murojaat qiladi  
- [D] Class nomi orqali chaqiriladi  

> **To'g'ri javob:** C  
> **Tushuntirish:** Instansiya metodi — eng keng tarqalgan metod turi. Birinchi parametri `self` bo'lib, joriy obyektning atributlari va boshqa metodlariga murojaat qilish imkonini beradi.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
class Avtomobil:
    def __init__(self, tezlik):
        self.tezlik = tezlik

    def harakatlан(self):
        return f"Avtomobil {self.tezlik} km/h tezlikda ketmoqda"

a = Avtomobil(120)
print(a.harakatlan())
```

- [A] `Avtomobil 0 km/h tezlikda ketmoqda`  
- [B] `Avtomobil 120 km/h tezlikda ketmoqda`  
- [C] `harakatlan`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `a = Avtomobil(120)` orqali `self.tezlik = 120` o'rnatiladi. `a.harakatlan()` chaqirilganda metod `self.tezlik` ni ishlatib `"Avtomobil 120 km/h tezlikda ketmoqda"` qaytaradi.

---

## Savol 5

`@classmethod` dekoratori bilan e'lon qilingan metodning birinchi parametri nima bo'ladi?

- [A] `self`  
- [B] `this`  
- [C] `cls`  
- [D] `class`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Class metodi `@classmethod` dekoratori bilan belgilanadi va birinchi parametri `cls` bo'ladi. `cls` — bu classning o'ziga ishora qiladi (instansiyaga emas).

---

## Savol 6

Quyidagi kodda `Doira.standart_yaratish()` qanday natija beradi?

```python
class Doira:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def standart_yaratish(cls):
        return cls(1)

d = Doira.standart_yaratish()
print(d.radius)
```

- [A] `None`  
- [B] Xato beradi  
- [C] `1`  
- [D] `cls`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `standart_yaratish` class metodi `cls(1)` orqali yangi `Doira` obyekti yaratadi (radius=1). `d.radius` → `1` qaytaradi.

---

## Savol 7

`@staticmethod` qachon ishlatiladi?

- [A] Har doim instansiya metodlari o'rniga  
- [B] Metod na `self`, na `cls` ga muhtoj bo'lmaganda — classga mantiqan tegishli, lekin mustaqil funksiya bo'lganda  
- [C] Faqat meros olishda  
- [D] Faqat yopiq metodlar uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** Statik metod na obyektga (`self`), na classga (`cls`) bog'liq emas. Classga mantiqan tegishli, lekin ularning ma'lumotlariga muhtoj bo'lmagan yordamchi funksiyalar uchun ishlatiladi.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
class Hisob:
    @staticmethod
    def qoshish(a, b):
        return a + b

print(Hisob.qoshish(10, 20))
```

- [A] Xato beradi, chunki `self` yo'q  
- [B] `Hisob`  
- [C] `30`  
- [D] `None`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `@staticmethod` metodi `self` yoki `cls` talab qilmaydi. `Hisob.qoshish(10, 20)` to'g'ridan-to'g'ri chaqiriladi va `10 + 20 = 30` qaytaradi.

---

## Savol 9

Quyidagi 3 ta metod turini to'g'ri ajrating:

```python
class Misol:
    def metod_a(self):         # ???
        pass

    @classmethod
    def metod_b(cls):          # ???
        pass

    @staticmethod
    def metod_c():             # ???
        pass
```

- [A] Hammasi instansiya metodi  
- [B] `metod_a` — statik, `metod_b` — class, `metod_c` — instansiya  
- [C] `metod_a` — instansiya, `metod_b` — class, `metod_c` — statik  
- [D] `metod_a` — class, `metod_b` — instansiya, `metod_c` — statik  

> **To'g'ri javob:** C  
> **Tushuntirish:** `self` li metod — instansiya metodi. `@classmethod` + `cls` — class metodi. `@staticmethod` + parametrsiz — statik metod. Bu uchala tur OOP da tez-tez birga ishlatiladi.

---

## Savol 10

Yopiq metod (private method) qanday e'lon qilinadi?

- [A] `def metod_nomi()` — oddiy nom bilan  
- [B] `def _metod_nomi()` — bir pastki chiziq bilan  
- [C] `def __metod_nomi()` — ikki pastki chiziq bilan  
- [D] `@private def metod_nomi()` — dekorator bilan  

> **To'g'ri javob:** C  
> **Tushuntirish:** `__metod_nomi` (ikki pastki chiziq) bilan boshlangan metodlar yopiq hisoblanadi. Python name mangling mexanizmi orqali tashqaridan bevosita chaqirishni qiyinlashtiradi.

---

## Savol 11

Quyidagi kodda xato bormi?

```python
class Salomlashish:
    def salom_ber(ism):
        print(f"Salom, {ism}!")

s = Salomlashish()
s.salom_ber("Ali")
```

- [A] Xato yo'q, to'g'ri ishlaydi  
- [B] Ha, `self` parametri yetishmayapti  
- [C] Ha, `print` funksiyasi noto'g'ri ishlatilgan  
- [D] Ha, class nomi katta harfda bo'lmasligi kerak  

> **To'g'ri javob:** B  
> **Tushuntirish:** Instansiya metodi birinchi parametr sifatida `self` ni talab qiladi. `salom_ber(ism)` da `self` yo'q, shuning uchun `s.salom_ber("Ali")` chaqirilganda `TypeError` xatosi yuzaga keladi.

---

## Savol 12

`__str__` va `__repr__` metodlari o'rtasidagi farq nima?

- [A] Ikkalasi bir xil vazifani bajaradi  
- [B] `__str__` foydalanuvchi uchun o'qilishi oson matn, `__repr__` dasturchi uchun aniq texnik ma'lumot qaytaradi  
- [C] `__repr__` faqat xato xabarlarida ishlatiladi  
- [D] `__str__` faqat raqamli qiymatlar uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `__str__` — `print()` chaqirilganda ishlatiladi va foydalanuvchiga qulay matn qaytaradi. `__repr__` — obyektning aniq texnik tavsifi bo'lib, asosan debug uchun, `repr()` yoki konsol chiqishida ishlatiladi.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
class Ombor:
    mahsulotlar = []

    def qosh(self, narsa):
        self.mahsulotlar.append(narsa)

o1 = Ombor()
o2 = Ombor()
o1.qosh("Olma")
print(o2.mahsulotlar)
```

- [A] `[]`  
- [B] `["Olma"]`  
- [C] Xato beradi  
- [D] `None`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `mahsulotlar = []` — bu class atributi (o'zgaruvchan, mutable). `o1.qosh("Olma")` orqali umumiy ro'yxatga element qo'shildi. `o2` ham xuddi shu class atributini ko'rgani uchun `["Olma"]` chiqaradi. Bu klassik tuzoq!

---

## Savol 14

Method chaining (zanjirli metod chaqirish) qanday amalga oshiriladi?

- [A] Metodlar `None` qaytarishi kerak  
- [B] Har bir metod `self` ni qaytarsa, metodlarni nuqta orqali ketma-ket chaqirish mumkin  
- [C] Faqat `@classmethod` bilan mumkin  
- [D] Alohida kutubxona kerak  

> **To'g'ri javob:** B  
> **Tushuntirish:** Metod `return self` bilan tugasa, natijada yana o'sha obyekt qaytariladi. Bu `obyekt.metod1().metod2().metod3()` ko'rinishida ketma-ket chaqirishga imkon beradi.

---

## Savol 15

Quyidagi kodning natijasi nima?

```python
class Quruvchi:
    def __init__(self):
        self.qismlar = []

    def qosh(self, qism):
        self.qismlar.append(qism)
        return self

    def qur(self):
        return " + ".join(self.qismlar)

natija = Quruvchi().qosh("Poydevor").qosh("Devor").qosh("Tom").qur()
print(natija)
```

- [A] `['Poydevor', 'Devor', 'Tom']`  
- [B] `Poydevor + Devor + Tom`  
- [C] Xato beradi  
- [D] `None`  

> **To'g'ri javob:** B  
> **Tushuntirish:** Har bir `qosh()` metodi `self` ni qaytargani uchun zanjirli chaqirish mumkin. `qur()` esa ro'yxat elementlarini `" + "` bilan birlashtiradi. Natija: `"Poydevor + Devor + Tom"`.

---