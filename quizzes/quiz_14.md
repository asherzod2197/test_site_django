## Savol 1

Getter metodi nima?

- [A] Obyektni o'chiruvchi metod  
- [B] Yopiq (private) yoki himoyalangan atributning qiymatini tashqariga xavfsiz qaytaruvchi metod  
- [C] Yangi atribut yaratuvchi metod  
- [D] Classni nusxalovchi metod  

> **To'g'ri javob:** B  
> **Tushuntirish:** Getter — bu private atributni tashqaridan o'qish imkonini beruvchi metod. U encapsulationni saqlab, atributga bevosita kirishni oldini oladi va qiymatni nazorat ostida qaytaradi.

---

## Savol 2

Setter metodi nima?

- [A] Atributni o'qish uchun ishlatiladigan metod  
- [B] Yopiq atributning qiymatini validatsiya qilib o'zgartiruvchi metod  
- [C] Classni o'chirish uchun ishlatiladigan metod  
- [D] Yangi obyekt yaratuvchi metod  

> **To'g'ri javob:** B  
> **Tushuntirish:** Setter — private atributga qiymat belgilash uchun ishlatiladigan metod. U kiruvchi ma'lumotni tekshirish (validatsiya) imkonini beradi va noto'g'ri qiymatlarning o'rnatilishini oldini oladi.

---

## Savol 3

Getter va Setter metodlarining asosiy maqsadi nima?

- [A] Kodni qisqartirish  
- [B] Encapsulationni ta'minlab, atributlarga nazorat ostida kirish va o'zgartirish imkonini berish  
- [C] Dastur tezligini oshirish  
- [D] Faqat meros olishda ishlatiladi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Getter va Setter metodlarining asosiy maqsadi — encapsulationni saqlagan holda private atributlarga nazorat ostida kirish imkonini berish. Setter validatsiya qo'shish, getter esa qiymatni xavfsiz qaytarish imkonini beradi.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
class Talaba:
    def __init__(self, ism):
        self.__ism = ism

    def get_ism(self):
        return self.__ism

t = Talaba("Sardor")
print(t.get_ism())
```

- [A] `None`  
- [B] `__ism`  
- [C] `Sardor`  
- [D] `AttributeError`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `get_ism()` — getter metod bo'lib, `self.__ism` ni qaytaradi. `Talaba("Sardor")` da `__ism = "Sardor"` o'rnatilgan. `t.get_ism()` → `"Sardor"`.

---

## Savol 5

Quyidagi kodning natijasi nima?

```python
class Mahsulot:
    def __init__(self, narx):
        self.__narx = narx

    def get_narx(self):
        return self.__narx

    def set_narx(self, yangi_narx):
        if yangi_narx > 0:
            self.__narx = yangi_narx

m = Mahsulot(50000)
m.set_narx(75000)
print(m.get_narx())
```

- [A] `50000`  
- [B] `0`  
- [C] `75000`  
- [D] `AttributeError`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `set_narx(75000)` da `75000 > 0` shart bajarildi → `__narx = 75000`. `get_narx()` → `75000`.

---

## Savol 6

Quyidagi kodning natijasi nima?

```python
class Hisob:
    def __init__(self, balans):
        self.__balans = balans

    def set_balans(self, yangi):
        if yangi >= 0:
            self.__balans = yangi
        else:
            print("Manfiy balans qabul qilinmaydi!")

    def get_balans(self):
        return self.__balans

h = Hisob(100000)
h.set_balans(-500)
print(h.get_balans())
```

- [A] `-500`  
- [B] `0`  
- [C] `Manfiy balans qabul qilinmaydi!` va `100000`  
- [D] `AttributeError`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `set_balans(-500)` da `-500 >= 0` shart bajarilmadi → `else` bloki ishladi. `__balans` o'zgarmadi. `get_balans()` → `100000`.

---

## Savol 7

`@property` dekoratori nimani amalga oshiradi?

- [A] Metodlarni statik qiladi  
- [B] Metodni atribut kabi qavssiz chaqirish imkonini beruvchi getter yaratadi  
- [C] Classni yopadi  
- [D] Meros olishni taqiqlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `@property` dekoratori metoddan xuddi atribut kabi foydalanish imkonini beradi. `obj.metod_nomi` (qavssiz) ko'rinishida chaqiriladi. Bu getter yaratishning Pythonic (Pythonga xos) usuli.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
class Doira:
    def __init__(self, r):
        self.__r = r

    @property
    def radius(self):
        return self.__r

    @property
    def yuza(self):
        return round(3.14 * self.__r ** 2, 2)

d = Doira(7)
print(d.radius)
print(d.yuza)
```

- [A] Xato beradi, qavs yo'q  
- [B] `7` va `153.94`  
- [C] `7` va `3.14`  
- [D] `None` va `None`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `@property` bilan belgilangan metodlar atribut kabi qavssiz chaqiriladi. `d.radius` → `7`. `d.yuza` → `3.14 * 49 = 153.86` → `round(..., 2)` → `153.86`.

---

## Savol 9

`@property.setter` qanday ishlatiladi?

- [A] `@property` ni o'chirish uchun  
- [B] `@property` bilan juftlikda ishlatiladi — `obj.atribut = qiymat` sintaksisida qiymat o'rnatadi  
- [C] Faqat class metodlarida ishlatiladi  
- [D] Atributni himoyalash uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `@property.setter` — property ning yozish qismi. `obj.atribut = qiymat` yozilganda ishga tushadi va qiymat belgilashdan oldin validatsiya qilish imkonini beradi.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
class Temperatura:
    def __init__(self, daraja):
        self.__daraja = daraja

    @property
    def daraja(self):
        return self.__daraja

    @daraja.setter
    def daraja(self, yangi):
        if yangi >= -273.15:
            self.__daraja = yangi
        else:
            print("Mutlaq noldan past!")

t = Temperatura(25)
t.daraja = 37
print(t.daraja)
t.daraja = -300
print(t.daraja)
```

- [A] `37`, `37`  
- [B] `37`, `Mutlaq noldan past!` va `37`  
- [C] `25`, `37`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `t.daraja = 37` → `-273.15` dan katta → `__daraja = 37`. `t.daraja = -300` → shart bajarilmadi → `"Mutlaq noldan past!"` chiqdi, qiymat o'zgarmadi. `t.daraja` → `37`.

---

## Savol 11

Quyidagi kodda xato bormi?

```python
class Yosh:
    def __init__(self, yosh):
        self.__yosh = yosh

    @property
    def yosh(self):
        return self.__yosh

    @yosh.setter
    def yosh(self, yangi):
        if 0 < yangi < 150:
            self.__yosh = yangi

y = Yosh(25)
print(y.yosh)
y.yosh = 30
print(y.yosh)
```

- [A] Ha, `@property` da xato bor  
- [B] Ha, setter noto'g'ri yozilgan  
- [C] Xato yo'q — `25` va `30` chiqadi  
- [D] Ha, `__yosh` ga murojaat qilib bo'lmaydi  

> **To'g'ri javob:** C  
> **Tushuntirish:** Kod to'g'ri. `y.yosh` → `25`. `y.yosh = 30` → `0 < 30 < 150` → `__yosh = 30`. `y.yosh` → `30`.

---

## Savol 12

Oddiy getter/setter va `@property` o'rtasidagi farq nima?

- [A] Hech qanday farq yo'q  
- [B] `@property` atribut kabi qavssiz chaqiriladi va kodni yanada Pythonic qiladi; oddiy getter/setter esa metod kabi `()` bilan chaqiriladi  
- [C] Oddiy getter/setter tezroq ishlaydi  
- [D] `@property` faqat class metodlarida ishlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Oddiy getter: `obj.get_ism()` — qavs bilan chaqiriladi. `@property`: `obj.ism` — atribut kabi qavssiz. `@property` kodni yanada tabiiy va o'qilishi oson qiladi. Tashqi interfeys o'zgarmagan holda ichki implementatsiyani almashtirish mumkin.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
class Oylik:
    def __init__(self, summa):
        self.__summa = summa

    @property
    def summa(self):
        return f"{self.__summa:,} so'm"

    @summa.setter
    def summa(self, yangi):
        if yangi >= 1000000:
            self.__summa = yangi
        else:
            print("Minimal oylik 1,000,000 so'm!")

x = Oylik(3000000)
print(x.summa)
x.summa = 5000000
print(x.summa)
```

- [A] `3000000` va `5000000`  
- [B] `3,000,000 so'm` va `5,000,000 so'm`  
- [C] Xato beradi  
- [D] `None` va `None`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `x.summa` getter formatlangan qiymat qaytaradi: `"3,000,000 so'm"`. `x.summa = 5000000` → setter → `__summa = 5000000`. `x.summa` → `"5,000,000 so'm"`.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
class Talaba:
    def __init__(self, ism, ball):
        self.__ism = ism
        self.__ball = ball

    def get_ism(self):
        return self.__ism

    def get_ball(self):
        return self.__ball

    def set_ball(self, yangi):
        if 0 <= yangi <= 100:
            self.__ball = yangi
        else:
            print("Ball 0 dan 100 gacha bo'lishi kerak!")

t = Talaba("Zulfiya", 75)
t.set_ball(110)
t.set_ball(90)
print(t.get_ism(), t.get_ball())
```

- [A] `Zulfiya 75`  
- [B] `Zulfiya 110`  
- [C] `Ball 0 dan 100 gacha bo'lishi kerak!` va `Zulfiya 90`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `set_ball(110)` → `0 <= 110 <= 100` shart bajarilmadi → xabar chiqdi. `set_ball(90)` → shart bajarildi → `__ball = 90`. Natija: `Zulfiya 90`.

---

## Savol 15

`@property.deleter` nima uchun ishlatiladi?

- [A] Butun classni o'chirish uchun  
- [B] `del obj.atribut` sintaksisi chaqirilganda bajariladigan mantiqni belgilash uchun  
- [C] Faqat list atributlarni tozalash uchun  
- [D] Setter ni o'chirish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `@property.deleter` — `del obj.atribut` yozilganda ishga tushadigan metodni belgilaydi. O'chirishdan oldin jurnal yozish, resurs bo'shatish yoki boshqa amallar bajarish imkonini beradi.

---

## Savol 16

Quyidagi kodning natijasi nima?

```python
class Fayl:
    def __init__(self, nom):
        self.__nom = nom

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, yangi):
        if yangi.endswith(".txt") or yangi.endswith(".py"):
            self.__nom = yangi
        else:
            print("Faqat .txt yoki .py fayllari!")

    @nom.deleter
    def nom(self):
        print(f"'{self.__nom}' o'chirildi")
        self.__nom = None

f = Fayl("hujjat.txt")
f.nom = "dastur.py"
print(f.nom)
del f.nom
print(f.nom)
```

- [A] `dastur.py`, `dastur.py o'chirildi`, `hujjat.txt`  
- [B] `dastur.py`, `'dastur.py' o'chirildi`, `None`  
- [C] Xato beradi  
- [D] `hujjat.txt`, `None`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `f.nom = "dastur.py"` → `.py` bilan tugaydi → `__nom = "dastur.py"`. `f.nom` → `"dastur.py"`. `del f.nom` → deleter: `"'dastur.py' o'chirildi"` va `__nom = None`. `f.nom` → `None`.

---

## Savol 17

Quyidagi kodda nima xato?

```python
class Xodim:
    def __init__(self, ism):
        self.__ism = ism

    @property
    def ism(self):
        return self.__ism

x = Xodim("Bobur")
x.ism = "Jasur"
print(x.ism)
```

- [A] `@property` noto'g'ri yozilgan  
- [B] `setter` e'lon qilinmagan, shuning uchun `x.ism = "Jasur"` `AttributeError` beradi  
- [C] Xato yo'q, `Jasur` chiqadi  
- [D] `__ism` ga murojaat qilib bo'lmaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `@property` faqat getter e'lon qilgan. Setter bo'lmasa, `x.ism = "Jasur"` orqali qiymat o'rnatishga urinish `AttributeError: can't set attribute` xatosini beradi.

---

## Savol 18

Quyidagi kodning natijasi nima?

```python
class Parol:
    def __init__(self, parol):
        self.__parol = parol

    @property
    def parol(self):
        return "*" * len(self.__parol)

    @parol.setter
    def parol(self, yangi):
        if len(yangi) >= 8:
            self.__parol = yangi
        else:
            print("Parol kamida 8 ta belgidan iborat bo'lishi kerak!")

p = Parol("secret123")
print(p.parol)
p.parol = "abc"
p.parol = "yangiparol"
print(p.parol)
```

- [A] `secret123`, `abc`, `yangiparol`  
- [B] `*********`, xabar chiqadi, `**********`  
- [C] `*********`, `*********`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `p.parol` getter `"*"` lar qaytaradi: `"secret123"` → 9 ta `"*"`. `p.parol = "abc"` → uzunlik 3 < 8 → xabar. `p.parol = "yangiparol"` → 10 >= 8 → o'rnatildi. `p.parol` → 10 ta `"*"`.

---

## Savol 19

Quyidagi kodning natijasi nima?

```python
class To_rtburchak:
    def __init__(self, en, bo_y):
        self.__en = en
        self.__bo_y = bo_y

    @property
    def en(self):
        return self.__en

    @en.setter
    def en(self, qiymat):
        if qiymat > 0:
            self.__en = qiymat

    @property
    def bo_y(self):
        return self.__bo_y

    @bo_y.setter
    def bo_y(self, qiymat):
        if qiymat > 0:
            self.__bo_y = qiymat

    @property
    def yuza(self):
        return self.__en * self.__bo_y

t = To_rtburchak(4, 5)
t.en = 6
t.bo_y = -3
print(t.en, t.bo_y, t.yuza)
```

- [A] `6 -3 -18`  
- [B] `6 5 30`  
- [C] `4 5 20`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `t.en = 6` → `6 > 0` → `__en = 6`. `t.bo_y = -3` → `-3 > 0` shart bajarilmadi → `__bo_y` o'zgarmadi, `5` qoldi. `t.yuza` → `6 * 5 = 30`. Natija: `6 5 30`.

---

## Savol 20

Quyidagi kodning natijasi nima?

```python
class Avtomobil:
    def __init__(self, model, tezlik):
        self.__model = model
        self.__tezlik = tezlik

    @property
    def tezlik(self):
        return self.__tezlik

    @tezlik.setter
    def tezlik(self, yangi):
        if 0 <= yangi <= 300:
            self.__tezlik = yangi
        else:
            print(f"Tezlik 0-300 orasida bo'lishi kerak!")

    @property
    def holat(self):
        if self.__tezlik == 0:
            return "To'xtagan"
        elif self.__tezlik <= 60:
            return "Sekin"
        elif self.__tezlik <= 120:
            return "O'rtacha"
        else:
            return "Tez"

a = Avtomobil("BMW", 0)
a.tezlik = 80
print(a.tezlik, a.holat)
a.tezlik = 350
print(a.tezlik, a.holat)
```

- [A] `80 O'rtacha`, `350 Tez`  
- [B] `80 O'rtacha`, xabar va `80 O'rtacha`  
- [C] `0 To'xtagan`, `80 O'rtacha`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `a.tezlik = 80` → `0 <= 80 <= 300` → `__tezlik = 80`. `a.holat` → `"O'rtacha"`. `a.tezlik = 350` → shart bajarilmadi → xabar chiqdi, `__tezlik = 80` qoldi. `a.tezlik` → `80`, `a.holat` → `"O'rtacha"`.

---

## Savol 21

Quyidagi kodning natijasi nima?

```python
class Dokon:
    def __init__(self, nomi):
        self.__nomi = nomi
        self.__ochiq = False

    @property
    def ochiq(self):
        return self.__ochiq

    @ochiq.setter
    def ochiq(self, holat):
        if isinstance(holat, bool):
            self.__ochiq = holat
        else:
            print("Faqat True yoki False!")

    def __str__(self):
        holat = "ochiq" if self.__ochiq else "yopiq"
        return f"{self.__nomi} hozir {holat}"

d = Dokon("Najot Market")
d.ochiq = True
print(d)
d.ochiq = "ha"
print(d.ochiq)
```

- [A] `Najot Market hozir ochiq`, `True`  
- [B] `Najot Market hozir ochiq`, xabar va `True`  
- [C] `Najot Market hozir yopiq`, `False`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `d.ochiq = True` → `isinstance(True, bool)` → `True` → `__ochiq = True`. `str(d)` → `"Najot Market hozir ochiq"`. `d.ochiq = "ha"` → `isinstance("ha", bool)` → `False` → xabar. `d.ochiq` → `True` (o'zgarmagan).

---

## Savol 22

Quyidagi kodning natijasi nima?

```python
class Kitob:
    def __init__(self, nomi, sahifalar):
        self.__nomi = nomi
        self.__sahifalar = sahifalar
        self.__joriy = 0

    @property
    def joriy(self):
        return self.__joriy

    @joriy.setter
    def joriy(self, bet):
        if 0 <= bet <= self.__sahifalar:
            self.__joriy = bet
        else:
            print(f"Bet 0 dan {self.__sahifalar} gacha bo'lishi kerak!")

    @property
    def qolgan(self):
        return self.__sahifalar - self.__joriy

k = Kitob("Algoritm", 300)
k.joriy = 150
print(k.joriy, k.qolgan)
k.joriy = 400
print(k.joriy, k.qolgan)
```

- [A] `150 150`, `400 -100`  
- [B] `150 150`, xabar va `150 150`  
- [C] `0 300`, `150 150`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `k.joriy = 150` → `0 <= 150 <= 300` → `__joriy = 150`. `k.qolgan` → `300 - 150 = 150`. `k.joriy = 400` → `0 <= 400 <= 300` shart bajarilmadi → xabar. `k.joriy` → `150`, `k.qolgan` → `150`.

---

## Savol 23

Getter metodida qo'shimcha hisob-kitob qilish mumkinmi?

- [A] Yo'q, getter faqat qiymatni qaytaradi  
- [B] Ha, getter atribut qiymatini qaytarishdan oldin hisob-kitob yoki formatlash bajarishi mumkin  
- [C] Faqat setter da hisob-kitob qilish mumkin  
- [D] Faqat `@staticmethod` da hisob-kitob qilish mumkin  

> **To'g'ri javob:** B  
> **Tushuntirish:** Getter shunchaki qiymat qaytarish bilan chegaralanmaydi — u qaytarishdan oldin hisoblash, formatlash, konvertatsiya va boshqa amallar bajarishi mumkin. Masalan, `celsius` ni `fahrenheit` ga aylantirish yoki sonni formatlash.

---

## Savol 24

Quyidagi kodning natijasi nima?

```python
class Valyuta:
    def __init__(self, usd):
        self.__usd = usd

    @property
    def usd(self):
        return self.__usd

    @usd.setter
    def usd(self, yangi):
        if yangi >= 0:
            self.__usd = yangi

    @property
    def uzs(self):
        return self.__usd * 12700

    @property
    def eur(self):
        return round(self.__usd / 1.08, 2)

v = Valyuta(100)
print(v.uzs)
print(v.eur)
v.usd = 200
print(v.uzs)
```

- [A] `1270000`, `92.59`, `1270000`  
- [B] `1270000`, `92.59`, `2540000`  
- [C] `100`, `100`, `200`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `v.uzs` → `100 * 12700 = 1270000`. `v.eur` → `round(100/1.08, 2) = 92.59`. `v.usd = 200` → setter → `__usd = 200`. `v.uzs` → `200 * 12700 = 2540000`.

---

## Savol 25

Quyidagi kodda nima muammo bor va uni qanday tuzatish mumkin?

```python
class Uchburchak:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

u = Uchburchak(3, 4, 5)
u.a = -10
print(u.a)
```

- [A] Muammo yo'q  
- [B] Tomonlar public bo'lgani uchun manfiy qiymat ham o'rnatildi — setter bilan validatsiya kerak  
- [C] `__init__` da xato bor  
- [D] `print` noto'g'ri ishlatilgan  

> **To'g'ri javob:** B  
> **Tushuntirish:** `a`, `b`, `c` public atributlar — hech qanday validatsiyasiz manfiy qiymat ham o'rnatiladi. To'g'ri yechim: `self.__a = a` qilib, `@property` va setter bilan `if qiymat > 0` validatsiya qo'shish kerak.

---

## Savol 26

Quyidagi kodning natijasi nima?

```python
class Talabalar:
    def __init__(self):
        self.__royxat = []

    @property
    def soni(self):
        return len(self.__royxat)

    @property
    def royxat(self):
        return self.__royxat.copy()

    def qosh(self, ism):
        if ism not in self.__royxat:
            self.__royxat.append(ism)
        else:
            print(f"{ism} allaqachon ro'yxatda!")

t = Talabalar()
t.qosh("Ali")
t.qosh("Vali")
t.qosh("Ali")
print(t.soni)
print(t.royxat)
```

- [A] `3`, `["Ali", "Vali", "Ali"]`  
- [B] `2`, `["Ali", "Vali"]`  
- [C] `1`, `["Ali"]`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `qosh("Ali")` → qo'shildi. `qosh("Vali")` → qo'shildi. `qosh("Ali")` → allaqachon bor → xabar. `t.soni` → `2`. `t.royxat` → `["Ali", "Vali"]` nusxasi qaytariladi.

---

## Savol 27

Quyidagi kodning natijasi nima?

```python
class Telefon:
    def __init__(self, model, batareya):
        self.__model = model
        self.__batareya = batareya

    @property
    def batareya(self):
        return f"{self.__batareya}%"

    @batareya.setter
    def batareya(self, yangi):
        if 0 <= yangi <= 100:
            self.__batareya = yangi
        else:
            print("Batareya 0-100% orasida!")

    @batareya.deleter
    def batareya(self):
        print("Batareya ma'lumoti o'chirildi!")
        self.__batareya = 0

t = Telefon("Samsung", 80)
t.batareya = 95
print(t.batareya)
del t.batareya
print(t.batareya)
```

- [A] `95%`, `0%`  
- [B] `95%`, `Batareya ma'lumoti o'chirildi!` va `0%`  
- [C] `80%`, `0%`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `t.batareya = 95` → setter → `__batareya = 95`. `t.batareya` → `"95%"`. `del t.batareya` → deleter: xabar chiqadi, `__batareya = 0`. `t.batareya` → `"0%"`.

---

## Savol 28

Quyidagi kodning natijasi nima?

```python
class Matritsa:
    def __init__(self, n):
        self.__n = n
        self.__data = [[0]*n for _ in range(n)]

    @property
    def o_lcham(self):
        return f"{self.__n}x{self.__n}"

    def set_qiymat(self, i, j, val):
        if 0 <= i < self.__n and 0 <= j < self.__n:
            self.__data[i][j] = val
        else:
            print("Indeks xato!")

    def get_qiymat(self, i, j):
        if 0 <= i < self.__n and 0 <= j < self.__n:
            return self.__data[i][j]
        return None

m = Matritsa(3)
m.set_qiymat(0, 0, 5)
m.set_qiymat(1, 1, 8)
m.set_qiymat(3, 3, 10)
print(m.o_lcham)
print(m.get_qiymat(0, 0), m.get_qiymat(1, 1))
```

- [A] `3x3`, `5 8`  
- [B] `3x3`, `Indeks xato!` va `5 8`  
- [C] `3x3`, `None None`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `set_qiymat(3,3,10)` → `0 <= 3 < 3` shart bajarilmadi → `"Indeks xato!"`. `m.o_lcham` → `"3x3"`. `get_qiymat(0,0)` → `5`, `get_qiymat(1,1)` → `8`.

---

## Savol 29

Quyidagi kodning natijasi nima?

```python
class Hisobot:
    def __init__(self, nomi):
        self.__nomi = nomi
        self.__malumotlar = []

    @property
    def nomi(self):
        return self.__nomi.upper()

    @nomi.setter
    def nomi(self, yangi):
        if len(yangi) >= 3:
            self.__nomi = yangi.strip()
        else:
            print("Nom kamida 3 ta harf bo'lishi kerak!")

    def qosh(self, qiymat):
        self.__malumotlar.append(qiymat)

    @property
    def jami(self):
        return sum(self.__malumotlar)

    @property
    def ortacha(self):
        if self.__malumotlar:
            return round(self.jami / len(self.__malumotlar), 2)
        return 0

h = Hisobot("oylik")
h.nomi = "  daromad  "
h.qosh(500000)
h.qosh(750000)
h.qosh(1000000)
print(h.nomi)
print(h.jami)
print(h.ortacha)
```

- [A] `oylik`, `2250000`, `750000.0`  
- [B] `DAROMAD`, `2250000`, `750000.0`  
- [C] `daromad`, `2250000`, `750000.0`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `h.nomi = "  daromad  "` → `len >= 3` → `.strip()` → `"daromad"`. `h.nomi` getter → `.upper()` → `"DAROMAD"`. `h.jami` → `500000 + 750000 + 1000000 = 2250000`. `h.ortacha` → `2250000 / 3 = 750000.0`.

---

## Savol 30

Quyidagi to'liq namunaning natijasi nima?

```python
class BankHisob:
    def __init__(self, egasi, balans):
        self.__egasi = egasi
        self.__balans = balans
        self.__tranzaksiyalar = []

    @property
    def egasi(self):
        return self.__egasi

    @property
    def balans(self):
        return self.__balans

    def kirim(self, summa):
        if summa > 0:
            self.__balans += summa
            self.__tranzaksiyalar.append(f"+{summa}")
        else:
            print("Summa musbat bo'lishi kerak!")

    def chiqim(self, summa):
        if 0 < summa <= self.__balans:
            self.__balans -= summa
            self.__tranzaksiyalar.append(f"-{summa}")
        else:
            print("Yetarli mablag' yo'q yoki summa noto'g'ri!")

    @property
    def tranzaksiyalar(self):
        return self.__tranzaksiyalar.copy()

h = BankHisob("Murod", 1000000)
h.kirim(500000)
h.chiqim(200000)
h.chiqim(2000000)
print(h.balans)
print(len(h.tranzaksiyalar))
```

- [A] `1300000`, `3`  
- [B] `Yetarli mablag' yo'q yoki summa noto'g'ri!` va `1300000`, `2`  
- [C] `1000000`, `0`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `kirim(500000)` → `__balans = 1500000`, tranzaksiya `"+500000"`. `chiqim(200000)` → `200000 <= 1500000` → `__balans = 1300000`, tranzaksiya `"-200000"`. `chiqim(2000000)` → `2000000 > 1300000` → xabar, qo'shilmadi. `h.balans` → `1300000`. Tranzaksiyalar: `2` ta.

---