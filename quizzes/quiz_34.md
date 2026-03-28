## Savol 1

Virtual muhit faollashtirilganligini terminalda qanday bilish mumkin?

- [A] Terminal rangi o'zgaradi  
- [B] Terminal satrining boshida muhit nomi `(myenv)` ko'rinishida chiqadi  
- [C] Python versiyasi o'zgaradi  
- [D] Yangi oyna ochiladi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Virtual muhit faollashtirilganda terminal satri boshida `(myenv)` kabi qavs ichida muhit nomi ko'rinadi. Bu muhit hozir faol ekanligini bildiradi.

---

## Savol 2

Windows CMD da virtual muhitni faollashtirish uchun qaysi buyruq ishlatiladi?

- [A] `source myenv/bin/activate`  
- [B] `./myenv/activate`  
- [C] `myenv\Scripts\activate.bat`  
- [D] `bash myenv\activate`  

> **To'g'ri javob:** C  
> **Tushuntirish:** Windows CMD da `myenv\Scripts\activate.bat` yoki qisqacha `myenv\Scripts\activate` buyrug'i virtual muhitni faollashtiradi. `.bat` kengaytmali fayl CMD uchun mo'ljallangan.

---

## Savol 3

Windows PowerShell da virtual muhitni faollashtirish uchun qaysi buyruq ishlatiladi?

- [A] `myenv\Scripts\activate.bat`  
- [B] `myenv\Scripts\Activate.ps1`  
- [C] `source myenv/Scripts/activate`  
- [D] `powershell myenv\activate`  

> **To'g'ri javob:** B  
> **Tushuntirish:** PowerShell da `myenv\Scripts\Activate.ps1` skripti ishlatiladi. Ba'zida skript bajarishga ruxsat berish uchun avval `Set-ExecutionPolicy RemoteSign` buyrug'ini ishlatish kerak bo'ladi.

---

## Savol 4

Linux va macOS da `source` o'rniga qaysi qisqartma bilan ham virtual muhitni faollashtirish mumkin?

- [A] `run myenv/bin/activate`  
- [B] `exec myenv/bin/activate`  
- [C] `. myenv/bin/activate`  
- [D] `sh myenv/bin/activate`  

> **To'g'ri javob:** C  
> **Tushuntirish:** `. myenv/bin/activate` — bu `source myenv/bin/activate` buyrug'ining qisqartmasi. Nuqta (`.`) POSIX shellda `source` bilan bir xil vazifani bajaradi.

---

## Savol 5

Virtual muhit faollashtirilgandan keyin `pip install` buyrug'i paketni qayerga o'rnatadi?

- [A] Tizimning umumiy Python papkasiga  
- [B] Foydalanuvchining uy papkasiga  
- [C] Faol virtual muhitning `site-packages` papkasiga  
- [D] Joriy ishchi papkaga  

> **To'g'ri javob:** C  
> **Tushuntirish:** Virtual muhit faollashtirilganda `pip` avtomatik ravishda o'sha muhitning `Lib/site-packages` papkasini ko'rsatadi va barcha paketlar shu yerga o'rnatiladi.

---

## Savol 6

Qaysi buyruq virtual muhit faol yoki emasligidan qat'i nazar, uning Python interpretatorini to'g'ridan-to'g'ri ishlatadi?

- [A] `python script.py`  
- [B] `myenv/bin/python script.py` (Linux) yoki `myenv\Scripts\python script.py` (Windows)  
- [C] `venv python script.py`  
- [D] `activate && python script.py`  

> **To'g'ri javob:** B  
> **Tushuntirish:** Virtual muhitni faollashtirmasdan ham uning Python interpretatoriga to'liq yo'l ko'rsatib ishlatish mumkin. Bu avtomatlashtirish skriptlarida qulay usul hisoblanadi.

---

## Savol 7

PowerShell da virtual muhitni faollashtirishda `cannot be loaded because running scripts is disabled` xatosi chiqsa, qanday hal qilinadi?

- [A] Virtual muhitni qayta yaratish  
- [B] `Set-ExecutionPolicy Unrestricted -Scope CurrentUser` buyrug'ini ishlatish  
- [C] Python ni qayta o'rnatish  
- [D] CMD ga o'tish va u yerda faollashtirish  

> **To'g'ri javob:** B  
> **Tushuntirish:** Bu xato PowerShell da skript bajarishga ruxsat yo'qligini bildiradi. `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` yoki `Unrestricted` buyrug'i bilan joriy foydalanuvchi uchun ruxsat beriladi.

---

## Savol 8

Virtual muhit faollashtirilganda `PATH` muhit o'zgaruvchisida qanday o'zgarish bo'ladi?

- [A] `PATH` o'zgaruvchisi to'liq o'chiriladi  
- [B] Virtual muhitning `Scripts/bin` papkasi `PATH` ning boshiga qo'shiladi  
- [C] `PATH` o'zgaruvchisi tizim papkasiga yo'naltiriladi  
- [D] Hech qanday o'zgarish bo'lmaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Faollashtirish skripti virtual muhitning `Scripts` (Windows) yoki `bin` (Linux/macOS) papkasini `PATH` o'zgaruvchisining boshiga qo'shadi. Shuning uchun `python` va `pip` buyruqlari virtual muhitnikini ishlatadi.

---

## Savol 9

`deactivate` buyrug'i ishlatilgandan keyin qanday holat yuzaga keladi?

- [A] Virtual muhit papkasi o'chiriladi  
- [B] Terminal yopiladi  
- [C] Tizimning asosiy Python muhitiga qaytiladi va `PATH` asl holatiga keladi  
- [D] Barcha o'rnatilgan paketlar o'chiriladi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `deactivate` buyrug'i `PATH` o'zgaruvchisidan virtual muhit yo'lini olib tashlaydi va tizimning asosiy Python muhitiga qaytaradi. Virtual muhit papkasi va uning paketlari o'zgarmaydi.

---

## Savol 10

Quyidagi holatlardan qaysi biri virtual muhit to'g'ri faollashtirilmaganligini bildiradi?

- [A] Terminal satrida `(myenv)` ko'rinadi  
- [B] `pip list` faqat bir nechta paket ko'rsatadi  
- [C] `which python` yoki `where python` buyrug'i tizim Python yo'lini ko'rsatadi  
- [D] `python --version` buyrug'i ishlaydi  

> **To'g'ri javob:** C  
> **Tushuntirish:** `which python` (Linux/macOS) yoki `where python` (Windows) buyrug'i virtual muhit faollashtirilgan bo'lsa, uning yo'lini ko'rsatishi kerak. Agar tizim Python yo'lini ko'rsatsa, virtual muhit faol emas demakdir.

---