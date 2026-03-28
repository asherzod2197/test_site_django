## Savol 1

`__init__` metodi nima?

- [A] Classni o'chiruvchi metod  
- [B] Obyekt yaratilganda avtomatik chaqiriladigan konstruktor metod  
- [C] Faqat class atributlarini o'quvchi metod  
- [D] Dastur boshlanishida bir marta ishlaydigan funksiya  

> **To'g'ri javob:** B  
> **Tushuntirish:** `__init__` — bu konstruktor metod bo'lib, classdan yangi obyekt yaratilgan zahoti avtomatik chaqiriladi va obyektning boshlang'ich holatini (atributlarini) o'rnatadi.

---

## Savol 2

`__init__` metodining birinchi parametri nima bo'lishi shart?

- [A] `this`  
- [B] `init`  
- [C] `self`  
- [D] `cls`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `__init__` metodining birinchi parametri `self` bo'lishi shart. `self` — bu yaratilayotgan obyektning o'ziga ishora qiladi va atributlarni o'rnatish uchun ishlatiladi.

---

## Savol 3

Quyidagi kodda `__init__` necha marta chaqiriladi?

```python
class Kalit:
    def __init__(self):
        print("Kalit yaratildi")

k1 = Kalit()
k2 = Kalit()
k3 = Kalit()
```

- [A] 1 marta  
- [B] 2 marta  
- [C] 3 marta  
- [D] 0 marta  

> **To'g'ri javob:** C  
> **Tushuntirish:** Har bir obyekt yaratilganda `__init__` bir marta chaqiriladi. `k1`, `k2`, `k3` — 3 ta obyekt yaratilgani uchun `"Kalit yaratildi"` 3 marta chiqariladi.

---

## Savol 4

`__init__` metodisiz class yaratish mumkinmi?

- [A] Yo'q, `__init__` majburiy  
- [B] Ha, lekin obyekt yaratib bo'lmaydi  
- [C] Ha, `__init__` ixtiyoriy — bo'lmasa Python standart bo'sh konstruktorni ishlatadi  
- [D] Faqat meros olish orqali mumkin  

> **To'g'ri javob:** C  
> **Tushuntirish:** `__init__` ixtiyoriy. Agar yozilmasa, Python avtomatik ravishda bo'sh konstruktorni qo'llaydi va obyekt hali ham yaratilishi mumkin, faqat boshlang'ich atributlar bo'lmaydi.

---

## Savol 5

Quyidagi kodning natijasi nima?

```python
class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif

k = Kitob("Xamsa", "Navoiy")
print(k.nomi, "-", k.muallif)
```

- [A] `nomi - muallif`  
- [B] `Kitob - Kitob`  
- [C] `Xamsa - Navoiy`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Kitob("Xamsa", "Navoiy")` chaqirilganda `self.nomi = "Xamsa"` va `self.muallif = "Navoiy"` o'rnatiladi. `k.nomi` → `"Xamsa"`, `k.muallif` → `"Navoiy"`.

---

## Savol 6

`__init__` metodi qanday qiymat qaytaradi?

- [A] Yaratilgan obyektni  
- [B] `True` yoki `False`  
- [C] Hech narsa qaytarmaydi (`None`)  
- [D] `self` ni  

> **To'g'ri javob:** C  
> **Tushuntirish:** `__init__` metodi hech qachon qiymat qaytarmaydi — doim `None` qaytaradi. Agar `return` orqali boshqa qiymat qaytarishga urinilsa, Python `TypeError` xatosi beradi.

---

## Savol 7

Quyidagi kodda xato bormi?

```python
class Foydalanuvchi:
    def __init__(self, ism):
        self.ism = ism
        return self.ism

f = Foydalanuvchi("Hamid")
```

- [A] Xato yo'q  
- [B] Ha, `__init__` da `return` ishlatib bo'lmaydi (faqat `None` qaytarish mumkin)  
- [C] Ha, `self` noto'g'ri ishlatilgan  
- [D] Ha, `ism` parametri noto'g'ri  

> **To'g'ri javob:** B  
> **Tushuntirish:** `__init__` metodida `return None` (yoki bo'sh `return`) ruxsat etiladi, lekin boshqa qiymat qaytarish `TypeError: __init__() should return None` xatosini beradi.

---

## Savol 8

Default (standart) parametrli `__init__` qanday yoziladi?

```python
class Talaba:
    def __init__(self, ism, ball=0):
        self.ism = ism
        self.ball = ball
```

Quyidagi chaqiruvlardan qaysi biri to'g'ri?

- [A] Faqat `Talaba("Ali", 90)` to'g'ri  
- [B] Faqat `Talaba("Ali")` to'g'ri  
- [C] Ikkala `Talaba("Ali")` va `Talaba("Ali", 90)` ham to'g'ri  
- [D] Ikkalasi ham xato  

> **To'g'ri javob:** C  
> **Tushuntirish:** `ball=0` standart qiymat bo'lgani uchun u ixtiyoriy. `Talaba("Ali")` → `ball=0`, `Talaba("Ali", 90)` → `ball=90`. Ikkalasi ham to'g'ri ishlaydi.

---

## Savol 9

Quyidagi kodning natijasi nima?

```python
class Shakl:
    def __init__(self, rang="qizil", o_lcham=10):
        self.rang = rang
        self.o_lcham = o_lcham

s = Shakl()
print(s.rang, s.o_lcham)
```

- [A] Xato beradi, argumentlar talab qilinadi  
- [B] `None None`  
- [C] `qizil 10`  
- [D] `rang o_lcham`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Barcha parametrlar standart qiymatga ega (`rang="qizil"`, `o_lcham=10`). `Shakl()` hech qanday argument uzatmay chaqirilganda standart qiymatlar ishlatiladi. Natija: `qizil 10`.

---

## Savol 10

`__init__` ichida boshqa metodlarni chaqirish mumkinmi?

- [A] Yo'q, `__init__` faqat atributlarni belgilashi mumkin  
- [B] Ha, `self.metod_nomi()` orqali boshqa metodlarni chaqirish mumkin  
- [C] Faqat statik metodlarni chaqirish mumkin  
- [D] Faqat meros olingan metodlarni chaqirish mumkin  

> **To'g'ri javob:** B  
> **Tushuntirish:** `__init__` ichida `self` orqali classning istalgan metodini chaqirish mumkin. Bu boshlang'ich sozlamalar yoki tekshiruvlarni tashkil qilish uchun qulay usul.

---

## Savol 11

Quyidagi kodning natijasi nima?

```python
class Hisoblagich:
    def __init__(self, boshlangich=0):
        self.qiymat = boshlangich
        self.ikkilantir()

    def ikkilantir(self):
        self.qiymat *= 2

h = Hisoblagich(5)
print(h.qiymat)
```

- [A] `5`  
- [B] `0`  
- [C] `10`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Hisoblagich(5)` chaqirilganda `self.qiymat = 5` o'rnatiladi, so'ng `self.ikkilantir()` chaqirilib `self.qiymat *= 2` → `10` bo'ladi. Natija: `10`.

---

## Savol 12

Meros olishda farzand class `__init__` ni e'lon qilmasa nima bo'ladi?

- [A] Xato beradi  
- [B] Farzand class ota classning `__init__` ini meros oladi va ishlatadi  
- [C] Farzand class hech qanday konstruktorsiz qoladi  
- [D] Python avtomatik bo'sh `__init__` yaratadi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Agar farzand class o'z `__init__` ini e'lon qilmasa, Python meros zanjiri bo'yicha ota classning `__init__` ini topadi va ishlatadi. Bu meros olishning asosiy xususiyatlaridan biri.

---

## Savol 13

`super().__init__()` nima uchun ishlatiladi?

- [A] Farzand classni o'chirish uchun  
- [B] Farzand class `__init__` ichida ota classning `__init__` ini chaqirish uchun  
- [C] Faqat statik metodlarda ishlatiladi  
- [D] Yangi class yaratish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `super().__init__()` — bu farzand classning `__init__` ichidan ota classning `__init__` ini chaqiradi. Bu ota classning atributlarini ham o'rnatish uchun zarur.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
class Hayvon:
    def __init__(self, ism):
        self.ism = ism

class It(Hayvon):
    def __init__(self, ism, zot):
        super().__init__(ism)
        self.zot = zot

i = It("Rex", "Labrador")
print(i.ism, i.zot)
```

- [A] Xato beradi  
- [B] `Rex Labrador`  
- [C] `ism zot`  
- [D] `None None`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `super().__init__(ism)` orqali `Hayvon.__init__` chaqirilib `self.ism = "Rex"` o'rnatiladi. So'ng `self.zot = "Labrador"` belgilanadi. Natija: `Rex Labrador`.

---

## Savol 15

`__init__` da `*args` ishlatish nima uchun kerak?

- [A] Faqat kalit-qiymat argumentlar qabul qilish uchun  
- [B] Noma'lum miqdorda pozitsion argumentlarni qabul qilish uchun  
- [C] Faqat bitta argument qabul qilish uchun  
- [D] Argumentlarni o'chirish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `*args` noma'lum miqdordagi pozitsion argumentlarni tuple ko'rinishida qabul qiladi. Bu `__init__` da turli sonli argumentlar bilan moslashuvchan obyekt yaratish imkonini beradi.

---

## Savol 16

Quyidagi kodning natijasi nima?

```python
class Savatcha:
    def __init__(self, *mahsulotlar):
        self.mahsulotlar = list(mahsulotlar)

s = Savatcha("Olma", "Nok", "Uzum")
print(len(s.mahsulotlar))
```

- [A] `0`  
- [B] `1`  
- [C] `2`  
- [D] `3`  

> **To'g'ri javob:** D  
> **Tushuntirish:** `*mahsulotlar` 3 ta argumentni (`"Olma"`, `"Nok"`, `"Uzum"`) tuple sifatida qabul qiladi. `list(mahsulotlar)` → `["Olma", "Nok", "Uzum"]`. `len()` → `3`.

---

## Savol 17

`**kwargs` ni `__init__` da ishlatishdan maqsad nima?

- [A] Faqat raqamli argumentlar qabul qilish  
- [B] Noma'lum miqdorda kalit-qiymat (keyword) argumentlarni qabul qilish  
- [C] Argumentlarni saralash  
- [D] Atributlarni o'chirish  

> **To'g'ri javob:** B  
> **Tushuntirish:** `**kwargs` noma'lum miqdordagi kalit-qiymat argumentlarni lug'at (dict) ko'rinishida qabul qiladi. Bu moslashuvchan va kengaytiriladigan konstruktor yozish uchun ishlatiladi.

---

## Savol 18

Quyidagi kodning natijasi nima?

```python
class Parametrlar:
    def __init__(self, **kwargs):
        for kalit, qiymat in kwargs.items():
            setattr(self, kalit, qiymat)

p = Parametrlar(ism="Laylo", yosh=22, shahar="Toshkent")
print(p.ism, p.yosh)
```

- [A] Xato beradi  
- [B] `Laylo 22`  
- [C] `ism yosh`  
- [D] `None None`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `**kwargs` orqali `{'ism': 'Laylo', 'yosh': 22, 'shahar': 'Toshkent'}` lug'ati olinadi. `setattr` har bir kalit-qiymatni atributga aylantiradi. `p.ism` → `"Laylo"`, `p.yosh` → `22`.

---

## Savol 19

Quyidagi kodda xato qayerda?

```python
class Doira:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius manfiy bo'lishi mumkin emas!")
        self.radius = radius

d = Doira(-5)
```

- [A] Xato yo'q, kod to'g'ri  
- [B] `raise` `__init__` da ishlatilishi mumkin emas  
- [C] `ValueError` xatosi chiqadi — radius manfiy bo'lishi mumkin emas  
- [D] `if` operatori `__init__` da ishlatilmaydi  

> **To'g'ri javob:** C  
> **Tushuntirish:** Kod sintaktik jihatdan to'g'ri. `Doira(-5)` chaqirilganda `radius < 0` sharti bajariladi va `ValueError: Radius manfiy bo'lishi mumkin emas!` xatosi chiqariladi. Bu `__init__` da validatsiya qilishning to'g'ri usuli.

---

## Savol 20

`__init__` va `__new__` metodlari o'rtasidagi farq nima?

- [A] Ikkalasi bir xil vazifani bajaradi  
- [B] `__new__` xotirada obyekt uchun joy ajratadi, `__init__` esa shu obyektni atributlar bilan to'ldiradi  
- [C] `__new__` faqat meros olishda ishlatiladi  
- [D] `__init__` xotirani boshqaradi, `__new__` atributlarni belgilaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `__new__` obyektni yaratadi (xotira ajratadi) va uni qaytaradi. `__init__` esa yaratilgan obyektni qabul qilib, atributlarini o'rnatadi. Odatda faqat `__init__` bilan ishlash yetarli.

---

## Savol 21

Quyidagi kodning natijasi nima?

```python
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

b = B()
```

- [A] Faqat `B init`  
- [B] Faqat `A init`  
- [C] `A init` keyin `B init`  
- [D] `B init` keyin `A init`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `B()` yaratilganda `B.__init__` chaqiriladi. U `super().__init__()` bilan avval `A.__init__` ni chaqiradi (`A init` chiqadi), so'ng `print("B init")` ishlaydi. Natija: `A init`, `B init`.

---

## Savol 22

Class ichida bir nechta `__init__` metodi e'lon qilish mumkinmi?

- [A] Ha, har xil parametrlar bilan bir nechta yozsa bo'ladi  
- [B] Yo'q, Python'da bir classda faqat bitta `__init__` bo'lishi mumkin — keyingisi oldingi ni qayta yozadi  
- [C] Ha, `@overload` dekoratori bilan  
- [D] Faqat meros orqali mumkin  

> **To'g'ri javob:** B  
> **Tushuntirish:** Python method overloading ni qo'llab-quvvatlamaydi. Agar bir classda ikkita `__init__` yozilsa, ikkinchisi birinchisini ustiga yozadi (override). Moslashuvchanlik uchun `*args`, `**kwargs` yoki standart qiymatlar ishlatiladi.

---

## Savol 23

Quyidagi kodning natijasi nima?

```python
class Telefon:
    def __init__(self, model, xotira=128):
        self.model = model
        self.xotira = xotira

t1 = Telefon("Samsung")
t2 = Telefon("iPhone", 256)
print(t1.xotira, t2.xotira)
```

- [A] `128 128`  
- [B] `256 128`  
- [C] `128 256`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `t1 = Telefon("Samsung")` — `xotira` ko'rsatilmagan, standart `128` ishlatiladi. `t2 = Telefon("iPhone", 256)` — `xotira=256` berilgan. Natija: `128 256`.

---

## Savol 24

`__init__` da `self` o'rniga boshqa nom ishlatish mumkinmi?

- [A] Yo'q, `self` majburiy kalit so'z  
- [B] Ha, texnik jihatdan boshqa nom ham ishlaydi, lekin `self` ishlatish kuchli konventsiya  
- [C] Faqat `this` ishlatish mumkin  
- [D] Faqat `object` ishlatish mumkin  

> **To'g'ri javob:** B  
> **Tushuntirish:** `self` Python'da kalit so'z emas, shunchaki kuchli an'ana (konventsiya). Texnik jihatdan `def __init__(bu, ism)` ham ishlaydi, lekin jamoaviy ishda `self` ishlatish majburiy hisoblanadi.

---

## Savol 25

Quyidagi kodda nima muammo bor?

```python
class Odam:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

o = Odam("Sarvar")
```

- [A] Muammo yo'q  
- [B] `TypeError` — `yosh` argumenti berilmagan  
- [C] `AttributeError` — `ism` noto'g'ri  
- [D] `ValueError` — ism qisqa  

> **To'g'ri javob:** B  
> **Tushuntirish:** `__init__` ikkita majburiy argument (`ism` va `yosh`) talab qiladi. `Odam("Sarvar")` da faqat bittasi berilgani uchun `TypeError: __init__() missing 1 required positional argument: 'yosh'` xatosi yuzaga keladi.

---

## Savol 26

Quyidagi kodning natijasi nima?

```python
class Raqam:
    def __init__(self, qiymat):
        self.qiymat = qiymat
        self.kvadrat = qiymat ** 2
        self.kub = qiymat ** 3

r = Raqam(3)
print(r.kvadrat, r.kub)
```

- [A] `3 3`  
- [B] `6 9`  
- [C] `9 27`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Raqam(3)` chaqirilganda: `self.qiymat = 3`, `self.kvadrat = 3**2 = 9`, `self.kub = 3**3 = 27`. Natija: `9 27`.

---

## Savol 27

`__init__` ichida boshqa classdan obyekt yaratish mumkinmi?

- [A] Yo'q, bu rekursiyaga olib keladi  
- [B] Ha, `__init__` ichida istalgan classdan obyekt yaratish mumkin  
- [C] Faqat meros olingan classdan mumkin  
- [D] Faqat `super()` orqali mumkin  

> **To'g'ri javob:** B  
> **Tushuntirish:** `__init__` ichida boshqa classdan obyekt yaratish to'liq ruxsat etiladi. Bu **kompozitsiya** (composition) deb ataladi — bir class boshqa classning obyektini o'z ichida saqlaydi.

---

## Savol 28

Quyidagi kodning natijasi nima?

```python
class Manzil:
    def __init__(self, shahar):
        self.shahar = shahar

class Shaxs:
    def __init__(self, ism, shahar):
        self.ism = ism
        self.manzil = Manzil(shahar)

s = Shaxs("Dilnoza", "Samarqand")
print(s.ism, s.manzil.shahar)
```

- [A] `Dilnoza Manzil`  
- [B] `Dilnoza Samarqand`  
- [C] Xato beradi  
- [D] `Shaxs Samarqand`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `Shaxs.__init__` ichida `Manzil("Samarqand")` obyekti yaratiladi. `s.manzil` — `Manzil` obyekti, `s.manzil.shahar` → `"Samarqand"`. Natija: `Dilnoza Samarqand`.

---

## Savol 29

Quyidagi kodda obyektlar soni hisoblanadimi?

```python
class Sensor:
    soni = 0

    def __init__(self):
        Sensor.soni += 1

s1 = Sensor()
s2 = Sensor()
s3 = Sensor()
print(Sensor.soni)
```

- [A] `0`  
- [B] `1`  
- [C] `3`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** Har bir `Sensor()` obyekti yaratilganda `__init__` chaqiriladi va `Sensor.soni += 1` bajariladi. 3 ta obyekt yaratilgani uchun `Sensor.soni` → `3` bo'ladi.

---

## Savol 30

Quyidagi kodda `__init__` to'g'ri ishlaydimi?

```python
class Matris:
    def __init__(self, qatorlar, ustunlar, standart=0):
        self.qatorlar = qatorlar
        self.ustunlar = ustunlar
        self.data = [[standart] * ustunlar for _ in range(qatorlar)]

m = Matris(3, 4)
print(len(m.data), len(m.data[0]))
```

- [A] Xato beradi  
- [B] `3 3`  
- [C] `4 3`  
- [D] `3 4`  

> **To'g'ri javob:** D  
> **Tushuntirish:** `Matris(3, 4)` — 3 qator, 4 ustunli matris yaratiladi. `self.data` — 3 ta list bo'lib, har biri 4 ta `0` dan iborat. `len(m.data)` → `3`, `len(m.data[0])` → `4`. Natija: `3 4`.

---