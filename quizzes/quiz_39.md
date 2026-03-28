## Savol 1

Django development serverini ishga tushirish uchun qaysi buyruq ishlatiladi?

- [A] `django-admin runserver`  
- [B] `python manage.py runserver`  
- [C] `python manage.py startserver`  
- [D] `pip run django`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `python manage.py runserver` — Django loyihasining ichki development serverini ishga tushiradi. Bu buyruq faqat loyiha papkasida, ya'ni `manage.py` fayli joylashgan joyda bajarilishi kerak.

---

## Savol 2

Django development serveri standart holda qaysi manzil va portda ishlaydi?

- [A] `http://localhost:3000`  
- [B] `http://0.0.0.0:8080`  
- [C] `http://127.0.0.1:8000`  
- [D] `http://localhost:5000`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Django serveri standart holda `http://127.0.0.1:8000` manzilida ishga tushadi. `127.0.0.1` — faqat mahalliy kompyuterdan kirish mumkin bo'lgan loopback manzil, `8000` esa standart port.

---

## Savol 3

Django serverni 9000-portda ishga tushirish uchun qaysi buyruq ishlatiladi?

- [A] `python manage.py runserver --port 9000`  
- [B] `python manage.py runserver -p 9000`  
- [C] `python manage.py runserver 9000`  
- [D] `python manage.py runserver :9000`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Port raqamini o'zgartirish uchun `python manage.py runserver 9000` buyrug'i ishlatiladi. Shunda server `http://127.0.0.1:9000` manzilida ishlaydi. Shuningdek, `python manage.py runserver 0.0.0.0:9000` kabi to'liq manzil ham ko'rsatish mumkin.

---

## Savol 4

`python manage.py runserver` buyrug'i bajarilganda qaysi xato `migrate` buyrug'ini ishlatish kerakligini bildiradi?

- [A] `ModuleNotFoundError`  
- [B] `You have unapplied migrations`  
- [C] `TemplateDoesNotExist`  
- [D] `ImproperlyConfigured`  

> **To'g'ri javob:** B  
> **Tushuntirish:** Server ishga tushganda `You have unapplied migrations` ogohlantirishи qo'llanilmagan migratsiyalar borligini bildiradi. `python manage.py migrate` buyrug'i bilan barcha migratsiyalarni bazaga qo'llash kerak.

---

## Savol 5

Django development serveri production (ishlab chiqarish) muhiti uchun mos keladimi?

- [A] Ha, u har qanday muhitda ishlaydi  
- [B] Ha, agar `DEBUG=False` qo'yilsa  
- [C] Yo'q, u faqat ishlab chiqish (development) uchun mo'ljallangan  
- [D] Ha, agar HTTPS ulansa  

> **To'g'ri javob:** C  
> **Tushuntirish:** Django ning ichki development serveri (`runserver`) faqat dasturlash jarayonida foydalanish uchun mo'ljallangan. Production uchun Gunicorn, uWSGI kabi WSGI serverlari va Nginx yoki Apache kabi veb-serverlar ishlatiladi.

---