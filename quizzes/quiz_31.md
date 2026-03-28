## Savol 1

`return` operatori bo'lmagan funksiya qanday qiymat qaytaradi?

- [A] `0`
- [B] `False`
- [C] `None`
- [D] Bo'sh string `""`

> **To'g'ri javob:** C
> **Tushuntirish:** `return` ko'rsatilmagan yoki `return` (qiymatsiz) yozilgan funksiya `None` qaytaradi. Bu Python ning standart xulq-atvori — har bir funksiya albatta biror qiymat qaytaradi.

---

## Savol 2

`return` operatori funksiyada qanday vazifa bajaradi?

- [A] Faqat matn ekranga chiqaradi
- [B] Funksiyani to'xtatib, chaqirgan joyga qiymat qaytaradi
- [C] Funksiyani qayta ishga tushiradi
- [D] O'zgaruvchini o'chiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `return qiymat` — funksiya bajarilishini darhol to'xtatadi va ko'rsatilgan qiymatni chaqirgan joyga qaytaradi. `return` dan keyingi kod hech qachon ishlamaydi.

---

## Savol 3

`print()` va `return` ning asosiy farqi nima?

- [A] `print()` raqam, `return` matn chiqaradi
- [B] `print()` ekranga chiqaradi, hech narsa qaytarmaydi; `return` qiymat qaytaradi, ekranga chiqarmaydi
- [C] `return` faqat raqam qaytaradi
- [D] Hech qanday farq yo'q

> **To'g'ri javob:** B
> **Tushuntirish:** `print(x)` — `x` ni ekranga chiqaradi, `None` qaytaradi. `return x` — `x` ni chaqirgan joyga qaytaradi, ekranda hech narsa ko'rinmaydi. `return` qiymati saqlanishi, boshqa amallarda ishlatilishi mumkin.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
def salom():
    print("Salom!")

natija = salom()
print(natija)
```

- [A] `Salom!`, `Salom!`
- [B] `Salom!`, `None`
- [C] `None`, `Salom!`
- [D] `None`, `None`

> **To'g'ri javob:** B
> **Tushuntirish:** `salom()` chaqirilganda `print("Salom!")` ishlaydi → ekranda `Salom!`. Lekin funksiya `return` yo'qligi uchun `None` qaytaradi → `natija = None`. `print(natija)` → `None`.

---

## Savol 5

Quyidagi kodning natijasi nima?

```python
def kvadrat(x):
    return x * x

natija = kvadrat(5)
print(natija)
print(kvadrat(3) + kvadrat(4))
```

- [A] `25`, `7`
- [B] `25`, `25`
- [C] `25`, `25`
- [D] `25`, `49`

> **To'g'ri javob:** C — lekin to'g'risi:

> **To'g'ri javob:** A aslida emas. `kvadrat(3)=9`, `kvadrat(4)=16`, `9+16=25`. 

> **To'g'ri javob:** D  
> **Tushuntirish:** `kvadrat(5)` → `25`. `kvadrat(3)` → `9`, `kvadrat(4)` → `16`, `9+16=25`... Yo'q: `3*3=9`, `4*4=16`, `9+16=25`. Javob: `25`, `25`.

> **To'g'ri javob:** C  
> **Tushuntirish:** `kvadrat(5)` → `5*5=25`. `kvadrat(3)+kvadrat(4)` → `9+16=25`. Natija: `25`, `25`.

---

## Savol 6

Quyidagi kodning natijasi nima?

```python
def aytish(matn):
    print(matn)

def qaytarish(matn):
    return matn

a = aytish("test")
b = qaytarish("test")
print(type(a))
print(type(b))
```

- [A] `<class 'NoneType'>`, `<class 'NoneType'>`
- [B] `<class 'str'>`, `<class 'str'>`
- [C] `<class 'NoneType'>`, `<class 'str'>`
- [D] `<class 'str'>`, `<class 'NoneType'>`

> **To'g'ri javob:** C
> **Tushuntirish:** `aytish("test")` → `print` ishlaydi, `None` qaytaradi → `a = None` → `type(a)` → `NoneType`. `qaytarish("test")` → `"test"` qaytaradi → `b = "test"` → `type(b)` → `str`.

---

## Savol 7

Returnsiz funksiya qachon ishlatiladi?

- [A] Hech qachon, har doim `return` bo'lishi kerak
- [B] Faqat ekranga chiqarish, fayl yozish, ro'yxatni o'zgartirish kabi yon ta'sir (side effect) uchun mo'ljallangan holatlarda
- [C] Faqat math amallar uchun
- [D] Kichik funksiyalarda

> **To'g'ri javob:** B
> **Tushuntirish:** Returnsiz funksiyalar natija qaytarish o'rniga biror ish qiladi: ekranga chiqarish, faylga yozish, listni o'zgartirish, ma'lumotlar bazasiga saqlash kabi. Qiymatni qayta ishlatish shart bo'lmasa `return` shart emas.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
def chiziq(belgi="-", uzunlik=20):
    print(belgi * uzunlik)

chiziq()
chiziq("*", 10)
chiziq(uzunlik=5)
```

- [A] `--------------------` / `**********` / `-----`
- [B] `--------------------` / `----------` / `-----`
- [C] `********************` / `**********` / `-----`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `chiziq()` → standart `"-"*20`. `chiziq("*",10)` → `"*"*10`. `chiziq(uzunlik=5)` → `belgi` standart `"-"`, `uzunlik=5` → `"-----"`.

---

## Savol 9

`return` dan keyin yozilgan kod ishlaydimi?

- [A] Ha, har doim ishlaydi
- [B] Yo'q — `return` funksiyani to'xtatadi, undan keyingi kod hech qachon ishlamaydi
- [C] Faqat `return None` dan keyin ishlaydi
- [D] Shart blokida ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `return` — funksiyani darhol tugatadi. Undan keyingi kod **unreachable** (yetib bo'lmaydigan) hisoblanadi. Ko'pgina kod muharrirlari bu haqda ogohlantiradi.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
def tekshir(son):
    if son > 0:
        return "musbat"
    return "manfiy yoki nol"
    print("Bu hech qachon chiqmaydi")

print(tekshir(5))
print(tekshir(-3))
```

- [A] `musbat`, `manfiy yoki nol`, `Bu hech qachon chiqmaydi`
- [B] `musbat`, `manfiy yoki nol`
- [C] `musbat`, `None`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `tekshir(5)` → `5>0` → `return "musbat"` — funksiya to'xtaydi. `tekshir(-3)` → shart bajarilmaydi → `return "manfiy yoki nol"`. `print(...)` hech qachon ishlamaydi.

---

## Savol 11

Funksiya bir nechta `return` ga ega bo'lishi mumkinmi?

- [A] Yo'q, faqat bitta `return` bo'lishi mumkin
- [B] Ha, lekin faqat bittasi ishlaydi — birinchi yetib borilgan `return`
- [C] Faqat `if-else` ichida bo'lsa mumkin
- [D] Ikki `return` bo'lsa xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** Bir funksiyada bir nechta `return` bo'lishi mumkin (masalan shart blokida), lekin faqat birinchi bajarilgan `return` ishlaydi va funksiyani to'xtatadi. Qolgan `return` lar ishlamaydi.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
def toq_juft(n):
    if n % 2 == 0:
        return "juft"
    else:
        return "toq"

print(toq_juft(4))
print(toq_juft(7))
print(toq_juft(0))
```

- [A] `juft`, `toq`, `toq`
- [B] `juft`, `toq`, `juft`
- [C] `toq`, `juft`, `juft`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `toq_juft(4)` → `4%2==0` → `"juft"`. `toq_juft(7)` → `7%2==1` → `"toq"`. `toq_juft(0)` → `0%2==0` → `"juft"`.

---

## Savol 13

Funksiya bir nechta qiymat qaytara oladimi?

- [A] Yo'q, faqat bitta qiymat
- [B] Ha, vergul bilan yozilsa tuple sifatida qaytaradi
- [C] Faqat list sifatida qaytarishi mumkin
- [D] Faqat ikkita qiymat qaytarishi mumkin

> **To'g'ri javob:** B
> **Tushuntirish:** `return a, b, c` — Python bu qiymatlarni tuple ga yig'ib qaytaradi. `x, y, z = funksiya()` — unpacking bilan alohida o'zgaruvchilarga olish mumkin.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
def min_max(r):
    return min(r), max(r)

kichik, katta = min_max([3, 1, 7, 2, 9])
print(kichik)
print(katta)
print(type(min_max([1, 2, 3])))
```

- [A] `1`, `9`, `<class 'list'>`
- [B] `1`, `9`, `<class 'tuple'>`
- [C] `9`, `1`, `<class 'tuple'>`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `min_max(...)` → `(1, 9)` tuple qaytaradi. `kichik=1`, `katta=9`. `type(...)` → `<class 'tuple'>` — bir nechta qiymat qaytarish tuple orqali amalga oshadi.

---

## Savol 15

Quyidagi kodning natijasi nima?

```python
def hisob(a, b):
    yig = a + b
    ayir = a - b
    return yig, ayir

natija = hisob(10, 3)
print(natija)
print(natija[0])
print(natija[1])
```

- [A] `13 7`, `13`, `7`
- [B] `(13, 7)`, `13`, `7`
- [C] `[13, 7]`, `13`, `7`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `return yig, ayir` → `(13, 7)` tuple. `natija = (13, 7)`. `natija[0]` → `13`. `natija[1]` → `7`.

---

## Savol 16

`return` bilan `return None` ning farqi bormi?

- [A] Ha, katta farq bor
- [B] Yo'q — `return`, `return None` va `return` yo'qligi — uchala ham `None` qaytaradi
- [C] `return` xato beradi, `return None` ishlamaydi
- [D] Faqat `return None` to'g'ri yozuv

> **To'g'ri javob:** B
> **Tushuntirish:** `return`, `return None`, va umuman `return` bo'lmasligi — uchala holat ham `None` qaytaradi. Ular funksional jihatdan bir xil. Ba'zan kodni o'qilishi uchun `return None` aniq yoziladi.

---

## Savol 17

Quyidagi kodning natijasi nima?

```python
def f1():
    return

def f2():
    return None

def f3():
    pass

print(f1() == f2())
print(f2() == f3())
print(f1() is None)
```

- [A] `False`, `False`, `False`
- [B] `True`, `True`, `True`
- [C] `True`, `False`, `True`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `f1()`, `f2()`, `f3()` — uchala ham `None` qaytaradi. `None == None` → `True`. `None is None` → `True`.

---

## Savol 18

Returnsiz funksiya natijasini boshqa amallarda ishlatsa nima bo'ladi?

- [A] `0` bilan ishlaydi
- [B] `None` bilan amal bajarishga uriniladi → `TypeError`
- [C] Bo'sh string bilan ishlaydi
- [D] Avtomatik `0` ga aylanadi

> **To'g'ri javob:** B
> **Tushuntirish:** `None` ustida son yoki string amallari bajarib bo'lmaydi. `None + 5` → `TypeError`. Shuning uchun qiymat qaytarishi kerak bo'lgan funksiyada `return` yozish muhim.

---

## Savol 19

Quyidagi kodning natijasi nima?

```python
def uch_barobar(x):
    print(x * 3)

natija = uch_barobar(4)
print(natija + 1)
```

- [A] `12`, `13`
- [B] `12`, `TypeError`
- [C] `12`, `None`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `uch_barobar(4)` → `print(12)` ishlaydi (ekranda `12`), lekin `None` qaytaradi. `natija = None`. `None + 1` → `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`.

---

## Savol 20

Quyidagi kodning natijasi nima?

```python
def to'la_ism(ism, familiya):
    return ism + " " + familiya

def chop(ism, familiya):
    print(ism + " " + familiya)

a = to'la_ism("Ali", "Valiyev")
b = chop("Vali", "Aliyev")

print(a.upper())
print(b)
```

- [A] `ALI VALIYEV`, `VALI ALIYEV`
- [B] `Vali Aliyev`, `ALI VALIYEV`, `None`
- [C] `Vali Aliyev` \n `ALI VALIYEV` \n `None`
- [D] `Vali Aliyev`, `ALI VALIYEV`, `None`

> **To'g'ri javob:** D
> **Tushuntirish:** `to'la_ism(...)` → `"Ali Valiyev"` qaytaradi → `a = "Ali Valiyev"`. `chop(...)` → `print("Vali Aliyev")` ekranda chiqadi, `None` qaytaradi → `b = None`. `a.upper()` → `"ALI VALIYEV"`. `print(b)` → `None`.

---

## Savol 21

Quyidagi kodning natijasi nima?

```python
def solishtr(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None

x = solishtr(5, 3)
y = solishtr(4, 4)
print(x)
print(y is None)
```

- [A] `5`, `False`
- [B] `5`, `True`
- [C] `3`, `True`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `solishtr(5,3)` → `5>3` → `return 5`. `solishtr(4,4)` → teng → `return None`. `x=5`. `y is None` → `True`.

---

## Savol 22

Quyidagi kodning natijasi nima?

```python
def chop_qilish(r):
    for element in r:
        print(element)

def filtrlash(r, chegara):
    natija = []
    for x in r:
        if x > chegara:
            natija.append(x)
    return natija

sonlar = [1, 5, 3, 8, 2, 9, 4]
katta = filtrlash(sonlar, 4)
chop_qilish(katta)
```

- [A] `1 5 3 8 2 9 4`
- [B] `5 8 9`
- [C] `5`, `8`, `9` (har biri alohida qatorda)
- [D] Xato beradi

> **To'g'ri javob:** C
> **Tushuntirish:** `filtrlash(sonlar, 4)` → `4` dan katta: `[5, 8, 9]`. `chop_qilish([5,8,9])` → `for` bilan har elementni `print` qiladi: `5`, `8`, `9` alohida qatorlarda.

---

## Savol 23

Funksiya ichida `return` shart bloki ichida bo'lsa nima bo'ladi?

- [A] Shart bajarilmasa `return` ishlamaydi va funksiya avtomatik `None` qaytaradi
- [B] Xato beradi
- [C] Shart bajarilmasa `0` qaytariladi
- [D] Funksiya to'xtamaydi

> **To'g'ri javob:** A
> **Tushuntirish:** Agar `return` faqat `if` blokida bo'lsa va shart bajarilmasa, `return` ga yetilmaydi. Funksiya oxirigacha ishlaydi va `None` qaytaradi. Bu ko'p uchraydigan xato manbai.

---

## Savol 24

Quyidagi kodning natijasi nima?

```python
def topish(r, qidiruv):
    for i, x in enumerate(r):
        if x == qidiruv:
            return i

print(topish([10, 20, 30, 40], 30))
print(topish([10, 20, 30, 40], 99))
```

- [A] `2`, `0`
- [B] `2`, `None`
- [C] `2`, `-1`
- [D] `2`, `KeyError`

> **To'g'ri javob:** B
> **Tushuntirish:** `topish(...,30)` → `30` 2-indeksda → `return 2`. `topish(...,99)` → `99` topilmaydi → `return` ga yetilmaydi → `None` qaytaradi.

---

## Savol 25

Returnsiz va returnli funksiyalar qaysi mezon bo'yicha tanlanadi?

- [A] Funksiya uzunligi bo'yicha
- [B] Natija qayta ishlatilishi kerak bo'lsa `return`, faqat ish bajarish kerak bo'lsa returnsiz
- [C] Har doim `return` yaxshiroq
- [D] Har doim returnsiz yaxshiroq

> **To'g'ri javob:** B
> **Tushuntirish:** `return` — natijani boshqa hisoblashlarda, o'zgaruvchida saqlash, boshqa funksiyaga berish uchun kerak. Returnsiz — faqat yon ta'sir (ekranga chiqarish, faylga yozish, listni o'zgartirish) uchun ishlatiladi. Maqsadga qarab tanlanadi.

---

## Savol 26

Quyidagi kodning natijasi nima?

```python
def xabar(ism, yoshmi=True):
    if yoshmi:
        print(f"Assalomu alaykum, {ism}!")
    else:
        print(f"Salom, {ism}!")

def olish(ism, yoshmi=True):
    if yoshmi:
        return f"Assalomu alaykum, {ism}!"
    else:
        return f"Salom, {ism}!"

xabar("Bobur")
x = olish("Sarvar", False)
print(x.upper())
```

- [A] `Assalomu alaykum, Bobur!` / `SALOM, SARVAR!`
- [B] `Assalomu alaykum, Bobur!` / `Salom, Sarvar!`
- [C] `None` / `SALOM, SARVAR!`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `xabar("Bobur")` → `yoshmi=True` → `print(...)` chiqaradi. `olish("Sarvar",False)` → `return "Salom, Sarvar!"`. `x.upper()` → `"SALOM, SARVAR!"`.

---

## Savol 27

Quyidagi kodning natijasi nima?

```python
def ro'yxat_chop(r):
    if not r:
        print("Ro'yxat bo'sh!")
        return
    for i, x in enumerate(r, 1):
        print(f"{i}. {x}")

ro'yxat_chop(["Python", "Java", "C++"])
ro'yxat_chop([])
```

- [A] `1. Python` / `2. Java` / `3. C++` / `Ro'yxat bo'sh!`
- [B] `1. Python` / `2. Java` / `3. C++` / `None`
- [C] Xato beradi
- [D] Hech narsa chiqmaydi

> **To'g'ri javob:** A
> **Tushuntirish:** `ro'yxat_chop([...])` → ro'yxat to'la → `for` bilan chiqaradi. `ro'yxat_chop([])` → `not []` → `True` → `"Ro'yxat bo'sh!"` chiqarib, `return` bilan to'xtaydi (bo'sh `return` → `None`).

---

## Savol 28

Quyidagi kodning natijasi nima?

```python
def yosh_tekshir(yosh):
    if yosh < 0:
        return "Noto'g'ri yosh"
    if yosh < 18:
        return "Voyaga yetmagan"
    if yosh < 65:
        return "Voyaga yetgan"
    return "Keksa"

print(yosh_tekshir(-5))
print(yosh_tekshir(15))
print(yosh_tekshir(30))
print(yosh_tekshir(70))
```

- [A] `Noto'g'ri yosh`, `Voyaga yetmagan`, `Voyaga yetgan`, `Keksa`
- [B] `Keksa`, `Voyaga yetmagan`, `Voyaga yetgan`, `Keksa`
- [C] `Noto'g'ri yosh`, `Voyaga yetmagan`, `Voyaga yetgan`, `Voyaga yetgan`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `-5<0` → `"Noto'g'ri yosh"`. `15<18` → `"Voyaga yetmagan"`. `30<65` → `"Voyaga yetgan"`. `70>=65` → oxirgi `return "Keksa"`.

---

## Savol 29

Quyidagi kodning natijasi nima?

```python
def ikki_tomonlama(r):
    r.append(99)

sonlar = [1, 2, 3]
natija = ikki_tomonlama(sonlar)
print(sonlar)
print(natija)
```

- [A] `[1, 2, 3]`, `[1, 2, 3, 99]`
- [B] `[1, 2, 3, 99]`, `None`
- [C] `[1, 2, 3]`, `None`
- [D] `[1, 2, 3, 99]`, `[1, 2, 3, 99]`

> **To'g'ri javob:** B
> **Tushuntirish:** `r.append(99)` — asl `sonlar` listini o'zgartiradi (list mutable, reference orqali). Funksiya `None` qaytaradi. `sonlar` → `[1,2,3,99]`. `natija = None`.

---

## Savol 30

Quyidagi kodning natijasi nima?

```python
def tozalash(d, kalit):
    if kalit in d:
        del d[kalit]
        return True
    return False

ma'lumot = {"ism": "Ali", "yosh": 20, "shahar": "Toshkent"}
x = tozalash(ma'lumot, "yosh")
y = tozalash(ma'lumot, "kasb")
print(x, y)
print(len(ma'lumot))
```

- [A] `True True`, `1`
- [B] `True False`, `2`
- [C] `False True`, `2`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `tozalash(ma'lumot,"yosh")` → `"yosh"` bor → o'chiriladi → `True`. `tozalash(ma'lumot,"kasb")` → `"kasb"` yo'q → `False`. `len(ma'lumot)` → `"ism"` va `"shahar"` qoldi → `2`.

---

## Savol 31

Quyidagi kodda xato bormi?

```python
def f(x):
    if x > 0:
        return x

natija = f(5) + f(-3)
print(natija)
```

- [A] Xato yo'q, `2` chiqadi
- [B] `f(-3)` → `None` → `None + 5` → `TypeError`
- [C] `f(5)` → `5`, `f(-3)` → `0` → `5` chiqadi
- [D] Ikkalasi ham `None` → `TypeError`

> **To'g'ri javob:** B
> **Tushuntirish:** `f(5)` → `5>0` → `return 5`. `f(-3)` → shart bajarilmaydi → `None`. `5 + None` → `TypeError: unsupported operand type(s)`.

---

## Savol 32

Quyidagi kodning natijasi nima?

```python
def chegara(son, min_q=0, max_q=100):
    if son < min_q:
        return min_q
    if son > max_q:
        return max_q
    return son

print(chegara(50))
print(chegara(-10))
print(chegara(150))
print(chegara(75, 50, 80))
```

- [A] `50`, `0`, `100`, `75`
- [B] `50`, `-10`, `150`, `75`
- [C] `50`, `0`, `100`, `80`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `chegara(50)` → `0<=50<=100` → `50`. `chegara(-10)` → `-10<0` → `0`. `chegara(150)` → `150>100` → `100`. `chegara(75,50,80)` → `50<=75<=80` → `75`.

---

## Savol 33

Quyidagi kodning natijasi nima?

```python
def sarlavha(matn, belgi="="):
    chiziq = belgi * len(matn)
    print(chiziq)
    print(matn)
    print(chiziq)

x = sarlavha("Python kursi")
print(x)
```

- [A] `============` / `Python kursi` / `============` / `None`
- [B] `============` / `Python kursi` / `============` / `Python kursi`
- [C] `None` / `Python kursi` / `None` / `None`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `sarlavha("Python kursi")` → `len("Python kursi")=12` → `"="*12`. Uch `print`. Funksiya `None` qaytaradi → `x=None` → `print(x)` → `None`.

---

## Savol 34

Quyidagi kodning natijasi nima?

```python
def bo'linish(a, b):
    if b == 0:
        print("Nolga bo'lib bo'lmaydi!")
        return
    return a / b

x = bo'linish(10, 2)
y = bo'linish(5, 0)
print(x)
print(y)
```

- [A] `5.0`, `None`
- [B] `5.0`, `Nolga bo'lib bo'lmaydi!` so'ng `None`
- [C] `5.0`, `0`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `bo'linish(10,2)` → `5.0` qaytaradi. `bo'linish(5,0)` → `b==0` → `print(...)` chiqaradi va bo'sh `return` → `None`. `print(x)` → `5.0`. `print(y)` → `None`.

---

## Savol 35

Quyidagi kodning natijasi nima?

```python
def statistika(r):
    if not r:
        return None, None, None
    return min(r), max(r), len(r)

a, b, c = statistika([3, 1, 7, 2])
print(a, b, c)

x, y, z = statistika([])
print(x, y, z)
```

- [A] `1 7 4`, `None None None`
- [B] `1 7 4`, `0 0 0`
- [C] `3 7 4`, `None None None`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `statistika([3,1,7,2])` → `(1, 7, 4)` → `a=1, b=7, c=4`. `statistika([])` → `not []` → `True` → `(None, None, None)` → `x=None, y=None, z=None`.

---

## Savol 36

Quyidagi kodning natijasi nima?

```python
def qayta_format(ism, familiya, yosh):
    to'liq = f"{familiya} {ism}"
    yosh_matn = f"{yosh} yosh"
    return to'liq, yosh_matn

natija = qayta_format("Ali", "Valiyev", 25)
print(natija)
print(len(natija))
print(natija[0])
```

- [A] `("Valiyev Ali", "25 yosh")`, `2`, `"Valiyev Ali"`
- [B] `["Valiyev Ali", "25 yosh"]`, `2`, `"Valiyev Ali"`
- [C] `"Valiyev Ali 25 yosh"`, `1`, `"V"`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** Bir nechta qiymat → tuple qaytaradi: `("Valiyev Ali", "25 yosh")`. `len(natija)` → `2`. `natija[0]` → `"Valiyev Ali"`.

---

## Savol 37

Quyidagi kodning natijasi nima?

```python
def log(xabar, daraja="INFO"):
    print(f"[{daraja}] {xabar}")

def xato_log(xabar):
    log(xabar, daraja="XATO")

def ogohlantirish(xabar):
    log(xabar, "OGOHLANTIRISH")

log("Tizim ishga tushdi")
xato_log("Fayl topilmadi")
ogohlantirish("Xotira kam")
```

- [A] `[INFO] Tizim ishga tushdi` / `[XATO] Fayl topilmadi` / `[OGOHLANTIRISH] Xotira kam`
- [B] `[INFO] Tizim ishga tushdi` / `[INFO] Fayl topilmadi` / `[INFO] Xotira kam`
- [C] Xato beradi
- [D] `[XATO] Tizim ishga tushdi` / `[XATO] Fayl topilmadi` / `[XATO] Xotira kam`

> **To'g'ri javob:** A
> **Tushuntirish:** `log(...)` standart `"INFO"`. `xato_log` → `log` ga `daraja="XATO"` bilan chaqiradi. `ogohlantirish` → pozitsion `"OGOHLANTIRISH"` bilan.

---

## Savol 38

Quyidagi kodning natijasi nima?

```python
def tekshir_va_qaytarish(r, qidiruv):
    for element in r:
        if element == qidiruv:
            return True
    return False

def hisobla(r, qidiruv):
    soni = 0
    for element in r:
        if element == qidiruv:
            soni += 1
    print(f"'{qidiruv}' → {soni} marta")

mevalar = ["olma", "banan", "olma", "gilos", "olma"]
print(tekshir_va_qaytarish(mevalar, "banan"))
print(tekshir_va_qaytarish(mevalar, "anor"))
hisobla(mevalar, "olma")
```

- [A] `True`, `False`, `'olma' → 3 marta`
- [B] `True`, `None`, `'olma' → 3 marta`
- [C] `True`, `False`, `None`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `tekshir_va_qaytarish(...,"banan")` → topildi → `True`. `tekshir_va_qaytarish(...,"anor")` → topilmadi → `False`. `hisobla(...,"olma")` → `print` chiqaradi, `None` qaytaradi (lekin natijasi ishlatilmaydi).

---

## Savol 39

Quyidagi kodning natijasi nima?

```python
def format_narx(narx, valyuta="so'm"):
    if narx < 0:
        return None
    return f"{narx:,} {valyuta}"

narxlar = [15000, -500, 230000, 0]
for n in narxlar:
    natija = format_narx(n)
    if natija is None:
        print("Noto'g'ri narx")
    else:
        print(natija)
```

- [A] `15,000 so'm` / `Noto'g'ri narx` / `230,000 so'm` / `0 so'm`
- [B] `15,000 so'm` / `-500 so'm` / `230,000 so'm` / `0 so'm`
- [C] `15000 so'm` / `Noto'g'ri narx` / `230000 so'm` / `0 so'm`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `15000` → `"15,000 so'm"`. `-500<0` → `None` → `"Noto'g'ri narx"`. `230000` → `"230,000 so'm"`. `0>=0` → `"0 so'm"`.

---

## Savol 40

Quyidagi to'liq kodning natijasi nima?

```python
def hisob_kitob(ism, narx, soni, chegirma=0):
    jami = narx * soni
    chegirma_miqdori = jami * chegirma / 100
    to'lov = jami - chegirma_miqdori
    return ism, jami, to'lov

def chek_chop(ism, jami, to'lov):
    print(f"Xaridor: {ism}")
    print(f"Jami:    {jami:,.0f} so'm")
    print(f"To'lov:  {to'lov:,.0f} so'm")

nomi, jami, to'lov = hisob_kitob("Sardor", 25000, 3, chegirma=10)
chek_chop(nomi, jami, to'lov)
```

- [A] `Xaridor: Sardor` / `Jami: 75,000 so'm` / `To'lov: 67,500 so'm`
- [B] `Xaridor: Sardor` / `Jami: 75,000 so'm` / `To'lov: 75,000 so'm`
- [C] `Xaridor: Sardor` / `Jami: 25,000 so'm` / `To'lov: 22,500 so'm`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `jami = 25000*3 = 75000`. `chegirma_miqdori = 75000*10/100 = 7500`. `to'lov = 75000-7500 = 67500`. `hisob_kitob` → `("Sardor", 75000, 67500)`. `chek_chop` ekranga chiqaradi.

---