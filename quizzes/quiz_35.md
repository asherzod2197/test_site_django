## Savol 1

Django nima?

- [A] JavaScript asosida ishlayдigan frontend freymvork  
- [B] Python dasturlash tili uchun yuqori darajali veb-freymvork  
- [C] Ma'lumotlar bazasini boshqarish tizimi  
- [D] Linux operatsion tizimi uchun vosita  

> **To'g'ri javob:** B  
> **Tushuntirish:** Django — Python dasturlash tili asosida yaratilgan, tez va xavfsiz veb-saytlar va veb-ilovalar qurish uchun mo'ljallangan yuqori darajali freymvork. 2005-yilda ochiq manba sifatida chiqarilgan.

---

## Savol 2

Django qaysi arxitektura patternga asoslanadi?

- [A] MVC (Model-View-Controller)  
- [B] MVP (Model-View-Presenter)  
- [C] MVT (Model-View-Template)  
- [D] MVVM (Model-View-ViewModel)  

> **To'g'ri javob:** C  
> **Tushuntirish:** Django MVT (Model-View-Template) arxitekturasiga asoslanadi. Model — ma'lumotlar bazasi bilan ishlaydi, View — biznes mantiqini bajaradi, Template — HTML sahifani ko'rsatadi.

---

## Savol 3

Django ning asosiy shiorи (motto) qaysi?

- [A] "Write once, run anywhere"  
- [B] "The web framework for perfectionists with deadlines"  
- [C] "Simple is better than complex"  
- [D] "Code less, do more"  

> **To'g'ri javob:** B  
> **Tushuntirish:** Django ning rasmiy shiari "The web framework for perfectionists with deadlines" — ya'ni "Muddatlari bor perfeksionistlar uchun veb-freymvork". Bu Django ning tez ishlab chiqishga yo'naltirilganligini bildiradi.

---

## Savol 4

Django da ORM nima vazifani bajaradi?

- [A] HTML sahifalarni yaratadi  
- [B] Python kodi orqali ma'lumotlar bazasi bilan ishlashga imkon beradi  
- [C] Foydalanuvchi autentifikatsiyasini boshqaradi  
- [D] Statik fayllarni xizmat qiladi  

> **To'g'ri javob:** B  
> **Tushuntirish:** ORM (Object-Relational Mapping) — Python obyektlari orqali ma'lumotlar bazasiga so'rov yuborish imkonini beradi. SQL yozmasdan, Python kodi orqali jadvallar yaratish va ma'lumotlar bilan ishlash mumkin.

---

## Savol 5

Django Admin paneli nima?

- [A] Django ni o'rnatish uchun ishlatiladigan buyruq satri vositasi  
- [B] Avtomatik yaratilgan, ma'lumotlar bazasini boshqarish uchun tayyor veb-interfeys  
- [C] Django loyihasini serverga joylashtirish vositasi  
- [D] Foydalanuvchilar uchun profil sahifasi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Django Admin — loyiha modellari asosida avtomatik yaratilgan kuchli boshqaruv interfeysi. Superuser ma'lumotlar bazasidagi barcha yozuvlarni ko'rish, qo'shish, tahrirlash va o'chirishi mumkin.

---

## Savol 6

Django da `migrations` nima uchun ishlatiladi?

- [A] Fayllarni bir serverdan boshqasiga ko'chirish uchun  
- [B] Model o'zgarishlarini ma'lumotlar bazasiga qo'llash uchun  
- [C] Foydalanuvchilarni bir loyihadan boshqasiga o'tkazish uchun  
- [D] Loyihani yangi versiyaga yangilash uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** Migrations — Django modellarda qilingan o'zgarishlarni (yangi jadval, ustun qo'shish, o'chirish) ma'lumotlar bazasiga aks ettiradi. `makemigrations` o'zgarishni tayyorlaydi, `migrate` esa uni bazaga qo'llaydi.

---

## Savol 7

Django da `urls.py` fayli qanday vazifani bajaradi?

- [A] Ma'lumotlar bazasi jadvallarini belgilaydi  
- [B] HTML shablonlarni saqlaydi  
- [C] URL manzillarni tegishli view funksiyalariga yo'naltiradi  
- [D] Loyiha sozlamalarini saqlaydi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `urls.py` fayli URL routing vazifasini bajaradi — har bir URL manzilni qaysi `view` funksiyasi yoki klassi qayta ishlashini belgilaydi. Bu Django ning "URL dispatcher" mexanizmi deyiladi.

---

## Savol 8

Django ning qaysi xususiyati xavfsizlikni ta'minlashda yordam beradi?

- [A] Faqat HTTPS ni qo'llab-quvvatlaydi  
- [B] CSRF himoyasi, SQL injection oldini olish va XSS himoyasi  
- [C] Faqat ro'yxatdan o'tgan foydalanuvchilarga ruxsat beradi  
- [D] Barcha so'rovlarni shifrlaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Django o'z ichida CSRF (Cross-Site Request Forgery) himoyasi, ORM orqali SQL injection dan himoya va avtomatik HTML ekranlash (XSS dan himoya) kabi muhim xavfsizlik mexanizmlarini taqdim etadi.

---

## Savol 9

Django da `settings.py` fayli nima uchun ishlatiladi?

- [A] Loyiha URL larini belgilash uchun  
- [B] Ma'lumotlar bazasi modellari yozish uchun  
- [C] Loyihaning barcha konfiguratsiya va sozlamalarini saqlash uchun  
- [D] HTML shablonlar yaratish uchun  

> **To'g'ri javob:** C  
> **Tushuntirish:** `settings.py` loyihaning markaziy konfiguratsiya fayli hisoblanadi. Unda ma'lumotlar bazasi ulanishi, o'rnatilgan ilovalar (`INSTALLED_APPS`), statik fayllar yo'li, maxfiy kalit va boshqa sozlamalar saqlanadi.

---

## Savol 10

Django da `app` (ilova) tushunchasi nimani anglatadi?

- [A] Butun Django loyihasini  
- [B] Foydalanuvchi interfeysini  
- [C] Loyiha ichidagi muayyan funksionallikni amalga oshiruvchi mustaqil modul  
- [D] Ma'lumotlar bazasi ulanishini  

> **To'g'ri javob:** C  
> **Tushuntirish:** Django loyihasi bir yoki bir nechta `app` lardan tashkil topadi. Har bir app muayyan funksionallikni — masalan, blog, do'kon, autentifikatsiya — mustaqil modul sifatida amalga oshiradi. Bu kodning qayta ishlatilishini ta'minlaydi.

---