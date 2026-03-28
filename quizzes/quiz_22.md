## Savol 1

Tuple nima?

- [A] O'zgaruvchan, tartibli elementlar to'plami
- [B] O'zgarmas (immutable), tartibli elementlar to'plami
- [C] Kalit-qiymat juftliklarini saqlaydigan tuzilma
- [D] Faqat raqamlarni saqlaydigan maxsus list

> **To'g'ri javob:** B
> **Tushuntirish:** Tuple — tartibli (ordered) va o'zgarmas (immutable) ma'lumot turi. Yaratilgandan keyin elementlarini o'zgartirish, qo'shish yoki o'chirish mumkin emas. Dumaloq qavs `()` bilan yoziladi.

---

## Savol 2

Tuple qanday yaratiladi?

- [A] `[1, 2, 3]`
- [B] `{1, 2, 3}`
- [C] `(1, 2, 3)`
- [D] `<1, 2, 3>`

> **To'g'ri javob:** C
> **Tushuntirish:** Tuple dumaloq qavslar `(...)` ichiga elementlarni vergul bilan yozib yaratiladi. Qavssiz ham yaratish mumkin: `t = 1, 2, 3`. `tuple()` konstruktori ham ishlatiladi.

---

## Savol 3

Quyidagi kodning natijasi nima?

```python
t = ("olma", "banan", "gilos")
print(t[0])
print(t[-1])
print(type(t))
```

- [A] `"banan"`, `"gilos"`, `<class 'list'>`
- [B] `"olma"`, `"gilos"`, `<class 'tuple'>`
- [C] `"olma"`, `"banan"`, `<class 'tuple'>`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `t[0]` → birinchi element: `"olma"`. `t[-1]` → oxirgi element: `"gilos"`. `type(t)` → `<class 'tuple'>`.

---

## Savol 4

Tuple o'zgarmas ekanligi nimani bildiradi?

- [A] Elementlarni o'qib bo'lmaydi
- [B] Tuple ga yangi element qo'shish, mavjudini o'zgartirish yoki o'chirish mumkin emas
- [C] Tuple faqat bir marta ishlatiladi
- [D] Tuple elementlari doim bir xil turda bo'lishi kerak

> **To'g'ri javob:** B
> **Tushuntirish:** Immutable — yaratilgandan so'ng o'zgartirib bo'lmaydi. `t[0] = 99` → `TypeError`. Lekin tuple o'zgaruvchisini qayta belgilash mumkin: `t = (1, 2)` → `t = (3, 4)`.

---

## Savol 5

Quyidagi kodda nima sodir bo'ladi?

```python
t = ("Ali", "Vali", "Gali")
t[0] = "Zulfiya"
print(t)
```

- [A] `("Zulfiya", "Vali", "Gali")` chiqadi
- [B] `TypeError` — tuple o'zgarmas
- [C] `ValueError` beradi
- [D] Hech narsa bo'lmaydi, `t` o'zgarmaydi

> **To'g'ri javob:** B
> **Tushuntirish:** Tuple immutable — elementni o'zgartirishga urinish `TypeError: 'tuple' object does not support item assignment` xatosini beradi.

---

## Savol 6

Bitta elementli tuple qanday yaratiladi?

- [A] `t = ("salom")`
- [B] `t = ["salom"]`
- [C] `t = ("salom",)`
- [D] `t = tuple("salom")`

> **To'g'ri javob:** C
> **Tushuntirish:** `("salom")` — bu shunchaki `"salom"` string (qavs matematik). Bitta elementli tuple uchun oxiriga vergul kerak: `("salom",)`. `type(("salom"))` → `str`, `type(("salom",))` → `tuple`.

---

## Savol 7

Quyidagi kodning natijasi nima?

```python
a = ("python")
b = ("python",)
print(type(a))
print(type(b))
print(len(b))
```

- [A] `<class 'tuple'>`, `<class 'tuple'>`, `1`
- [B] `<class 'str'>`, `<class 'tuple'>`, `1`
- [C] `<class 'str'>`, `<class 'str'>`, `6`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `("python")` → `str`. `("python",)` → bitta elementli `tuple`. `len(("python",))` → `1` (bitta element).

---

## Savol 8

Tuple va list o'rtasidagi asosiy farq nima?

- [A] Tuple faqat raqamlarni saqlaydi
- [B] List o'zgarmas, Tuple o'zgaruvchan
- [C] Tuple o'zgarmas (immutable), List o'zgaruvchan (mutable)
- [D] Hech qanday farq yo'q, ikkalasi bir xil

> **To'g'ri javob:** C
> **Tushuntirish:** Asosiy farq: `tuple` immutable — o'zgartirish mumkin emas. `list` mutable — o'zgartirish mumkin. Tuple doimiy ma'lumotlar (koordinatalar, ranglar) uchun, list esa o'zgaruvchan to'plamlar uchun ishlatiladi.

---

## Savol 9

Quyidagi kodning natijasi nima?

```python
t = ("a", "b", "c", "b", "a")
print(t.count("b"))
print(t.index("c"))
print(len(t))
```

- [A] `1`, `2`, `5`
- [B] `2`, `2`, `5`
- [C] `2`, `3`, `4`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `count("b")` → `"b"` 2 marta bor: `2`. `index("c")` → `"c"` 2-indeksda: `2`. `len(t)` → 5 ta element: `5`.

---

## Savol 10

Tuple "unpacking" (qadoqdan chiqarish) nima?

- [A] Tuple ni listga aylantirish
- [B] Tuple elementlarini alohida o'zgaruvchilarga biriktirish
- [C] Tuple ni o'chirish
- [D] Tuple dan nusxa olish

> **To'g'ri javob:** B
> **Tushuntirish:** `a, b, c = ("Ali", "Vali", "Gali")` — tuple elementlari mos o'zgaruvchilarga biriktiriladi. O'zgaruvchilar soni tuple uzunligiga teng bo'lishi shart, aks holda `ValueError`.

---

## Savol 11

Quyidagi kodning natijasi nima?

```python
ism, yosh, shahar = ("Sardor", 22, "Toshkent")
print(ism)
print(yosh)
print(shahar)
```

- [A] `("Sardor", 22, "Toshkent")`, xato, xato
- [B] `Sardor`, `22`, `Toshkent`
- [C] `Sardor`, `Toshkent`, `22`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** Unpacking — `ism="Sardor"`, `yosh=22`, `shahar="Toshkent"`. Tartib saqlanadi. Natija: `Sardor`, `22`, `Toshkent`.

---

## Savol 12

`*` (yulduzcha) bilan unpacking qanday ishlaydi?

```python
birinchi, *o'rtalar, oxirgi = ("A", "B", "C", "D", "E")
print(birinchi)
print(o'rtalar)
print(oxirgi)
```

- [A] `"A"`, `("B", "C", "D")`, `"E"`
- [B] `"A"`, `["B", "C", "D"]`, `"E"`
- [C] `"A"`, `"B"`, `"E"`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `*o'rtalar` — qolgan elementlarni **list** sifatida oladi. `birinchi="A"`, `o'rtalar=["B","C","D"]` (list!), `oxirgi="E"`.

---

## Savol 13

Tuple qachon listdan afzalroq ishlatiladi?

- [A] Ko'p elementlar saqlash kerak bo'lganda
- [B] Ma'lumotlar o'zgarmasligi kafolatlanishi yoki dict kalit sifatida ishlatish kerak bo'lganda
- [C] Elementlarni tartiblash kerak bo'lganda
- [D] Faqat matn saqlash kerak bo'lganda

> **To'g'ri javob:** B
> **Tushuntirish:** Tuple afzalliklari: (1) immutable — tasodifiy o'zgarishdan himoya; (2) `dict` kalit bo'la oladi (list bo'lmaydi); (3) listga qaraganda tezroq va kam xotira oladi; (4) koordinatalar, RGB ranglar kabi o'zgarmas ma'lumotlar uchun.

---

## Savol 14

Quyidagi kodning natijasi nima?

```python
t1 = ("olma", "banan")
t2 = ("gilos", "nok")
t3 = t1 + t2
t4 = t1 * 2
print(t3)
print(t4)
```

- [A] `("olma","banan","gilos","nok")`, `("olma","banan","olma","banan")`
- [B] `["olma","banan","gilos","nok"]`, `["olma","banan","olma","banan"]`
- [C] `("olma","banan")`, `("olma","banan")`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `+` — yangi tuple birlashtiradi: `("olma","banan","gilos","nok")`. `*` — takrorlaydi: `("olma","banan","olma","banan")`. Natijalar ham tuple bo'ladi.

---

## Savol 15

Quyidagi kodning natijasi nima?

```python
t = ("python", "java", "c++", "javascript")
print(t[1:3])
print("java" in t)
print(t[-2])
```

- [A] `("java", "c++")`, `True`, `"c++"`
- [B] `("java", "c++", "javascript")`, `True`, `"java"`
- [C] `["java", "c++"]`, `False`, `"c++"`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** `t[1:3]` → indeks 1 dan 2 gacha: `("java","c++")`. `"java" in t` → `True`. `t[-2]` → oxiridan ikkinchi: `"c++"`.

---

## Savol 16

Tuple ni listga va listni tuple ga qanday aylantirish mumkin?

- [A] `tuple.to_list()` va `list.to_tuple()`
- [B] `list(tuple_nomi)` va `tuple(list_nomi)`
- [C] `tuple[:]` va `list[:]`
- [D] Aylantirish mumkin emas

> **To'g'ri javob:** B
> **Tushuntirish:** `list((1,2,3))` → `[1,2,3]`. `tuple([1,2,3])` → `(1,2,3)`. Bu o'zaro aylantirishning standart usuli.

---

## Savol 17

Quyidagi kodning natijasi nima?

```python
t = ("Ali", "Vali", "Gali")
r = list(t)
r.append("Zulfiya")
t2 = tuple(r)
print(t)
print(t2)
```

- [A] `("Ali","Vali","Gali","Zulfiya")`, `("Ali","Vali","Gali","Zulfiya")`
- [B] `("Ali","Vali","Gali")`, `("Ali","Vali","Gali","Zulfiya")`
- [C] `("Ali","Vali","Gali")`, `["Ali","Vali","Gali","Zulfiya"]`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `list(t)` → `["Ali","Vali","Gali"]`. `append("Zulfiya")` → `["Ali","Vali","Gali","Zulfiya"]`. `tuple(r)` → `("Ali","Vali","Gali","Zulfiya")`. Asl `t` o'zgarmaydi.

---

## Savol 18

Quyidagi kodning natijasi nima?

```python
talabalar = [("Ali", "A"), ("Vali", "B"), ("Gali", "A")]
for ism, baho in talabalar:
    print(f"{ism}: {baho}")
```

- [A] `("Ali","A")`, `("Vali","B")`, `("Gali","A")`
- [B] `Ali: A`, `Vali: B`, `Gali: A`
- [C] `Ali`, `Vali`, `Gali`
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `for ism, baho in talabalar` — har tuple `ism` va `baho` ga unpackinglanadi. `("Ali","A")` → `ism="Ali"`, `baho="A"` → `Ali: A`.

---

## Savol 19

Quyidagi kodning natijasi nima?

```python
t = ("nom", ["Python", "Java"], "til")
t[1].append("C++")
print(t)
```

- [A] `("nom", ["Python", "Java"], "til")` — o'zgarmadi
- [B] `TypeError` beradi
- [C] `("nom", ["Python", "Java", "C++"], "til")`
- [D] `("nom", "C++", "til")`

> **To'g'ri javob:** C
> **Tushuntirish:** Tuple immutable — lekin ichidagi list mutable. `t[1]` — bu list, unga `append("C++")` qilish mumkin. Tuple ning o'zi o'zgarmadi (list havolasi bir xil), lekin list ichidagi qiymat o'zgardi.

---

## Savol 20

Quyidagi to'liq kodning natijasi nima?

```python
shaxslar = (
    ("Ali", "Toshkent", 25),
    ("Vali", "Samarqand", 30),
    ("Zulfiya", "Toshkent", 22),
    ("Gali", "Buxoro", 28)
)

toshkentliklar = []
for ism, shahar, yosh in shaxslar:
    if shahar == "Toshkent":
        toshkentliklar.append(ism)

print(len(toshkentliklar))
print(toshkentliklar[0])
print("Vali" in toshkentliklar)
```

- [A] `2`, `"Ali"`, `False`
- [B] `1`, `"Zulfiya"`, `False`
- [C] `2`, `"Zulfiya"`, `True`
- [D] Xato beradi

> **To'g'ri javob:** A
> **Tushuntirish:** Toshkentliklar: `"Ali"` va `"Zulfiya"` → 2 ta. `toshkentliklar[0]` → `"Ali"`. `"Vali"` Samarqandlik → `"Vali" in toshkentliklar` → `False`.

---