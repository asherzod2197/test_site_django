## Savol 1

Dictionary (lug'at) nima?

- [A] Tartibli, o'zgarmas elementlar to'plami
- [B] Kalit-qiymat (key-value) juftliklarini saqlaydigan o'zgaruvchan to'plam
- [C] Faqat matn saqlaydi gan maxsus tuzilma
- [D] Listning boshqa nomi

> **To'g'ri javob:** B
> **Tushuntirish:** Dictionary — kalit-qiymat (key: value) juftliklarini saqlaydigan o'zgaruvchan (mutable) ma'lumot turi. Har bir kalitga mos bitta qiymat bo'ladi. `{}` yoki `dict()` bilan yaratiladi.

---

## Savol 2

Dictionary qanday yaratiladi?

- [A] `d = [kalit: qiymat]`
- [B] `d = (kalit: qiymat)`
- [C] `d = {kalit: qiymat}`
- [D] `d = <kalit: qiymat>`

> **To'g'ri javob:** C
> **Tushuntirish:** Dictionary jingalak qavslar `{}` ichida `kalit: qiymat` juftliklari vergul bilan yoziladi. Masalan: `{"ism": "Ali", "yosh": 25}`. `dict()` konstruktori ham ishlatiladi.

---

## Savol 3

Quyidagi kodning natijasi nima?

```python
d = {"ism": "Sardor", "yosh": 22, "shahar": "Toshkent"}
print(d["ism"])
print(d["yosh"])
```

- [A] `"Sardor"`, `"Toshkent"`
- [B] `"Sardor"`, `22`
- [C] `22`, `"Toshkent"`
- [D] `KeyError`

> **To'g'ri javob:** B
> **Tushuntirish:** `d["ism"]` — `"ism"` kalitiga mos qiymat: `"Sardor"`. `d["yosh"]` — `"yosh"` kalitiga mos qiymat: `22`.

---

## Savol 4

Dictionary kaliti (key) qanday bo'lishi kerak?

- [A] Faqat string bo'lishi kerak
- [B] Faqat raqam bo'lishi kerak
- [C] O'zgarmas (immutable) bo'lishi kerak — string, int, tuple va boshqalar
- [D] Istalgan turdagi bo'lishi mumkin

> **To'g'ri javob:** C
> **Tushuntirish:** Kalit hashable, ya'ni o'zgarmas bo'lishi shart. `str`, `int`, `float`, `tuple` — kalit bo'la oladi. `list`, `dict`, `set` — mutable, shuning uchun kalit bo'la olmaydi → `TypeError`.

---

## Savol 5

Quyidagi kodda qaysi kalit xato beradi?

```python
d = {}
d["ism"] = "Ali"       # 1
d[42] = "raqam"        # 2
d[(1, 2)] = "tuple"    # 3
d[[1, 2]] = "list"     # 4
```

- [A] `1` — string kalit bo'la olmaydi
- [B] `2` — int kalit bo'la olmaydi
- [C] `3` — tuple kalit bo'la olmaydi
- [D] `4` — list kalit bo'la olmaydi

> **To'g'ri javob:** D
> **Tushuntirish:** `list` mutable → hashable emas → `TypeError: unhashable type: 'list'`. String, int, tuple — hammasi hashable, shuning uchun kalit bo'la oladi.

---

## Savol 6

Dictionary da mavjud bo'lmagan kalitga murojaat qilsa nima bo'ladi?

- [A] `None` qaytaradi
- [B] `0` qaytaradi
- [C] `KeyError` beradi
- [D] Bo'sh string qaytaradi

> **To'g'ri javob:** C
> **Tushuntirish:** `d["mavjud_emas"]` → `KeyError`. Buning oldini olish uchun `d.get("kalit")` ishlatiladi — kalit topilmasa `None` (yoki ko'rsatilgan standart qiymat) qaytaradi.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
d = {"a": 1, "b": 2, "c": 3}
print(d.get("b"))
print(d.get("z"))
print(d.get("z", "topilmadi"))
```

- [A] `2`, `KeyError`, `"topilmadi"`
- [B] `2`, `None`, `"topilmadi"`
- [C] `2`, `0`, `"topilmadi"`
- [D] `2`, `None`, `None`

> **To'g'ri javob:** B
> **Tushuntirish:** `get("b")` → `2`. `get("z")` — kalit yo'q → `None`. `get("z", "topilmadi")` — kalit yo'q, standart qiymat → `"topilmadi"`.

---

## Savol 8

Dictionary ga yangi kalit-qiymat qo'shish va mavjudini yangilash qanday?

- [A] `d.add(kalit, qiymat)`
- [B] `d.insert(kalit, qiymat)`
- [C] `d[kalit] = qiymat`
- [D] `d.append(kalit, qiymat)`

> **To'g'ri javob:** C
> **Tushuntirish:** `d[kalit] = qiymat` — agar kalit mavjud bo'lmasa yangi qo'shadi, mavjud bo'lsa qiymatini yangilaydi. Bu eng oddiy va keng tarqalgan usul.

---

## Savol 9

Quyidagi kodning natijasi nima?

```python
d = {"ism": "Ali", "yosh": 20}
d["yosh"] = 21
d["shahar"] = "Buxoro"
print(d)
```

- [A] `{"ism": "Ali", "yosh": 20}`
- [B] `{"ism": "Ali", "yosh": 21}`
- [C] `{"ism": "Ali", "yosh": 21, "shahar": "Buxoro"}`
- [D] `KeyError`

> **To'g'ri javob:** C
> **Tushuntirish:** `d["yosh"] = 21` — mavjud kalit yangilanadi. `d["shahar"] = "Buxoro"` — yangi kalit qo'shiladi. Natija: `{"ism": "Ali", "yosh": 21, "shahar": "Buxoro"}`.

---

## Savol 10

`in` operatori dictionary da qanday ishlaydi?

- [A] Qiymatlarni tekshiradi
- [B] Kalitlarni tekshiradi
- [C] Ham kalit, ham qiymatni tekshiradi
- [D] Faqat raqamli kalitlar uchun ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `"kalit" in d` — faqat **kalitlar** orasidan qidiradi. Qiymatlarni tekshirish uchun `"qiymat" in d.values()` ishlatiladi.

---

## Savol 11

Quyidagi kodning natijasi nima?

```python
d = {"a": 1, "b": 2, "c": 3}
print("a" in d)
print(1 in d)
print(1 in d.values())
```

- [A] `True`, `True`, `True`
- [B] `True`, `False`, `True`
- [C] `True`, `True`, `False`
- [D] `False`, `False`, `True`

> **To'g'ri javob:** B
> **Tushuntirish:** `"a" in d` — kalit qidiruvi → `True`. `1 in d` — `1` kalit emas → `False`. `1 in d.values()` — qiymatlar orasida → `True`.

---

## Savol 12

`keys()`, `values()`, `items()` metodlari nima qaytaradi?

- [A] Uchala ham list qaytaradi
- [B] `keys()` — kalitlar, `values()` — qiymatlar, `items()` — `(kalit, qiymat)` juftliklari
- [C] `keys()` — qiymatlar, `values()` — kalitlar, `items()` — list
- [D] Uchala ham tuple qaytaradi

> **To'g'ri javob:** B
> **Tushuntirish:** `d.keys()` — barcha kalitlar (`dict_keys`). `d.values()` — barcha qiymatlar (`dict_values`). `d.items()` — `(kalit, qiymat)` tuple juftliklari (`dict_items`). `list()` bilan listga aylantiriladi.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
d = {"nom": "Python", "versiya": 3, "ochiq": True}
for kalit, qiymat in d.items():
    print(f"{kalit}: {qiymat}")
```

- [A] Faqat kalitlar chiqadi
- [B] Faqat qiymatlar chiqadi
- [C] `nom: Python` / `versiya: 3` / `ochiq: True`
- [D] `KeyError`

> **To'g'ri javob:** C
> **Tushuntirish:** `d.items()` — `(kalit, qiymat)` juftliklarini qaytaradi. `for kalit, qiymat in d.items()` — unpackinig orqali har juftlik chiqariladi.

---

## Savol 14

`del` kalit so'zi dictionary da qanday ishlatiladi?

- [A] Butun dictionaryni o'chiradi
- [B] Ko'rsatilgan kalitni va unga mos qiymatni o'chiradi
- [C] Faqat qiymatni `None` ga o'zgartiradi
- [D] Listdagi kabi indeks bo'yicha o'chiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `del d["kalit"]` — o'sha kalit va uning qiymatini dictionarydan butunlay o'chiradi. Kalit mavjud bo'lmasa `KeyError`. `d.pop("kalit")` ham xuddi shunday, lekin qiymatni qaytaradi.

---

## Savol 15

Quyidagi kodning natijasi nima?

```python
d = {"a": 1, "b": 2, "c": 3, "d": 4}
del d["b"]
print(len(d))
print("b" in d)
```

- [A] `4`, `True`
- [B] `3`, `False`
- [C] `3`, `True`
- [D] `KeyError`

> **To'g'ri javob:** B
> **Tushuntirish:** `del d["b"]` — `"b"` kaliti o'chiriladi. `len(d)` → `3`. `"b" in d` → `False`.

---

## Savol 16

Dictionary da kalitlar takrorlanishi mumkinmi?

- [A] Ha, bir kalit bir necha qiymatga ega bo'la oladi
- [B] Yo'q, kalitlar noyob bo'lishi shart — bir xil kalit yozilsa, oxirgi qiymat saqlanadi
- [C] Faqat string kalitlar takrorlanishi mumkin
- [D] Python avtomatik xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** Dictionary da har kalit noyob. Bir xil kalit ikki marta yozilsa, ikkinchisi birinchisini **ustiga yozadi**. `{"a": 1, "a": 2}` → `{"a": 2}`.

---

## Savol 17

Quyidagi kodning natijasi nima?

```python
d = {"x": 10, "y": 20, "x": 30, "z": 40}
print(len(d))
print(d["x"])
```

- [A] `4`, `10`
- [B] `3`, `30`
- [C] `4`, `30`
- [D] `KeyError`

> **To'g'ri javob:** B
> **Tushuntirish:** `"x"` kaliti ikki marta — oxirgisi (`30`) saqlanadi. Noyob kalitlar: `"x"`, `"y"`, `"z"` → `len = 3`. `d["x"]` → `30`.

---

## Savol 18

`update()` metodi nima qiladi?

- [A] Dictionaryni tartiblab qaytaradi
- [B] Boshqa dictionary yoki kalit-qiymat juftliklarini qo'shadi yoki mavjudlarini yangilaydi
- [C] Faqat mavjud kalitlarni yangilaydi, yangi qo'shmaydi
- [D] Dictionary ni tozalaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `d.update(boshqa_dict)` — `boshqa_dict` dagi kalitlar mavjud bo'lsa yangilaydi, bo'lmasa qo'shadi. `None` qaytaradi (in-place o'zgartiradi).

---

## Savol 19

Quyidagi kodning natijasi nima?

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
d1.update(d2)
print(d1)
print(d2)
```

- [A] `{"a":1, "b":2, "c":3}`, `{"b":99, "c":3}`
- [B] `{"a":1, "b":99, "c":3}`, `{"b":99, "c":3}`
- [C] `{"a":1, "b":99, "c":3}`, `{}`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `update(d2)` — `"b"` mavjud → `99` bilan yangilanadi. `"c"` yangi → qo'shiladi. `d1` → `{"a":1, "b":99, "c":3}`. `d2` o'zgarmaydi.

---

## Savol 20

Quyidagi to'liq kodning natijasi nima?

```python
talaba = {
    "ism": "Nilufar",
    "yoshlar": 20,
    "fanlar": ["Matematika", "Fizika"]
}

talaba["ball"] = 95
talaba["yoshlar"] = 21
del talaba["fanlar"]

print(len(talaba))
print("fanlar" in talaba)
print(talaba["yoshlar"])
```

- [A] `4`, `True`, `20`
- [B] `3`, `False`, `21`
- [C] `3`, `True`, `21`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `ball` qo'shiladi → 4 ta. `yoshlar` yangilanadi → `21`. `fanlar` o'chiriladi → 3 ta. `len` → `3`. `"fanlar" in talaba` → `False`. `talaba["yoshlar"]` → `21`.

---