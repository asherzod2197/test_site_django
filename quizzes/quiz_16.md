## Savol 1

`super()` funksiyasi nima?

- [A] Yangi class yaratuvchi funksiya  
- [B] Farzand class ichidan ota classning metod va atributlariga murojaat qilish imkonini beruvchi funksiya  
- [C] Classni o'chiruvchi funksiya  
- [D] Faqat `__init__` da ishlaydigan kalit so'z  

> **To'g'ri javob:** B  
> **Tushuntirish:** `super()` — farzand class ichidan ota classga (yoki MRO bo'yicha keyingi classga) murojaat qilish imkonini beradi. Ko'pincha `super().__init__()`, `super().metod()` ko'rinishida ishlatiladi.

---

## Savol 2

`super().__init__()` qaysi vazifani bajaradi?

- [A] Farzand classni o'chiradi  
- [B] Farzand classning `__init__` ini qayta chaqiradi  
- [C] Ota classning `__init__` ini chaqirib, ota class atributlarini o'rnatadi  
- [D] Yangi obyekt yaratadi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `super().__init__()` — farzand classning `__init__` ichida ota classning konstruktorini chaqiradi. Bu ota classda e'lon qilingan atributlarni ham farzand obyektida o'rnatish uchun zarur.

---

## Savol 3

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

- [A] `AttributeError`  
- [B] `None Labrador`  
- [C] `Rex Labrador`  
- [D] `Rex None`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `super().__init__(ism)` → `Hayvon.__init__` chaqirildi → `self.ism = "Rex"`. Keyin `self.zot = "Labrador"`. Natija: `Rex Labrador`.

---

## Savol 4

`super().__init__()` chaqirilmasa nima bo'ladi?

- [A] Hech narsa o'zgarmaydi, Python avtomatik chaqiradi  
- [B] Ota classning `__init__` da o'rnatilgan atributlar farzand obyektida bo'lmaydi  
- [C] Xato yuzaga keladi va dastur to'xtaydi  
- [D] Faqat ota classning metodlari ishlamay qoladi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `super().__init__()` chaqirilmasa, ota classning konstruktori ishlamaydi va ota classda `self.atribut` shaklida belgilangan qiymatlar farzand obyektida mavjud bo'lmaydi. Natijada `AttributeError` yuzaga kelishi mumkin.

---

## Savol 5

Quyidagi kodning natijasi nima?

```python
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

class C(B):
    def __init__(self):
        super().__init__()
        print("C init")

obj = C()
```

- [A] `C init`  
- [B] `A init`, `C init`  
- [C] `C init`, `B init`, `A init`  
- [D] `A init`, `B init`, `C init`  

> **To'g'ri javob:** D  
> **Tushuntirish:** `C()` → `C.__init__` → `super().__init__()` → `B.__init__` → `super().__init__()` → `A.__init__` → `"A init"`. Keyin `B` ga qaytadi → `"B init"`. Keyin `C` ga qaytadi → `"C init"`. Natija: `A init`, `B init`, `C init`.

---

## Savol 6

`super()` faqat `__init__` da ishlatilishi mumkinmi?

- [A] Ha, faqat `__init__` da ishlaydi  
- [B] Yo'q, `super()` har qanday metod ichida ota classning xuddi shu nomli yoki boshqa metodini chaqirish uchun ishlatilishi mumkin  
- [C] Faqat `@classmethod` da ishlaydi  
- [D] Faqat `@staticmethod` da ishlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `super()` istalgan metod ichida ishlatilishi mumkin. `super().metod_nomi()` ko'rinishida ota classning ixtiyoriy metodini chaqirish mumkin. Bu method overriding bilan birgalikda juda keng ishlatiladi.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
class Xodim:
    def malumot(self):
        return "Xodim"

class Menejer(Xodim):
    def malumot(self):
        ota = super().malumot()
        return f"{ota} > Menejer"

class Direktor(Menejer):
    def malumot(self):
        ota = super().malumot()
        return f"{ota} > Direktor"

d = Direktor()
print(d.malumot())
```

- [A] `Direktor`  
- [B] `Xodim > Direktor`  
- [C] `Xodim > Menejer > Direktor`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Direktor.malumot()` → `super().malumot()` → `Menejer.malumot()` → `super().malumot()` → `Xodim.malumot()` → `"Xodim"`. Keyin `"Xodim > Menejer"` qaytadi. Keyin `"Xodim > Menejer > Direktor"`.

---

## Savol 8

Ko'p meros olishda `super()` qaysi classni chaqiradi?

- [A] Har doim birinchi ota classni  
- [B] MRO (Method Resolution Order) bo'yicha keyingi classni  
- [C] Har doim `object` classini  
- [D] So'nggi ota classni  

> **To'g'ri javob:** B  
> **Tushuntirish:** Ko'p meros olishda `super()` MRO bo'yicha keyingi classni chaqiradi. MRO C3 linearizatsiya algoritmi bilan aniqlanadi. `ClassName.__mro__` orqali tartibni ko'rish mumkin.

---

## Savol 9

Quyidagi kodning natijasi nima?

```python
class A:
    def salom(self):
        return "A salom"

class B(A):
    def salom(self):
        return f"B + {super().salom()}"

class C(A):
    def salom(self):
        return f"C + {super().salom()}"

class D(B, C):
    def salom(self):
        return f"D + {super().salom()}"

print(D().salom())
print(D.__mro__)
```

- [A] `D + B + A salom`  
- [B] `D + B + C + A salom` va MRO: `D → B → C → A → object`  
- [C] `D + C + A salom`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** MRO: `D → B → C → A`. `D.salom()` → `"D + " + B.salom()` → `"D + B + " + C.salom()` → `"D + B + C + " + A.salom()` → `"D + B + C + A salom"`.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
class Shakllar:
    def __init__(self, rang):
        self.rang = rang

class Hajmli(Shakllar):
    def __init__(self, rang, qalinlik):
        super().__init__(rang)
        self.qalinlik = qalinlik

class Kub(Hajmli):
    def __init__(self, rang, qalinlik, tomon):
        super().__init__(rang, qalinlik)
        self.tomon = tomon

    def hajm(self):
        return self.tomon ** 3

k = Kub("ko'k", 2, 5)
print(k.rang, k.qalinlik, k.hajm())
```

- [A] `AttributeError`  
- [B] `ko'k 2 125`  
- [C] `ko'k None 125`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `Kub.__init__` → `super().__init__(rang, qalinlik)` → `Hajmli.__init__` → `super().__init__(rang)` → `Shakllar.__init__` → `self.rang = "ko'k"`. Keyin `self.qalinlik = 2`, `self.tomon = 5`. `k.hajm()` → `125`.

---

## Savol 11

Quyidagi kodda `super()` to'g'ri ishlatilganmi?

```python
class Transport:
    def __init__(self, nomi):
        self.nomi = nomi
        self.tezlik = 0

    def tezlash(self, qiymat):
        self.tezlik += qiymat
        return f"{self.nomi} {self.tezlik} km/h"

class Poyezd(Transport):
    def tezlash(self, qiymat):
        if qiymat <= 50:
            return super().tezlash(qiymat)
        return f"Poyezd uchun max oshirish: 50 km/h"

p = Poyezd("Afrosiyob")
print(p.tezlash(30))
print(p.tezlash(80))
```

- [A] Xato bor, `super()` `tezlash` da ishlatib bo'lmaydi  
- [B] `Afrosiyob 30 km/h`, `Poyezd uchun max oshirish: 50 km/h`  
- [C] `30`, `80`  
- [D] `AttributeError`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `super().tezlash(qiymat)` — to'g'ri ishlatish. `tezlash(30)` → `30 <= 50` → `super().tezlash(30)` → `"Afrosiyob 30 km/h"`. `tezlash(80)` → `80 > 50` → limit xabari.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
class Narx:
    def __init__(self, asosiy):
        self.asosiy = asosiy

    def hisobla(self):
        return self.asosiy

class SoliqliNarx(Narx):
    def __init__(self, asosiy, soliq=12):
        super().__init__(asosiy)
        self.soliq = soliq

    def hisobla(self):
        return super().hisobla() * (1 + self.soliq / 100)

class ChegirmaNarx(SoliqliNarx):
    def __init__(self, asosiy, soliq, chegirma):
        super().__init__(asosiy, soliq)
        self.chegirma = chegirma

    def hisobla(self):
        return super().hisobla() * (1 - self.chegirma / 100)

n = ChegirmaNarx(100000, 15, 10)
print(n.hisobla())
```

- [A] `100000`  
- [B] `115000.0`  
- [C] `103500.0`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `SoliqliNarx.hisobla()` → `100000 * 1.15 = 115000.0`. `ChegirmaNarx.hisobla()` → `115000 * 0.90 = 103500.0`.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
class Logger:
    def xabar(self, matn):
        return f"[LOG]: {matn}"

class TimestampLogger(Logger):
    def xabar(self, matn):
        asosiy = super().xabar(matn)
        return f"2025-01-01 | {asosiy}"

class PrefixLogger(TimestampLogger):
    def __init__(self, prefix):
        self.prefix = prefix

    def xabar(self, matn):
        asosiy = super().xabar(matn)
        return f"({self.prefix}) {asosiy}"

log = PrefixLogger("MUHIM")
print(log.xabar("Xato yuz berdi"))
```

- [A] `[LOG]: Xato yuz berdi`  
- [B] `2025-01-01 | [LOG]: Xato yuz berdi`  
- [C] `(MUHIM) 2025-01-01 | [LOG]: Xato yuz berdi`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `PrefixLogger.xabar()` → `super().xabar()` → `TimestampLogger.xabar()` → `super().xabar()` → `Logger.xabar()` → `"[LOG]: Xato yuz berdi"`. Keyin `"2025-01-01 | [LOG]: ..."`. Keyin `"(MUHIM) 2025-01-01 | [LOG]: ..."`.

---

## Savol 14

`super()` bilan `ClassName.metod(self)` o'rtasidagi farq nima?

- [A] Ikkalasi bir xil  
- [B] `super()` MRO ga amal qiladi va ko'p meros olishda xavfsiz; `ClassName.metod(self)` esa aniq classni chaqiradi va MRO ni chetlab o'tadi  
- [C] `ClassName.metod(self)` faqat `__init__` da ishlaydi  
- [D] `super()` faqat bitta meros olishda ishlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `super()` MRO bo'yicha ishlaydi va ko'p meros olishda ham to'g'ri zanjirni saqlaydi. `OtaClass.metod(self)` esa to'g'ridan-to'g'ri aniq classni chaqiradi — MRO ni hisobga olmaydi va ko'p meros olishda muammolarga olib kelishi mumkin.

---

## Savol 15

Quyidagi kodning natijasi nima?

```python
class Hisoblagich:
    def __init__(self, boshlangich=0):
        self.qiymat = boshlangich

    def oshir(self):
        self.qiymat += 1
        return self.qiymat

class IkkilantiruvchiHisoblagich(Hisoblagich):
    def oshir(self):
        super().oshir()
        return super().oshir()

h = IkkilantiruvchiHisoblagich(0)
print(h.oshir())
print(h.oshir())
```

- [A] `1`, `2`  
- [B] `2`, `4`  
- [C] `1`, `3`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `h.oshir()` ikkita `super().oshir()` chaqiradi: `0+1=1`, `1+1=2` → `2` qaytadi. Ikkinchi `h.oshir()`: `2+1=3`, `3+1=4` → `4` qaytadi. Natija: `2`, `4`.

---

## Savol 16

Quyidagi kodning natijasi nima?

```python
class Inson:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def __str__(self):
        return f"{self.ism} ({self.yosh})"

class Talaba(Inson):
    def __init__(self, ism, yosh, guruh):
        super().__init__(ism, yosh)
        self.guruh = guruh

    def __str__(self):
        asosiy = super().__str__()
        return f"{asosiy} - Guruh: {self.guruh}"

class AloTalaba(Talaba):
    def __init__(self, ism, yosh, guruh, stipendiya):
        super().__init__(ism, yosh, guruh)
        self.stipendiya = stipendiya

    def __str__(self):
        asosiy = super().__str__()
        return f"{asosiy} | Stipendiya: {self.stipendiya:,}"

t = AloTalaba("Nilufar", 19, "CS-101", 500000)
print(t)
```

- [A] `Nilufar (19)`  
- [B] `Nilufar (19) - Guruh: CS-101`  
- [C] `Nilufar (19) - Guruh: CS-101 | Stipendiya: 500,000`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `AloTalaba.__str__` → `super().__str__()` → `Talaba.__str__` → `super().__str__()` → `Inson.__str__` → `"Nilufar (19)"`. Keyin `"Nilufar (19) - Guruh: CS-101"`. Keyin `"Nilufar (19) - Guruh: CS-101 | Stipendiya: 500,000"`.

---

## Savol 17

Quyidagi kodning natijasi nima?

```python
class Shakl:
    def __init__(self, rang="oq"):
        self.rang = rang
        print(f"Shakl: {rang}")

class Toʻrtburchak(Shakl):
    def __init__(self, rang, en, boy):
        super().__init__(rang)
        self.en = en
        self.boy = boy
        print(f"To'rtburchak: {en}x{boy}")

class Kvadrat(Toʻrtburchak):
    def __init__(self, rang, tomon):
        super().__init__(rang, tomon, tomon)
        print(f"Kvadrat: {tomon}")

k = Kvadrat("yashil", 4)
```

- [A] Faqat `Kvadrat: 4`  
- [B] `Shakl: yashil`, `To'rtburchak: 4x4`, `Kvadrat: 4`  
- [C] `Kvadrat: 4`, `To'rtburchak: 4x4`, `Shakl: yashil`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `Kvadrat.__init__` → `super().__init__("yashil", 4, 4)` → `To'rtburchak.__init__` → `super().__init__("yashil")` → `Shakl.__init__` → `"Shakl: yashil"`. Keyin `"To'rtburchak: 4x4"`. Keyin `"Kvadrat: 4"`.

---

## Savol 18

Quyidagi kodning natijasi nima?

```python
class Hisob:
    def __init__(self, egasi):
        self.egasi = egasi
        self._tranzaksiyalar = []

    def kirim(self, summa):
        self._tranzaksiyalar.append(summa)
        return summa

    def balans(self):
        return sum(self._tranzaksiyalar)

class TejamHisob(Hisob):
    def __init__(self, egasi, foiz=5):
        super().__init__(egasi)
        self.foiz = foiz

    def kirim(self, summa):
        haqiqiy = super().kirim(summa)
        bonus = haqiqiy * self.foiz / 100
        super().kirim(bonus)
        return f"{haqiqiy} + {bonus} bonus"

t = TejamHisob("Jasur", 10)
print(t.kirim(100000))
print(t.balans())
```

- [A] `100000 + 10000.0 bonus`, `100000`  
- [B] `100000 + 10000.0 bonus`, `110000.0`  
- [C] `100000`, `110000`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `kirim(100000)` → `super().kirim(100000)` → `100000` tranzaksiyaga qo'shildi. `bonus = 10000`. `super().kirim(10000)` → bonus ham qo'shildi. `balans()` → `100000 + 10000 = 110000.0`.

---

## Savol 19

Quyidagi kodning natijasi nima?

```python
class Qurilma:
    def __init__(self, model, narx):
        self.model = model
        self.narx = narx

    def tavsif(self):
        return f"Model: {self.model}, Narx: {self.narx:,}"

class AqllıQurilma(Qurilma):
    def __init__(self, model, narx, os):
        super().__init__(model, narx)
        self.os = os

    def tavsif(self):
        return f"{super().tavsif()}, OS: {self.os}"

class Smartfon(AqllıQurilma):
    def __init__(self, model, narx, os, kamera):
        super().__init__(model, narx, os)
        self.kamera = kamera

    def tavsif(self):
        return f"{super().tavsif()}, Kamera: {self.kamera}MP"

s = Smartfon("Pixel 8", 9000000, "Android 14", 50)
print(s.tavsif())
print(isinstance(s, Qurilma))
```

- [A] `Model: Pixel 8, Narx: 9,000,000`, `False`  
- [B] `Model: Pixel 8, Narx: 9,000,000, OS: Android 14, Kamera: 50MP`, `True`  
- [C] `Kamera: 50MP`, `True`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `super()` zanjiri: `Qurilma` → `AqllıQurilma` → `Smartfon`. `tavsif()` har bosqichda kengayadi. `isinstance(s, Qurilma)` → meros zanjiri → `True`.

---

## Savol 20

Quyidagi to'liq namunaning natijasi nima?

```python
class Jonzot:
    def __init__(self, ism):
        self.ism = ism

    def ovqatlantir(self):
        return f"{self.ism} ovqatlandi"

class UyHayvoni(Jonzot):
    def __init__(self, ism, egasi):
        super().__init__(ism)
        self.egasi = egasi

    def ovqatlantir(self):
        asosiy = super().ovqatlantir()
        return f"{asosiy} ({self.egasi} tomonidan)"

class MurakkabUyHayvoni(UyHayvoni):
    def __init__(self, ism, egasi, ovqat):
        super().__init__(ism, egasi)
        self.ovqat = ovqat

    def ovqatlantir(self):
        asosiy = super().ovqatlantir()
        return f"{asosiy} [{self.ovqat}]"

    def malumot(self):
        return (f"Ism: {self.ism}, "
                f"Egasi: {self.egasi}, "
                f"Ovqat: {self.ovqat}")

m = MurakkabUyHayvoni("Fluffy", "Kamola", "Sut")
print(m.ovqatlantir())
print(m.malumot())
print(issubclass(MurakkabUyHayvoni, Jonzot))
```

- [A] `Fluffy ovqatlandi`, `Ism: Fluffy, Egasi: Kamola, Ovqat: Sut`, `False`  
- [B] `Fluffy ovqatlandi (Kamola tomonidan) [Sut]`, `Ism: Fluffy, Egasi: Kamola, Ovqat: Sut`, `True`  
- [C] `Fluffy ovqatlandi [Sut]`, `Ism: Fluffy`, `True`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `ovqatlantir()` zanjiri: `Jonzot` → `"Fluffy ovqatlandi"`. `UyHayvoni` → `"Fluffy ovqatlandi (Kamola tomonidan)"`. `MurakkabUyHayvoni` → `"Fluffy ovqatlandi (Kamola tomonidan) [Sut]"`. `malumot()` barcha atributlarni ko'rsatadi. `issubclass(MurakkabUyHayvoni, Jonzot)` → meros zanjiri → `True`.

---