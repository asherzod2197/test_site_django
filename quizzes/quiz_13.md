## Savol 1

Encapsulation (inkapsulyatsiya) nima?

- [A] Bir classdan boshqa class yaratish usuli  
- [B] Ma'lumotlar va metodlarni class ichida birlashtirish hamda tashqi kirishni nazorat qilish prinsipi  
- [C] Bir xil nomli metodlarni qayta ishlatish  
- [D] Faqat ma'lumotlarni ro'yxatda saqlash usuli  

> **To'g'ri javob:** B  
> **Tushuntirish:** Encapsulation — OOPning asosiy to'rtta tamoyilidan biri. U ma'lumotlar va metodlarni class ichida birlashtiradi hamda tashqaridan bevosita kirishni cheklaydi. Bu ma'lumotlarni himoya qilish va kodni tartibli saqlash imkonini beradi.

---

## Savol 2

Python'da encapsulation qanday darajalar orqali amalga oshiriladi?

- [A] Faqat bitta daraja — yopiq (private)  
- [B] Uch daraja: ochiq (public), himoyalangan (protected), yopiq (private)  
- [C] Ikki daraja: ochiq (public) va yopiq (private)  
- [D] To'rt daraja: ochiq, yarim ochiq, himoyalangan, yopiq  

> **To'g'ri javob:** B  
> **Tushuntirish:** Python'da encapsulation uch daraja orqali amalga oshiriladi: **public** (oddiy nom), **protected** (`_nom` — bitta pastki chiziq), **private** (`__nom` — ikki pastki chiziq). Bu Java yoki C++ dagi kabi qattiq cheklov emas, balki konventsiya asosida ishlaydi.

---

## Savol 3

Public (ochiq) atribut qanday belgilanadi?

- [A] `__atribut` — ikki pastki chiziq bilan  
- [B] `_atribut` — bitta pastki chiziq bilan  
- [C] `@public atribut` — dekorator bilan  
- [D] Oddiy nom bilan — hech qanday maxsus belgi yo'q  

> **To'g'ri javob:** D  
> **Tushuntirish:** Public atributlar maxsus belgilarsiz oddiy nom bilan e'lon qilinadi. Ular classdan tashqarida ham erkin o'qilishi va o'zgartirilishi mumkin. Masalan: `self.ism`, `self.yosh`.

---

## Savol 4

Protected (himoyalangan) atribut qanday belgilanadi va nima uchun ishlatiladi?

- [A] `__atribut` — ikki pastki chiziq, faqat class ichida  
- [B] `_atribut` — bitta pastki chiziq, dasturchilar uchun "ichki ishlatish uchun" signali  
- [C] `@protected atribut` — dekorator bilan  
- [D] `atribut_` — so'ngida pastki chiziq bilan  

> **To'g'ri javob:** B  
> **Tushuntirish:** `_atribut` (bitta pastki chiziq) — bu konventsiya bo'lib, "bu atributga tashqaridan murojaat qilmaslik kerak" degan signal beradi. Lekin Python buni texnik jihatdan taqiqlamaydi — bu faqat kelishuv.

---

## Savol 5

Private (yopiq) atribut qanday belgilanadi?

- [A] `atribut_` — so'ngida pastki chiziq  
- [B] `_atribut` — bitta pastki chiziq  
- [C] `__atribut` — ikki pastki chiziq  
- [D] `#atribut` — xesh belgisi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `__atribut` (ikki pastki chiziq prefiksi) — private atribut. Python bu atributga **name mangling** qo'llab, uni `_ClassName__atribut` ko'rinishiga o'zgartiradi va tashqaridan bevosita kirishni qiyinlashtiradi.

---

## Savol 6

Name mangling nima?

- [A] Atributni butunlay o'chirish  
- [B] Python'ning `__atribut` nomini `_ClassName__atribut` ko'rinishiga o'zgartirishi  
- [C] Atributni boshqa classga ko'chirish  
- [D] Metodlarni avtomatik yaratish  

> **To'g'ri javob:** B  
> **Tushuntirish:** Name mangling — Python'ning `__atribut` ni `_ClassName__atribut` formatiga o'zgartirish mexanizmi. Masalan, `Odam` classidagi `__ism` atributi aslida `_Odam__ism` sifatida saqlanadi. Bu tashqaridan kirishni qiyinlashtiradi, lekin imkonsiz qilmaydi.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
class Shaxs:
    def __init__(self, ism):
        self.__ism = ism

s = Shaxs("Kamola")
print(s.__ism)
```

- [A] `Kamola`  
- [B] `None`  
- [C] `AttributeError`  
- [D] `__ism`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `__ism` — private atribut, name mangling orqali `_Shaxs__ism` ga aylantirilgan. `s.__ism` orqali to'g'ridan-to'g'ri murojaat qilib bo'lmaydi → `AttributeError: 'Shaxs' object has no attribute '__ism'`.

---

## Savol 8

Private atributga tashqaridan qanday murojaat qilish mumkin?

- [A] Umuman mumkin emas  
- [B] `s._Shaxs__ism` — name mangling formatida  
- [C] `s.private_ism` — maxsus kalit so'z bilan  
- [D] Faqat `getattr()` orqali  

> **To'g'ri javob:** B  
> **Tushuntirish:** Name mangling sababli `__ism` aslida `_Shaxs__ism` nomi bilan saqlanadi. Shuning uchun `s._Shaxs__ism` orqali murojaat qilish texnik jihatdan mumkin. Lekin bu encapsulationni buzish hisoblanadi va qo'llanilmaydi.

---

## Savol 9

Getter metodi nima va nima uchun ishlatiladi?

- [A] Atributni o'chirish uchun  
- [B] Yopiq atributning qiymatini tashqariga xavfsiz tarzda qaytaruvchi metod  
- [C] Yangi atribut yaratish uchun  
- [D] Classni nusxalash uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** Getter — bu yopiq (private) atributni tashqaridan o'qish imkonini beruvchi metod. Odatda `get_atribut_nomi()` yoki `@property` dekoratori bilan yoziladi. Bu bevosita kirishni oldini oladi.

---

## Savol 10

Setter metodi nima va nima uchun ishlatiladi?

- [A] Atributni o'qish uchun  
- [B] Classni o'chirish uchun  
- [C] Yopiq atributni o'zgartirish uchun validatsiya qilib qiymat belgilovchi metod  
- [D] Yangi class yaratish uchun  

> **To'g'ri javob:** C  
> **Tushuntirish:** Setter — bu yopiq atributning qiymatini o'zgartirish uchun ishlatiladigan metod. U kiruvchi ma'lumotni tekshirish (validatsiya) imkonini beradi. Odatda `set_atribut_nomi()` yoki `@property.setter` bilan yoziladi.

---

## Savol 11

Quyidagi kodning natijasi nima?

```python
class Hisob:
    def __init__(self, balans):
        self.__balans = balans

    def get_balans(self):
        return self.__balans

    def set_balans(self, yangi_balans):
        if yangi_balans >= 0:
            self.__balans = yangi_balans

h = Hisob(100000)
h.set_balans(250000)
print(h.get_balans())
```

- [A] `100000`  
- [B] `0`  
- [C] `250000`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Hisob(100000)` → `__balans = 100000`. `set_balans(250000)` → `250000 >= 0` shart bajarildi → `__balans = 250000`. `get_balans()` → `250000`.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
class Hisob:
    def __init__(self, balans):
        self.__balans = balans

    def set_balans(self, yangi_balans):
        if yangi_balans >= 0:
            self.__balans = yangi_balans
        else:
            print("Xato: Balans manfiy bo'lishi mumkin emas!")

    def get_balans(self):
        return self.__balans

h = Hisob(500000)
h.set_balans(-1000)
print(h.get_balans())
```

- [A] `-1000`  
- [B] `0`  
- [C] `Xato: Balans manfiy bo'lishi mumkin emas!` va `500000`  
- [D] `AttributeError`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `set_balans(-1000)` da `-1000 >= 0` shart bajarilmadi → `else` bloki ishladi va xabar chiqdi. `__balans` o'zgarmadi. `get_balans()` → `500000`.

---

## Savol 13

`@property` dekoratori nima uchun ishlatiladi?

- [A] Metodlarni statik qilish uchun  
- [B] Metodni xuddi atribut kabi chaqirish imkonini beruvchi getter yaratish uchun  
- [C] Classni yopish uchun  
- [D] Meros olishni taqiqlash uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `@property` dekoratori metoddan xuddi atribut kabi foydalanish imkonini beradi. `obj.metod` ko'rinishida (qavssiz) chaqiriladi. Bu getter yaratishning Pythonic usuli hisoblanadi.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
class Doira:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @property
    def yuza(self):
        return 3.14 * self.__radius ** 2

d = Doira(5)
print(d.radius)
print(d.yuza)
```

- [A] Xato beradi, qavs qo'yilmagan  
- [B] `5` va `78.5`  
- [C] `5` va `3.14`  
- [D] `None` va `None`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `@property` bilan belgilangan metodlar atribut kabi qavssiz chaqiriladi. `d.radius` → `5`, `d.yuza` → `3.14 * 25 = 78.5`.

---

## Savol 15

`@property.setter` qanday ishlatiladi?

- [A] `@property` ni o'chirish uchun  
- [B] `@property` bilan birgalikda ishlatiladi va qiymat o'rnatish imkonini beradi  
- [C] Faqat class metodlarida ishlatiladi  
- [D] Atributni himoyalash uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `@property.setter` — bu `@property` ning yozish qismi. `obj.atribut = qiymat` sintaksisida chaqiriladi va qiymat belgilashda validatsiya qilish imkonini beradi.

---

## Savol 16

Quyidagi kodning natijasi nima?

```python
class Talaba:
    def __init__(self, ism, yosh):
        self.__ism = ism
        self.__yosh = yosh

    @property
    def yosh(self):
        return self.__yosh

    @yosh.setter
    def yosh(self, yangi_yosh):
        if 5 <= yangi_yosh <= 100:
            self.__yosh = yangi_yosh
        else:
            print("Noto'g'ri yosh!")

t = Talaba("Dilnoza", 20)
t.yosh = 25
print(t.yosh)
t.yosh = 150
print(t.yosh)
```

- [A] `25`, `150`  
- [B] `25`, `Noto'g'ri yosh!` va `25`  
- [C] `20`, `25`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `t.yosh = 25` → `5 <= 25 <= 100` shart bajarildi → `__yosh = 25`. `t.yosh = 150` → shart bajarilmadi → `"Noto'g'ri yosh!"` chiqdi, qiymat o'zgarmadi. `t.yosh` → `25`.

---

## Savol 17

Quyidagi kodda `_` (bitta pastki chiziq) bilan belgilangan atribut qanday ishlaydi?

```python
class Motor:
    def __init__(self, quvvat):
        self._quvvat = quvvat

m = Motor(150)
print(m._quvvat)
m._quvvat = 200
print(m._quvvat)
```

- [A] Xato beradi, `_quvvat` ga tashqaridan kiriб bo'lmaydi  
- [B] `150` va `200` — texnik jihatdan mumkin, lekin konventsiyaga ko'ra kirilmasligi kerak  
- [C] `None` va `None`  
- [D] `150` va `150` — o'zgartirib bo'lmaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `_quvvat` — protected atribut. Python buni texnik jihatdan taqiqlamaydi, shuning uchun `150` va `200` chiqadi. Lekin bu dasturchi uchun "ichki ishlatish" signaliga ko'ra murojaat qilinmasligi kerak.

---

## Savol 18

Quyidagi kodning natijasi nima?

```python
class Pasport:
    def __init__(self, ism, seria):
        self.ism = ism
        self.__seria = seria

    def malumot(self):
        return f"{self.ism} - {self.__seria}"

p = Pasport("Sardor", "AA1234567")
print(p.malumot())
print(p.__seria)
```

- [A] `Sardor - AA1234567` va `AA1234567`  
- [B] `Sardor - AA1234567` chiqadi, keyin `AttributeError`  
- [C] Ikki qator ham xato beradi  
- [D] `None` va `None`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `p.malumot()` class ichidan `self.__seria` ga murojaat qiladi → `"Sardor - AA1234567"` chiqadi. Keyin `p.__seria` tashqaridan chaqirilganda name mangling tufayli `AttributeError` yuzaga keladi.

---

## Savol 19

`@property.deleter` nima uchun ishlatiladi?

- [A] Butun classni o'chirish uchun  
- [B] `del obj.atribut` sintaksisi chaqirilganda bajariladigan mantiqni belgilash uchun  
- [C] Faqat list atributlarni tozalash uchun  
- [D] Atributni yashirish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `@property.deleter` — `del obj.atribut` yozilganda ishga tushadigan metodni belgilaydi. Bu atributni o'chirishdan oldin maxsus amallar bajarish (jurnal yozish, resurs bo'shatish) imkonini beradi.

---

## Savol 20

Quyidagi kodning natijasi nima?

```python
class Fayl:
    def __init__(self, nom):
        self.__nom = nom

    @property
    def nom(self):
        return self.__nom

    @nom.deleter
    def nom(self):
        print(f"{self.__nom} o'chirilmoqda...")
        del self.__nom

f = Fayl("hujjat.txt")
print(f.nom)
del f.nom
```

- [A] `hujjat.txt` chiqadi, keyin xato  
- [B] `hujjat.txt` chiqadi, keyin `hujjat.txt o'chirilmoqda...`  
- [C] Faqat xato beradi  
- [D] `None` chiqadi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `f.nom` → `"hujjat.txt"`. `del f.nom` → `@nom.deleter` ishga tushadi → `"hujjat.txt o'chirilmoqda..."` chiqadi va `__nom` o'chiriladi.

---

## Savol 21

Encapsulation qanday afzallikllar beradi?

- [A] Kodni faqat qisqartiradi  
- [B] Ma'lumotlarni himoya qiladi, validatsiya imkonini beradi, kodni modulli va ta'mirlanishi oson qiladi  
- [C] Faqat dastur tezligini oshiradi  
- [D] Faqat meros olishni osonlashtiradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Encapsulationning asosiy afzalliklari: (1) ma'lumotlarni noto'g'ri o'zgartirishdan himoya qiladi, (2) setter orqali validatsiya imkonini beradi, (3) ichki implementatsiyani o'zgartirish tashqi interfeysga ta'sir qilmaydi, (4) kodni modulli va tushunarli qiladi.

---

## Savol 22

Quyidagi kodning natijasi nima?

```python
class Temperatura:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, qiymat):
        if qiymat < -273.15:
            raise ValueError("Mutlaq noldan past bo'lishi mumkin emas!")
        self.__celsius = qiymat

    @property
    def fahrenheit(self):
        return self.__celsius * 9/5 + 32

t = Temperatura(100)
print(t.fahrenheit)
```

- [A] `100`  
- [B] `37.0`  
- [C] `212.0`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `t.fahrenheit` → `100 * 9/5 + 32 = 180 + 32 = 212.0`. `@property` orqali `fahrenheit` atribut kabi chaqiriladi va celsius dan hisoblangan qiymat qaytariladi.

---

## Savol 23

Quyidagi kodda encapsulationning qaysi printsipi buzilgan?

```python
class BankHisob:
    def __init__(self, balans):
        self.balans = balans

b = BankHisob(1000000)
b.balans = -9999999
print(b.balans)
```

- [A] Hech narsa buzilmagan  
- [B] `balans` public atribut bo'lgani uchun tashqaridan validatsiyasiz o'zgartirildi — encapsulation buzildi  
- [C] `__init__` noto'g'ri yozilgan  
- [D] Meros olish qoidasi buzilgan  

> **To'g'ri javob:** B  
> **Tushuntirish:** `balans` public atribut — tashqaridan istalgan qiymat, hatto manfiy ham, bemalol o'rnatilishi mumkin. Bu encapsulationni buzadi. To'g'ri yechim — `__balans` qilib, setter orqali validatsiya qo'shish.

---

## Savol 24

Quyidagi kodning natijasi nima?

```python
class Parol:
    def __init__(self, parol):
        self.__parol = parol

    def tekshir(self, kiritilgan):
        return self.__parol == kiritilgan

    def ozgartir(self, eski, yangi):
        if self.__parol == eski:
            self.__parol = yangi
            return "Parol o'zgartirildi!"
        return "Eski parol noto'g'ri!"

p = Parol("secret123")
print(p.tekshir("secret123"))
print(p.ozgartir("secret123", "newpass456"))
print(p.tekshir("newpass456"))
```

- [A] `False`, `Eski parol noto'g'ri!`, `False`  
- [B] `True`, `Parol o'zgartirildi!`, `True`  
- [C] Xato beradi  
- [D] `True`, `None`, `False`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `tekshir("secret123")` → `True`. `ozgartir("secret123", "newpass456")` → parol to'g'ri, yangilanadi → `"Parol o'zgartirildi!"`. `tekshir("newpass456")` → yangi parol bilan `True`.

---

## Savol 25

Quyidagi kodning natijasi nima?

```python
class Karta:
    def __init__(self, raqam, cvv):
        self.egasi = "Noma'lum"
        self._raqam = raqam
        self.__cvv = cvv

    def to_string(self):
        return f"**** **** **** {self._raqam[-4:]}"

k = Karta("1234567890123456", "123")
k.egasi = "Jasur"
print(k.egasi)
print(k.to_string())
print(k._raqam)
print(k.__cvv)
```

- [A] Hammasi chiqadi  
- [B] `Jasur`, `**** **** **** 3456`, `1234567890123456` chiqadi, keyin `AttributeError`  
- [C] Faqat `AttributeError`  
- [D] `Jasur`, `None`, `None`, `123`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `k.egasi` → `"Jasur"` (public). `k.to_string()` → `"**** **** **** 3456"`. `k._raqam` → texnik mumkin → `"1234567890123456"`. `k.__cvv` → name mangling → `AttributeError`.

---

## Savol 26

Meros olishda private atributlarga farzand class murojaat qila oladimi?

- [A] Ha, meros orqali barcha atributlarga murojaat qilish mumkin  
- [B] Yo'q, `__atribut` name mangling tufayli farzand classdan ham to'g'ridan-to'g'ri ko'rinmaydi  
- [C] Faqat `super()` orqali mumkin  
- [D] Faqat getter metod orqali mumkin  

> **To'g'ri javob:** B  
> **Tushuntirish:** Name mangling `__atribut` ni `_OtaClass__atribut` ga aylantiradi. Farzand class `self.__atribut` deb murojaat qilsa, Python uni `_FarzandClass__atribut` deb izlaydi — bu boshqacha nom, shuning uchun topilmaydi.

---

## Savol 27

Quyidagi kodning natijasi nima?

```python
class Ota:
    def __init__(self):
        self.__sir = "ota siri"

    def sir_ko_rsat(self):
        return self.__sir

class Farzand(Ota):
    def farzand_sir(self):
        return self.__sir

f = Farzand()
print(f.sir_ko_rsat())
print(f.farzand_sir())
```

- [A] `ota siri` va `ota siri`  
- [B] `ota siri` chiqadi, keyin `AttributeError`  
- [C] Ikki qator ham xato  
- [D] `None` va `None`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `f.sir_ko_rsat()` — ota classning metodi, `self.__sir` → `_Ota__sir` → `"ota siri"` chiqadi. `f.farzand_sir()` — farzand classda `self.__sir` → `_Farzand__sir` deb qidiriladi, lekin bunday atribut yo'q → `AttributeError`.

---

## Savol 28

`@property` ishlatishning oddiy getter metoddan afzalligi nima?

- [A] Hech qanday afzalligi yo'q  
- [B] `@property` atribut kabi qavssiz chaqiriladi, kodni yanada o'qilishi oson va Pythonic qiladi  
- [C] `@property` tezroq ishlaydi  
- [D] `@property` faqat private atributlar uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `@property` bilan `obj.radius` (atribut kabi), oddiy getter bilan esa `obj.get_radius()` (metod kabi) chaqiriladi. `@property` kodni yanada tabiiy, o'qilishi oson va Pythonic qiladi. Tashqi interfeys o'zgarmagan holda ichki implementatsiyani o'zgartirish mumkin.

---

## Savol 29

Quyidagi kodning natijasi nima?

```python
class Ombor:
    def __init__(self):
        self.__mahsulotlar = {}

    def qosh(self, nom, miqdor):
        if miqdor > 0:
            self.__mahsulotlar[nom] = miqdor
        else:
            print(f"{nom} uchun miqdor manfiy bo'lishi mumkin emas!")

    def olish(self, nom):
        return self.__mahsulotlar.get(nom, "Topilmadi")

    @property
    def jami(self):
        return sum(self.__mahsulotlar.values())

o = Ombor()
o.qosh("Olma", 50)
o.qosh("Nok", -5)
o.qosh("Uzum", 30)
print(o.olish("Nok"))
print(o.jami)
```

- [A] `Topilmadi`, `80`  
- [B] `-5`, `75`  
- [C] `Topilmadi`, `50`  
- [D] Xato beradi  

> **To'g'ri javob:** A  
> **Tushuntirish:** `qosh("Nok", -5)` → miqdor manfiy, qo'shilmadi. `olish("Nok")` → lug'atda yo'q → `"Topilmadi"`. `jami` → `50 + 30 = 80`. Natija: `Topilmadi`, `80`.

---

## Savol 30

Quyidagi to'liq encapsulation namunasidagi kodning natijasi nima?

```python
class Xodim:
    def __init__(self, ism, oylik):
        self.__ism = ism
        self.__oylik = oylik

    @property
    def ism(self):
        return self.__ism

    @property
    def oylik(self):
        return f"{self.__oylik:,} so'm"

    @oylik.setter
    def oylik(self, yangi):
        if yangi >= 1000000:
            self.__oylik = yangi
        else:
            print("Minimal oylik 1,000,000 so'm!")

    def __str__(self):
        return f"Xodim: {self.__ism}, Oylik: {self.oylik}"

x = Xodim("Bobur", 3000000)
x.oylik = 5000000
print(x.oylik)
x.oylik = 500000
print(x.oylik)
print(x)
```

- [A] `5,000,000 so'm`, `500,000 so'm`, `Xodim: Bobur, Oylik: 500,000 so'm`  
- [B] `5,000,000 so'm`, `Minimal oylik 1,000,000 so'm!` va `5,000,000 so'm`, `Xodim: Bobur, Oylik: 5,000,000 so'm`  
- [C] Xato beradi  
- [D] `3,000,000 so'm`, `5,000,000 so'm`, `Xodim: Bobur, Oylik: 3,000,000 so'm`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `x.oylik = 5000000` → `5000000 >= 1000000` → `__oylik = 5000000`. `x.oylik` → `"5,000,000 so'm"`. `x.oylik = 500000` → shart bajarilmadi → `"Minimal oylik 1,000,000 so'm!"`. `x.oylik` → `"5,000,000 so'm"` (o'zgarmagan). `str(x)` → `"Xodim: Bobur, Oylik: 5,000,000 so'm"`.

---