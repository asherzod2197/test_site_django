## Savol 1

Django loyihasidagi `manage.py` fayli qaysi papkada joylashadi?

- [A] Loyiha ichki papkasida  
- [B] `templates` papkasida  
- [C] Loyihaning tashqi (ildiz) papkasida  
- [D] `static` papkasida  

> **To'g'ri javob:** C  
> **Tushuntirish:** `manage.py` fayli loyihaning eng tashqi (root) papkasida joylashadi — `django-admin startproject` buyrug'i bajarilgan joyda. U loyihani boshqaruvchi asosiy vosita bo'lib, barcha `python manage.py ...` buyruqlari shu fayl orqali bajariladi.

---

## Savol 2

`settings.py` faylida `INSTALLED_APPS` ro'yxati nima uchun ishlatiladi?

- [A] O'rnatilgan Python paketlarini ko'rsatish uchun  
- [B] Loyihada faol bo'lgan Django ilovalari (app) va uchinchi tomon paketlarini ro'yxatga olish uchun  
- [C] Ma'lumotlar bazasi jadvallarini belgilash uchun  
- [D] URL manzillarni ro'yxatga olish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `INSTALLED_APPS` — `settings.py` dagi ro'yxat bo'lib, loyihada ishlaydigan barcha Django ilovalarini o'z ichiga oladi. Yangi app yaratilganda yoki uchinchi tomon paketi qo'shilganda, uni shu ro'yxatga kiritish shart.

---

## Savol 3

`settings.py` faylida `DEBUG = True` parametri nima vazifasini bajaradi?

- [A] Loyihani tezroq ishlashini ta'minlaydi  
- [B] Xato yuzaga kelganda brauzerda batafsil xato ma'lumotini ko'rsatadi  
- [C] Ma'lumotlar bazasini sinxronlashtiradi  
- [D] Foydalanuvchi autentifikatsiyasini yoqadi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `DEBUG = True` rejimida xato yuzaga kelganda Django brauzerda kod satrlari, o'zgaruvchilar va stack trace bilan batafsil xato sahifasini ko'rsatadi. Production da `DEBUG = False` qo'yilishi shart — aks holda maxfiy ma'lumotlar ochilishi mumkin.

---

## Savol 4

`settings.py` faylida `DATABASES` sozlamasi nima uchun ishlatiladi?

- [A] Ma'lumotlar bazasi so'rovlarini yozib borish uchun  
- [B] Loyiha ulanadigan ma'lumotlar bazasi turi, nomi va ulanish parametrlarini belgilash uchun  
- [C] Ma'lumotlar bazasi zaxira nusxasini yaratish uchun  
- [D] Foydalanuvchilar jadvalini yaratish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `DATABASES` lug'ati ma'lumotlar bazasi ulanish sozlamalarini saqlaydi. Standart holda SQLite ishlatiladi. PostgreSQL, MySQL yoki boshqa bazaga o'tish uchun shu sozlamadagi `ENGINE`, `NAME`, `USER`, `PASSWORD`, `HOST` parametrlarini o'zgartirish kerak.

---

## Savol 5

`urls.py` faylida `urlpatterns` ro'yxati nima vazifasini bajaradi?

- [A] Barcha URL manzillarni bloklash uchun  
- [B] Har bir URL manzilni tegishli view ga yo'naltiruvchi qoidalar to'plamini belgilash uchun  
- [C] Statik fayllar manzillarini saqlash uchun  
- [D] Foydalanuvchi ruxsatlarini boshqarish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `urlpatterns` — `urls.py` dagi ro'yxat bo'lib, `path()` yoki `re_path()` funksiyalari orqali URL manzillarni view funksiya yoki klasslariga bog'laydi. Brauzerdan so'rov kelganda Django shu ro'yxatdan mos URL ni qidiradi.

---

## Savol 6

`wsgi.py` fayli qanday vazifani bajaradi?

- [A] Django modellarini ma'lumotlar bazasiga ulaydi  
- [B] WSGI muvofiq veb-serverlar bilan Django loyihasini ulash uchun kirish nuqtasini taqdim etadi  
- [C] Foydalanuvchi sessiyalarini boshqaradi  
- [D] Statik fayllarni xizmat qiladi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `wsgi.py` — WSGI (Web Server Gateway Interface) standarti asosida ishlovchi Gunicorn yoki Apache kabi veb-serverlar bilan Django ni ulash uchun kirish nuqtasi. Production da server shu fayl orqali Django ilovasini ishga tushiradi.

---

## Savol 7

`asgi.py` fayli `wsgi.py` dan qanday farq qiladi?

- [A] Hech qanday farq yo'q, ikkalasi bir xil vazifani bajaradi  
- [B] `asgi.py` asinxron so'rovlar, WebSocket va real-vaqt ilovalar uchun mo'ljallangan  
- [C] `asgi.py` faqat ma'lumotlar bazasi so'rovlari uchun ishlatiladi  
- [D] `asgi.py` faqat Windows serverlarida ishlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `asgi.py` — ASGI (Asynchronous Server Gateway Interface) standarti uchun kirish nuqtasi. U `wsgi.py` dan farqli o'laroq WebSocket, long-polling va asinxron so'rovlarni qo'llab-quvvatlaydi. Django Channels bilan ishlashda `asgi.py` ishlatiladi.

---

## Savol 8

`settings.py` faylida `SECRET_KEY` nima uchun ishlatiladi?

- [A] Ma'lumotlar bazasi parolini saqlash uchun  
- [B] Sessiyalar, CSRF tokenlar va boshqa kriptografik operatsiyalar uchun ishlatiladigan maxfiy kalit  
- [C] Admin foydalanuvchi paroli uchun  
- [D] API so'rovlarini autentifikatsiya qilish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `SECRET_KEY` — Django ning kriptografik xavfsizlik mexanizmlari (sessiyalar, CSRF himoya, parol tiklash tokenlar) uchun ishlatiladigan noyob maxfiy kalit. Uni hech qachon ochiq holda GitHub ga yuklash yoki boshqalar bilan ulashish mumkin emas.

---

## Savol 9

`settings.py` faylida `TEMPLATES` sozlamasi nima uchun ishlatiladi?

- [A] Ma'lumotlar bazasi jadvallarini belgilash uchun  
- [B] Django ning template dvigatelini va shablonlar papkasini sozlash uchun  
- [C] Statik fayllar manzilini belgilash uchun  
- [D] O'rnatilgan ilovalar ro'yxatini saqlash uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `TEMPLATES` sozlamasi Django ning qaysi template dvigateli (odatda DTL) ishlatilishini, shablonlar qaysi papkadan qidirilishini (`DIRS`) va context processorlar ro'yxatini belgilaydi.

---

## Savol 10

`settings.py` faylida `STATIC_URL` parametri nima uchun ishlatiladi?

- [A] Ma'lumotlar bazasi fayli joylashgan manzilni belgilash uchun  
- [B] CSS, JavaScript va rasmlar kabi statik fayllarning URL prefiksini belgilash uchun  
- [C] Loyiha bosh sahifasining URL manzilini belgilash uchun  
- [D] Admin panel URL manzilini belgilash uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `STATIC_URL` statik fayllar (CSS, JS, rasmlar) uchun URL prefiksini belgilaydi. Standart qiymati `/static/`. HTML templateda `{% load static %}` va `{% static 'fayl.css' %}` teglari orqali ishlatiladi.

---

## Savol 11

`settings.py` faylida `ALLOWED_HOSTS` parametri nima uchun ishlatiladi?

- [A] Ruxsat berilgan foydalanuvchilar ro'yxatini saqlash uchun  
- [B] Loyihaga kirishi mumkin bo'lgan domen va IP manzillar ro'yxatini belgilash uchun  
- [C] O'rnatilgan ilovalar ro'yxatini belgilash uchun  
- [D] Ma'lumotlar bazasi serverlarini ro'yxatga olish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `ALLOWED_HOSTS` — `DEBUG = False` bo'lganda Django qabul qiladigan domen va IP manzillar ro'yxati. Masalan, `['example.com', 'www.example.com']`. Bu HTTP Host header hujumlaridan himoya qiladi. Development da `['*']` yoki `['127.0.0.1']` ishlatiladi.

---

## Savol 12

Loyiha `urls.py` faylida ilovaning (app) URL faylini ulash uchun qaysi funksiya ishlatiladi?

- [A] `link()`  
- [B] `connect()`  
- [C] `include()`  
- [D] `attach()`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `include()` funksiyasi loyihaning asosiy `urls.py` faylida ilovaning o'z `urls.py` faylini ulash uchun ishlatiladi. Masalan, `path('blog/', include('blog.urls'))` — `blog/` prefiksi bilan kelgan barcha so'rovlarni `blog` ilovasining URL fayliga yo'naltiradi.

---

## Savol 13

`__init__.py` fayli Django loyiha papkasida nima vazifasini bajaradi?

- [A] Loyiha sozlamalarini saqlaydi  
- [B] Papkani Python paketi sifatida belgilaydi  
- [C] Ma'lumotlar bazasini ishga tushiradi  
- [D] Server konfiguratsiyasini saqlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `__init__.py` — bo'sh fayl bo'lib, Python ga ushbu papka oddiy papka emas, balki Python paketi ekanligini bildiradi. Bu papkadagi modullarni boshqa joydan import qilish imkonini beradi.

---

## Savol 14

`settings.py` faylida `TIME_ZONE` parametri nima uchun ishlatiladi?

- [A] Server ishga tushish vaqtini belgilash uchun  
- [B] Loyihada ishlatiladigan vaqt mintaqasini belgilash uchun  
- [C] Sessiya muddatini belgilash uchun  
- [D] Kesh muddatini belgilash uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `TIME_ZONE` parametri loyihada ishlatiladigan vaqt mintaqasini belgilaydi. Masalan, `'Asia/Tashkent'` — O'zbekiston vaqti uchun. `USE_TZ = True` bilan birgalikda ma'lumotlar bazasida vaqt UTC da saqlanib, ko'rsatishda belgilangan vaqt mintaqasiga o'giriladi.

---

## Savol 15

`settings.py` faylida `LANGUAGE_CODE` parametri nima uchun ishlatiladi?

- [A] Dasturlash tili versiyasini belgilash uchun  
- [B] Loyihaning standart tilini belgilash uchun  
- [C] Ma'lumotlar bazasi tilini belgilash uchun  
- [D] Template tilini belgilash uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** `LANGUAGE_CODE` loyihaning standart tilini belgilaydi. Masalan, `'uz'` — o'zbek tili, `'en-us'` — ingliz tili (AQSh). Bu parametr Django admin paneli, xato xabarlari va tarjima tizimi (`i18n`) uchun ishlatiladi.

---