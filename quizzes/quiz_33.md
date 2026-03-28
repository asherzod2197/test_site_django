## Savol 1

Python'da virtual muhit (virtual environment) yaratish uchun qaysi modul ishlatiladi?

- [A] `virtualenv`  
- [B] `venv`  
- [C] `env`  
- [D] `pyenv`  

> **To'g'ri javob:** B  
> **Tushuntirish:** `venv` — Python 3.3 dan boshlab standart kutubxonaga kiritilgan modul bo'lib, virtual muhit yaratish uchun ishlatiladi. Uni alohida o'rnatish shart emas.

---

## Savol 2

`myenv` nomli virtual muhit yaratish uchun qaysi buyruq to'g'ri?

- [A] `python -m venv create myenv`  
- [B] `python venv myenv`  
- [C] `python -m venv myenv`  
- [D] `venv create myenv`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `python -m venv myenv` buyrug'i joriy papkada `myenv` nomli virtual muhit papkasini yaratadi. `-m` flagi modulni to'g'ridan-to'g'ri ishga tushirish uchun ishlatiladi.

---

## Savol 3

Windows tizimida virtual muhitni faollashtirish uchun qaysi buyruq ishlatiladi?

- [A] `source myenv/bin/activate`  
- [B] `myenv\Scripts\activate`  
- [C] `activate myenv`  
- [D] `myenv/activate.bat`  

> **To'g'ri javob:** B  
> **Tushuntirish:** Windows'da virtual muhitni faollashtirish uchun `myenv\Scripts\activate` buyrug'i ishlatiladi. Faollashgandan so'ng terminal satri boshida `(myenv)` ko'rinadi.

---

## Savol 4

Linux va macOS tizimlarida virtual muhitni faollashtirish uchun qaysi buyruq ishlatiladi?

- [A] `myenv\Scripts\activate`  
- [B] `activate myenv`  
- [C] `source myenv/bin/activate`  
- [D] `run myenv/activate`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Linux va macOS'da `source myenv/bin/activate` buyrug'i virtual muhitni faollashtiradi. `source` buyrug'i skriptni joriy terminalda bajaradi.

---

## Savol 5

Faol virtual muhitni o'chirish (deaktivatsiya) uchun qaysi buyruq ishlatiladi?

- [A] `stop`  
- [B] `exit`  
- [C] `venv off`  
- [D] `deactivate`  

> **To'g'ri javob:** D  
> **Tushuntirish:** `deactivate` buyrug'i barcha operatsion tizimlarda bir xil ishlaydi va faol virtual muhitni o'chirib, tizimning asosiy Python muhitiga qaytaradi.

---

## Savol 6

Virtual muhit yaratilganda uning ichida qanday papkalar hosil bo'ladi?

- [A] `src`, `lib`, `bin`  
- [B] `Scripts` (yoki `bin`), `Lib` (yoki `lib`), `Include`  
- [C] `packages`, `modules`, `cache`  
- [D] `python`, `pip`, `site`  

> **To'g'ri javob:** B  
> **Tushuntirish:** Virtual muhit papkasida `Scripts/bin` (bajariladigan fayllar), `Lib/lib` (o'rnatilgan paketlar) va `Include` (sarlavha fayllar) papkalari yaratiladi.

---

## Savol 7

Virtual muhitda o'rnatilgan paketlar qayerda saqlanadi?

- [A] Tizimning umumiy Python papkasida  
- [B] Foydalanuvchining `Documents` papkasida  
- [C] Virtual muhit papkasi ichidagi `Lib/site-packages` papkasida  
- [D] `C:/Python/packages` papkasida  

> **To'g'ri javob:** C  
> **Tushuntirish:** Virtual muhit faollashtirilganda `pip install` bilan o'rnatilgan barcha paketlar `myenv/Lib/site-packages/` papkasiga joylashadi va faqat shu muhitda ko'rinadi.

---

## Savol 8

Quyidagi buyruqlardan qaysi biri virtual muhitni tizim paketlarisiz (izolyatsiya qilingan holda) yaratadi?

- [A] `python -m venv myenv --no-pip`  
- [B] `python -m venv myenv`  
- [C] `python -m venv myenv --system-site-packages`  
- [D] `python -m venv myenv --global`  

> **To'g'ri javob:** B  
> **Tushuntirish:** Standart holda `python -m venv myenv` buyrug'i to'liq izolyatsiya qilingan muhit yaratadi. `--system-site-packages` flagi esa aksincha — tizimda o'rnatilgan paketlarni virtual muhitda ham ko'rinadigan qiladi.

---

## Savol 9

Bir nechta loyiha bir xil paketning turli versiyalarini ishlatishi kerak bo'lsa, qaysi yondashuv to'g'ri?

- [A] Har safar PIP ni qayta o'rnatish  
- [B] Har bir loyiha uchun alohida virtual muhit yaratish  
- [C] Paketni ikki marta o'rnatish  
- [D] Faqat eng yangi versiyani ishlatish  

> **To'g'ri javob:** B  
> **Tushuntirish:** Virtual muhitlar aynan shu muammo uchun yaratilgan. Har bir loyiha o'zining izolyatsiya qilingan muhitida ishlaydi, shuning uchun versiyalar o'rtasida to'qnashuv bo'lmaydi.

---

## Savol 10

`python -m venv myenv --copies` buyrug'idagi `--copies` flagi nima vazifani bajaradi?

- [A] Virtual muhitni nusxalab boshqa joyga saqlaydi  
- [B] Python va pip fayllarini simvolik havola o'rniga to'g'ridan-to'g'ri nusxa sifatida joylashtiradi  
- [C] Virtual muhitni avtomatik faollashtiradi  
- [D] O'rnatilgan paketlarning zaxira nusxasini yaratadi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `--copies` flagi Python interpretatori va skriptlarni simvolik havola (symlink) o'rniga haqiqiy nusxa sifatida virtual muhitga joylashtiradi. Bu ayniqsa Windows'da yoki asl fayllar o'chirilgan holatlarda foydali bo'ladi.

---