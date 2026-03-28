## Savol 1

Class (sinf) nima?

- [A] Faqat ma'lumotlarni saqlash uchun ishlatiladigan o'zgaruvchi  
- [B] Obyektlarni yaratish uchun shablon (qolip) bo'lib, atributlar va metodlarni o'z ichiga oladi  
- [C] Dasturni tezlashtirish uchun ishlatiladigan maxsus funksiya  
- [D] Faqat raqamli ma'lumotlar bilan ishlaydigan tuzilma  

> **To'g'ri javob:** B  
> **Tushuntirish:** Class — bu obyektlarni yaratish uchun qolip bo'lib, u atributlar (ma'lumotlar) va metodlar (funksiyalar)ni bir joyda birlashtiradi.

---

## Savol 2

Classdan obyekt yaratish qanday ataladi?

- [A] Kompilyatsiya  
- [B] Instansiyalashtirish (Instantiation)  
- [C] Deklaratsiya  
- [D] Iteratsiya  

> **To'g'ri javob:** B  
> **Tushuntirish:** Classdan aniq obyekt yaratish jarayoni instansiyalashtirish deyiladi. Yaratilgan obyekt esa class instansiyasi (instance) hisoblanadi.

---

## Savol 3

Quyidagi Python kodida nima yaratilmoqda?

```python
class Mashina:
    pass
```

- [A] Funksiya  
- [B] O'zgaruvchi  
- [C] Bo'sh class  
- [D] Modul  

> **To'g'ri javob:** C  
> **Tushuntirish:** `class Mashina:` kalit so'zi bilan bo'sh class e'lon qilinmoqda. `pass` ichida hech narsa yo'qligini bildiradi.

---

## Savol 4

Class ichidagi `__init__` metodi nima vazifani bajaradi?

- [A] Classni o'chiradi  
- [B] Obyekt yaratilganda avtomatik chaqirilib, boshlang'ich qiymatlarni belgilaydi  
- [C] Faqat matn chiqarish uchun ishlatiladi  
- [D] Classni boshqa classdan meros olishga majbur qiladi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `__init__` — bu konstruktor metod bo'lib, obyekt yaratilgan zahoti avtomatik ishga tushadi va atributlarning boshlang'ich qiymatlarini o'rnatadi.

---

## Savol 5

`self` parametri nima vazifani bajaradi?

- [A] Barcha classlarga murojaat qiladi  
- [B] Joriy obyektning o'ziga murojaat qiladi  
- [C] Faqat `__init__` metodida ishlatiladi  
- [D] Dasturni to'xtatadi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `self` — bu joriy obyektni ifodalovchi parametr bo'lib, class metodlari ichida obyektning o'z atributlari va metodlariga murojaat qilish uchun ishlatiladi.

---

## Savol 6

Quyidagi kodda `mening_mashinam.rang` qanday natija beradi?

```python
class Mashina:
    def __init__(self, rang):
        self.rang = rang

mening_mashinam = Mashina("qizil")
print(mening_mashinam.rang)
```

- [A] `Mashina`  
- [B] `rang`  
- [C] `qizil`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Mashina("qizil")` chaqirilganda `__init__` ichida `self.rang = "qizil"` qiymati o'rnatiladi. Shuning uchun `mening_mashinam.rang` → `qizil` chiqaradi.

---

## Savol 7

Class atributlari va instansiya atributlari o'rtasidagi farq nima?

- [A] Hech qanday farq yo'q, ikkalasi bir xil  
- [B] Class atributlari barcha obyektlar uchun umumiy, instansiya atributlari har bir obyektga alohida tegishli  
- [C] Instansiya atributlari faqat `__init__` dan tashqarida e'lon qilinadi  
- [D] Class atributlari faqat raqamlardan iborat bo'lishi mumkin  

> **To'g'ri javob:** B  
> **Tushuntirish:** Class atributlari classning barcha instansiyalari tomonidan birgalikda ishlatiladi. Instansiya atributlari esa har bir obyektga xos bo'lib, odatda `__init__` ichida `self` orqali e'lon qilinadi.

---

## Savol 8

Quyidagi kodda nechta obyekt yaratilgan?

```python
class Talaba:
    def __init__(self, ism):
        self.ism = ism

t1 = Talaba("Ali")
t2 = Talaba("Vali")
t3 = Talaba("Gani")
```

- [A] 1  
- [B] 2  
- [C] 3  
- [D] 0  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Talaba` classidan `t1`, `t2` va `t3` nomli 3 ta alohida obyekt yaratilgan. Har biri o'zining `ism` atributiga ega.

---

## Savol 9

Class metodlari bilan oddiy funksiyalar o'rtasidagi asosiy farq nima?

- [A] Metodlar hech qachon parametr qabul qilmaydi  
- [B] Metodlar class ichida e'lon qilinadi va birinchi parametri sifatida `self` ni qabul qiladi  
- [C] Funksiyalar class ichida ham e'lon qilinishi mumkin  
- [D] Metodlar faqat `return` operatori bilan tugashi shart  

> **To'g'ri javob:** B  
> **Tushuntirish:** Class metodlari class bloki ichida yoziladi va birinchi parametri sifatida `self` (joriy obyekt) ni oladi. Bu ularning oddiy funksiyalardan asosiy farqidir.

---

## Savol 10

`__str__` metodi qanday maqsadda ishlatiladi?

- [A] Classni o'chirish uchun  
- [B] Ikki obyektni solishtirish uchun  
- [C] Obyektni matn ko'rinishida chiqarish uchun `print()` da foydalaniladi  
- [D] Yangi atribut qo'shish uchun  

> **To'g'ri javob:** C  
> **Tushuntirish:** `__str__` — bu maxsus (dunder) metod bo'lib, `print(obyekt)` chaqirilganda avtomatik ishga tushadi va obyektning matn ko'rinishini qaytaradi.

---

## Savol 11

Encapsulation (inkapsulyatsiya) class bilan qanday bog'liq?

- [A] Inkapsulyatsiya classlar o'rtasida meros olishni anglatadi  
- [B] Inkapsulyatsiya ma'lumotlar va metodlarni class ichida birlashtirish hamda tashqaridan kirishni cheklashdir  
- [C] Inkapsulyatsiya faqat `__init__` metodida amalga oshiriladi  
- [D] Inkapsulyatsiya classni bir necha faylga bo'lish demakdir  

> **To'g'ri javob:** B  
> **Tushuntirish:** Inkapsulyatsiya — OOPning asosiy tamoyillaridan biri bo'lib, ma'lumotlar va metodlarni class ichida yashirish va himoya qilishni anglatadi. `_` yoki `__` prefikslari orqali amalga oshiriladi.

---

## Savol 12

Quyidagi kodda xato bormi?

```python
class Doira:
    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return 3.14 * self.radius ** 2

d = Doira(5)
print(d.yuza())
```

- [A] Ha, `self` ishlatilmasligi kerak  
- [B] Ha, `__init__` noto'g'ri yozilgan  
- [C] Yo'q, kod to'g'ri va `78.5` chiqaradi  
- [D] Ha, `Doira` classi `pass` bilan tugashi kerak  

> **To'g'ri javob:** C  
> **Tushuntirish:** Kod sintaktik jihatdan to'g'ri. `d = Doira(5)` orqali radius=5 bo'lgan obyekt yaratiladi. `d.yuza()` → `3.14 * 5² = 78.5` ni qaytaradi.

---

## Savol 13

Python'da `isinstance()` funksiyasi nima uchun ishlatiladi?

- [A] Ikki classni bir-biriga aylantirish uchun  
- [B] Obyektning ma'lum bir classga mansub yoki yo'qligini tekshirish uchun  
- [C] Class ichidagi metodlar sonini hisoblash uchun  
- [D] Classni o'chirish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `isinstance(obyekt, Class)` — bu obyektning ko'rsatilgan class yoki uning avlodiga tegishli ekanligini tekshiradi va `True` yoki `False` qaytaradi.

---

## Savol 14

Quyidagi kodda `Kuchuk.tur` qanday natija beradi?

```python
class Hayvon:
    tur = "Sut emizuvchi"

class Kuchuk(Hayvon):
    pass

print(Kuchuk.tur)
```

- [A] `None`  
- [B] Xato beradi, chunki `Kuchuk` classida `tur` yo'q  
- [C] `Sut emizuvchi`  
- [D] `Hayvon`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Kuchuk` classi `Hayvon` classidan meros olgan. Shuning uchun `Hayvon` dagi `tur` class atributiga `Kuchuk` orqali ham murojaat qilish mumkin — natija `Sut emizuvchi` bo'ladi.

---

## Savol 15

Destruktor (`__del__`) metodi qachon chaqiriladi?

- [A] Obyekt yaratilganda  
- [B] Metod chaqirilganda  
- [C] Obyekt xotiradan o'chirilganda yoki dastur tugaganda  
- [D] Class e'lon qilingan paytda  

> **To'g'ri javob:** C  
> **Tushuntirish:** `__del__` — bu destruktor metod bo'lib, obyekt xotiradan o'chirilayotganda (garbage collector tomonidan) yoki dastur yakunlanayotganda avtomatik chaqiriladi. U resurslarni tozalash uchun ishlatiladi.

---