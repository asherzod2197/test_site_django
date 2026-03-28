## Savol 1

Pozitsion argument (positional argument) nima?

- [A] Faqat raqamli qiymatlar
- [B] Funksiya chaqirishda tartib bo'yicha parametrlarga biriktirilgan qiymatlar
- [C] Kalit so'z bilan beriladigan argumentlar
- [D] Standart qiymatli argumentlar

> **To'g'ri javob:** B
> **Tushuntirish:** Pozitsion argumentlar ketma-ketlik bo'yicha biriktiriladi: `f(1, 2, 3)` — birinchi argument birinchi parametrga, ikkinchisi ikkinchisiga. Tartib muhim — o'zgartirsa natija o'zgarishi mumkin.

---

## Savol 2

Quyidagi kodning natijasi nima?

```python
def ayirma(a, b):
    return a - b

print(ayirma(10, 3))
print(ayirma(3, 10))
```

- [A] `7`, `7`
- [B] `7`, `-7`
- [C] `-7`, `7`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `ayirma(10, 3)` → `a=10, b=3` → `10-3=7`. `ayirma(3, 10)` → `a=3, b=10` → `3-10=-7`. Pozitsion argumentlarda tartib natijaga ta'sir qiladi.

---

## Savol 3

Kalit so'z argumenti (keyword argument) nima?

- [A] Faqat string qiymatlar
- [B] `parametr_nomi=qiymat` shaklida beriladigan argument — tartibdan mustaqil
- [C] Standart qiymatli parametrlar
- [D] Majburiy argumentlar

> **To'g'ri javob:** B
> **Tushuntirish:** `f(b=2, a=1)` — kalit so'z argumentlari nomi bilan biriktiriladi, tartib muhim emas. Pozitsion va kalit so'z aralashtirilganda pozitsionlar **oldin** kelishi shart.

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
def tanishtir(ism, yosh, shahar):
    print(f"{ism}, {yosh} yosh, {shahar}")

tanishtir(yosh=22, shahar="Samarqand", ism="Dilnoza")
```

- [A] Xato beradi — tartib noto'g'ri
- [B] `Dilnoza, 22 yosh, Samarqand`
- [C] `yosh, ism, shahar`
- [D] `22, Dilnoza, Samarqand`

> **To'g'ri javob:** B
> **Tushuntirish:** Kalit so'z argumentlarida tartib muhim emas — har biri nomi bilan mos parametrga birikadi: `ism="Dilnoza"`, `yosh=22`, `shahar="Samarqand"`.

---

## Savol 5

Pozitsion va kalit so'z argumentlari aralashtirilganda qaysi qoida amal qiladi?

- [A] Kalit so'z argumentlari har doim birinchi kelishi kerak
- [B] Pozitsion argumentlar kalit so'z argumentlaridan **oldin** kelishi shart
- [C] Tartib umuman muhim emas
- [D] Aralashtirib bo'lmaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `f(1, b=2)` — to'g'ri. `f(a=1, 2)` — **xato** `SyntaxError`. Pozitsion argumentlar avval, kalit so'z argumentlari keyin kelishi shart.

---

## Savol 6

Quyidagi kodning natijasi nima?

```python
def to'rtburchak(en, bo'y, rang="oq"):
    print(f"{en}x{bo'y}, rang: {rang}")

to'rtburchak(4, 5)
to'rtburchak(4, 5, "ko'k")
to'rtburchak(bo'y=3, en=6)
```

- [A] `4x5, rang: oq` / `4x5, rang: ko'k` / `6x3, rang: oq`
- [B] `4x5, rang: oq` / `4x5, rang: oq` / `6x3, rang: oq`
- [C] Xato beradi
- [D] `4x5, rang: oq` / `4x5, rang: ko'k` / `3x6, rang: oq`

> **To'g'ri javob:** A
> **Tushuntirish:** `to'rtburchak(4,5)` → `rang` standart `"oq"`. `to'rtburchak(4,5,"ko'k")` → `rang="ko'k"`. `to'rtburchak(bo'y=3, en=6)` → kalit so'z, `en=6, bo'y=3`, `rang` standart `"oq"`.

---

## Savol 7

Standart qiymatli parametr qayerda yozilishi kerak?

- [A] Istalgan joyda
- [B] Standart qiymatsiz parametrlardan **oldin**
- [C] Standart qiymatsiz parametrlardan **keyin**
- [D] Faqat bitta standart parametr bo'lishi mumkin

> **To'g'ri javob:** C
> **Tushuntirish:** `def f(a, b=2):` — to'g'ri. `def f(a=1, b):` — **noto'g'ri**, `SyntaxError`. Standart qiymatli parametrlar majburiy (standart qiymatsiz) parametrlardan keyin kelishi shart.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
def salomlash(ism, munosabat="Assalomu alaykum"):
    print(f"{munosabat}, {ism}!")

salomlash("Kamol")
salomlash("Jasur", "Salom")
salomlash(munosabat="Xayrli kun", ism="Malika")
```

- [A] `Assalomu alaykum, Kamol!` / `Salom, Jasur!` / `Xayrli kun, Malika!`
- [B] `Assalomu alaykum, Kamol!` / `Assalomu alaykum, Jasur!` / `Xayrli kun, Malika!`
- [C] Xato beradi
- [D] `Assalomu alaykum, Kamol!` / `Salom, Jasur!` / `Malika, Xayrli kun!`

> **To'g'ri javob:** A
> **Tushuntirish:** `salomlash("Kamol")` → `munosabat` standart. `salomlash("Jasur","Salom")` → standart ustiga yoziladi. `salomlash(munosabat=..., ism=...)` → kalit so'z, tartib muhim emas.

---

## Savol 9

Argument soni parametrlar sonidan kam bo'lsa nima bo'ladi?

- [A] Qolgan parametrlar `0` bo'ladi
- [B] Qolgan parametrlar `None` bo'ladi
- [C] `TypeError` — majburiy argument berilmadi
- [D] Funksiya ishlamaydi, lekin xato chiqmaydi

> **To'g'ri javob:** C
> **Tushuntirish:** Standart qiymatsiz parametrga argument berilmasa `TypeError: f() missing required positional argument` xatosi chiqadi. Faqat standart qiymatli parametrlar argumentsiz qolishi mumkin.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
def hisob(a, b, amal="+"):
    if amal == "+":
        return a + b
    elif amal == "-":
        return a - b
    elif amal == "*":
        return a * b
    else:
        return "Noma'lum amal"

print(hisob(10, 5))
print(hisob(10, 5, "-"))
print(hisob(10, 5, amal="*"))
print(hisob(10, 5, "/"))
```

- [A] `15`, `5`, `50`, `2`
- [B] `15`, `5`, `50`, `"Noma'lum amal"`
- [C] `15`, `5`, `15`, `"Noma'lum amal"`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `hisob(10,5)` → `"+"` standart → `15`. `hisob(10,5,"-")` → `5`. `hisob(10,5,amal="*")` → `50`. `hisob(10,5,"/")` → `else` → `"Noma'lum amal"`.

---

## Savol 11

Quyidagi kodning natijasi nima?

```python
def chegirma(narx, foiz=10):
    chegirma_miqdori = narx * foiz / 100
    return narx - chegirma_miqdori

print(chegirma(50000))
print(chegirma(50000, 20))
print(chegirma(foiz=15, narx=80000))
```

- [A] `45000.0`, `40000.0`, `68000.0`
- [B] `45000`, `40000`, `68000`
- [C] `50000`, `50000`, `80000`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `chegirma(50000)` → `foiz=10` → `50000 - 5000 = 45000.0`. `chegirma(50000,20)` → `50000 - 10000 = 40000.0`. `chegirma(foiz=15, narx=80000)` → `80000 - 12000 = 68000.0`.

---

## Savol 12

Funksiyaga argument sifatida boshqa funksiya natijasini berish mumkinmi?

- [A] Yo'q, faqat o'zgaruvchi beriladi
- [B] Ha, funksiya chaqiruvi natijasi (qaytargan qiymati) argument sifatida beriladi
- [C] Faqat `int` qaytaruvchi funksiyalar uchun
- [D] Faqat `print()` uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `f(g(x))` — avval `g(x)` ishlaydi, natijasi `f()` ga argument sifatida beriladi. Masalan: `print(len("salom"))` — `len()` natijasi `print()` ga beriladi.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
def kvadrat(x):
    return x * x

def ikki_barobar(x):
    return x * 2

print(kvadrat(ikki_barobar(3)))
print(ikki_barobar(kvadrat(4)))
```

- [A] `36`, `32`
- [B] `12`, `32`
- [C] `36`, `16`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `ikki_barobar(3)` → `6`. `kvadrat(6)` → `36`. `kvadrat(4)` → `16`. `ikki_barobar(16)` → `32`.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
def f(x, y, z=0):
    return x + y + z

a = f(1, 2)
b = f(1, 2, 3)
c = f(1, y=2)
d = f(z=5, x=1, y=2)

print(a, b, c, d)
```

- [A] `3`, `6`, `3`, `8`
- [B] `3 6 3 8`
- [C] `0 6 3 8`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `f(1,2)` → `z=0` standart → `3`. `f(1,2,3)` → `6`. `f(1,y=2)` → `z=0` → `3`. `f(z=5,x=1,y=2)` → kalit so'z → `1+2+5=8`. Barchasi `print` → `3 6 3 8`.

---

## Savol 15

Quyidagi to'liq kodning natijasi nima?

```python
def baholash(ism, ball, chegara=60, a'lo=90):
    if ball >= a'lo:
        holat = "A'lo"
    elif ball >= chegara:
        holat = "O'tdi"
    else:
        holat = "O'tmadi"
    return f"{ism}: {holat} ({ball})"

print(baholash("Ali", 95))
print(baholash("Vali", 72))
print(baholash("Gali", 45))
print(baholash("Zulfiya", 85, a'lo=80))
```

- [A] `Ali: A'lo (95)` / `Vali: O'tdi (72)` / `Gali: O'tmadi (45)` / `Zulfiya: O'tdi (85)`
- [B] `Ali: A'lo (95)` / `Vali: O'tdi (72)` / `Gali: O'tmadi (45)` / `Zulfiya: A'lo (85)`
- [C] `Ali: A'lo (95)` / `Vali: O'tmadi (72)` / `Gali: O'tmadi (45)` / `Zulfiya: A'lo (85)`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `baholash("Ali",95)` → `95>=90` → `A'lo`. `baholash("Vali",72)` → `72>=60` → `O'tdi`. `baholash("Gali",45)` → `45<60` → `O'tmadi`. `baholash("Zulfiya",85,a'lo=80)` → `a'lo=80`, `85>=80` → `A'lo`.

---