## Savol 1

To'g'ridan-to'g'ri (literal) usulda dictionary qanday yaratiladi?

- [A] `d = [kalit: qiymat]`
- [B] `d = {kalit: qiymat}`
- [C] `d = (kalit: qiymat)`
- [D] `d = kalit: qiymat`

> **To'g'ri javob:** B
> **Tushuntirish:** Jingalak qavslar `{}` ichida `kalit: qiymat` juftliklari vergul bilan yoziladi. Masalan: `d = {"ism": "Ali", "yosh": 25}`. Bu eng keng tarqalgan usul.

---

## Savol 2

Bo'sh dictionary qanday yaratiladi?

- [A] Faqat `{}` bilan
- [B] Faqat `dict()` bilan
- [C] `{}` yoki `dict()` — ikkalasi ham bo'sh dictionary yaratadi
- [D] `{:}` bilan

> **To'g'ri javob:** C
> **Tushuntirish:** `d = {}` va `d = dict()` — ikkalasi ham bo'sh dictionary yaratadi. `{}` yozish osonroq, `dict()` konstruktor sifatida ishlaydi. `{:}` esa sintaksis xato.

---

## Savol 3

Quyidagi kodning natijasi nima?

```python
d = {}
print(type(d))
print(len(d))
```

- [A] `<class 'set'>`, `0`
- [B] `<class 'dict'>`, `0`
- [C] `<class 'dict'>`, `1`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `{}` — bo'sh dictionary (set emas!). `type(d)` → `<class 'dict'>`. `len(d)` → `0`. Bo'sh set yaratish uchun `set()` ishlatiladi, `{}` emas.

---

## Savol 4

`dict()` konstruktori qanday ishlaydi?

- [A] Faqat bo'sh dictionary yaratadi
- [B] Kalit-qiymat argumentlari yoki boshqa iterabldan dictionary yaratadi
- [C] Faqat listdan dictionary yaratadi
- [D] Faqat tuple dan dictionary yaratadi

> **To'g'ri javob:** B
> **Tushuntirish:** `dict()` bir necha usulda ishlaydi: `dict(a=1, b=2)` — kalit-argument sifatida; `dict([("a",1)])` — juftliklar listidan; `dict(zip(kalitlar, qiymatlar))` — zip orqali.

---

## Savol 5

Quyidagi kodning natijasi nima?

```python
d = dict(ism="Sardor", yosh=22, shahar="Navoiy")
print(d["ism"])
print(d["yosh"])
```

- [A] Xato beradi, `dict()` da `=` ishlatilmaydi
- [B] `"Sardor"`, `22`
- [C] `"ism"`, `"yosh"`
- [D] `None`, `None`

> **To'g'ri javob:** B
> **Tushuntirish:** `dict(kalit=qiymat)` — kalitlar **string** sifatida saqlanadi. `ism="Sardor"` → `{"ism": "Sardor"}`. `d["ism"]` → `"Sardor"`. Diqqat: bu usulda kalit faqat oddiy identifikator bo'lishi mumkin.

---

## Savol 6

Juftliklar ro'yxatidan dictionary qanday yaratiladi?

- [A] `dict({(k,v)})`
- [B] `dict([(k1,v1), (k2,v2)])`
- [C] `dict[[k1,v1], [k2,v2]]`
- [D] `{[(k1,v1), (k2,v2)]}`

> **To'g'ri javob:** B
> **Tushuntirish:** `dict()` ga `(kalit, qiymat)` tuplelar listini berish mumkin. Masalan: `dict([("a", 1), ("b", 2)])` → `{"a": 1, "b": 2}`.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
juftliklar = [("olma", 500), ("banan", 300), ("gilos", 800)]
narxlar = dict(juftliklar)
print(narxlar["banan"])
print(len(narxlar))
```

- [A] `500`, `3`
- [B] `300`, `3`
- [C] `300`, `2`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `dict(juftliklar)` — `(kalit, qiymat)` juftliklardan dictionary yaratadi. `narxlar["banan"]` → `300`. `len` → `3`.

---

## Savol 8

`zip()` yordamida dictionary qanday yaratiladi?

- [A] `{zip(kalitlar, qiymatlar)}`
- [B] `dict(zip(kalitlar, qiymatlar))`
- [C] `zip(kalitlar, qiymatlar).to_dict()`
- [D] `dict.zip(kalitlar, qiymatlar)`

> **To'g'ri javob:** B
> **Tushuntirish:** `zip(kalitlar, qiymatlar)` — ikkala listni juftlab beradi. `dict()` uni dictionary ga aylantiradi. Masalan: `dict(zip(["a","b"], [1,2]))` → `{"a":1, "b":2}`.

---

## Savol 9

Quyidagi kodning natijasi nima?

```python
fanlar = ["Matematika", "Fizika", "Kimyo"]
baholar = [90, 85, 78]
d = dict(zip(fanlar, baholar))
print(d["Fizika"])
print("Kimyo" in d)
```

- [A] `90`, `True`
- [B] `85`, `True`
- [C] `85`, `False`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `zip(fanlar, baholar)` → `[("Matematika",90), ("Fizika",85), ("Kimyo",78)]`. `dict()` → `{"Matematika":90, "Fizika":85, "Kimyo":78}`. `d["Fizika"]` → `85`. `"Kimyo" in d` → `True`.

---

## Savol 10

`fromkeys()` metodi qanday ishlaydi?

- [A] Mavjud dictionaryni nusxalaydi
- [B] Berilgan kalitlar ro'yxatidan, barcha qiymatlari bir xil bo'lgan dictionary yaratadi
- [C] Faqat bo'sh dictionary yaratadi
- [D] Kalitlarni qiymatlar bilan almashtiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `dict.fromkeys(kalitlar, standart_qiymat)` — barcha kalitlarga bir xil qiymat beradi. Standart qiymat ko'rsatilmasa `None` bo'ladi. Masalan: `dict.fromkeys(["a","b","c"], 0)` → `{"a":0, "b":0, "c":0}`.

---

## Savol 11

Quyidagi kodning natijasi nima?

```python
kalitlar = ["ism", "yosh", "shahar"]
d = dict.fromkeys(kalitlar)
print(d)

d2 = dict.fromkeys(kalitlar, "nomalum")
print(d2["yosh"])
```

- [A] `{"ism":None, "yosh":None, "shahar":None}`, `None`
- [B] `{"ism":None, "yosh":None, "shahar":None}`, `"nomalum"`
- [C] `{}`, `"nomalum"`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `fromkeys(kalitlar)` — standart qiymat yo'q → barchasi `None`. `fromkeys(kalitlar, "nomalum")` → `{"ism":"nomalum", "yosh":"nomalum", "shahar":"nomalum"}`. `d2["yosh"]` → `"nomalum"`.

---

## Savol 12

Quyidagi kodning natijasi nima?

```python
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {**d1, **d2}
print(d3)
print(len(d3))
```

- [A] `{"a":1, "b":2}`, `2`
- [B] `{"a":1, "b":2, "c":3, "d":4}`, `4`
- [C] `[{"a":1, "b":2}, {"c":3, "d":4}]`, `2`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `{**d1, **d2}` — `**` operatori dictionaryni "yoyadi". Ikkalasini birlashtirib yangi dictionary yaratadi. Bir xil kalit bo'lsa, oxirgisi ustun turadi. `len` → `4`.

---

## Savol 13

Quyidagi kodning natijasi nima?

```python
d1 = {"x": 1, "y": 2}
d2 = {"y": 99, "z": 3}
d3 = {**d1, **d2}
print(d3["y"])
print(d3["x"])
```

- [A] `2`, `1`
- [B] `99`, `1`
- [C] `2`, `99`
- [D] `KeyError`

> **To'g'ri javob:** B
> **Tushuntirish:** `{**d1, **d2}` — `"y"` ikki dictionary da ham bor. `d2` keyinroq kelgani uchun `d2["y"] = 99` ustun turadi. `d3["y"]` → `99`. `d3["x"]` → `1`.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
sonlar = [1, 2, 3, 4, 5]
d = {}
for son in sonlar:
    d[son] = son ** 2
print(d[3])
print(len(d))
```

- [A] `9`, `5`
- [B] `6`, `5`
- [C] `9`, `4`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `for` tsikli har sonni kalit, uning kvadratini qiymat sifatida qo'shadi: `{1:1, 2:4, 3:9, 4:16, 5:25}`. `d[3]` → `9`. `len(d)` → `5`.

---

## Savol 15

Quyidagi to'liq kodning natijasi nima?

```python
ismlar = ["Ali", "Vali", "Gali"]
balllar = [88, 94, 76]

d = dict(zip(ismlar, balllar))
d["Zulfiya"] = 91
d.update({"Ali": 90})

print(len(d))
print(d["Ali"])
print("Gali" in d)
```

- [A] `4`, `88`, `True`
- [B] `4`, `90`, `True`
- [C] `3`, `90`, `False`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `zip` → `{"Ali":88, "Vali":94, "Gali":76}`. `d["Zulfiya"]=91` → 4 ta. `update({"Ali":90})` → `"Ali"` ning qiymati `90` ga yangilanadi. `len` → `4`. `d["Ali"]` → `90`. `"Gali" in d` → `True`.

---