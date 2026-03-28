## Savol 1

Funksiya nima?

- [A] O'zgaruvchini saqlash uchun maxsus joy
- [B] Muayyan vazifani bajaradigan, nom berilgan va qayta ishlatilishi mumkin bo'lgan kod bloki
- [C] Faqat matematika hisob-kitoblarini bajaruvchi qurilma
- [D] Python dagi maxsus kalit so'z

> **To'g'ri javob:** B
> **Tushuntirish:** Funksiya — nom berilgan, muayyan vazifani bajaradigan kod bloki. Bir marta yozilib, ko'p marta chaqirilishi mumkin. Bu kodni takrorlamaslik (DRY — Don't Repeat Yourself) va tartibli yozish imkonini beradi.

---

## Savol 2

Python da funksiya qanday e'lon qilinadi?

- [A] `function nomi():`
- [B] `func nomi():`
- [C] `def nomi():`
- [D] `define nomi():`

> **To'g'ri javob:** C
> **Tushuntirish:** Python da funksiya `def` kalit so'zi bilan e'lon qilinadi: `def funksiya_nomi():`. `def` — "define" (belgilash) so'zining qisqartmasi.

---

## Savol 3

Quyidagi kodning natijasi nima?

```python
def salom():
    print("Salom, Dunyo!")

salom()
salom()
```

- [A] Faqat bir marta `Salom, Dunyo!` chiqadi
- [B] Ikki marta `Salom, Dunyo!` chiqadi
- [C] Hech narsa chiqmaydi
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `def salom():` — funksiyani e'lon qiladi (lekin ishlatmaydi). `salom()` — har chaqirilganda funksiya tanasi ishlaydi. Ikkita chaqiruv → ikki marta chiqadi.

---

## Savol 4

Funksiya parametri va argumentning farqi nima?

- [A] Hech qanday farq yo'q, bir xil tushuncha
- [B] Parametr — funksiya e'lonidagi o'zgaruvchi nomi; argument — funksiya chaqirilganda beriladigan haqiqiy qiymat
- [C] Argument — e'londagi nom, parametr — chaqirishdagi qiymat
- [D] Parametr faqat raqam, argument faqat matn bo'ladi

> **To'g'ri javob:** B
> **Tushuntirish:** `def yig'(a, b):` — `a` va `b` **parametrlar**. `yig'(3, 5)` — `3` va `5` **argumentlar**. Parametr — shablon, argument — unga beriladigan haqiqiy qiymat.

---

## Savol 5

Quyidagi kodning natijasi nima?

```python
def kutib_olish(ism):
    print(f"Xush kelibsiz, {ism}!")

kutib_olish("Malika")
kutib_olish("Jasur")
```

- [A] `Xush kelibsiz, ism!` ikki marta
- [B] `Xush kelibsiz, Malika!` va `Xush kelibsiz, Jasur!`
- [C] Hech narsa chiqmaydi
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `ism` parametriga `"Malika"` va `"Jasur"` argumentlari beriladi. Har safar `ism` o'sha qiymatni oladi va `f-string` da chiqariladi.

---

## Savol 6

`return` operatori nima qiladi?

- [A] Funksiyani e'lon qiladi
- [B] Funksiyani to'xtatib, chaqirgan joyga qiymat qaytaradi
- [C] Faqat matn chiqaradi
- [D] Parametrlarni aniqlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `return qiymat` — funksiya bajarilishini to'xtatib, ko'rsatilgan qiymatni chaqirgan joyga qaytaradi. `return` siz funksiya `None` qaytaradi. `return` dan keyin yozilgan kod ishlamaydi.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
def ikkilantir(son):
    return son * 2

natija = ikkilantir(7)
print(natija)
print(ikkilantir(10))
```

- [A] `7`, `10`
- [B] `14`, `20`
- [C] `None`, `None`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `ikkilantir(7)` → `7 * 2 = 14` qaytaradi → `natija = 14`. `ikkilantir(10)` → `20` qaytaradi va `print` chiqaradi.

---

## Savol 8

`return` va `print()` ning farqi nima?

- [A] Hech qanday farq yo'q
- [B] `print()` — ekranga chiqaradi, dasturda ishlatib bo'lmaydi; `return` — qiymat qaytaradi, uni o'zgaruvchiga saqlash yoki boshqa amallarda ishlatish mumkin
- [C] `return` faqat raqam qaytaradi
- [D] `print()` qiymat qaytaradi, `return` chiqaradi

> **To'g'ri javob:** B
> **Tushuntirish:** `print(5)` — `5` ni ekranga chiqaradi, `None` qaytaradi. `return 5` — `5` ni qaytaradi, ekranga hech narsa chiqarmaydi. `return` qiymati o'zgaruvchiga saqlanadi yoki boshqa funksiyaga beriladi.

---

## Savol 9

Quyidagi kodning natijasi nima?

```python
def hisob(a, b):
    print(a + b)

def hisob2(a, b):
    return a + b

x = hisob(3, 4)
y = hisob2(3, 4)
print(x)
print(y)
```

- [A] `7`, `7`, `7`, `7`
- [B] `7`, `None`, `7`
- [C] `None`, `7`, `None`, `7`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `hisob(3,4)` → `print` bilan `7` chiqaradi, lekin `None` qaytaradi → `x = None`. `hisob2(3,4)` → `7` qaytaradi → `y = 7`. `print(x)` → `None`. `print(y)` → `7`.

---

## Savol 10

Standart (default) parametr qiymat nima?

- [A] Funksiya har doim ishlatadigan yagona qiymat
- [B] Argument berilmagan holda parametrning oladigan oldindan belgilangan qiymati
- [C] Faqat `None` bo'lishi mumkin
- [D] Funksiya qaytaradigan qiymat

> **To'g'ri javob:** B
> **Tushuntirish:** `def f(x, n=2):` — `n` ning standart qiymati `2`. `f(5)` — `n=2` ishlatiladi. `f(5, 3)` — `n=3` bo'ladi. Standart qiymatli parametrlar **oxirda** yoziladi.

---

## Savol 11

Quyidagi kodning natijasi nima?

```python
def tabriklash(ism, munosabat="Xush kelibsiz"):
    print(f"{munosabat}, {ism}!")

tabriklash("Sherzod")
tabriklash("Nodira", "Salom")
```

- [A] `Xush kelibsiz, Sherzod!` va `Xush kelibsiz, Nodira!`
- [B] `Xush kelibsiz, Sherzod!` va `Salom, Nodira!`
- [C] Xato beradi
- [D] `Salom, Sherzod!` va `Salom, Nodira!`

> **To'g'ri javob:** B
> **Tushuntirish:** `tabriklash("Sherzod")` — `munosabat` berilmagan → standart: `"Xush kelibsiz"`. `tabriklash("Nodira", "Salom")` — `munosabat="Salom"` berilgan → standart ustiga yoziladi.

---

## Savol 12

Funksiya nechta qiymat qaytara oladi?

- [A] Faqat bitta
- [B] Faqat ikkita
- [C] Bir nechta — tuple sifatida qaytaradi
- [D] Umuman qaytara olmaydi

> **To'g'ri javob:** C
> **Tushuntirish:** `return a, b, c` — Python bu qiymatlarni tuple ga yig'adi va qaytaradi. `x, y, z = funksiya()` — unpacking bilan alohida o'zgaruvchilarga olish mumkin.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
def min_max(r):
    return min(r), max(r)

kichik, katta = min_max([3, 1, 7, 2, 9, 4])
print(kichik)
print(katta)
```

- [A] `(1, 9)`, xato
- [B] `1`, `9`
- [C] `3`, `9`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `min_max` → `(1, 9)` tuple qaytaradi. `kichik, katta = (1, 9)` → unpacking. `kichik = 1`, `katta = 9`.

---

## Savol 14

Lokal (local) va global o'zgaruvchi nima?

- [A] Lokal — butun dasturda ko'rinadigan, global — faqat funksiya ichida
- [B] Lokal — faqat funksiya ichida yaratilgan va ko'rinadigan; global — funksiyadan tashqarida e'lon qilingan, butun dasturda ko'rinadigan
- [C] Ikkalasi bir xil, faqat nomlari boshqa
- [D] Python da lokal o'zgaruvchi mavjud emas

> **To'g'ri javob:** B
> **Tushuntirish:** Lokal — funksiya ichida yaratiladi, funksiya tugagach yo'q bo'ladi. Global — modul darajasida e'lon qilinadi, hamma joydan ko'rinadi. Funksiya ichida global o'zgaruvchini o'zgartirish uchun `global` kalit so'zi kerak.

---

## Savol 15

Quyidagi kodning natijasi nima?

```python
x = 10

def funksiya():
    x = 99
    print(x)

funksiya()
print(x)
```

- [A] `99`, `99`
- [B] `10`, `10`
- [C] `99`, `10`
- [D] Xato beradi

> **To'g'ri javob:** C
> **Tushuntirish:** Funksiya ichidagi `x = 99` — lokal o'zgaruvchi, global `x` ga ta'sir qilmaydi. `funksiya()` → lokal `x = 99` chiqadi. `print(x)` → global `x = 10` chiqadi.

---