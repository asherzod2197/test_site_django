## Savol 1

Django ni PIP yordamida o'rnatish uchun qaysi buyruq ishlatiladi?

- [A] `pip add django`  
- [B] `pip get django`  
- [C] `pip install django`  
- [D] `pip setup django`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `pip install django` buyrug'i PyPI dan Django ning eng yangi barqaror versiyasini yuklab o'rnatadi. Katta harf bilan ham (`Django`) yozish mumkin, natija bir xil bo'ladi.

---

## Savol 2

Django ning muayyan versiyasini, masalan 4.2 ni o'rnatish uchun qaysi buyruq to'g'ri?

- [A] `pip install django -v 4.2`  
- [B] `pip install django==4.2`  
- [C] `pip install django@4.2`  
- [D] `pip install django[4.2]`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `pip install django==4.2` buyrug'i Django ning aynan 4.2 versiyasini o'rnatadi. `==` operatori PIP da aniq versiyani belgilash uchun standart sintaksis hisoblanadi.

---

## Savol 3

Django muvaffaqiyatli o'rnatilganini tekshirish uchun qaysi buyruq ishlatiladi?

- [A] `django --version`  
- [B] `pip show django`  
- [C] `python -m django --version`  
- [D] B va C ikkalasi ham to'g'ri  

> **To'g'ri javob:** D  
> **Tushuntirish:** `pip show django` — o'rnatilgan Django haqida batafsil ma'lumot (versiya, muallif, joy) ko'rsatadi. `python -m django --version` esa faqat versiya raqamini chiqaradi. Ikkalasi ham Django o'rnatilganini tasdiqlash uchun ishlatiladi.

---

## Savol 4

Virtual muhit faollashtirilmagan holda `pip install django` buyrug'i bajarilsa, Django qayerga o'rnatiladi?

- [A] Joriy papkaga  
- [B] Tizimning umumiy (global) Python muhitiga  
- [C] Vaqtinchalik papkaga  
- [D] Brauzer keshiga  

> **To'g'ri javob:** B  
> **Tushuntirish:** Virtual muhitsiz o'rnatilgan Django tizimning umumiy Python muhitiga tushadi. Bu boshqa loyihalar bilan versiya to'qnashuviga olib kelishi mumkin. Shuning uchun har doim avval virtual muhit yaratib, faollashtirib, keyin Django o'rnatish tavsiya etiladi.

---

## Savol 5

Django o'rnatilgandan so'ng yangi loyiha yaratish uchun qaysi buyruq ishlatiladi?

- [A] `django new loyiha_nomi`  
- [B] `django-admin startproject loyiha_nomi`  
- [C] `pip start loyiha_nomi`  
- [D] `python manage.py startproject loyiha_nomi`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `django-admin startproject loyiha_nomi` buyrug'i Django o'rnatilgandan keyin yangi loyiha skelet tuzilmasini yaratadi. Bu buyruq `manage.py`, `settings.py`, `urls.py` va boshqa asosiy fayllarni avtomatik hosil qiladi.

---