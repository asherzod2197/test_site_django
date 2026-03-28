## Savol 1



Quyidagi kodning natijasi nima?

```python
print(list(range(2, 10, 2)))
```



- [A] [2, 4, 6, 8, 10] 
- [B] [2, 4, 6, 8] 
- [C] [0, 2, 4, 6, 8] 
- [D] [2, 3, 4, 5, 6, 7, 8, 9] 


> **To'g'ri javob:** B 
> **Tushuntirish:** range(2, 10, 2) — 2 dan 8 gacha, 2 qadam: 2, 4, 6, 8.


---


## Savol 2



OOP da 'Object' nima?



- [A] Classning o'zi 
- [B] Class asosida yaratilgan konkret nusxa (instance) 
- [C] Metod nomi 
- [D] Atribut qiymati 


> **To'g'ri javob:** B 
> **Tushuntirish:** Object — classdan yaratilgan konkret nusxa. Masalan, `it = It()` — `it` bu `It` classining obyekti.


---


## Savol 3



Quyidagi kodning natijasi nima?

```python
class Kafe:
    nomi = 'Bahor'

print(Kafe.nomi)
```



- [A] Xato beradi 
- [B] None 
- [C] Bahor 
- [D] Kafe 


> **To'g'ri javob:** C 
> **Tushuntirish:** Kafe.nomi — class atributiga to'g'ridan-to'g'ri murojaat: 'Bahor'.


---


## Savol 4



Quyidagi kodning natijasi nima?

```python
class Doira:
    pass

d = Doira()
print(isinstance(d, Doira))
```



- [A] False 
- [B] None 
- [C] True 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** isinstance(d, Doira) → d Doira classining instansiyasimi → True.


---


## Savol 5



Quyidagi kodning natijasi nima?

```python
class Kalkulyator:
    def qoshish(self, a, b):
        return a + b

k = Kalkulyator()
print(k.qoshish(3, 7))
```



- [A] None 
- [B] 37 
- [C] 10 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** k.qoshish(3, 7) — self=k, a=3, b=7. 3 + 7 = 10.


---


## Savol 6



self nima uchun kerak?



- [A] Faqat __init__ uchun 
- [B] Metodda obyektning o'z atributlari va metodlariga murojaat qilish uchun 
- [C] Class atributiga murojaat uchun 
- [D] Faqat parametrlarni o'tkazish uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** self — chaqirilayotgan obyektning o'zi. self.ism, self.run() kabi murojaat qilish uchun.


---


## Savol 7



Quyidagi kodning natijasi nima?

```python
class Avtomobil:
    davlat = "O'zbekiston"

a1 = Avtomobil()
a2 = Avtomobil()
a1.davlat = 'Rossiya'
print(a1.davlat)
print(a2.davlat)
```



- [A] O'zbekiston, O'zbekiston 
- [B] Rossiya, Rossiya 
- [C] Rossiya, O'zbekiston 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** a1.davlat = 'Rossiya' — a1 ga instance atribut. a2 class atributidan → O'zbekiston.


---


## Savol 8



Protected atribut qanday e'lon qilinadi?



- [A] protect self.x = 5 
- [B] self.__x = 5 
- [C] self._x = 5 
- [D] self.x = private(5) 


> **To'g'ri javob:** C 
> **Tushuntirish:** Bitta pastki chiziq _ — konventsiya bo'yicha protected: self._x.


---


## Savol 9



Method overriding nima?



- [A] Overloading 
- [B] Farzand classda ota class metodini qayta e'lon qilib, xatti-harakatini o'zgartirish 
- [C] Abstraction 
- [D] Encapsulation 


> **To'g'ri javob:** B 
> **Tushuntirish:** Method overriding — farzand classda ota class metodini qayta yozish.


---


## Savol 10



@dataclass qaysi metodlarni avtomatik yaratadi?



- [A] Faqat __init__ 
- [B] __init__, __repr__, __eq__ 
- [C] __init__, __str__, __del__ 
- [D] Faqat __repr__ 


> **To'g'ri javob:** B 
> **Tushuntirish:** @dataclass avtomatik: __init__, __repr__, __eq__ metodlarini yaratadi.


---


## Savol 11



Windows da virtual muhitni faollashtirish buyrug'i qaysi?



- [A] source venv/bin/activate 
- [B] venv\Scripts\activate 
- [C] activate venv 
- [D] python activate venv 


> **To'g'ri javob:** B 
> **Tushuntirish:** Windows: venv\Scripts\activate. Linux/Mac: source venv/bin/activate.


---


## Savol 12



Virtual muhit faollashtirilganini terminalda qanday bilish mumkin?



- [A] Imkoni yo'q 
- [B] Terminal satrining boshida (muhit_nomi) ko'rinadi 
- [C] pip --version buyrug'i 
- [D] python --check-venv 


> **To'g'ri javob:** B 
> **Tushuntirish:** Faollashtirilganda: (myenv) user@machine:~$ — qavs ichida muhit nomi ko'rinadi.


---


## Savol 13



BotFather da yangi bot yaratish uchun qaysi buyruq ishlatiladi?



- [A] /newbot 
- [B] /createbot 
- [C] /makebot 
- [D] /start 


> **To'g'ri javob:** A 
> **Tushuntirish:** /newbot — BotFather da yangi bot yaratish buyrug'i.


---


## Savol 14



Quyidagi kodda nima qilinmoqda?

```python
@dp.message(Command('start'))
async def start_handler(message: Message):
    await message.answer('Salom!')
```



- [A] start nomli funksiya yaratilmoqda 
- [B] /start komandasi uchun handler — bot 'Salom!' javobini yuboradi 
- [C] Xabar o'chirilmoqda 
- [D] Bot o'chirilmoqda 


> **To'g'ri javob:** B 
> **Tushuntirish:** @dp.message(Command('start')) — /start komandasini ushlaydi. answer() — javob yuboradi.


---


## Savol 15



Quyidagi to'liq echo bot kodida xato bormi?

```python
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

bot = Bot(token='TOKEN')
dp = Dispatcher()

@dp.message()
async def echo(message: Message):
    await message.answer(message.text)

asyncio.run(dp.start_polling(bot))
```



- [A] Ha, import noto'g'ri 
- [B] Ha, handler noto'g'ri 
- [C] Yo'q — to'liq to'g'ri echo bot 
- [D] Ha, asyncio.run noto'g'ri 


> **To'g'ri javob:** C 
> **Tushuntirish:** Bu to'liq to'g'ri minimal echo bot kodi.


---


## Savol 16



Quyidagi kodning natijasi nima?

```python
r = range(1, 10, 3)
print(list(r))
```



- [A] [1, 4, 7, 10] 
- [B] [1, 4, 7] 
- [C] [1, 3, 6, 9] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** range(1, 10, 3): 1, 4, 7 (10 kirmaydi).


---


## Savol 17



Protsedural va OOP dasturlashning farqi nima?



- [A] Hech qanday farq yo'q 
- [B] Protsedural — funksiyalar ketma-ketligi; OOP — ma'lumot va xulq-atvor bitta obyektda 
- [C] OOP faqat raqamlar bilan ishlaydi 
- [D] Protsedural yangi, OOP eski paradigma 


> **To'g'ri javob:** B 
> **Tushuntirish:** Protsedural — funksiyalar ketma-ketligi. OOP — ma'lumot va xulq-atvor bitta obyektda birlashadi.


---


## Savol 18



Class va funksiya o'rtasidagi asosiy farq nima?



- [A] Hech qanday farq yo'q 
- [B] Class — atributlar va metodlarni birlashtiruvchi tuzilma; funksiya — faqat amallar bajaradi 
- [C] Funksiya tezroq ishlaydi 
- [D] Class faqat raqamlar bilan ishlaydi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Class — ma'lumot va xulq-atvor birlashtiradi. Funksiya — faqat amallar bajaradi.


---


## Savol 19



Quyidagi kodning natijasi nima?

```python
class Raqam:
    qiymat = 10

r = Raqam()
print(type(r))
print(type(Raqam))
```



- [A] <class 'int'>, <class 'int'> 
- [B] <class '__main__.Raqam'>, <class 'type'> 
- [C] <class 'object'>, <class 'type'> 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** type(r) → <class '__main__.Raqam'>. type(Raqam) → <class 'type'>.


---


## Savol 20



Quyidagi kodning natijasi nima?

```python
class Shakllar:
    def yuza(self, a, b):
        return a * b

    def perimetr(self, a, b):
        return 2 * (a + b)

s = Shakllar()
print(s.yuza(4, 5))
print(s.perimetr(4, 5))
```



- [A] 20, 18 
- [B] 9, 18 
- [C] 20, 9 
- [D] Xato beradi 


> **To'g'ri javob:** A 
> **Tushuntirish:** yuza(4,5) → 4*5=20. perimetr(4,5) → 2*(4+5)=18.


---


## Savol 21



Quyidagi kodning natijasi nima?

```python
class Doira:
    def __init__(self, r):
        self.r = r

    def yuza(self):
        return 3.14 * self.r ** 2

d = Doira(3)
print(d.yuza())
```



- [A] 9.42 
- [B] 28.26 
- [C] 18.84 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** 3.14 * 3**2 = 3.14 * 9 = 28.26.


---


## Savol 22



Quyidagi kodning natijasi nima?

```python
class Mehmon:
    pass

m = Mehmon()
m.ism = 'Zulfiya'
m.yosh = 25
print(hasattr(m, 'ism'))
print(hasattr(m, 'manzil'))
```



- [A] True, True 
- [B] True, False 
- [C] False, True 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** ism atributi bor → True. manzil atributi yo'q → False.


---


## Savol 23



Quyidagi kodning natijasi nima?

```python
class Maxfiy:
    def __init__(self):
        self.__sir = 'yashirin'

    def sir_ol(self):
        return self.__sir

m = Maxfiy()
print(m.sir_ol())
```



- [A] AttributeError 
- [B] None 
- [C] yashirin 
- [D] __sir 


> **To'g'ri javob:** C 
> **Tushuntirish:** __sir — private, lekin sir_ol() metodi orqali ichkaridan kirish mumkin → 'yashirin'.


---


## Savol 24



Ko'p bosqichli meros (multilevel inheritance) nima?



- [A] Bir class bir nechta classdan meros olishi 
- [B] A → B → C ko'rinishida zanjirsimon meros 
- [C] Bir class ikki marta meros olishi 
- [D] Faqat ikki classdan iborat meros 


> **To'g'ri javob:** B 
> **Tushuntirish:** Multilevel: A dan B, B dan C meros oladi. C — A va B ning barcha xususiyatlariga ega.


---


## Savol 25



@dataclass bilan yaratilgan obyektni print qilsak nima ko'rinadi?



- [A] Xotira manzili 
- [B] ClassName(field1=val1, field2=val2, ...) ko'rinishida 
- [C] None 
- [D] Faqat class nomi 


> **To'g'ri javob:** B 
> **Tushuntirish:** @dataclass __repr__ yaratadi → Nuqta(x=1.0, y=2.0) ko'rinishida chiqaradi.


---


## Savol 26



self nima?



- [A] Python kalit so'zi 
- [B] Instance metodidagi chaqirilayotgan obyektga havola 
- [C] Class nomi 
- [D] Atribut qiymati 


> **To'g'ri javob:** B 
> **Tushuntirish:** self — instance metodining birinchi parametri bo'lib, chaqirilayotgan obyektning o'ziga ishora qiladi.


---


## Savol 27



Atribut nima?



- [A] Classning funksiyasi 
- [B] Obyekt yoki class ga tegishli ma'lumot (o'zgaruvchi) 
- [C] Python kalit so'zi 
- [D] Modul nomi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Atribut — class yoki obyektga tegishli ma'lumot. Masalan, mashina.rang, mashina.tezlik.


---


## Savol 28



Encapsulation (inkapsulyatsiya) nima?



- [A] Bir classdan boshqasiga meros olish 
- [B] Ma'lumotlar va metodlarni bitta classda birlashtirish va tashqaridan kirishni cheklash 
- [C] Funksiyalarni qayta ishlatish 
- [D] Kodlarni qisqartirish usuli 


> **To'g'ri javob:** B 
> **Tushuntirish:** Encapsulation — ma'lumot va metodlarni yashirish, tashqi kirishni cheklash.


---


## Savol 29



Inheritance (meros olish) nima?



- [A] Bir xil nomli metodlarni qayta ishlatish 
- [B] Mavjud classning atribut va metodlarini yangi class tomonidan meros qilib olish mexanizmi 
- [C] Ma'lumotlarni yashirish usuli 
- [D] Faqat atributlarni boshqa classga ko'chirish 


> **To'g'ri javob:** B 
> **Tushuntirish:** Inheritance — OOP ning asosiy tamoyillaridan biri. Ota class xususiyatlarini farzand class meros oladi.


---


## Savol 30



@dataclass dekoratori nima?



- [A] Classni o'chirish uchun 
- [B] Class uchun __init__, __repr__, __eq__ metodlarini avtomatik yaratuvchi dekorator 
- [C] Classni import qilish uchun 
- [D] Faqat atributlarni chiqarish uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** @dataclass — boilerplate kodni (takroriy __init__ va boshqa metodlar) avtomatik yaratadi.


---


## Savol 31



Virtual environment (virtual muhit) nima?



- [A] Operatsion tizimning virtual versiyasi 
- [B] Loyiha uchun izolyatsiyalangan Python muhiti — alohida kutubxonalar bilan 
- [C] Python ning yangi versiyasi 
- [D] Faqat web uchun muhit 


> **To'g'ri javob:** B 
> **Tushuntirish:** Virtual muhit — har bir loyiha uchun alohida izolyatsiyalangan Python va kutubxonalar to'plami.


---


## Savol 32



venv moduli Python ning nechanchi versiyasida o'rnatilgan keladi?



- [A] Python 2.7 
- [B] Python 3.3+ 
- [C] Python 3.8+ 
- [D] Faqat Python 3.10+ 


> **To'g'ri javob:** B 
> **Tushuntirish:** venv — Python 3.3 dan boshlab standart kutubxonaga kiritilgan.


---


## Savol 33



Telegram bot nima?



- [A] Oddiy Telegram foydalanuvchisi 
- [B] Telegram da avtomatik javob beruvchi va vazifalar bajaruvchi dastur 
- [C] Faqat xabar yuboruvchi dastur 
- [D] Telegram serverining bir qismi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Telegram bot — Telegram API orqali boshqariladigan, avtomatik javob beruvchi va turli vazifalar bajaruvchi dastur.


---


## Savol 34



Aiogram nima?



- [A] Telegram rasmniy kutubxonasi 
- [B] Python da Telegram bot yaratish uchun asynchronous kutubxona 
- [C] Faqat Django uchun 
- [D] Web framework 


> **To'g'ri javob:** B 
> **Tushuntirish:** Aiogram — Python da async/await asosida Telegram bot yaratish uchun kuchli kutubxona.


---


## Savol 35



Echo bot nima?



- [A] Faqat /start komandasini qabul qiladigan bot 
- [B] Foydalanuvchi yozgan har qanday xabarni aynan qaytarib yuboradigan bot 
- [C] Faqat rasm yuboradigan bot 
- [D] Admin uchun boshqaruv boti 


> **To'g'ri javob:** B 
> **Tushuntirish:** Echo bot — foydalanuvchi yozgan har qanday matnni o'sha shaklda qaytarib yuboradi.


---