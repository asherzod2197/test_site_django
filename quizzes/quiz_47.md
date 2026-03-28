## Savol 1

`def` kalit so'zi nima uchun ishlatiladi?

- [A] O'zgaruvchi e'lon qilish uchun
- [B] Funksiya e'lon qilish (yaratish) uchun
- [C] Shart tekshirish uchun
- [D] Modul import qilish uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `def` — "define" so'zining qisqartmasi. Funksiya nomini, parametrlarini va tanasini belgilaydi. `def` yozilganda funksiya hali ishlamaydi — faqat e'lon qilinadi.

---

## Savol 2

Funksiya e'lonining to'g'ri sintaksisi qaysi?

- [A] `def nomi{}: kod`
- [B] `function nomi(): kod`
- [C] `def nomi(): \n    kod`
- [D] `define nomi(): kod`

> **To'g'ri javob:** C
> **Tushuntirish:** To'g'ri sintaksis: `def nomi():` — ikki nuqta bilan tugaydi. Funksiya tanasi **4 ta bo'sh joy** (indent) bilan ichkariga yoziladi. `function` yoki `define` Python da kalit so'z emas.

---

## Savol 3

Quyidagi kodning natijasi nima?

```python
def chop_et():
    print("Birinchi")
    print("Ikkinchi")

print("Nol")
chop_et()
print("Uchinchi")
```

- [A] `Nol`, `Birinchi`, `Ikkinchi`, `Uchinchi`
- [B] `Birinchi`, `Ikkinchi`, `Nol`, `Uchinchi`
- [C] `Nol`, `Uchinchi`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `def chop_et():` — faqat e'lon, hali ishlamaydi. `print("Nol")` → `Nol`. `chop_et()` → `Birinchi`, `Ikkinchi`. `print("Uchinchi")` → `Uchinchi`.

---

## Savol 4

Funksiya tanasi (body) qanday belgilanadi?

- [A] `{}` qavslar bilan
- [B] `begin...end` kalit so'zlari bilan
- [C] Indentatsiya (4 ta bo'sh joy yoki 1 tab) bilan
- [D] `()` qavslar bilan

> **To'g'ri javob:** C
> **Tushuntirish:** Python da kod bloklari indentatsiya bilan belgilanadi. Funksiya tanasi `def` satridan keyin 4 ta bo'sh joy (yoki 1 tab) ichkariga yoziladi. Indentatsiya buzilsa `IndentationError` beradi.

---

## Savol 5

Quyidagi kodning natijasi nima?

```python
def aytish(narsa):
    print(f"Bu {narsa}!")

aytish("kitob")
aytish("qalam")
aytish("daftar")
```

- [A] `Bu narsa!` uch marta
- [B] `Bu kitob!`, `Bu qalam!`, `Bu daftar!`
- [C] Faqat `Bu kitob!`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `narsa` parametriga har safar boshqa argument beriladi: `"kitob"`, `"qalam"`, `"daftar"`. Har chaqiruvda `f-string` mos qiymat bilan chiqadi.

---

## Savol 6

Bir nechta parametrli funksiya qanday yaratiladi?

- [A] `def f(a; b; c):`
- [B] `def f(a, b, c):`
- [C] `def f(a b c):`
- [D] `def f[a, b, c]:`

> **To'g'ri javob:** B
> **Tushuntirish:** Parametrlar vergul bilan ajratiladi: `def f(a, b, c):`. Chaqirishda ham xuddi shunday: `f(1, 2, 3)`. Parametrlar soni va tartibi mos bo'lishi shart.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
def tanishtir(ism, yosh, shahar):
    print(f"{ism}, {yosh} yosh, {shahar}dan")

tanishtir("Sarvar", 20, "Buxoro")
```

- [A] `Sarvar, yosh yosh, shahardan`
- [B] `ism, 20 yosh, Buxoradan`
- [C] `Sarvar, 20 yosh, Buxoradan`
- [D] Xato beradi

> **To'g'ri javob:** C
> **Tushuntirish:** Uchta argument tartib bilan parametrlarga biriktiriladi: `ism="Sarvar"`, `yosh=20`, `shahar="Buxoro"`. `f-string` ularni mos o'rinlarga qo'yadi.

---

## Savol 8

`return` bo'lmagan funksiya nima qaytaradi?

- [A] `0`
- [B] `False`
- [C] `None`
- [D] Bo'sh string `""`

> **To'g'ri javob:** C
> **Tushuntirish:** `return` yozilmagan yoki `return` (qiymatsiz) yozilgan funksiya `None` qaytaradi. `x = funksiya()` → `x = None`. Bu Python ning standart xulq-atvori.

---

## Savol 9

Quyidagi kodning natijasi nima?

```python
def tekshir(son):
    if son > 0:
        return "musbat"
    elif son < 0:
        return "manfiy"
    else:
        return "nol"

print(tekshir(5))
print(tekshir(-3))
print(tekshir(0))
```

- [A] `True`, `False`, `True`
- [B] `musbat`, `manfiy`, `nol`
- [C] `5`, `-3`, `0`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `tekshir(5)` → `5 > 0` → `"musbat"`. `tekshir(-3)` → `-3 < 0` → `"manfiy"`. `tekshir(0)` → `else` → `"nol"`.

---

## Savol 10

Kalit so'z argumentlari (keyword arguments) nima?

- [A] Faqat raqamli argumentlar
- [B] Funksiya chaqirishda `parametr_nomi=qiymat` shaklida beriladigan argumentlar — tartib muhim emas
- [C] Standart qiymatli parametrlar
- [D] `*args` bilan beriladigan argumentlar

> **To'g'ri javob:** B
> **Tushuntirish:** `f(b=2, a=1)` — kalit so'z argumentlari. Tartibdan qat'i nazar, nom bilan biriktiriladi. Oddiy (pozitsion) va kalit so'z argumentlari aralashtirilishi mumkin, lekin pozitsionlar oldin kelishi shart.

---

## Savol 11

Quyidagi kodning natijasi nima?

```python
def to'rtburchak(en, bo'y):
    return en * bo'y

yuza1 = to'rtburchak(4, 5)
yuza2 = to'rtburchak(bo'y=5, en=4)
print(yuza1)
print(yuza2)
print(yuza1 == yuza2)
```

- [A] `20`, `20`, `True`
- [B] `9`, `9`, `True`
- [C] `20`, `45`, `False`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `to'rtburchak(4, 5)` — pozitsion: `en=4`, `bo'y=5` → `20`. `to'rtburchak(bo'y=5, en=4)` — kalit so'z: tartib farq qilmaydi → `20`. `20 == 20` → `True`.

---

## Savol 12

Standart qiymatli parametr qayerda yozilishi kerak?

- [A] Istalgan joyda
- [B] Standart qiymatsiz parametrlardan **oldin**
- [C] Standart qiymatsiz parametrlardan **keyin**
- [D] Faqat birinchi parametr standart bo'lishi mumkin

> **To'g'ri javob:** C
> **Tushuntirish:** `def f(a, b=2):` — to'g'ri. `def f(a=1, b):` — **noto'g'ri**, `SyntaxError`. Standart qiymatli parametrlar majburiy parametrlardan keyin kelishi shart, aks holda Python qaysi argumentni qaysi parametrga biriktirish kerakligini bilmay qoladi.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
def salomlash(ism, til="uz"):
    if til == "uz":
        print(f"Salom, {ism}!")
    elif til == "en":
        print(f"Hello, {ism}!")
    else:
        print(f"Hi, {ism}!")

salomlash("Kamol")
salomlash("John", "en")
salomlash("Sara", "fr")
```

- [A] Uch marta `Salom!`
- [B] `Salom, Kamol!`, `Hello, John!`, `Hi, Sara!`
- [C] `Salom, Kamol!`, `Salom, John!`, `Hi, Sara!`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `salomlash("Kamol")` → `til` standart `"uz"` → `"Salom, Kamol!"`. `salomlash("John","en")` → `"Hello, John!"`. `salomlash("Sara","fr")` → `else` → `"Hi, Sara!"`.

---

## Savol 14

`return` dan keyin yozilgan kod ishlaydimi?

- [A] Ha, har doim ishlaydi
- [B] Yo'q — `return` funksiyani to'xtatadi, undan keyingi kod hech qachon ishlamaydi
- [C] Faqat `return None` dan keyin ishlaydi
- [D] Faqat `try` blokida ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `return` — funksiyani darhol to'xtatadi. Undan keyingi kod **unreachable code** (yetib bo'lmaydigan kod) deyiladi va hech qachon bajarilmaydi. Ko'pgina muharririar bu haqda ogohlantiradi.

---

## Savol 15

Quyidagi to'liq kodning natijasi nima?

```python
def baholash(ball, ism="Talaba"):
    if ball >= 90:
        daraja = "A'lo"
    elif ball >= 70:
        daraja = "Yaxshi"
    elif ball >= 50:
        daraja = "Qoniqarli"
    else:
        daraja = "Qoniqarsiz"
    return f"{ism}: {daraja}"

print(baholash(95, "Zulfiya"))
print(baholash(73))
print(baholash(45))
```

- [A] `Zulfiya: A'lo`, `Talaba: Yaxshi`, `Talaba: Qoniqarli`
- [B] `Zulfiya: A'lo`, `Talaba: Yaxshi`, `Talaba: Qoniqarsiz`
- [C] `Zulfiya: Yaxshi`, `Talaba: Yaxshi`, `Talaba: Qoniqarsiz`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `baholash(95, "Zulfiya")` → `95 >= 90` → `"A'lo"` → `"Zulfiya: A'lo"`. `baholash(73)` → `ism` standart `"Talaba"`, `73 >= 70` → `"Yaxshi"` → `"Talaba: Yaxshi"`. `baholash(45)` → `45 < 50` → `"Qoniqarsiz"` → `"Talaba: Qoniqarsiz"`.

---