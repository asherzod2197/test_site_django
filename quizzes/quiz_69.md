## Savol 1



range() funksiyasining to'liq sintaksisi qanday?



- [A] range(stop) 
- [B] range(start, stop) 
- [C] range(start, stop, step) 
- [D] range(step, start, stop) 


> **To'g'ri javob:** C 
> **Tushuntirish:** range(start, stop, step) — start: boshlang'ich, stop: tugash (kirmaydi), step: qadam. Faqat stop berilsa start=0, step=1 bo'ladi.


---


## Savol 2



OOP ning asosiy 4 tamoyili qaysilar?



- [A] Funksiya, Tsikl, Shart, O'zgaruvchi 
- [B] Encapsulation, Inheritance, Polymorphism, Abstraction 
- [C] Class, Object, Method, Attribute 
- [D] Import, Module, Package, Library 


> **To'g'ri javob:** B 
> **Tushuntirish:** OOP 4 tamoyili: Encapsulation, Inheritance, Polymorphism, Abstraction.


---


## Savol 3



Class nomini yozishda qaysi uslub tavsiya etiladi?



- [A] kichik_harf 
- [B] KATTA_HARF 
- [C] CamelCase (har so'z bosh harf) 
- [D] camelCase 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da class nomlari CamelCase: Mashina, BankHisobi, OnlineDokon.


---


## Savol 4



Quyidagi kodning natijasi nima?

```python
class It:
    ovoz = 'Vov'

i1 = It()
i2 = It()
print(i1.ovoz)
print(i2.ovoz)
```



- [A] Xato beradi 
- [B] Vov, Vov 
- [C] None, None 
- [D] Vov, None 


> **To'g'ri javob:** B 
> **Tushuntirish:** i1 va i2 — It classining ikki obyekti. Ikkalasi ovoz atributini meros oladi → Vov.


---


## Savol 5



Instance metodning birinchi parametri nima bo'lishi shart?



- [A] cls 
- [B] this 
- [C] self 
- [D] object 


> **To'g'ri javob:** C 
> **Tushuntirish:** self — instance metodining birinchi parametri. Chaqirilayotgan obyektni ko'rsatadi.


---


## Savol 6



self ixtiyoriy nommi yoki majburiy?



- [A] Majburiy, faqat 'self' deb yozilishi kerak 
- [B] Ixtiyoriy nom, lekin 'self' ishlatish konventsiya 
- [C] Har doim 'this' deb yoziladi 
- [D] Har doim 'object' deb yoziladi 


> **To'g'ri javob:** B 
> **Tushuntirish:** self — konventsiya bo'yicha nom. Texnik jihatdan boshqa nom ham bo'ladi, lekin self standart.


---


## Savol 7



Instance atribut va class atributning farqi nima?



- [A] Hech qanday farq yo'q 
- [B] Instance atribut — har obyektga xos, class atribut — barcha obyektlar uchun umumiy 
- [C] Class atribut tezroq ishlaydi 
- [D] Instance atribut faqat __init__ da bo'ladi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Class atribut — barcha instansiyalarga umumiy. Instance atribut — faqat o'sha obyektga xos.


---


## Savol 8



Python da private atribut qanday e'lon qilinadi?



- [A] private self.x = 5 
- [B] self.x = 5 
- [C] self.__x = 5 
- [D] self._private_x = 5 


> **To'g'ri javob:** C 
> **Tushuntirish:** Ikki pastki chiziq __ — private atribut: self.__x. Tashqaridan to'g'ridan-to'g'ri kirish mumkin emas.


---


## Savol 9



Python da meros olish qanday yoziladi?



- [A] class Farzand extends Ota: 
- [B] class Farzand inherits Ota: 
- [C] class Farzand(Ota): 
- [D] class Farzand -> Ota: 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da meros olish: class FarzandClass(OtaClass):


---


## Savol 10



@dataclass dan foydalanish uchun nima import qilinadi?



- [A] from class import dataclass 
- [B] from dataclasses import dataclass 
- [C] import dataclass 
- [D] from python import dataclass 


> **To'g'ri javob:** B 
> **Tushuntirish:** from dataclasses import dataclass — to'g'ri import.


---


## Savol 11



Virtual environment nima uchun kerak?



- [A] Python ni o'rnatish uchun 
- [B] Har bir loyiha uchun alohida kutubxona versiyalarini boshqarish uchun 
- [C] Dasturni tezlashtirish uchun 
- [D] Faqat Windows uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** Loyiha A: Django 3.2, Loyiha B: Django 4.0 — virtual muhit bu konfliktni hal qiladi.


---


## Savol 12



Quyidagi buyruq nima qiladi?

```bash
python -m venv myproject_env
```



- [A] myproject_env papkasini o'chiradi 
- [B] myproject_env nomli virtual muhit yaratadi 
- [C] myproject_env ga kiradi 
- [D] pip ni yangilaydi 


> **To'g'ri javob:** B 
> **Tushuntirish:** python -m venv myproject_env — shu nomda virtual muhit yaratadi.


---


## Savol 13



BotFather nima?



- [A] Telegram kompaniyasi rahbari 
- [B] Telegram da yangi botlar yaratish va boshqarish uchun rasmiy bot 
- [C] Bot xavfsizligi tizimi 
- [D] Telegram guruh administratori 


> **To'g'ri javob:** B 
> **Tushuntirish:** BotFather — Telegram ning rasmiy boti. Yangi bot yaratish, token olish, sozlash uchun ishlatiladi.


---


## Savol 14



Aiogram o'rnatish buyrug'i qaysi?



- [A] python install aiogram 
- [B] pip install aiogram 
- [C] pip install telegram-aiogram 
- [D] conda install aiogram 


> **To'g'ri javob:** B 
> **Tushuntirish:** pip install aiogram — to'g'ri o'rnatish buyrug'i.


---


## Savol 15



Echo bot uchun qaysi handler yoziladi?

```python
@dp.message()
async def echo(message: Message):
    await message.answer(message.text)
```



- [A] Faqat /start uchun 
- [B] Barcha kelgan xabarlar uchun — matnni qaytarib yuboradi 
- [C] Faqat raqamlar uchun 
- [D] Admin xabarlari uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** @dp.message() — hamma xabarlarni ushlaydi. message.answer(message.text) — xabarni qaytaradi.


---


## Savol 16



Quyidagi kodning natijasi nima?

```python
print(list(range(10, 0, -2)))
```



- [A] [10, 8, 6, 4, 2, 0] 
- [B] [10, 8, 6, 4, 2] 
- [C] [8, 6, 4, 2] 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** range(10, 0, -2) — 10 dan 2 gacha (0 kirmaydi), -2 qadam: 10, 8, 6, 4, 2.


---


## Savol 17



OOP dan foydalanishning asosiy afzalligi nima?



- [A] Kodni qisqartirish 
- [B] Kodni qayta ishlatish, tartibli va kengaytiriladigan qilish 
- [C] Faqat grafik interfeyslar yaratish 
- [D] Dasturni tezlashtirish 


> **To'g'ri javob:** B 
> **Tushuntirish:** OOP — reusability (qayta ishlatish), modularity (tartiblilik), scalability (kengaytirish).


---


## Savol 18



Bir Python faylida nechta class yozish mumkin?



- [A] Faqat bitta 
- [B] Faqat ikkita 
- [C] Istalgancha 
- [D] Faqat 10 ta 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da bir faylda istalgancha class yozish mumkin.


---


## Savol 19



Ikki obyektning id lari bir xil bo'ladimi?

```python
class A:
    pass
a1 = A()
a2 = A()
print(id(a1) == id(a2))
```



- [A] True 
- [B] False 
- [C] None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Har bir yangi obyektning o'z xotira manzili bor → id lar farqli → False.


---


## Savol 20



Bir class ichida nechta metod bo'lishi mumkin?



- [A] Faqat bitta 
- [B] Faqat 10 ta 
- [C] Istalgancha 
- [D] Faqat 5 ta 


> **To'g'ri javob:** C 
> **Tushuntirish:** Class ichida istalgancha metod yozish mumkin.


---


## Savol 21



Quyidagi kodning natijasi nima?

```python
class Kvadrat:
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2

    def perimetr(self):
        return 4 * self.tomon

k = Kvadrat(5)
print(k.yuza())
print(k.perimetr())
```



- [A] 25, 20 
- [B] 10, 20 
- [C] 25, 10 
- [D] Xato beradi 


> **To'g'ri javob:** A 
> **Tushuntirish:** yuza() → 5**2 = 25. perimetr() → 4*5 = 20.


---


## Savol 22



Atributga qanday murojaat qilinadi?



- [A] obyekt->atribut 
- [B] obyekt::atribut 
- [C] obyekt.atribut 
- [D] obyekt[atribut] 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da atributga nuqta . orqali: obyekt.atribut.


---


## Savol 23



Name mangling nima?



- [A] Atribut nomini o'chirish 
- [B] Python ning __x atributini _ClassName__x ga o'zgartirishi 
- [C] Metodlarni yashirish 
- [D] Class nomini o'zgartirish 


> **To'g'ri javob:** B 
> **Tushuntirish:** Name mangling: self.__x → Python ichida _ClassName__x sifatida saqlanadi.


---


## Savol 24



Quyidagi kodning natijasi nima?

```python
class Shakl:
    def yuza(self):
        return 'Hisoblanmadi'

class Kvadrat(Shakl):
    def __init__(self, t):
        self.t = t

    def yuza(self):
        return self.t ** 2

k = Kvadrat(5)
print(k.yuza())
```



- [A] Hisoblanmadi 
- [B] 5 
- [C] 25 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** Kvadrat yuza() ni override qilgan → 5**2 = 25.


---


## Savol 25



Quyidagi ikki kod ekvivalentmi?

```python
# 1-usul
@dataclass
class A:
    x: int
    y: int

# 2-usul
class B:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```



- [A] Yo'q, umuman boshqacha 
- [B] Ha, asosan ekvivalent (+ repr va eq ham qo'shiladi) 
- [C] Faqat __init__ jihatidan ekvivalent 
- [D] 2-usul noto'g'ri 


> **To'g'ri javob:** B 
> **Tushuntirish:** @dataclass __init__ ni yaratadi + __repr__ va __eq__ ham qo'shiladi.


---


## Savol 26



self yordamida metod ichidan boshqa metodni chaqirish qanday amalga oshiriladi?



- [A] methodName() 
- [B] ClassName.methodName() 
- [C] self.methodName() 
- [D] super().methodName() 


> **To'g'ri javob:** C 
> **Tushuntirish:** Metod ichidan boshqa metodga: self.methodName().


---


## Savol 27



Quyidagi kodning natijasi nima?

```python
class Tovar:
    kategoriya = 'Oziq-ovqat'

t1 = Tovar()
t2 = Tovar()
t1.kategoriya = 'Kiyim'
print(Tovar.kategoriya)
print(t1.kategoriya)
print(t2.kategoriya)
```



- [A] Kiyim, Kiyim, Kiyim 
- [B] Oziq-ovqat, Kiyim, Oziq-ovqat 
- [C] Oziq-ovqat, Oziq-ovqat, Oziq-ovqat 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** t1.kategoriya = 'Kiyim' — faqat t1 ga instance atribut. Tovar va t2 o'zgarmaydi.


---


## Savol 28



Quyidagi kodning natijasi nima?

```python
class Hisobvar:
    def __init__(self, balans):
        self.__balans = balans

    def balans_korsatish(self):
        return self.__balans

h = Hisobvar(500000)
print(h.balans_korsatish())
print(h._Hisobvar__balans)
```



- [A] 500000, AttributeError 
- [B] 500000, 500000 
- [C] AttributeError, 500000 
- [D] None, None 


> **To'g'ri javob:** B 
> **Tushuntirish:** balans_korsatish() → 500000. _Hisobvar__balans → name mangling orqali → 500000.


---


## Savol 29



issubclass() funksiyasi nima qaytaradi?



- [A] Obyektning classini 
- [B] Bir classning boshqasidan meros olgan-olmaganini — True/False 
- [C] Class metodlari ro'yxatini 
- [D] Class atributlarini 


> **To'g'ri javob:** B 
> **Tushuntirish:** issubclass(Farzand, Ota) → True yoki False. Classlar bilan ishlaydi.


---


## Savol 30



Quyidagi kodning natijasi nima?

```python
from dataclasses import dataclass

@dataclass
class Talaba:
    ism: str
    ball: int

t1 = Talaba('Ali', 90)
t2 = Talaba('Ali', 90)
print(t1 == t2)
```



- [A] False 
- [B] True 
- [C] None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** @dataclass __eq__ yaratadi: barcha maydonlar teng bo'lsa True. t1 == t2 → True.


---


## Savol 31



Virtual muhit faollashtirilib, 'pip install requests' bajarilsa, kutubxona qayerga o'rnatiladi?



- [A] Global Python ga 
- [B] Faqat joriy papkaga 
- [C] Virtual muhit papkasiga — izolyatsiyalangan 
- [D] Sistemaga 


> **To'g'ri javob:** C 
> **Tushuntirish:** Virtual muhit faollashtirilganda pip faqat shu muhitga o'rnatadi — global Python ga ta'sir qilmaydi.


---


## Savol 32



which python (Linux) yoki where python (Windows) buyrug'i nima ko'rsatadi?



- [A] Python kodi 
- [B] Faol Python ning qaysi muhitda ekanini ko'rsatadi 
- [C] O'rnatilgan kutubxonalar 
- [D] Python versiyasi 


> **To'g'ri javob:** B 
> **Tushuntirish:** which python — joriy faol Python ning yo'lini ko'rsatadi. Virtual muhitda uning yo'li ko'rinadi.


---


## Savol 33



Token ni saqlashda qaysi amaliyot tavsiya etiladi?



- [A] Kodning ichiga yozish 
- [B] .env fayl yoki muhit o'zgaruvchilari (environment variables) orqali saqlash 
- [C] GitHub ga yuklash 
- [D] Telegram ga yuborish 


> **To'g'ri javob:** B 
> **Tushuntirish:** Token .env faylda saqlanadi. python-dotenv bilan o'qiladi. Hech qachon GitHub ga yuklanmaydi.


---


## Savol 34



message.answer() va message.reply() ning farqi nima?



- [A] Hech qanday farq yo'q 
- [B] answer() — oddiy xabar; reply() — foydalanuvchining xabariga javob sifatida 
- [C] reply() tezroq ishlaydi 
- [D] answer() faqat admin uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** answer() — yangi xabar. reply() — foydalanuvchi xabariga reply (quote) bilan javob.


---


## Savol 35



Echo bot qanday maqsadda ishlatiladi?



- [A] Faqat ishlab chiqarishda 
- [B] Bot yaratishni o'rganish uchun boshlang'ich misol sifatida 
- [C] Faqat test uchun 
- [D] Faqat admin botlar uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** Echo bot — Telegram botni o'rganishning eng oddiy va birinchi misoli.


---