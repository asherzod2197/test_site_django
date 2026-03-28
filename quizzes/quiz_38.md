## Savol 1

Django da yangi loyiha yaratish uchun qaysi buyruq ishlatiladi?

- [A] `django startproject loyiha_nomi`  
- [B] `django-admin startproject loyiha_nomi`  
- [C] `python manage.py startproject loyiha_nomi`  
- [D] `pip create loyiha_nomi`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `django-admin startproject loyiha_nomi` — Django o'rnatilgandan keyin yangi loyiha tuzilmasini yaratuvchi rasmiy buyruq. U `manage.py` va loyiha sozlama fayllarini avtomatik hosil qiladi.

---

## Savol 2

`startproject` buyrug'i bajarilgandan so'ng qaysi fayllar va papkalar avtomatik yaratiladi?

- [A] Faqat `settings.py` fayli  
- [B] `manage.py`, va ichida `settings.py`, `urls.py`, `wsgi.py`, `asgi.py` bo'lgan loyiha papkasi  
- [C] Faqat `manage.py` va `models.py`  
- [D] `index.html`, `style.css` va `script.js`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `startproject` buyrug'i tashqi papkada `manage.py` va loyiha nomi bilan ichki papka yaratadi. Ichki papkada `__init__.py`, `settings.py`, `urls.py`, `wsgi.py` va `asgi.py` fayllari bo'ladi.

---

## Savol 3

`manage.py` fayli qanday vazifani bajaradi?

- [A] Loyihaning HTML sahifalarini saqlaydi  
- [B] Ma'lumotlar bazasi modellarini belgilaydi  
- [C] Loyihani boshqarish uchun ishlatiladigan buyruq satri vositasi  
- [D] Foydalanuvchi autentifikatsiyasini boshqaradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `manage.py` — Django loyihasini boshqarishning asosiy vositasi. U orqali server ishga tushiriladi (`runserver`), migratsiyalar bajariladi (`migrate`), superuser yaratiladi (`createsuperuser`) va boshqa ko'plab buyruqlar ishlatiladi.

---

## Savol 4

Django loyihasini joriy papkada (alohida papka yaratmasdan) yaratish uchun qaysi buyruq ishlatiladi?

- [A] `django-admin startproject loyiha_nomi`  
- [B] `django-admin startproject loyiha_nomi --here`  
- [C] `django-admin startproject loyiha_nomi .`  
- [D] `django-admin startproject . loyiha_nomi`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `django-admin startproject loyiha_nomi .` buyrug'idagi oxirdagi nuqta (`.`) loyiha fayllarini yangi papka yaratmasdan joriy papkaga joylashtiradi. Bu Docker yoki allaqachon yaratilgan papkada ishlashda qulay usul.

---

## Savol 5

Django development serverini ishga tushirish uchun qaysi buyruq ishlatiladi?

- [A] `django-admin runserver`  
- [B] `pip start server`  
- [C] `python server.py`  
- [D] `python manage.py runserver`  

> **To'g'ri javob:** D  
> **Tushuntirish:** `python manage.py runserver` buyrug'i Django ning ichki development serverini ishga tushiradi. Server standart holda `http://127.0.0.1:8000` manzilida ishlaydi. Bu server faqat ishlab chiqish uchun mo'ljallangan, production uchun emas.

---