## Savol 1

Django da model yaratish uchun qaysi klassdan meros olish kerak?

- [A] `django.Model`
- [B] `models.BaseModel`
- [C] `models.Model`
- [D] `django.db.Model`

> **To'g'ri javob:** C
> **Tushuntirish:** Barcha Django modellari `models.Model` klassidan meros olishi shart. `from django.db import models` import qilinadi, so'ng `class NomModel(models.Model):` ko'rinishida yoziladi. Bu Django ORM ning asosiy mexanizmi.

---

## Savol 2

Quyidagi model kodida xato bormi?

```python
from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    matn = models.TextField()
```

- [A] Ha — `TextField` uchun `max_length` yozilmagan
- [B] Ha — `id` maydoni qo'lda yozilmagan
- [C] Xato yo'q — to'g'ri yozilgan
- [D] Ha — `models.Model` o'rniga `Model` yozilishi kerak

> **To'g'ri javob:** C
> **Tushuntirish:** Kod to'liq to'g'ri. `id` maydoni Django tomonidan avtomatik qo'shiladi. `TextField` uchun `max_length` majburiy emas. `from django.db import models` import qilingan, shuning uchun `models.Model` to'g'ri.

---

## Savol 3

`CharField` uchun nima majburiy parametr hisoblanadi?

- [A] `null=True`
- [B] `max_length`
- [C] `default`
- [D] `blank=True`

> **To'g'ri javob:** B
> **Tushuntirish:** `CharField` da `max_length` **majburiy** parametr. U ma'lumotlar bazasida VARCHAR uzunligini belgilaydi. Yozilmasa `TypeError` xatosi chiqadi. `TextField` da esa `max_length` majburiy emas — cheksiz matn uchun mo'ljallangan.

---

## Savol 4

`TextField` va `CharField` ning asosiy farqi nima?

- [A] `TextField` faqat raqamlar uchun
- [B] `CharField` katta matnlar uchun, `TextField` qisqa matnlar uchun
- [C] `TextField` uzun/cheksiz matnlar uchun, `CharField` qisqa matnlar (`max_length` bilan) uchun
- [D] Ular bir xil, faqat nomi farq qiladi

> **To'g'ri javob:** C
> **Tushuntirish:** `CharField` — qisqa matnlar (nom, sarlavha, telefon) uchun, `max_length` majburiy. `TextField` — uzun matnlar (maqola, tavsif, izoh) uchun, `max_length` shart emas. Ma'lumotlar bazasida `CharField` → `VARCHAR`, `TextField` → `TEXT`.

---

## Savol 5

Quyidagi maydon qanday turdagi ma'lumot saqlaydi?

```python
tug'ilgan_kun = models.DateField()
```

- [A] Sana va vaqt: `2024-01-15 10:30:00`
- [B] Faqat sana: `2024-01-15`
- [C] Faqat vaqt: `10:30:00`
- [D] Unix timestamp: `1705312200`

> **To'g'ri javob:** B
> **Tushuntirish:** `DateField` — faqat sana saqlaydi (`YYYY-MM-DD`). Sana **va** vaqt kerak bo'lsa `DateTimeField` ishlatiladi. Faqat vaqt kerak bo'lsa `TimeField` ishlatiladi.

---

## Savol 6

`auto_now_add=True` va `auto_now=True` parametrlarining farqi nima?

- [A] Ikkalasi bir xil ishlaydi
- [B] `auto_now_add` — faqat yaratilganda vaqtni saqlaydi; `auto_now` — har saqlanganda yangilanadi
- [C] `auto_now` — faqat yaratilganda; `auto_now_add` — har saqlanganda
- [D] Ikkalasi ham faqat o'qish uchun emas

> **To'g'ri javob:** B
> **Tushuntirish:** `auto_now_add=True` — obyekt **birinchi marta** yaratilganda avtomatik joriy vaqtni qo'yadi, keyin o'zgarmaydi (masalan, `yaratilgan_vaqt`). `auto_now=True` — obyekt **har safar saqlanganida** vaqt yangilanadi (masalan, `yangilangan_vaqt`).

---

## Savol 7

Quyidagi model to'g'rimi?

```python
class Mahsulot(models.Model):
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    miqdor = models.IntegerField(default=0)
    mavjud = models.BooleanField(default=True)
```

- [A] Xato — `DecimalField` uchun `max_digits` yozilmasligi kerak
- [B] Xato — `BooleanField` uchun `default` yozilmasligi kerak
- [C] To'g'ri — barcha maydonlar to'g'ri yozilgan
- [D] Xato — `IntegerField` uchun `decimal_places` kerak

> **To'g'ri javob:** C
> **Tushuntirish:** `DecimalField` uchun `max_digits` (jami raqamlar soni) va `decimal_places` (kasrdan keyingi raqamlar) — ikkisi ham majburiy. `IntegerField` va `BooleanField` uchun `default` — ixtiyoriy, lekin tavsiya etiladi.

---

## Savol 8

`null=True` va `blank=True` parametrlarining farqi nima?

- [A] Ikkalasi bir xil — maydonni ixtiyoriy qiladi
- [B] `null=True` — ma'lumotlar bazasida `NULL` saqlanishi mumkin; `blank=True` — forma validatsiyasida bo'sh qoldirish mumkin
- [C] `blank=True` — ma'lumotlar bazasida `NULL`; `null=True` — formada bo'sh
- [D] `null=True` faqat `CharField` uchun ishlatiladi

> **To'g'ri javob:** B
> **Tushuntirish:** `null=True` — **database darajasida**: ustun `NULL` qiymat qabul qiladi. `blank=True` — **forma/validatsiya darajasida**: maydon bo'sh qoldirilishi mumkin. Ko'pincha birgalikda ishlatiladi. `CharField` va `TextField` uchun `null=True` o'rniga faqat `blank=True` tavsiya etiladi — bo'sh string `""` yetarli.

---

## Savol 9

`ForeignKey` maydoni nima uchun ishlatiladi?

- [A] Bir modelda bir nechta jadval yaratish uchun
- [B] Ikki model o'rtasida "ko'p-birga" (many-to-one) munosabat o'rnatish uchun
- [C] Modelni boshqa faylga ulash uchun
- [D] Maydonni majburiy qilish uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `ForeignKey` — "many-to-one" munosabat. Masalan, ko'p `Maqola` bitta `Muallif` ga tegishli bo'lishi mumkin. `on_delete` parametri majburiy: `CASCADE`, `SET_NULL`, `PROTECT` va boshqalar boshqa jadval yozuvi o'chirilganda nima bo'lishini belgilaydi.

---

## Savol 10

Quyidagi kodda `on_delete=models.CASCADE` nima vazifani bajaradi?

```python
class Maqola(models.Model):
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
```

- [A] `Maqola` o'chirilganda `Muallif` ham o'chadi
- [B] `Muallif` o'chirilganda unga bog'liq barcha `Maqola` lar ham o'chadi
- [C] Muallif o'chirilishining oldini oladi
- [D] `muallif` maydonini `NULL` ga o'rnatadi

> **To'g'ri javob:** B
> **Tushuntirish:** `CASCADE` — bog'liq obyekt (bu yerda `Muallif`) o'chirilganda, unga bog'liq barcha yozuvlar (`Maqola` lar) ham avtomatik o'chiriladi. `PROTECT` — o'chirishni bloklaydi. `SET_NULL` — `NULL` qo'yadi (buning uchun `null=True` ham kerak).

---

## Savol 11

`ManyToManyField` qanday holatda ishlatiladi?

- [A] Bir obyekt faqat bitta boshqa obyektga bog'liq bo'lsa
- [B] Bir obyekt ko'p boshqa obyektlarga, va ular ham ko'p birinchisiga bog'liq bo'lsa
- [C] Ikkita model o'rtasida hech qanday bog'liqlik bo'lmasa
- [D] Faqat bir tomonga bog'liqlik bo'lsa

> **To'g'ri javob:** B
> **Tushuntirish:** `ManyToManyField` — "ko'p-ko'p" munosabat. Masalan, `Maqola` ko'p `Teg` ga ega bo'lishi mumkin, va bitta `Teg` ko'p `Maqola` da ishlatilishi mumkin. Django bu uchun oraliq jadval avtomatik yaratadi.

---

## Savol 12

Quyidagi model metodining vazifasi nima?

```python
class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)

    def __str__(self):
        return self.sarlavha
```

- [A] Modelni saqlash uchun
- [B] Obyektni string ko'rinishida ifodalaydi — admin panelda va `print()` da ko'rinadi
- [C] Sarlavhani katta harfga o'zgartiradi
- [D] Faqat test uchun ishlatiladi

> **To'g'ri javob:** B
> **Tushuntirish:** `__str__` — Python ning maxsus metodi. Django modelida u admin panelda, `QuerySet` da va `print()` chaqirilganda obyektning matnli tasvirini qaytaradi. Yozilmasa `<Maqola object (1)>` ko'rinishi chiqadi.

---

## Savol 13

`Meta` ichki klassining vazifasi nima?

```python
class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)

    class Meta:
        ordering = ['-yaratilgan_vaqt']
        verbose_name = 'Maqola'
```

- [A] Modelni boshqa modellarga ulash uchun
- [B] Model haqidagi metadata: saralash, jadval nomi, admin nomi va boshqalarni belgilaydi
- [C] Faqat admin panel uchun kerak
- [D] Migratsiya sozlamalarini belgilaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `Meta` — model konfiguratsiyasi: `ordering` (standart saralash), `verbose_name` (admin paneldagi nomi), `db_table` (jadval nomi), `unique_together` (birgalikda unikal maydonlar) va boshqalar. Bu ma'lumotlar bazasida emas, Django darajasida ishlaydi.

---

## Savol 14

`EmailField` qanday validatsiya qiladi?

- [A] Hech qanday validatsiya yo'q — oddiy `CharField` bilan bir xil
- [B] Faqat `@` belgisi borligini tekshiradi
- [C] Email formatini tekshiradi (`user@example.com`)
- [D] Email serverga ulanib tekshiradi

> **To'g'ri javob:** C
> **Tushuntirish:** `EmailField` — ichki `CharField` bo'lib, Django validatori orqali email formatini tekshiradi. Noto'g'ri format bo'lsa forma validatsiyasida xato beradi. Ma'lumotlar bazasida `VARCHAR` sifatida saqlanadi. Standart `max_length=254`.

---

## Savol 15

Quyidagi maydon nima saqlaydi va qanday ishlatiladi?

```python
rasm = models.ImageField(upload_to='rasmlar/')
```

- [A] Rasmni ma'lumotlar bazasida binary formatda saqlaydi
- [B] Rasmning faylga yo'lini (`rasmlar/fayl.jpg`) ma'lumotlar bazasida saqlaydi, faylni esa `MEDIA_ROOT` papkasiga yuklaydi
- [C] URL manzilini saqlaydi
- [D] Faqat rasm nomini saqlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `ImageField` — fayl yo'lini DB da saqlaydi, haqiqiy faylni `MEDIA_ROOT/rasmlar/` papkasiga yuklaydi. Ishlatish uchun `Pillow` kutubxonasi o'rnatilgan bo'lishi (`pip install Pillow`) va `settings.py` da `MEDIA_ROOT`, `MEDIA_URL` sozlangan bo'lishi kerak.

---

## Savol 16

`SlugField` nima uchun ishlatiladi?

- [A] Foydalanuvchi parolini saqlash uchun
- [B] URL uchun qulay qisqa identifikator: faqat harf, raqam, tire va pastki chiziq
- [C] Katta hajmli matn saqlash uchun
- [D] Tasodifiy kalit yaratish uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `SlugField` — URL da ishlatish uchun mo'ljallangan maydon. Masalan, `"Django haqida maqola"` sarlavhasidan `"django-haqida-maqola"` slug yaratiladi. Faqat `[a-z0-9_-]` belgilarga ruxsat beriladi. Ko'pincha `unique=True` bilan ishlatiladi.

---

## Savol 17

`unique=True` parametri nima vazifani bajaradi?

- [A] Maydonni majburiy qiladi
- [B] Ushbu maydonda bir xil qiymat ikki marta saqlanmasligi kafolatlanadi
- [C] Maydonni indekslaydi (tezlashtiradi)
- [D] Maydonni faqat o'qish uchun qiladi

> **To'g'ri javob:** B
> **Tushuntirish:** `unique=True` — ma'lumotlar bazasida `UNIQUE` cheklov qo'yadi. Agar bir xil qiymatli ikkinchi yozuv saqlashga harakat qilinsa `IntegrityError` (yoki forma orqali validatsiya xatosi) chiqadi. Email, username, slug kabi maydonlarda ko'p ishlatiladi.

---

## Savol 18

Quyidagi model to'g'ri yozilganmi?

```python
class Foydalanuvchi(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    ro'yxatdan_o'tgan = models.DateTimeField(auto_now_add=True)
    faol = models.BooleanField(default=True)
```

- [A] Xato — `IntegerField` da `null=True` ishlatilmaydi
- [B] Xato — `DateTimeField` da `auto_now_add` bo'lmaydi
- [C] To'g'ri — barcha maydonlar to'g'ri ishlatilgan
- [D] Xato — `EmailField` da `unique` bo'lmaydi

> **To'g'ri javob:** C
> **Tushuntirish:** Barcha maydonlar to'g'ri: `CharField` `max_length` bilan, `IntegerField` `null/blank` bilan (ixtiyoriy maydon), `EmailField` `unique` bilan, `DateTimeField` `auto_now_add` bilan, `BooleanField` `default` bilan — hammasi standart Django amaliyotiga mos.

---

## Savol 19

`PositiveIntegerField` va `IntegerField` ning farqi nima?

- [A] Hech qanday farq yo'q
- [B] `PositiveIntegerField` — faqat musbat (0 va undan katta) son qabul qiladi; `IntegerField` — manfiy sonlarni ham qabul qiladi
- [C] `IntegerField` — faqat musbat; `PositiveIntegerField` — manfiy ham
- [D] `PositiveIntegerField` — kasrli sonlar uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `IntegerField` — `-2147483648` dan `2147483647` gacha. `PositiveIntegerField` — `0` dan `2147483647` gacha. Miqdor, yosh, reyting kabi manfiy bo'lmaydigan qiymatlar uchun `PositiveIntegerField` tavsiya etiladi.

---

## Savol 20

Quyidagi kodda `choices` parametri nima qiladi?

```python
class Buyurtma(models.Model):
    HOLAT = [
        ('kutilmoqda', 'Kutilmoqda'),
        ('tasdiqlandi', 'Tasdiqlandi'),
        ('yetkazildi', 'Yetkazildi'),
    ]
    holat = models.CharField(max_length=20, choices=HOLAT, default='kutilmoqda')
```

- [A] Ma'lumotlar bazasida ro'yxat (array) saqlaydi
- [B] Maydon faqat belgilangan qiymatlardan birini qabul qiladi — formada dropdown ko'rinishida chiqadi
- [C] Faqat admin panelda ko'rinish uchun
- [D] Qiymatlar sonini cheklaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `choices` — maydon qabul qiladigan qiymatlar ro'yxatini belgilaydi. Har bir element `(db_qiymati, ko'rsatiladigan_nomi)` juftligidan iborat. Formada `<select>` elementi sifatida chiqadi. Ma'lumotlar bazasida faqat `db_qiymati` (`'kutilmoqda'` va h.k.) saqlanadi.

---

## Savol 21

`OneToOneField` qaysi holda ishlatiladi?

- [A] Ko'p obyekt ko'p boshqa obyektga bog'liq bo'lganda
- [B] Bitta obyekt aynan bitta boshqa obyektga bog'liq bo'lganda (1-1 munosabat)
- [C] Bog'liq obyektlar yo'q bo'lganda
- [D] `ForeignKey` bilan bir xil

> **To'g'ri javob:** B
> **Tushuntirish:** `OneToOneField` — har bir obyekt boshqa jadvaldagi aynan bitta obyektga bog'liq. Masalan, har bir `User` uchun bitta `Profil`. `ForeignKey` bilan farqi: `ForeignKey` ko'p yozuvdan bitta chet kalitga, `OneToOneField` esa bitta-bitta munosabatni kafolatlaydi.

---

## Savol 22

Quyidagi model `migrations` ga qanday ta'sir qiladi?

```python
class Yangi(models.Model):
    nom = models.CharField(max_length=50)
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- [A] Hech narsa bo'lmaydi
- [B] `yangi` nomli jadval yaratiladi: `id` (avtomatik) va `nom` ustunlari bilan
- [C] Faqat Python fayli yaratiladi, DB da hech narsa bo'lmaydi
- [D] `makemigrations` xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `makemigrations` model asosida migration fayl yaratadi. `migrate` esa shu faylni o'qib, ma'lumotlar bazasida `appnomi_yangi` nomli jadval yaratadi. `id` ustuni avtomatik `BigAutoField` sifatida qo'shiladi.

---

## Savol 23

`verbose_name` parametri qanday ishlatiladi?

```python
class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200, verbose_name="Maqola sarlavhasi")
```

- [A] Ma'lumotlar bazasidagi ustun nomini o'zgartiradi
- [B] Admin panel va formalarda maydonning ko'rsatiladigan nomini belgilaydi
- [C] Python dagi o'zgaruvchi nomini o'zgartiradi
- [D] `max_length` ni bekor qiladi

> **To'g'ri javob:** B
> **Tushuntirish:** `verbose_name` — faqat ko'rsatish uchun. Admin panelda, formalarda `sarlavha` o'rniga `Maqola sarlavhasi` ko'rinadi. Ma'lumotlar bazasida ustun nomi hamon `sarlavha` bo'lib qoladi. Ixtiyoriy parametr.

---

## Savol 24

Quyidagi maydon qanday qiymat qaytaradi agar hech narsa kiritilmasa?

```python
izoh = models.TextField(blank=True, default='')
```

- [A] `None`
- [B] `NULL`
- [C] Bo'sh string `""`
- [D] `False`

> **To'g'ri javob:** C
> **Tushuntirish:** `default=''` — hech narsa kiritilmasa, bo'sh string `""` saqlanadi. `null=True` yozilmaganligi sababli `NULL` saqlanmaydi. `blank=True` forma validatsiyasida bo'sh qoldirishga ruxsat beradi. `CharField` va `TextField` uchun shu yondashuv tavsiya etiladi.

---

## Savol 25

`db_column` parametri nima uchun ishlatiladi?

```python
ism = models.CharField(max_length=100, db_column='first_name')
```

- [A] Python dagi maydon nomini o'zgartiradi
- [B] Ma'lumotlar bazasidagi ustun nomini belgilaydi — `ism` o'rniga `first_name` bo'ladi
- [C] Admin paneldagi nomni o'zgartiradi
- [D] Maydonni boshqa jadvalga ulaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `db_column` — ma'lumotlar bazasidagi haqiqiy ustun nomini belgilaydi. Yozilmasa Django `ism` nomini ishlatadi. Eski ma'lumotlar bazasi sxemalari bilan ishlashda yoki ustun nomini Python nomidan farqlashtirish kerakda foydali.

---

## Savol 26

Quyidagi modelda `ordering = ['-yaratilgan']` nima anglatadi?

```python
class Xabar(models.Model):
    matn = models.TextField()
    yaratilgan = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-yaratilgan']
```

- [A] Eng eski xabarlar birinchi chiqadi
- [B] Eng yangi xabarlar birinchi chiqadi (teskari tartibda saralash)
- [C] Matniga qarab saralaydi
- [D] Hech qanday tartib yo'q

> **To'g'ri javob:** B
> **Tushuntirish:** Minus belgisi (`-`) teskari (descending) tartibni bildiradi. `ordering = ['-yaratilgan']` — yangi yozuvlar birinchi. `ordering = ['yaratilgan']` (minus yo'q) — eski yozuvlar birinchi. QuerySet da `order_by()` chaqirmasdan ham shu tartib qo'llaniladi.

---

## Savol 27

`FloatField` va `DecimalField` ning farqi nima va qaysi biri moliyaviy ma'lumotlar uchun tavsiya etiladi?

- [A] `FloatField` aniqroq — moliyaviy ma'lumotlar uchun afzal
- [B] `DecimalField` aniqroq, moliyaviy va pul ma'lumotlari uchun tavsiya etiladi; `FloatField` ilmiy hisoblashlar uchun
- [C] Ular bir xil
- [D] `FloatField` pul uchun, `DecimalField` ilmiy uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `FloatField` — Python `float` (IEEE 754), yaxlitlash xatolari bor. `DecimalField` — Python `Decimal`, aniq hisoblash. Masalan, `0.1 + 0.2` `FloatField` da `0.30000000000000004` bo'lishi mumkin. Narx, valyuta, bank ma'lumotlari uchun har doim `DecimalField` ishlatiladi.

---

## Savol 28

Quyidagi kodda `related_name` nima vazifani bajaradi?

```python
class Maqola(models.Model):
    muallif = models.ForeignKey(
        'Muallif',
        on_delete=models.CASCADE,
        related_name='maqolalar'
    )
```

- [A] `Maqola` dan `Muallif` ga o'tish uchun
- [B] `Muallif` dan uning barcha `Maqola` lariga teskari yo'nalishda murojaat qilish uchun: `muallif.maqolalar.all()`
- [C] Maydonga qo'shimcha nom beradi
- [D] Ma'lumotlar bazasidagi ustun nomini o'zgartiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `related_name` — teskari (reverse) munosabat nomi. `muallif_obj.maqolalar.all()` — shu muallifning barcha maqolalari. Belgilanmasa Django avtomatik `maqola_set` nomini beradi. `related_name` ni aniq ko'rsatish kodni o'qilishi osonlashtiradi.

---

## Savol 29

Quyidagi to'liq modeldagi barcha maydonlarning maqsadini belgilang:

```python
class Kurs(models.Model):
    nomi = models.CharField(max_length=255)
    tavsif = models.TextField(blank=True)
    narx = models.DecimalField(max_digits=8, decimal_places=2)
    davomiyligi = models.PositiveIntegerField(help_text="Soatlarda")
    chiqarilgan = models.DateField()
    faol = models.BooleanField(default=True)
    yaratilgan = models.DateTimeField(auto_now_add=True)
    yangilangan = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-yaratilgan']

    def __str__(self):
        return self.nomi
```

Quyidagilardan qaysi xulosa **noto'g'ri**?

- [A] `tavsif` bo'sh qolishi mumkin
- [B] `yaratilgan` va `yangilangan` qo'lda o'zgartirilishi mumkin
- [C] Kurslar yangilaridan eskisiga qarab tartiblangan
- [D] `narx` kasr qiymat qabul qiladi

> **To'g'ri javob:** B
> **Tushuntirish:** `auto_now_add=True` va `auto_now=True` bilan belgilangan maydonlar **avtomatik** to'ldiriladi va qo'lda o'zgartirib bo'lmaydi — ular `editable=False` ga ega. Qolgan xulosalar to'g'ri: `blank=True` → bo'sh qoldirish mumkin; `DecimalField` → kasr; `ordering=['-yaratilgan']` → yangilardan eskiga.

---

## Savol 30

`makemigrations` va `migrate` buyruqlarining farqi nimada?

- [A] Ikkalasi bir xil — faqat biri qisqaroq
- [B] `makemigrations` — model o'zgarishlarini migration fayliga yozadi; `migrate` — migration fayllarini o'qib ma'lumotlar bazasini yangilaydi
- [C] `migrate` — migration fayl yaratadi; `makemigrations` — DB ga qo'llaydi
- [D] `makemigrations` faqat yangi modellar uchun, `migrate` eski modellar uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `makemigrations` — `models.py` dagi o'zgarishlarni aniqlaydi va `migrations/00XX_....py` fayl yaratadi (DB ga hech narsa qilinmaydi). `migrate` — yaratilgan migration fayllarini o'qib, haqiqiy SQL so'rovlar orqali ma'lumotlar bazasi sxemasini yangilaydi. Ikkalasi birgalikda ishlatiladi.

---