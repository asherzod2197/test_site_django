## Savol 1

Inheritance (meros olish) nima?

- [A] Bir xil nomli metodlarni qayta ishlatish  
- [B] Mavjud classning atribut va metodlarini yangi class tomonidan meros qilib olish mexanizmi  
- [C] Ma'lumotlarni yashirish usuli  
- [D] Faqat atributlarni boshqa classga ko'chirish  

> **To'g'ri javob:** B  
> **Tushuntirish:** Inheritance — OOPning asosiy to'rtta tamoyilidan biri. U mavjud class (ota class) ning xususiyatlari va metodlarini yangi class (farzand class) tomonidan meros qilib olish imkonini beradi. Bu kodni qayta ishlatish va tizimni kengaytirish imkonini beradi.

---

## Savol 2

Meros olishda ota class va farzand class qanday ataladi?

- [A] Asosiy class va yordamchi class  
- [B] Ota class (parent/base/super class) va farzand class (child/derived/sub class)  
- [C] Birinchi class va ikkinchi class  
- [D] Katta class va kichik class  

> **To'g'ri javob:** B  
> **Tushuntirish:** Meros olishda meros berayotgan class **ota class** (parent, base, super class), meros olayotgan class esa **farzand class** (child, derived, sub class) deb ataladi. Python'da `class Farzand(Ota):` sintaksisi ishlatiladi.

---

## Savol 3

Python'da meros olish qanday yoziladi?

- [A] `class Farzand extends Ota:`  
- [B] `class Farzand inherits Ota:`  
- [C] `class Farzand(Ota):`  
- [D] `class Farzand -> Ota:`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Python'da meros olish sintaksisi `class FarzandClass(OtaClass):` ko'rinishida bo'ladi. Qavs ichiga ota class nomi yoziladi. Bu Java dagi `extends` kalit so'ziga o'xshaydi.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
class Hayvon:
    def nafas_ol(self):
        return "Nafas olmoqda"

class It(Hayvon):
    def vov(self):
        return "Vov-vov!"

i = It()
print(i.nafas_ol())
print(i.vov())
```

- [A] Xato beradi, `It` classida `nafas_ol` yo'q  
- [B] `Nafas olmoqda` va `Vov-vov!`  
- [C] `None` va `Vov-vov!`  
- [D] `Nafas olmoqda` va `None`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `It` classi `Hayvon` dan meros olgan, shuning uchun `nafas_ol()` metodini ham ishlatishi mumkin. `i.nafas_ol()` → `"Nafas olmoqda"`, `i.vov()` → `"Vov-vov!"`.

---

## Savol 5

`super()` funksiyasi nima uchun ishlatiladi?

- [A] Farzand classni o'chirish uchun  
- [B] Farzand class ichidan ota classning metod va `__init__` ini chaqirish uchun  
- [C] Yangi class yaratish uchun  
- [D] Faqat statik metodlarda ishlatiladi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `super()` — farzand class ichidan ota classga murojaat qilish imkonini beradi. Ko'pincha `super().__init__()` ko'rinishida farzandning `__init__` ichida ota classning konstruktorini chaqirish uchun ishlatiladi.

---

## Savol 6

Quyidagi kodning natijasi nima?

```python
class Transport:
    def __init__(self, nomi, tezlik):
        self.nomi = nomi
        self.tezlik = tezlik

class Avtomobil(Transport):
    def __init__(self, nomi, tezlik, eshik):
        super().__init__(nomi, tezlik)
        self.eshik = eshik

a = Avtomobil("BMW", 200, 4)
print(a.nomi, a.tezlik, a.eshik)
```

- [A] Xato beradi  
- [B] `BMW 200 4`  
- [C] `None None 4`  
- [D] `BMW None 4`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `super().__init__(nomi, tezlik)` ota classning `__init__` ini chaqiradi → `self.nomi = "BMW"`, `self.tezlik = 200`. Keyin `self.eshik = 4`. Natija: `BMW 200 4`.

---

## Savol 7

Farzand class ota classning metodini bekor qilishi (override) nima deyiladi?

- [A] Overloading  
- [B] Encapsulation  
- [C] Method overriding  
- [D] Abstraction  

> **To'g'ri javob:** C  
> **Tushuntirish:** **Method overriding** — farzand classda ota classning metodini qayta e'lon qilib, uning xatti-harakatini o'zgartirish. Farzand classda ota class bilan bir xil nomli metod yozilsa, u ota classning metodini yopadi.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
class Shakl:
    def yuza(self):
        return "Yuza hisoblanmadi"

class Kvadrat(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2

k = Kvadrat(5)
print(k.yuza())
```

- [A] `Yuza hisoblanmadi`  
- [B] `5`  
- [C] `25`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Kvadrat` classi `yuza()` metodini override qilgan. `k.yuza()` farzand classning metodini chaqiradi: `5 ** 2 = 25`.

---

## Savol 9

`isinstance()` funksiyasi meros olish bilan qanday bog'liq?

- [A] Faqat to'g'ridan-to'g'ri classni tekshiradi  
- [B] Obyekt ko'rsatilgan class yoki uning farzand classiga mansub ekanligini tekshiradi  
- [C] Faqat ota classni tekshiradi  
- [D] Classni o'chirish uchun ishlatiladi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `isinstance(obyekt, Class)` meros zanjirini hisobga oladi. Agar `It` classi `Hayvon` dan meros olsa, `isinstance(it_obyekti, Hayvon)` → `True` qaytaradi. Bu polimorfizmda juda foydali.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

obj = C()
print(isinstance(obj, C))
print(isinstance(obj, B))
print(isinstance(obj, A))
```

- [A] `True`, `False`, `False`  
- [B] `True`, `True`, `False`  
- [C] `True`, `True`, `True`  
- [D] `False`, `False`, `True`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `C` classi `B` dan, `B` classi `A` dan meros olgan. `obj` — `C` instansiyasi. `isinstance(obj, C)` → `True`, `isinstance(obj, B)` → `True` (meros zanjiri), `isinstance(obj, A)` → `True` (meros zanjiri).

---

## Savol 11

`issubclass()` funksiyasi nima uchun ishlatiladi?

- [A] Obyektning classini tekshirish uchun  
- [B] Bir classning boshqa classdan meros olgan yoki olmagnini tekshirish uchun  
- [C] Classni o'chirish uchun  
- [D] Ota class metodlarini chaqirish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `issubclass(FarzandClass, OtaClass)` — birinchi class ikkinchisidan (to'g'ridan-to'g'ri yoki bilvosita) meros olgan bo'lsa `True`, aks holda `False` qaytaradi. Obyektlar emas, classlar bilan ishlaydi.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
class Ota:
    def salom(self):
        return "Ota: Salom!"

class Farzand(Ota):
    def salom(self):
        ota_salom = super().salom()
        return f"{ota_salom} | Farzand: Salom!"

f = Farzand()
print(f.salom())
```

- [A] `Ota: Salom!`  
- [B] `Farzand: Salom!`  
- [C] `Ota: Salom! | Farzand: Salom!`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Farzand.salom()` ichida `super().salom()` ota classning metodini chaqiradi → `"Ota: Salom!"`. Keyin farzand o'z qismini qo'shadi. Natija: `"Ota: Salom! | Farzand: Salom!"`.

---

## Savol 13

Ko'p bosqichli meros (multilevel inheritance) nima?

- [A] Bir class bir nechta classdan meros olishi  
- [B] A → B → C ko'rinishida, har bir class oldingi classdan meros olishi  
- [C] Bir class ikki marta meros olishi  
- [D] Faqat ikki classdan iborat meros  

> **To'g'ri javob:** B  
> **Tushuntirish:** Ko'p bosqichli meros — A classdan B meros oladi, B classdan esa C meros oladi. C class A va B ning barcha xususiyatlarini meros oladi. Bu zanjirsimon meros deb ham ataladi.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
class Ajdod:
    def kim(self):
        return "Men Ajdod"

class Ota(Ajdod):
    def kim(self):
        return "Men Ota"

class Nabira(Ota):
    pass

n = Nabira()
print(n.kim())
```

- [A] `Men Ajdod`  
- [B] `Men Ota`  
- [C] `None`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `Nabira` o'z `kim()` metodini e'lon qilmagan. Python MRO bo'yicha qidiradi: `Nabira` → `Ota` → `Ajdod`. `Ota` da `kim()` topildi → `"Men Ota"`.

---

## Savol 15

Ko'p meros olish (multiple inheritance) nima?

- [A] Bir classdan bir nechta obyekt yaratish  
- [B] Bitta farzand classning bir nechta ota classdan bir vaqtda meros olishi  
- [C] Ko'p bosqichli meros olish  
- [D] Bir class metodlarini bir nechta marta chaqirish  

> **To'g'ri javob:** B  
> **Tushuntirish:** Ko'p meros olish — bir farzand class bir vaqtda bir nechta ota classdan meros olishi. Python'da `class Farzand(Ota1, Ota2, Ota3):` ko'rinishida yoziladi. Bu Java'da mavjud emas.

---

## Savol 16

Quyidagi kodning natijasi nima?

```python
class Suzuvchi:
    def harakat(self):
        return "Suzmoqda"

class Uchuvchi:
    def harakat(self):
        return "Uchmoqda"

class Urdak(Suzuvchi, Uchuvchi):
    pass

u = Urdak()
print(u.harakat())
```

- [A] `Suzmoqda va Uchmoqda`  
- [B] `Uchmoqda`  
- [C] `Suzmoqda`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** Ko'p meros olishda Python MRO (Method Resolution Order) qoidasiga amal qiladi. `class Urdak(Suzuvchi, Uchuvchi)` da `Suzuvchi` birinchi yozilgan, shuning uchun `harakat()` → `"Suzmoqda"` chiqaradi.

---

## Savol 17

MRO (Method Resolution Order) nima?

- [A] Metodlarni saralash algoritmi  
- [B] Python'ning ko'p meros olishda qaysi classning metodini avval ishlatishini aniqlash tartibi  
- [C] Metodlarni o'chirish tartibi  
- [D] Faqat `super()` bilan ishlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** MRO — Python'da ko'p meros olishda metod qidiruv tartibi. Python C3 linearizatsiya algoritmini ishlatadi. `ClassName.__mro__` yoki `ClassName.mro()` orqali ko'rish mumkin.

---

## Savol 18

Quyidagi kodning natijasi nima?

```python
class Hayvon:
    def __init__(self, ism):
        self.ism = ism

    def ovoz(self):
        return "..."

class Mushuk(Hayvon):
    def ovoz(self):
        return "Miyov!"

class It(Hayvon):
    def ovoz(self):
        return "Hav-hav!"

hayvonlar = [Mushuk("Mitti"), It("Rex"), Mushuk("Oq")]
for h in hayvonlar:
    print(f"{h.ism}: {h.ovoz()}")
```

- [A] Xato beradi  
- [B] `Mitti: ...`, `Rex: ...`, `Oq: ...`  
- [C] `Mitti: Miyov!`, `Rex: Hav-hav!`, `Oq: Miyov!`  
- [D] `Mitti: Miyov!`, `Rex: Miyov!`, `Oq: Miyov!`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Bu **polimorfizm** namunasi. Har bir obyekt o'z classiga mos `ovoz()` metodini chaqiradi. `Mushuk` → `"Miyov!"`, `It` → `"Hav-hav!"`.

---

## Savol 19

Quyidagi kodning natijasi nima?

```python
class Shakllar:
    def __init__(self, rang):
        self.rang = rang

    def yuza(self):
        return 0

class Aylana(Shakllar):
    def __init__(self, rang, r):
        super().__init__(rang)
        self.r = r

    def yuza(self):
        return round(3.14 * self.r ** 2, 2)

class Kvadrat(Shakllar):
    def __init__(self, rang, tomon):
        super().__init__(rang)
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2

shakllar = [Aylana("qizil", 5), Kvadrat("yashil", 4)]
for s in shakllar:
    print(f"{s.rang}: {s.yuza()}")
```

- [A] `qizil: 0`, `yashil: 0`  
- [B] `qizil: 78.5`, `yashil: 16`  
- [C] `qizil: 5`, `yashil: 4`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `Aylana(5).yuza()` → `3.14 * 25 = 78.5`. `Kvadrat(4).yuza()` → `16`. Har bir farzand class `yuza()` ni override qilgan. Polimorfizm ishlaydi.

---

## Savol 20

Quyidagi kodning natijasi nima?

```python
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(B):
    def __init__(self):
        super().__init__()
        print("C")

obj = C()
```

- [A] `C`  
- [B] `A`, `B`, `C`  
- [C] `C`, `B`, `A`  
- [D] `A`, `C`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `C()` → `C.__init__` chaqiriladi → `super().__init__()` → `B.__init__` → `super().__init__()` → `A.__init__` → `"A"`. Keyin `B` ga qaytadi → `"B"`. Keyin `C` ga qaytadi → `"C"`. Natija: `A`, `B`, `C`.

---

## Savol 21

Farzand class ota classning `__init__` ini chaqirmasa nima bo'ladi?

- [A] Hech narsa o'zgarmaydi  
- [B] Ota classning `__init__` da belgilangan atributlar farzand obyektida yo'q bo'ladi  
- [C] Python avtomatik chaqiradi  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Farzand class `super().__init__()` ni chaqirmasa, ota classning `__init__` da belgilangan atributlar o'rnatilmaydi. Farzand metodi o'sha atributlarga murojaat qilsa, `AttributeError` yuzaga keladi.

---

## Savol 22

Quyidagi kodda xato bormi?

```python
class Ota:
    def __init__(self, ism):
        self.ism = ism

class Farzand(Ota):
    def __init__(self, ism, yosh):
        self.yosh = yosh

    def tanishuv(self):
        return f"{self.ism}, {self.yosh} yoshda"

f = Farzand("Ali", 20)
print(f.tanishuv())
```

- [A] Xato yo'q, `Ali, 20 yoshda` chiqadi  
- [B] `AttributeError` — `ism` atributi o'rnatilmagan  
- [C] `TypeError` — parametrlar noto'g'ri  
- [D] `NameError` — `Ota` topilmadi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `Farzand.__init__` da `super().__init__(ism)` chaqirilmagan. Shuning uchun `self.ism` o'rnatilmagan. `tanishuv()` da `self.ism` ga murojaat qilinganda `AttributeError` yuzaga keladi.

---

## Savol 23

Quyidagi kodning natijasi nima?

```python
class Xodim:
    def __init__(self, ism, oylik):
        self.ism = ism
        self.oylik = oylik

    def malumot(self):
        return f"{self.ism}: {self.oylik} so'm"

class Menejer(Xodim):
    def __init__(self, ism, oylik, bonus):
        super().__init__(ism, oylik)
        self.bonus = bonus

    def malumot(self):
        asosiy = super().malumot()
        return f"{asosiy} + {self.bonus} bonus"

m = Menejer("Sherzod", 5000000, 1000000)
print(m.malumot())
```

- [A] `Sherzod: 5000000 so'm`  
- [B] `Sherzod: 5000000 so'm + 1000000 bonus`  
- [C] `1000000 bonus`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `Menejer.malumot()` avval `super().malumot()` → `"Sherzod: 5000000 so'm"` ni oladi, keyin bonus qo'shadi. Natija: `"Sherzod: 5000000 so'm + 1000000 bonus"`.

---

## Savol 24

Quyidagi kodning natijasi nima?

```python
class Jonivor:
    toifa = "Hayvon"

    def __init__(self, ism):
        self.ism = ism

class Baliq(Jonivor):
    toifa = "Suv jonivori"

class Qush(Jonivor):
    pass

b = Baliq("Losos")
q = Qush("Burgut")
print(b.toifa, q.toifa)
```

- [A] `Hayvon Hayvon`  
- [B] `Suv jonivori Suv jonivori`  
- [C] `Suv jonivori Hayvon`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Baliq` o'zining `toifa = "Suv jonivori"` class attributini e'lon qilgan. `Qush` esa e'lon qilmagan → ota classdan `"Hayvon"` meros oladi. Natija: `Suv jonivori Hayvon`.

---

## Savol 25

Quyidagi kodning natijasi nima?

```python
class Geometriya:
    def __init__(self, rang):
        self.rang = rang

    def __str__(self):
        return f"{self.__class__.__name__}({self.rang})"

class Uchburchak(Geometriya):
    def __init__(self, rang, asos, balandlik):
        super().__init__(rang)
        self.asos = asos
        self.balandlik = balandlik

    def yuza(self):
        return 0.5 * self.asos * self.balandlik

u = Uchburchak("sariq", 6, 4)
print(u)
print(u.yuza())
```

- [A] `Geometriya(sariq)`, `12.0`  
- [B] `Uchburchak(sariq)`, `12.0`  
- [C] `Uchburchak(sariq)`, `24`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `__str__` da `self.__class__.__name__` joriy obyektning class nomini qaytaradi — `"Uchburchak"`. `str(u)` → `"Uchburchak(sariq)"`. `u.yuza()` → `0.5 * 6 * 4 = 12.0`.

---

## Savol 26

Diamond muammosi nima?

- [A] Kvadrat shaklida meros olish  
- [B] Ko'p meros olishda bir metod bir nechta ota classda mavjud bo'lganda qaysi biri ishlatilishini aniqlash muammosi  
- [C] Uchburchak shaklida meros olish  
- [D] Meros olishda xotira muammosi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Diamond muammosi — D classi B va C classlaridan meros olsa, B va C esa A classdan meros olsa va A da metod mavjud bo'lsa — qaysi metod ishlatiladi degan savol. Python bu muammoni MRO (C3 linearizatsiya) orqali hal qiladi.

---

## Savol 27

Quyidagi kodning natijasi nima?

```python
class A:
    def kim(self):
        return "A"

class B(A):
    def kim(self):
        return "B"

class C(A):
    def kim(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.kim())
print(D.__mro__)
```

- [A] `A` chiqadi  
- [B] `C` chiqadi  
- [C] `B` chiqadi va MRO: `D → B → C → A → object`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** MRO: `D → B → C → A → object`. `d.kim()` da avval `D` da qidiriladi (yo'q), so'ng `B` da topiladi → `"B"`. `D.__mro__` → `(<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)`.

---

## Savol 28

Quyidagi kodning natijasi nima?

```python
class Shahar:
    def __init__(self, nomi, aholi):
        self.nomi = nomi
        self.aholi = aholi

    def tavsif(self):
        return f"{self.nomi}: {self.aholi:,} kishi"

class Poytaxt(Shahar):
    def __init__(self, nomi, aholi, davlat):
        super().__init__(nomi, aholi)
        self.davlat = davlat

    def tavsif(self):
        asosiy = super().tavsif()
        return f"{asosiy} ({self.davlat} poytaxti)"

p = Poytaxt("Toshkent", 3000000, "O'zbekiston")
print(p.tavsif())
```

- [A] `Toshkent: 3,000,000 kishi`  
- [B] `O'zbekiston poytaxti`  
- [C] `Toshkent: 3,000,000 kishi (O'zbekiston poytaxti)`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Poytaxt.tavsif()` avval `super().tavsif()` → `"Toshkent: 3,000,000 kishi"` ni oladi, keyin `" (O'zbekiston poytaxti)"` qo'shadi. Natija to'liq tavsif.

---

## Savol 29

Quyidagi kodning natijasi nima?

```python
class Elektr:
    def quvvat(self):
        return "Elektr quvvati"

class Benzin:
    def quvvat(self):
        return "Benzin quvvati"

class Gibrid(Elektr, Benzin):
    def quvvat(self):
        e = super().quvvat()
        return f"Gibrid: {e} + Benzin quvvati"

g = Gibrid()
print(g.quvvat())
```

- [A] `Gibrid: Benzin quvvati + Benzin quvvati`  
- [B] `Gibrid: Elektr quvvati + Benzin quvvati`  
- [C] `Elektr quvvati`  
- [D] Xato beradi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `super().quvvat()` MRO bo'yicha `Elektr.quvvat()` ni chaqiradi (`Elektr` `Benzin` dan oldin yozilgan). `"Elektr quvvati"` qaytadi. Natija: `"Gibrid: Elektr quvvati + Benzin quvvati"`.

---

## Savol 30

Quyidagi kodning natijasi nima?

```python
class Narx:
    def __init__(self, asosiy):
        self.asosiy = asosiy

    def jami(self):
        return self.asosiy

class QQSNarx(Narx):
    def __init__(self, asosiy, qqs=15):
        super().__init__(asosiy)
        self.qqs = qqs

    def jami(self):
        return self.asosiy * (1 + self.qqs / 100)

class ChegirmaNarx(QQSNarx):
    def __init__(self, asosiy, qqs, chegirma):
        super().__init__(asosiy, qqs)
        self.chegirma = chegirma

    def jami(self):
        qqsli = super().jami()
        return qqsli * (1 - self.chegirma / 100)

n = ChegirmaNarx(100000, 15, 10)
print(n.jami())
```

- [A] `100000`  
- [B] `115000.0`  
- [C] `103500.0`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `QQSNarx.jami()` → `100000 * 1.15 = 115000.0`. `ChegirmaNarx.jami()` → `115000 * (1 - 0.10) = 115000 * 0.90 = 103500.0`.

---

## Savol 31

`object` classi nima va Python meros olish bilan qanday bog'liq?

- [A] Python'da faqat meros olgan classlarga tegishli  
- [B] Python'da barcha classlar `object` classidan bilvosita meros oladi — u eng asosiy (base) class  
- [C] Faqat `int`, `str` kabi turdagi classlarga tegishli  
- [D] `object` classi Python'da mavjud emas  

> **To'g'ri javob:** B  
> **Tushuntirish:** Python 3 da barcha classlar `object` classidan bilvosita meros oladi. `object` classi eng asosiy base class bo'lib, `__str__`, `__repr__`, `__eq__` kabi asosiy metodlarni taqdim etadi. `class Mening:` deb yozsak ham, aslida `class Mening(object):` deb hisoblanadi.

---

## Savol 32

Quyidagi kodning natijasi nima?

```python
class Qurilma:
    def __init__(self, model, narx):
        self.model = model
        self.narx = narx

    def __str__(self):
        return f"{self.model} - {self.narx:,} so'm"

class Telefon(Qurilma):
    def __init__(self, model, narx, xotira):
        super().__init__(model, narx)
        self.xotira = xotira

    def __str__(self):
        asosiy = super().__str__()
        return f"{asosiy} ({self.xotira}GB)"

class Flagship(Telefon):
    def __init__(self, model, narx, xotira, kamera):
        super().__init__(model, narx, xotira)
        self.kamera = kamera

    def __str__(self):
        asosiy = super().__str__()
        return f"{asosiy} [{self.kamera}MP]"

f = Flagship("Galaxy S24", 12000000, 256, 200)
print(f)
```

- [A] `Galaxy S24 - 12,000,000 so'm`  
- [B] `Galaxy S24 - 12,000,000 so'm (256GB)`  
- [C] `Galaxy S24 - 12,000,000 so'm (256GB) [200MP]`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Flagship.__str__` → `super().__str__()` → `Telefon.__str__` → `super().__str__()` → `Qurilma.__str__` → `"Galaxy S24 - 12,000,000 so'm"`. Keyin `(256GB)` va `[200MP]` qo'shiladi. Natija: `"Galaxy S24 - 12,000,000 so'm (256GB) [200MP]"`.

---

## Savol 33

Quyidagi kodning natijasi nima?

```python
class Hisoblagich:
    def __init__(self, qiymat=0):
        self.qiymat = qiymat

    def oshir(self, n=1):
        self.qiymat += n
        return self

    def kamay(self, n=1):
        self.qiymat -= n
        return self

class KengaytirilganHisoblagich(Hisoblagich):
    def nolga_qaytarish(self):
        self.qiymat = 0
        return self

h = KengaytirilganHisoblagich(10)
h.oshir(5).oshir(3).kamay(2).nolga_qaytarish().oshir(7)
print(h.qiymat)
```

- [A] `23`  
- [B] `0`  
- [C] `7`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `10 + 5 = 15`, `15 + 3 = 18`, `18 - 2 = 16`, nolga qaytarildi: `0`, `0 + 7 = 7`. Method chaining ishladi. Natija: `7`.

---

## Savol 34

Quyidagi kodning natijasi nima?

```python
class Ota:
    def __init__(self, x):
        self.x = x

    def qiymat(self):
        return self.x

class Farzand1(Ota):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def qiymat(self):
        return super().qiymat() + self.y

class Farzand2(Farzand1):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def qiymat(self):
        return super().qiymat() + self.z

obj = Farzand2(10, 20, 30)
print(obj.qiymat())
```

- [A] `10`  
- [B] `30`  
- [C] `60`  
- [D] Xato beradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `Ota.qiymat()` → `10`. `Farzand1.qiymat()` → `super().qiymat() + y` = `10 + 20 = 30`. `Farzand2.qiymat()` → `super().qiymat() + z` = `30 + 30 = 60`. Natija: `60`.

---

## Savol 35

Quyidagi to'liq meros olish namunasining natijasi nima?

```python
class Jonzot:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def tanishuv(self):
        return f"Men {self.ism}, {self.yosh} yoshdaman"

class Inson(Jonzot):
    def __init__(self, ism, yosh, kasb):
        super().__init__(ism, yosh)
        self.kasb = kasb

    def tanishuv(self):
        asosiy = super().tanishuv()
        return f"{asosiy}, {self.kasb}man"

class Dasturchi(Inson):
    def __init__(self, ism, yosh, til):
        super().__init__(ism, yosh, "Dasturchi")
        self.til = til

    def tanishuv(self):
        asosiy = super().tanishuv()
        return f"{asosiy} ({self.til} dasturlash tili)"

    def kod_yoz(self):
        return f"{self.ism} {self.til} da kod yozmoqda..."

d = Dasturchi("Kamron", 25, "Python")
print(d.tanishuv())
print(d.kod_yoz())
print(isinstance(d, Inson))
print(isinstance(d, Jonzot))
```

- [A] `Men Kamron, 25 yoshdaman`, `Kamron Python da kod yozmoqda...`, `False`, `False`  
- [B] `Men Kamron, 25 yoshdaman, Dasturchiman (Python dasturlash tili)`, `Kamron Python da kod yozmoqda...`, `True`, `True`  
- [C] Xato beradi  
- [D] `Men Kamron, 25 yoshdaman (Python dasturlash tili)`, `Kamron Python da kod yozmoqda...`, `True`, `False`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `Dasturchi.tanishuv()` zanjiri: `Jonzot` → `"Men Kamron, 25 yoshdaman"`, `Inson` qo'shadi → `"..., Dasturchiman"`, `Dasturchi` qo'shadi → `"... (Python dasturlash tili)"`. `isinstance(d, Inson)` → `True`, `isinstance(d, Jonzot)` → `True` (meros zanjiri).

---