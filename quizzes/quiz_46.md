## Savol 1

Django modelida `__str__` metodi nima uchun yoziladi?

- [A] Modelni ma'lumotlar bazasiga saqlash uchun
- [B] Obyektning matnli tasvirini qaytaradi — admin panelda, `print()` da va QuerySet da ko'rinadi
- [C] Modelni o'chirish uchun
- [D] Faqat test yozish uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `__str__` yozilmasa admin panelda `Maqola object (1)` ko'rinadi. Yozilgandan keyin esa `Django bilan tanishuv` kabi mazmunli nom chiqadi. Python ning maxsus (dunder) metodi — `str(obj)` va `print(obj)` chaqirilganda ishlatiladi. Har doim `str` tipida qiymat qaytarishi shart.

---

## Savol 2

Quyidagi `__str__` metodining natijasi nima?

```python
class Muallif(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.familiya} {self.ism}"
```

`Muallif(ism="Ali", familiya="Valiyev")` ob'ekti uchun:

- [A] `Ali`
- [B] `Valiyev Ali`
- [C] `Ali Valiyev`
- [D] `Muallif object`

> **To'g'ri javob:** B
> **Tushuntirish:** `f"{self.familiya} {self.ism}"` — avval `familiya` (`Valiyev`), so'ng `ism` (`Ali`) chiqadi. `f-string` da tartib muhim — qaysi o'zgaruvchi oldin yozilsa, u oldin chiqadi.

---

## Savol 3

`get_absolute_url()` metodi nima uchun ishlatiladi?

```python
from django.urls import reverse

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
```

- [A] Maqolani o'chirish URL ini qaytaradi
- [B] Modelning "kanonik" URL ini qaytaradi — admin panelda "Ko'rish" tugmasi va shablonlarda ishlatiladi
- [C] Tashqi sayt URL ini qaytaradi
- [D] Faqat `redirect()` da ishlatiladi

> **To'g'ri javob:** B
> **Tushuntirish:** `get_absolute_url()` — Django konvensiyasi. Admin panelda saqlangandan keyin "Saytda ko'rish" tugmasi shu URL ga yo'naltiradi. Shablonda `{{ maqola.get_absolute_url }}` yoki `<a href="{{ object.get_absolute_url }}">` ko'rinishida ishlatiladi. `reverse()` bilan URL dinamik generatsiya qilinadi.

---

## Savol 4

`save()` metodini override qilish qachon kerak bo'ladi?

```python
class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.sarlavha)
        super().save(*args, **kwargs)
```

- [A] Har doim `save()` override qilinishi kerak
- [B] Saqlashdan oldin qo'shimcha mantiq bajarish kerak bo'lganda — masalan, maydon avtomatik to'ldirilishi
- [C] Faqat `slug` maydonlari uchun
- [D] `super().save()` chaqirilmasa ham ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `save()` override — saqlashdan oldin/keyin qo'shimcha amallar uchun. Yuqoridagi misolda `slug` bo'sh bo'lsa `sarlavha` dan avtomatik yaratiladi. **`super().save(*args, **kwargs)` chaqirilishi shart** — bo'lmasa ma'lumotlar bazasiga hech narsa saqlanmaydi.

---

## Savol 5

Quyidagi `save()` da xato bormi?

```python
class Mahsulot(models.Model):
    nomi = models.CharField(max_length=200)
    narx = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.narx < 0:
            self.narx = 0
        super().save(*args, **kwargs)
```

- [A] Ha — `super().save()` birinchi bo'lishi kerak
- [B] Ha — `if` sharti ishlaydi
- [C] Xato yo'q — manfiy narx nolga o'rnatiladi, so'ng saqlanadi
- [D] Ha — `*args, **kwargs` kerak emas

> **To'g'ri javob:** C
> **Tushuntirish:** Mantiq to'g'ri: avval tekshirish, so'ng `super().save()`. Agar `super().save()` birinchi bo'lsa, tekshirish foydasiz — ma'lumotlar bazasiga noto'g'ri qiymat tushib bo'ladi. `*args, **kwargs` — `update_fields`, `force_insert` kabi parametrlarni uzatish uchun kerak, qoldirish tavsiya etiladi.

---

## Savol 6

`delete()` metodini override qilish qanday holatda foydali?

```python
class Fayl(models.Model):
    nom = models.CharField(max_length=200)
    fayl = models.FileField(upload_to='fayllar/')

    def delete(self, *args, **kwargs):
        self.fayl.delete(save=False)
        super().delete(*args, **kwargs)
```

- [A] Hech qachon kerak emas — Django avtomatik qiladi
- [B] Ma'lumotlar bazasidan o'chirish bilan birga server diskidagi faylni ham o'chirish kerak bo'lganda
- [C] Faqat `CASCADE` bilan ishlaydi
- [D] `super().delete()` chaqirilmasa ham fayl o'chadi

> **To'g'ri javob:** B
> **Tushuntirish:** Django `FileField`/`ImageField` dagi fayllarni DB yozuvi o'chirilganda **avtomatik o'chirmaydi**. `delete()` override qilinib, avval disk faylini (`self.fayl.delete(save=False)`), so'ng DB yozuvini (`super().delete()`) o'chirish kerak. `save=False` — modelni qayta saqlamaslik uchun.

---

## Savol 7

Model metodlari va `@classmethod`, `@staticmethod` farqi nima?

```python
class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    nashr_qilingan = models.BooleanField(default=False)

    def sarlavhani_katta(self):           # oddiy metod
        return self.sarlavha.upper()

    @classmethod
    def nashr_qilinganlar(cls):           # classmethod
        return cls.objects.filter(nashr_qilingan=True)

    @staticmethod
    def slug_yaratish(matn):              # staticmethod
        from django.utils.text import slugify
        return slugify(matn)
```

- [A] Uchbalasi bir xil ishlaydi
- [B] Oddiy metod — `self` (obyekt), `classmethod` — `cls` (klass), `staticmethod` — na `self` na `cls` — faqat aloqador funksiya
- [C] `classmethod` faqat meros uchun
- [D] `staticmethod` Django da ishlamaydi

> **To'g'ri javob:** B
> **Tushuntirish:** Oddiy metod: `self` — bitta obyektga murojaat. `@classmethod`: `cls` — klassga murojaat, `QuerySet` qaytaruvchi "factory method" lar uchun. `@staticmethod`: na `self` na `cls` — modelga mantiqan bog'liq lekin obyekt/klassga muhtoj bo'lmagan yordamchi funksiyalar uchun.

---

## Savol 8

Quyidagi `property` dekorator nima qiladi?

```python
class Foydalanuvchi(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)

    @property
    def toliq_ism(self):
        return f"{self.ism} {self.familiya}"
```

Foydalanuvchi chaqirishning to'g'ri usuli qaysi?

- [A] `foydalanuvchi.toliq_ism()`
- [B] `foydalanuvchi.toliq_ism`
- [C] `Foydalanuvchi.toliq_ism`
- [D] `foydalanuvchi.get_toliq_ism()`

> **To'g'ri javob:** B
> **Tushuntirish:** `@property` — metodni atribut kabi chaqirish imkonini beradi. `foydalanuvchi.toliq_ism` — qavssiz, xuddi oddiy maydon kabi. Ma'lumotlar bazasida saqlanmaydi — har safar hisoblanadi. `foydalanuvchi.toliq_ism()` xato beradi (`TypeError: 'str' object is not callable`).

---

## Savol 9

`clean()` metodi qaysi bosqichda chaqiriladi?

```python
from django.core.exceptions import ValidationError

class Kurs(models.Model):
    boshlanish = models.DateField()
    tugash = models.DateField()

    def clean(self):
        if self.boshlanish and self.tugash:
            if self.boshlanish > self.tugash:
                raise ValidationError("Boshlanish sanasi tugash sanasidan keyin bo'lolmaydi!")
```

- [A] Ma'lumotlar bazasiga saqlashdan so'ng
- [B] Model validatsiyasi paytida — forma orqali yoki `full_clean()` chaqirilganda
- [C] Har safar maydon o'qilganda
- [D] Migratsiya paytida

> **To'g'ri javob:** B
> **Tushuntirish:** `clean()` — bir nechta maydon birgalikda tekshirilishi kerak bo'lganda (`cross-field validation`). Forma yuborilganda Django avtomatik chaqiradi. `save()` da **avtomatik chaqirilmaydi** — `full_clean()` ni qo'lda chaqirish yoki forma orqali ishlash kerak. `ValidationError` — forma xatosi sifatida ko'rsatiladi.

---

## Savol 10

`__repr__` va `__str__` ning farqi nima?

```python
class Tovar(models.Model):
    nomi = models.CharField(max_length=100)
    narx = models.IntegerField()

    def __str__(self):
        return self.nomi

    def __repr__(self):
        return f"Tovar(id={self.pk}, nomi='{self.nomi}', narx={self.narx})"
```

- [A] Ikkalasi bir xil — faqat nomi farq qiladi
- [B] `__str__` — foydalanuvchi uchun o'qilishi qulay matn; `__repr__` — dasturchi uchun aniq, debug uchun foydali tasvir
- [C] `__repr__` Django da ishlatilmaydi
- [D] `__str__` faqat admin panel uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `__str__` — `print(obj)`, shablon, admin — oddiy o'qilishi qulay matn. `__repr__` — Python shell da `obj` yozilganda, `repr(obj)`, log fayllarida — to'liq texnik ma'lumot. Django da asosiy `__str__` bo'lsa, `__repr__` qo'shimcha debug qulayligi. Agar `__str__` yozilmasa, `__repr__` ishlatiladi.

---

## Savol 11

Quyidagi model metodlari orasida ma'lumotlar bazasiga murojaat qilmaydigani qaysi?

```python
class Mahsulot(models.Model):
    nomi = models.CharField(max_length=200)
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    chegirma = models.IntegerField(default=0)

    def chegirmali_narx(self):                        # A
        return self.narx * (1 - self.chegirma / 100)

    @classmethod
    def arzon_mahsulotlar(cls, chegara):              # B
        return cls.objects.filter(narx__lt=chegara)

    def save(self, *args, **kwargs):                  # C
        super().save(*args, **kwargs)

    @staticmethod
    def valyuta_formatlash(qiymat):                   # D
        return f"{qiymat:,.2f} so'm"
```

- [A] Faqat A
- [B] Faqat B
- [C] A va D
- [D] Faqat C

> **To'g'ri javob:** C
> **Tushuntirish:** A — `self.narx` va `self.chegirma` allaqachon yuklangan atributlar, qo'shimcha DB so'rovi yo'q. D — faqat Python hisoblash. B — `cls.objects.filter()` — DB ga `SELECT` so'rov. C — `super().save()` — DB ga `INSERT`/`UPDATE` so'rov. A va D — sof Python, DB ga murojaat yo'q.

---

## Savol 12

`full_clean()` metodi nimalarni tekshiradi?

```python
mahsulot = Mahsulot(nomi="", narx=-100)
mahsulot.full_clean()  # ValidationError chiqarishi mumkin
```

- [A] Faqat `clean()` metodini chaqiradi
- [B] Barcha maydon validatsiyalari (`validate_*`), `clean_fields()`, `clean()` va `validate_unique()` ni ketma-ket bajaradi
- [C] Faqat `unique` maydonlarni tekshiradi
- [D] `save()` ni chaqiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `full_clean()` to'liq validatsiya zanjiri: 1) `clean_fields()` — har bir maydon qoidalari (`max_length`, `blank`, `null`), 2) `clean()` — cross-field validatsiya, 3) `validate_unique()` — `unique`, `unique_together` tekshiruvi. `save()` bu metodlarni **avtomatik chaqirmaydi** — forma orqali ishlashda Django o'zi chaqiradi.

---

## Savol 13

`Meta` ichki klassida `ordering` va uni `__str__` bilan birgalikda ishlatish qanday natija beradi?

```python
class Yangilik(models.Model):
    sarlavha = models.CharField(max_length=200)
    sana = models.DateField()

    class Meta:
        ordering = ['-sana']

    def __str__(self):
        return f"{self.sarlavha} ({self.sana})"
```

`Yangilik.objects.all()` qanday tartiblangan holda qaytariladi?

- [A] `sarlavha` bo'yicha A-Z tartibda
- [B] `sana` bo'yicha eng yangilardan eskisiga (descending)
- [C] `id` bo'yicha tartibda
- [D] Tasodifiy tartibda

> **To'g'ri javob:** B
> **Tushuntirish:** `Meta.ordering = ['-sana']` — minus belgisi descending (teskari) tartibni bildiradi. Yangi sana birinchi. `__str__` esa `"Django 5.0 yangiliklari (2024-03-15)"` ko'rinishida chiqadi. `ordering` QuerySet ga har safar avtomatik `ORDER BY sana DESC` qo'shadi.

---

## Savol 14

Quyidagi `get_*_display()` metodi qanday ishlaydi?

```python
class Buyurtma(models.Model):
    HOLAT = [
        ('K', 'Kutilmoqda'),
        ('T', 'Tasdiqlandi'),
        ('Y', 'Yetkazildi'),
    ]
    holat = models.CharField(max_length=1, choices=HOLAT, default='K')
```

`buyurtma.get_holat_display()` nima qaytaradi agar `buyurtma.holat == 'T'` bo'lsa?

- [A] `'T'`
- [B] `'Tasdiqlandi'`
- [C] `['T', 'Tasdiqlandi']`
- [D] `'HOLAT'`

> **To'g'ri javob:** B
> **Tushuntirish:** Django `choices` li har bir maydoni uchun avtomatik `get_MAYDON_NOMI_display()` metod yaratadi. Bu metod saqlangan qiymat (`'T'`) o'rniga ko'rsatiladigan nom (`'Tasdiqlandi'`) qaytaradi. Shablon: `{{ buyurtma.get_holat_display }}`, Python: `buyurtma.get_holat_display()`.

---

## Savol 15

Quyidagi `@classmethod` dan foydalanishning to'g'ri usuli qaysi?

```python
class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    faol = models.BooleanField(default=True)
    ko'rishlar = models.IntegerField(default=0)

    @classmethod
    def eng_mashhurlar(cls, n=5):
        return cls.objects.filter(faol=True).order_by('-ko\'rishlar')[:n]
```

- [A] `maqola_obj.eng_mashhurlar()`
- [B] `Maqola.eng_mashhurlar()` yoki `Maqola.eng_mashhurlar(10)`
- [C] `Maqola().eng_mashhurlar()`
- [D] `cls.eng_mashhurlar()`

> **To'g'ri javob:** B
> **Tushuntirish:** `@classmethod` — obyekt emas, **klass** orqali chaqiriladi: `Maqola.eng_mashhurlar()`. `n` parametrining standart qiymati `5` — `Maqola.eng_mashhurlar()` — 5 ta, `Maqola.eng_mashhurlar(10)` — 10 ta. Obyekt orqali ham chaqirilsa ishlaydi, lekin konvensiya bo'yicha klass orqali.

---

## Savol 16

Modelda `@property` bilan ma'lumotlar bazasidagi `@cached_property` ning farqi nima?

```python
from django.utils.functional import cached_property

class Muallif(models.Model):
    ism = models.CharField(max_length=100)

    @property
    def maqolalar_soni(self):
        return self.maqola_set.count()   # har safar DB ga murojaat

    @cached_property
    def profil_malumotlari(self):
        return self.profil  # bir marta bajariladi, natija xotirada saqlanadi
```

- [A] Ikkalasi bir xil
- [B] `@property` — har chaqirilganda hisoblanadi; `@cached_property` — birinchi chaqiruvda hisoblanib, natija obyekt xotirasida saqlanadi
- [C] `@cached_property` ma'lumotlar bazasida saqlanadi
- [D] `@cached_property` faqat string uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `@property` — har gal chaqirilganda qayta hisoblanadi (DB so'rovi, hisoblash). `@cached_property` — birinchi chaqiruvda bajariladi, natija `self.__dict__` ga saqlanadi. Ikkinchi chaqiruvda DB ga bormay, xotiradan oladi. Katta hisoblashlarda yoki bir nechta marta ishlatilsa `@cached_property` afzal.

---

## Savol 17

Quyidagi model `__eq__` metodini override qilmasa, ikkita obyektni solishtirish qanday ishlaydi?

```python
class Tovar(models.Model):
    nomi = models.CharField(max_length=100)

tovar1 = Tovar(pk=1, nomi="Kitob")
tovar2 = Tovar(pk=1, nomi="Kitob")
tovar3 = Tovar(pk=2, nomi="Kitob")

print(tovar1 == tovar2)   # ?
print(tovar1 == tovar3)   # ?
```

- [A] `False`, `False` — ikkalasi turli obyekt
- [B] `True`, `True` — `nomi` bir xil
- [C] `True`, `False` — Django modellari `pk` bo'yicha taqqoslaydi
- [D] `True`, `True` — barcha maydonlar bir xil bo'lsa

> **To'g'ri javob:** C
> **Tushuntirish:** Django `models.Model` ning `__eq__` metodi `pk` bo'yicha taqqoslaydi. `pk=1` bo'lgan ikki obiekt `==` bo'ladi (`True`). `pk=1` va `pk=2` bo'lsa `False`. `pk=None` (saqlanmagan) bo'lsa, har xil obyektlar `False` — hatto maydonlar bir xil bo'lsa ham.

---

## Savol 18

Quyidagi modelda `get_next_by_FIELD()` metodi nima qiladi?

```python
class Tadbir(models.Model):
    nomi = models.CharField(max_length=200)
    sana = models.DateField()

    def __str__(self):
        return self.nomi
```

`tadbir.get_next_by_sana()` nima qaytaradi?

- [A] Keyingi `id` li yozuvni
- [B] `sana` maydoni bo'yicha keyingi (undan katta sana) `Tadbir` obyektini
- [C] Joriy tadbirdan keyingi barcha tadbirlarni
- [D] Bu metod mavjud emas

> **To'g'ri javob:** B
> **Tushuntirish:** Django `DateField` va `DateTimeField` li modellarga avtomatik `get_next_by_FIELD()` va `get_previous_by_FIELD()` metodlarini qo'shadi. `tadbir.get_next_by_sana()` — shu tadbirdan keyingi sanali tadbirni qaytaradi. Topilmasa `DoesNotExist` chiqaradi. `filter_kwargs` argument bilan qo'shimcha filtr qo'shish mumkin.

---

## Savol 19

Quyidagi `save()` da `update_fields` parametri nima uchun?

```python
class Profil(models.Model):
    foydalanuvchi = models.OneToOneField(User, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='profil/', blank=True)
    bio = models.TextField(blank=True)
    oxirgi_faollik = models.DateTimeField(auto_now=True)

# Faqat bio ni yangilash:
profil.bio = "Yangi bio matni"
profil.save(update_fields=['bio'])
```

- [A] Faqat `bio` ustuni yangilanadi — boshqa ustunlar DB da o'zgarmaydi, `UPDATE` so'rovi optimallanadi
- [B] Barcha maydonlar saqlanadi
- [C] Xato beradi
- [D] `auto_now` ham yangilanmaydi

> **To'g'ri javob:** A
> **Tushuntirish:** `update_fields=['bio']` — faqat `bio` ustuni uchun `UPDATE` SQL so'rovi bajariladi: `UPDATE profil SET bio=... WHERE id=...`. Barcha maydonlarni yangilash (`UPDATE profil SET rasm=..., bio=..., oxirgi_faollik=...`) o'rniga faqat kerakli ustun — tezroq va xavfsizroq. Bir vaqtda turli joylarda saqlash muammosini kamaytiradi.

---

## Savol 20

Quyidagi to'liq modeldagi barcha metodlarni tahlil qiling — qaysi xulosa **noto'g'ri**?

```python
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Kurs(models.Model):
    DARAJA = [('B', 'Boshlang\'ich'), ('O', 'O\'rta'), ('Y', 'Yuqori')]

    nomi = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    daraja = models.CharField(max_length=1, choices=DARAJA)
    narx = models.DecimalField(max_digits=8, decimal_places=2)
    faol = models.BooleanField(default=True)

    class Meta:
        ordering = ['nomi']

    def __str__(self):
        return f"{self.nomi} ({self.get_daraja_display()})"

    def get_absolute_url(self):
        return reverse('kurslar:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nomi)
        super().save(*args, **kwargs)

    def clean(self):
        if self.narx and self.narx < 0:
            raise ValidationError({'narx': 'Narx manfiy bo\'lishi mumkin emas!'})

    @property
    def chegirmali_narx(self):
        return self.narx * 0.9

    @classmethod
    def faol_kurslar(cls):
        return cls.objects.filter(faol=True)
```

- [A] `kurs.__str__()` → `"Python kursi (Boshlang'ich)"` ko'rinishida chiqadi
- [B] `slug` avtomatik yaratiladi, lekin faqat birinchi saqlashda
- [C] `chegirmali_narx` ma'lumotlar bazasida alohida ustun sifatida saqlanadi
- [D] `faol_kurslar()` → `Kurs.faol_kurslar()` ko'rinishida chaqiriladi

> **To'g'ri javob:** C
> **Tushuntirish:** `@property` — **hisoblangan xususiyat**, ma'lumotlar bazasida saqlanmaydi. Har chaqiruvda `self.narx * 0.9` hisob-lanadi. DB da `chegirmali_narx` ustuni yo'q — migration ham yaratilmaydi. Qolganlar to'g'ri: `__str__` `get_daraja_display()` ni chaqiradi ✓; `save()` da `if not self.slug` — faqat birinchi marta ✓; `@classmethod` klass orqali chaqiriladi ✓.

---