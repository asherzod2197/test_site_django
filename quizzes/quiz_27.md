## Savol 1

`get()` metodi `d[kalit]` dan qanday farq qiladi?

- [A] Hech qanday farq yo'q
- [B] `get()` kalit topilmasa `KeyError` o'rniga `None` (yoki standart qiymat) qaytaradi
- [C] `get()` faqat string kalitlar uchun ishlaydi
- [D] `d[kalit]` tezroq ishlaydi va har doim afzal

> **To'g'ri javob:** B
> **Tushuntirish:** `d["kalit"]` — kalit yo'q bo'lsa `KeyError`. `d.get("kalit")` — kalit yo'q bo'lsa `None`. `d.get("kalit", "standart")` — kalit yo'q bo'lsa `"standart"` qaytaradi. Xavfsiz murojaat uchun `get()` afzal.

---

## Savol 2

Quyidagi kodning natijasi nima?

```python
d = {"ism": "Kamola", "yosh": 19}
print(d.get("ism"))
print(d.get("manzil"))
print(d.get("manzil", "ko'rsatilmagan"))
```

- [A] `"Kamola"`, `KeyError`, `"ko'rsatilmagan"`
- [B] `"Kamola"`, `None`, `"ko'rsatilmagan"`
- [C] `"Kamola"`, `None`, `None`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `get("ism")` → `"Kamola"`. `get("manzil")` — yo'q → `None`. `get("manzil", "ko'rsatilmagan")` — yo'q, standart qiymat → `"ko'rsatilmagan"`.

---

## Savol 3

`keys()` metodi nima qaytaradi?

- [A] Barcha qiymatlarni list ko'rinishida
- [B] Barcha kalitlarni `dict_keys` obyekti sifatida
- [C] Kalit-qiymat juftliklarini
- [D] Kalitlar sonini

> **To'g'ri javob:** B
> **Tushuntirish:** `d.keys()` — `dict_keys` obyekti qaytaradi. `list(d.keys())` bilan listga aylantiriladi. Dictionary o'zgarganda `dict_keys` ham avtomatik yangilanadi (dynamic view).

---

## Savol 4

Quyidagi kodning natijasi nima?

```python
d = {"a": 1, "b": 2, "c": 3}
kalitlar = list(d.keys())
print(kalitlar)
print(type(d.keys()))
```

- [A] `["a", "b", "c"]`, `<class 'list'>`
- [B] `["a", "b", "c"]`, `<class 'dict_keys'>`
- [C] `("a", "b", "c")`, `<class 'tuple'>`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `list(d.keys())` → `["a", "b", "c"]`. Lekin `d.keys()` ning o'z turi `<class 'dict_keys'>` — bu list emas, maxsus ko'rinish (view) obyekti.

---

## Savol 5

`values()` metodi haqida qaysi fikr to'g'ri?

- [A] Faqat noyob qiymatlarni qaytaradi
- [B] Barcha qiymatlarni `dict_values` obyekti sifatida qaytaradi — takroriy qiymatlar ham kiradi
- [C] Qiymatlarni tartiblangan holda qaytaradi
- [D] Faqat raqamli qiymatlarni qaytaradi

> **To'g'ri javob:** B
> **Tushuntirish:** `d.values()` — barcha qiymatlarni qaytaradi, takroriy bo'lsa ham. `dict_values` — dinamik ko'rinish, dictionary o'zgarganda u ham yangilanadi.

---

## Savol 6

Quyidagi kodning natijasi nima?

```python
d = {"x": 5, "y": 5, "z": 10}
qiymatlar = list(d.values())
print(qiymatlar)
print(qiymatlar.count(5))
```

- [A] `[5, 10]`, `1`
- [B] `[5, 5, 10]`, `2`
- [C] `[5, 5, 10]`, `1`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `d.values()` — takroriy ham bo'lsa hammasi chiqadi: `[5, 5, 10]`. `count(5)` → `2` (ikkita `5` bor).

---

## Savol 7

`items()` metodi nima qaytaradi va qanday ishlatiladi?

- [A] Faqat kalitlarni qaytaradi
- [B] `(kalit, qiymat)` tuple juftliklarini `dict_items` sifatida qaytaradi — `for` da unpacking bilan qulay
- [C] Qiymatlarni tartiblangan holda qaytaradi
- [D] Dictionary ni listga aylantiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `d.items()` → `dict_items([("a",1), ("b",2)])`. `for k, v in d.items():` — kalit va qiymatga birgalikda murojaat qilishning eng qulay usuli.

---

## Savol 8

Quyidagi kodning natijasi nima?

```python
d = {"Python": 1991, "Java": 1995, "C": 1972}
for til, yil in d.items():
    if yil < 1990:
        print(til)
```

- [A] `Python`, `Java`
- [B] `C`
- [C] `Python`, `Java`, `C`
- [D] Hech narsa chiqmaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `items()` — `(til, yil)` juftliklarini beradi. `1991 < 1990` → yo'q. `1995 < 1990` → yo'q. `1972 < 1990` → ha → `"C"` chiqadi.

---

## Savol 9

`update()` metodi nima qiladi?

- [A] Faqat mavjud kalitlarni yangilaydi, yangi qo'shmaydi
- [B] Faqat yangi kalitlarni qo'shadi, mavjudlarini o'zgartirmaydi
- [C] Boshqa dictionarydan ham kalitlarni qo'shadi, ham mavjudlarini yangilaydi
- [D] Yangi dictionary qaytaradi

> **To'g'ri javob:** C
> **Tushuntirish:** `d.update(boshqa)` — `boshqa` dagi kalitlar mavjud bo'lsa **yangilaydi**, bo'lmasa **qo'shadi**. In-place o'zgartiradi, `None` qaytaradi. `boshqa` dictionary, juftliklar listi yoki kalit=qiymat argumentlar bo'lishi mumkin.

---

## Savol 10

Quyidagi kodning natijasi nima?

```python
d = {"a": 1, "b": 2, "c": 3}
d.update({"b": 20, "d": 4})
d.update(e=5)
print(len(d))
print(d["b"])
print(d["e"])
```

- [A] `5`, `2`, `5`
- [B] `5`, `20`, `5`
- [C] `4`, `20`, `5`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `update({"b":20, "d":4})` → `"b"` yangilanadi, `"d"` qo'shiladi. `update(e=5)` → `"e"` qo'shiladi. Jami: `a,b,c,d,e` → `5`. `d["b"]` → `20`. `d["e"]` → `5`.

---

## Savol 11

`pop()` metodi qanday ishlaydi?

- [A] Oxirgi qo'shilgan elementni o'chirib qaytaradi
- [B] Ko'rsatilgan kalitni o'chirib, uning qiymatini qaytaradi
- [C] Tasodifiy elementni o'chiradi
- [D] Barcha elementlarni o'chiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `d.pop("kalit")` — kalitni o'chirib, qiymatini qaytaradi. `d.pop("kalit", standart)` — kalit yo'q bo'lsa `KeyError` o'rniga standart qiymat qaytaradi.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
d = {"a": 10, "b": 20, "c": 30}
olingan = d.pop("b")
yo_q = d.pop("z", "topilmadi")
print(olingan)
print(yo_q)
print(d)
```

- [A] `20`, `KeyError`, `{"a":10, "c":30}`
- [B] `20`, `"topilmadi"`, `{"a":10, "c":30}`
- [C] `20`, `None`, `{"a":10, "c":30}`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `pop("b")` → `20`, `"b"` o'chiriladi. `pop("z", "topilmadi")` → `"z"` yo'q, standart: `"topilmadi"`. `d` → `{"a":10, "c":30}`.

---

## Savol 13

`popitem()` metodi `pop()` dan qanday farq qiladi?

- [A] `popitem()` birinchi elementni o'chiradi
- [B] `popitem()` kalit ko'rsatmasdan eng oxirgi qo'shilgan `(kalit, qiymat)` juftligini o'chirib qaytaradi
- [C] `popitem()` tasodifiy elementni o'chiradi
- [D] `popitem()` faqat bo'sh dictionaryda ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `d.popitem()` — Python 3.7+ da eng oxirgi qo'shilgan `(kalit, qiymat)` tuple ni o'chirib qaytaradi. Bo'sh dictionaryda `KeyError` beradi. Kalit ko'rsatish shart emas.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
d = {"x": 1, "y": 2, "z": 3}
juftlik = d.popitem()
print(juftlik)
print(len(d))
```

- [A] `("x", 1)`, `2`
- [B] `("z", 3)`, `2`
- [C] `("y", 2)`, `2`
- [D] `{"x":1, "y":2}`, `2`

> **To'g'ri javob:** B
> **Tushuntirish:** `popitem()` Python 3.7+ da oxirgi qo'shilgan elementni oladi: `("z", 3)`. `len(d)` → `2` qoladi.

---

## Savol 15

`setdefault()` metodi qanday ishlaydi?

- [A] Barcha qiymatlarni standart qiymatga o'zgartiradi
- [B] Kalit mavjud bo'lsa qiymatini qaytaradi, bo'lmasa kalitni standart qiymat bilan qo'shib qaytaradi
- [C] Faqat bo'sh dictionarylarda ishlaydi
- [D] `get()` ning boshqa nomi

> **To'g'ri javob:** B
> **Tushuntirish:** `d.setdefault("kalit", standart)` — kalit bor bo'lsa mavjud qiymatni qaytaradi (o'zgartirmaydi). Yo'q bo'lsa `standart` qiymat bilan qo'shib, uni qaytaradi. `get()` dan farqi — yo'q bo'lsa dictionaryga qo'shadi.

---

## Savol 16

Quyidagi kodning natijasi nima?

```python
d = {"a": 1, "b": 2}
print(d.setdefault("a", 99))
print(d.setdefault("c", 99))
print(d)
```

- [A] `99`, `99`, `{"a":99, "b":2, "c":99}`
- [B] `1`, `99`, `{"a":1, "b":2, "c":99}`
- [C] `1`, `None`, `{"a":1, "b":2}`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `setdefault("a", 99)` — `"a"` mavjud, qiymatini qaytaradi: `1`. O'zgartirmaydi. `setdefault("c", 99)` — `"c"` yo'q, qo'shadi va `99` qaytaradi. `d` → `{"a":1, "b":2, "c":99}`.

---

## Savol 17

`clear()` metodi qanday ishlaydi va `del d` dan farqi nima?

- [A] `clear()` va `del d` bir xil ishlaydi
- [B] `clear()` — barcha elementlarni o'chirib bo'sh dictionary qoldiradi; `del d` — o'zgaruvchini butunlay o'chiradi
- [C] `clear()` — o'zgaruvchini o'chiradi, `del d` — bo'sh qoldiradi
- [D] `clear()` faqat katta dictionarylarda ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `d.clear()` → `d = {}` (bo'sh, lekin `d` o'zgaruvchisi saqlanadi). `del d` → `d` o'zgaruvchisi yo'q qilinadi, keyinchalik `d` ga murojaat `NameError` beradi.

---

## Savol 18

Quyidagi kodning natijasi nima?

```python
d = {"a": 1, "b": 2, "c": 3}
d.clear()
print(d)
print(type(d))
print(len(d))
```

- [A] `None`, `<class 'NoneType'>`, `0`
- [B] `{}`, `<class 'dict'>`, `0`
- [C] Xato beradi
- [D] `{"a":1, "b":2, "c":3}`, `<class 'dict'>`, `3`

> **To'g'ri javob:** B
> **Tushuntirish:** `clear()` barcha elementlarni o'chiradi, `d` bo'sh dictionary bo'lib qoladi: `{}`. `type` → `dict`. `len` → `0`.

---

## Savol 19

`copy()` metodi qanday nusxa yaratadi?

- [A] Chuqur nusxa (deep copy) — ichki dictionary lar ham yangi yaratiladi
- [B] Sirtqi nusxa (shallow copy) — ichki o'zgaruvchan obyektlar baham ko'riladi
- [C] Reference (havola) qaytaradi
- [D] Faqat kalitlarni nusxalaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `d.copy()` — sirtqi nusxa. Oddiy qiymatlar mustaqil, ichki list yoki dict lar baham ko'riladi. To'liq mustaqil nusxa uchun `copy.deepcopy(d)` kerak.

---

## Savol 20

Quyidagi kodning natijasi nima?

```python
asl = {"a": 1, "b": 2}
nusxa = asl.copy()
nusxa["c"] = 3
asl["a"] = 99
print(asl)
print(nusxa)
```

- [A] `{"a":99, "b":2, "c":3}`, `{"a":99, "b":2, "c":3}`
- [B] `{"a":99, "b":2}`, `{"a":1, "b":2, "c":3}`
- [C] `{"a":1, "b":2}`, `{"a":1, "b":2, "c":3}`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `copy()` mustaqil nusxa. `nusxa["c"]=3` faqat nusxaga qo'shiladi. `asl["a"]=99` faqat asliga ta'sir qiladi. Ular mustaqil.

---

## Savol 21

Qaysi metod yordamida dictionary da kalit yo'q bo'lsa xato chiqarmay ishlash mumkin?

- [A] `d[kalit]`
- [B] `d.keys()`
- [C] `d.get(kalit, standart)`
- [D] `d.values()`

> **To'g'ri javob:** C
> **Tushuntirish:** `d.get(kalit, standart)` — kalit topilmasa `KeyError` o'rniga standart qiymat qaytaradi. Bu xavfsiz murojaat usuli. `if kalit in d:` tekshiruvi ham ishlatiladi.

---

## Savol 22

`pop()` va `popitem()` metodlarining farqi nima?

- [A] Hech qanday farq yo'q
- [B] `pop(kalit)` — aniq kalit bo'yicha o'chiradi; `popitem()` — oxirgi qo'shilgan juftlikni o'chiradi
- [C] `popitem()` aniq kalit, `pop()` oxirgi element uchun
- [D] `pop()` qaytarmaydi, `popitem()` qaytaradi

> **To'g'ri javob:** B
> **Tushuntirish:** `pop("kalit")` — ko'rsatilgan kalitni o'chirib, faqat **qiymatni** qaytaradi. `popitem()` — kalit ko'rsatmasdan oxirgi `(kalit, qiymat)` **juftligini** o'chirib qaytaradi.

---

## Savol 23

Quyidagi kodning natijasi nima?

```python
d = {"ism": "Bobur", "yosh": 23, "kasb": "dasturchi"}

for kalit in list(d.keys()):
    if kalit != "ism":
        d.pop(kalit)

print(d)
```

- [A] `{}`
- [B] `{"ism": "Bobur"}`
- [C] `{"yosh": 23, "kasb": "dasturchi"}`
- [D] `RuntimeError`

> **To'g'ri javob:** B
> **Tushuntirish:** `list(d.keys())` — kalitlar nusxalanadi (tsikl davomida dictionaryni o'zgartirish xavfsiz bo'lsin). `"ism" != "ism"` → yo'q. `"yosh"` va `"kasb"` o'chiriladi. `d` → `{"ism": "Bobur"}`.

---

## Savol 24

`setdefault()` qaysi holatda ayniqsa foydali?

- [A] Dictionary ni tartiblashda
- [B] Kalit mavjudligini oldindan tekshirmay, yo'q bo'lsa darhol qo'shib davom etishda
- [C] Faqat raqamli qiymatlar bilan ishlashda
- [D] Dictionary ni nusxalashda

> **To'g'ri javob:** B
> **Tushuntirish:** `setdefault()` tekshiruv va qo'shishni bir vaqtda bajaradi. Masalan, har bir so'zning uchrash sonini sanashda: `d.setdefault(so'z, 0)` — so'z yo'q bo'lsa `0` bilan qo'shadi. `if so'z not in d: d[so'z] = 0` ni bir qatorda yozish.

---

## Savol 25

Quyidagi to'liq kodning natijasi nima?

```python
d = {"a": 10, "b": 20, "c": 30, "d": 40}

d.update({"a": 99, "e": 50})
d.setdefault("f", 60)
d.setdefault("a", 0)

olingan = d.pop("b")
juftlik = d.popitem()

print(len(d))
print(d["a"])
print(olingan)
```

- [A] `4`, `99`, `20`
- [B] `3`, `99`, `20`
- [C] `4`, `10`, `20`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `update` → `"a"=99`, `"e"=50` qo'shiladi → 5 ta. `setdefault("f",60)` → qo'shiladi → 6 ta. `setdefault("a",0)` → `"a"` bor, o'zgarmaydi. `pop("b")` → `20` qaytaradi, o'chiriladi → 5 ta. `popitem()` → oxirgi `("f",60)` olinadi → 4 ta. `len` → `4`. `d["a"]` → `99`. `olingan` → `20`.

---