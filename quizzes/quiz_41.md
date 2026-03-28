## Savol 1

Django da yangi app yaratish uchun qaysi buyruq ishlatiladi?

- [A] `django new app nomi`
- [B] `python manage.py startapp nomi`
- [C] `python manage.py createapp nomi`
- [D] `django-admin newapp nomi`

> **To'g'ri javob:** B
> **Tushuntirish:** `python manage.py startapp nomi` — Django loyihasida yangi app (ilova) yaratishning standart buyrug'i. `startapp` app papkasini va uning ichidagi barcha zaruriy fayllarni avtomatik yaratadi.

---

## Savol 2

`startapp` buyrug'i bajarilgandan so'ng qaysi fayllar **avtomatik** yaratilmaydi?

- [A] `models.py`
- [B] `views.py`
- [C] `urls.py`
- [D] `apps.py`

> **To'g'ri javob:** C
> **Tushuntirish:** `startapp` faqat `models.py`, `views.py`, `apps.py`, `admin.py`, `tests.py` va `migrations/` papkasini yaratadi. `urls.py` fayli **avtomatik yaratilmaydi** — uni dasturchi o'zi qo'lda yaratishi kerak.

---

## Savol 3

App yaratilgandan keyin uni loyihaga ulash uchun qaysi fayl o'zgartiriladi?

- [A] `manage.py`
- [B] `wsgi.py`
- [C] `settings.py` → `INSTALLED_APPS`
- [D] `asgi.py`

> **To'g'ri javob:** C
> **Tushuntirish:** Yangi app `settings.py` faylining `INSTALLED_APPS` ro'yxatiga qo'shilishi **shart**. Aks holda Django bu appni ko'rmaydi: migrations ishlamaydi, modellar e'tirof etilmaydi, admin panelda ko'rinmaydi.

---

## Savol 4

`INSTALLED_APPS` ga app qo'shishning to'g'ri usuli qaysi?

- [A] `'blog'` yoki `'blog.apps.BlogConfig'`
- [B] `blog.py`
- [C] `import blog`
- [D] `APPS = ['blog']`

> **To'g'ri javob:** A
> **Tushuntirish:** Ikki usul to'g'ri: oddiy `'blog'` yoki `apps.py` dagi config klassi orqali `'blog.apps.BlogConfig'`. Ikkinchi usul tavsiya etiladi, chunki u app konfiguratsiyasini to'liq nazorat qilish imkonini beradi.

---

## Savol 5

Quyidagi `apps.py` kodida `name` atributi nima vazifani bajaradi?

```python
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
```

- [A] App ning ko'rsatiladigan nomini belgilaydi
- [B] App ning Python import yo'lini belgilaydi — Django shu nom bilan appni topadi
- [C] Ma'lumotlar bazasi jadval nomini belgilaydi
- [D] URL yo'lini belgilaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `name = 'blog'` — Django ning bu app ni Python paketi sifatida topishi uchun zarur import yo'lidir. Agar loyiha papkasi ichida bo'lsa `name = 'myproject.blog'` ko'rinishida yoziladi.

---

## Savol 6

`startapp` buyrug'i yaratgan `migrations/` papkasining vazifasi nima?

- [A] Statik fayllarni saqlash
- [B] Ma'lumotlar bazasi sxemasidagi o'zgarishlarni kuzatib borish
- [C] Foydalanuvchi fayllarini yuklash
- [D] Test natijalarini saqlash

> **To'g'ri javob:** B
> **Tushuntirish:** `migrations/` — modellarda qilingan o'zgarishlar tarixini saqlaydi. `makemigrations` yangi migration fayl yaratadi, `migrate` esa shu o'zgarishlarni ma'lumotlar bazasiga qo'llaydi. `__init__.py` bu papkani Python paketi sifatida belgilaydi.

---

## Savol 7

Bir loyihada nechta app bo'lishi mumkin?

- [A] Faqat 1 ta
- [B] Maksimal 5 ta
- [C] Maksimal 10 ta
- [D] Cheklovsiz — keraklicha app yaratish mumkin

> **To'g'ri javob:** D
> **Tushuntirish:** Django loyihasida app soni cheklanmagan. Katta loyihalarda `users`, `blog`, `shop`, `orders`, `payments` kabi ko'plab applar bo'lishi odatiy holat. Har bir app mustaqil funksionallikni o'z ichiga oladi.

---

## Savol 8

Quyidagi buyruqlar ketma-ketligining to'g'ri tartibi qaysi?

```
1. python manage.py migrate
2. django-admin startproject mysite
3. python manage.py startapp blog
4. INSTALLED_APPS ga 'blog' qo'shish
```

- [A] `1 → 2 → 3 → 4`
- [B] `2 → 3 → 4 → 1`
- [C] `3 → 2 → 4 → 1`
- [D] `2 → 1 → 3 → 4`

> **To'g'ri javob:** B
> **Tushuntirish:** Avval loyiha yaratiladi (`startproject`), so'ng app (`startapp`), keyin `settings.py` ga app qo'shiladi, oxirida `migrate` bilan ma'lumotlar bazasi sozlanadi. Bu Django ni boshlash uchun standart ketma-ketlik.

---

## Savol 9

`admin.py` faylining asosiy vazifasi nima?

- [A] URL marshrutlarini belgilash
- [B] Modellarni Django admin paneliga ro'yxatdan o'tkazish
- [C] Ma'lumotlar bazasi ulanishini sozlash
- [D] Middleware qo'shish

> **To'g'ri javob:** B
> **Tushuntirish:** `admin.py` da modellar `admin.site.register(ModelNomi)` orqali ro'yxatdan o'tkaziladi. Shundan so'ng `/admin/` sahifasida ushbu modellar ko'rinib, ma'lumotlarni boshqarish imkoni paydo bo'ladi.

---

## Savol 10

`tests.py` faylining vazifasi nima?

- [A] Loyihani test serverda ishga tushirish
- [B] App uchun avtomatik testlar yozish
- [C] Ma'lumotlar bazasini test rejimida ochish
- [D] Foydalanuvchi kirishini tekshirish

> **To'g'ri javob:** B
> **Tushuntirish:** `tests.py` — app uchun unit va integration testlar yoziladigan fayl. `python manage.py test` buyrug'i shu fayldagi testlarni topib ishga tushiradi. `TestCase` klassi Django ning test frameworki asosini tashkil etadi.

---

## Savol 11

Quyidagi `views.py` kodida xato bormi?

```python
def bosh_sahifa(request):
    return render(request, 'blog/index.html')
```

- [A] Ha — `request` parametri noto'g'ri
- [B] Ha — `render` import qilinmagan
- [C] Ha — funksiya nomi noto'g'ri
- [D] Xato yo'q, lekin `from django.shortcuts import render` import qilingan bo'lishi kerak

> **To'g'ri javob:** D
> **Tushuntirish:** Funksiya sintaktik jihatdan to'g'ri. Lekin `render` ni ishlatish uchun faylning yuqorisida `from django.shortcuts import render` yozilishi shart. Bu import `startapp` da avtomatik yozib qo'yiladi.

---

## Savol 12

App nomini belgilashda qaysi qoida to'g'ri?

- [A] App nomi bo'sh joy va katta harf bilan boshlanishi mumkin: `My Blog`
- [B] App nomi kichik harf, raqam va pastki chiziq (`_`) dan iborat bo'lishi kerak: `my_blog`
- [C] App nomi raqam bilan boshlanishi mumkin: `1blog`
- [D] App nomi tire (`-`) bilan yoziladi: `my-blog`

> **To'g'ri javob:** B
> **Tushuntirish:** App nomi Python modul nomi sifatida ishlatiladi, shuning uchun Python identifikatori qoidalariga bo'ysunishi kerak: kichik harf bilan boshlash, bo'sh joy yo'q, tire yo'q, raqam bilan boshlanmaydi. `my_blog` kabi snake_case tavsiya etiladi.

---

## Savol 13

`default_auto_field = 'django.db.models.BigAutoField'` qatori nima vazifani bajaradi?

- [A] Barcha maydonlar uchun standart o'lchamni belgilaydi
- [B] Birlamchi kalit (primary key) maydonining standart turini belgilaydi
- [C] Ma'lumotlar bazasi serverini tanlaydi
- [D] Migratsiya versiyasini belgilaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `default_auto_field` — modellarda `id` maydoni uchun standart avtomatik birlamchi kalit turini belgilaydi. `BigAutoField` — 64-bitli butun son (1 dan 9.2×10¹⁸ gacha). Django 3.2 dan boshlab standart qiymat sifatida ishlatiladi.

---

## Savol 14

Quyidagi loyiha strukturasida `blog` app to'g'ri joylashganmi?

```
mysite/
    manage.py
    mysite/
        settings.py
        urls.py
    blog/
        __init__.py
        models.py
        views.py
        apps.py
```

- [A] Yo'q — `blog` `mysite/mysite/` ichida bo'lishi kerak
- [B] Ha — `manage.py` bilan bir darajada joylashishi to'g'ri
- [C] Yo'q — `blog` `manage.py` dan yuqorida bo'lishi kerak
- [D] Yo'q — `blog` alohida loyiha bo'lishi kerak

> **To'g'ri javob:** B
> **Tushuntirish:** `startapp` buyrug'i `manage.py` turgan katalogda ishga tushiriladi va app shu yerda yaratiladi. `mysite/` (loyiha paketi) va `blog/` (app paketi) `manage.py` bilan bir darajada turishi — to'g'ri va standart Django strukturasi.

---

## Savol 15

Quyidagi vaziyatda nima muammo bor?

```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... boshqa standart applar
    # 'blog' qo'shilmagan!
]
```
```python
# blog/models.py
class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
```
```bash
$ python manage.py makemigrations
```

- [A] Hech qanday muammo yo'q — migrations yaratiladi
- [B] `blog` `INSTALLED_APPS` ga qo'shilmaganligi sababli `Maqola` modeli uchun migration **yaratilmaydi**
- [C] `models.py` fayli yo'qligi sabab xato beradi
- [D] `makemigrations` ning o'zi appni avtomatik topadi

> **To'g'ri javob:** B
> **Tushuntirish:** Django faqat `INSTALLED_APPS` da ro'yxatdan o'tgan applarning modellarini kuzatadi. `blog` qo'shilmagan bo'lsa, `makemigrations` `blog` app uchun hech qanday migration yaratmaydi va `No changes detected` xabari chiqadi. Yechim: `'blog'` yoki `'blog.apps.BlogConfig'` ni `INSTALLED_APPS` ga qo'shish.

---