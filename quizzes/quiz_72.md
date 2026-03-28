## Savol 1



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


## Savol 2



OOP dan foydalanishning asosiy afzalligi nima?



- [A] Kodni qisqartirish 
- [B] Kodni qayta ishlatish, tartibli va kengaytiriladigan qilish 
- [C] Faqat grafik interfeyslar yaratish 
- [D] Dasturni tezlashtirish 


> **To'g'ri javob:** B 
> **Tushuntirish:** OOP — reusability (qayta ishlatish), modularity (tartiblilik), scalability (kengaytirish).


---


## Savol 3



Bir Python faylida nechta class yozish mumkin?



- [A] Faqat bitta 
- [B] Faqat ikkita 
- [C] Istalgancha 
- [D] Faqat 10 ta 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da bir faylda istalgancha class yozish mumkin.


---


## Savol 4



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


## Savol 5



Bir class ichida nechta metod bo'lishi mumkin?



- [A] Faqat bitta 
- [B] Faqat 10 ta 
- [C] Istalgancha 
- [D] Faqat 5 ta 


> **To'g'ri javob:** C 
> **Tushuntirish:** Class ichida istalgancha metod yozish mumkin.


---


## Savol 6



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


## Savol 7



Atributga qanday murojaat qilinadi?



- [A] obyekt->atribut 
- [B] obyekt::atribut 
- [C] obyekt.atribut 
- [D] obyekt[atribut] 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da atributga nuqta . orqali: obyekt.atribut.


---


## Savol 8



Name mangling nima?



- [A] Atribut nomini o'chirish 
- [B] Python ning __x atributini _ClassName__x ga o'zgartirishi 
- [C] Metodlarni yashirish 
- [D] Class nomini o'zgartirish 


> **To'g'ri javob:** B 
> **Tushuntirish:** Name mangling: self.__x → Python ichida _ClassName__x sifatida saqlanadi.


---


## Savol 9



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


## Savol 10



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


## Savol 11



Virtual muhitni yaratish buyrug'i qaysi?



- [A] python create venv myenv 
- [B] python -m venv myenv 
- [C] pip install venv myenv 
- [D] venv create myenv 


> **To'g'ri javob:** B 
> **Tushuntirish:** python -m venv myenv — 'myenv' nomli virtual muhit yaratadi.


---


## Savol 12



pip freeze > requirements.txt buyrug'i nima qiladi?



- [A] requirements.txt ni o'chiradi 
- [B] O'rnatilgan barcha kutubxonalar ro'yxatini requirements.txt ga yozadi 
- [C] requirements.txt dan kutubxona o'rnatadi 
- [D] Virtual muhit yaratadi 


> **To'g'ri javob:** B 
> **Tushuntirish:** pip freeze — o'rnatilgan kutubxonalar va versiyalar. > requirements.txt — faylga yozadi.


---


## Savol 13



Telegram Bot API qanday protokol orqali ishlaydi?



- [A] FTP 
- [B] SMTP 
- [C] HTTP/HTTPS (REST API) 
- [D] WebSocket faqat 


> **To'g'ri javob:** C 
> **Tushuntirish:** Telegram Bot API — HTTPS REST API orqali ishlaydi. JSON format.


---


## Savol 14



Aiogram da async/await nima uchun ishlatiladi?



- [A] Kodni qisqartirish uchun 
- [B] Ko'p foydalanuvchi bilan bir vaqtda ishlash — bloklashmaslik uchun 
- [C] Faqat estetik sabab 
- [D] Xatoliklarni kamaytirish uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** async/await — asinxron dasturlash. Bitta so'rov kutayotganda boshqasini ham bajaradi.


---


## Savol 15



Echo botda message.text None bo'lishi mumkinmi?



- [A] Yo'q, har doim matn bo'ladi 
- [B] Ha — foydalanuvchi rasm, video, sticker yuborganda text None 
- [C] Faqat buyruqlarda 
- [D] Faqat guruhda 


> **To'g'ri javob:** B 
> **Tushuntirish:** Rasm, video, audio va boshqa media xabarlarda message.text None bo'ladi.


---


## Savol 16



range() funksiyasi qaysi turdagi obyekt qaytaradi?



- [A] list 
- [B] tuple 
- [C] range 
- [D] generator 


> **To'g'ri javob:** C 
> **Tushuntirish:** range() — range turidagi obyekt qaytaradi. Bu iterable, lekin list emas.


---


## Savol 17



Quyidagi kodning natijasi nima?

```python
class Mashina:
    pass

m = Mashina()
print(type(m))
```



- [A] <class 'type'> 
- [B] <class '__main__.Mashina'> 
- [C] <class 'object'> 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** type(m) → m ning classi: <class '__main__.Mashina'>.


---


## Savol 18



Quyidagi kodning natijasi nima?

```python
class Kitob:
    janr = 'Roman'

k1 = Kitob()
k2 = Kitob()
print(k1.janr == k2.janr)
```



- [A] False 
- [B] True 
- [C] None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Ikkalasi ham 'Roman' class atributini meros oladi. 'Roman' == 'Roman' → True.


---


## Savol 19



Quyidagi kodning natijasi nima?

```python
class Kalit:
    pass

k = Kalit()
k.rang = 'sariq'
print(k.rang)
```



- [A] Xato beradi 
- [B] None 
- [C] sariq 
- [D] '' 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da obyektga dinamik atribut qo'shish mumkin: k.rang = 'sariq'.


---


## Savol 20



Metod ichidan boshqa metodini chaqirish uchun nima yoziladi?



- [A] method_nomi() 
- [B] self->method_nomi() 
- [C] self.method_nomi() 
- [D] this.method_nomi() 


> **To'g'ri javob:** C 
> **Tushuntirish:** Metod ichidan boshqa metodga self.method_nomi() orqali murojaat qilinadi.


---


## Savol 21



Quyidagi kodning natijasi nima?

```python
class Hisobvar:
    def __init__(self, balans):
        self.balans = balans

    def kirim(self, summa):
        self.balans += summa
        return self.balans

h = Hisobvar(10000)
print(h.kirim(5000))
print(h.balans)
```



- [A] 15000, 10000 
- [B] 15000, 15000 
- [C] 5000, 15000 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** kirim(5000) → self.balans = 10000+5000 = 15000 → qaytaradi. h.balans → 15000.


---


## Savol 22



Quyidagi kodning natijasi nima?

```python
class Narx:
    qqs = 12

    def __init__(self, asos):
        self.asos = asos

    def jami(self):
        return self.asos * (1 + self.qqs / 100)

n = Narx(50000)
print(n.jami())
```



- [A] 50000 
- [B] 56000.0 
- [C] 6000.0 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** self.qqs → class atribut 12. 50000 * 1.12 = 56000.0.


---


## Savol 23



Encapsulation nimani ta'minlaydi?



- [A] Kodni qisqartiradi 
- [B] Ma'lumotlarning yaxlitligini va xavfsizligini ta'minlaydi 
- [C] Dasturni tezlashtiradi 
- [D] Faqat xatoliklarni kamaytiradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Encapsulation — ma'lumotlarni yashirish orqali to'g'ridan-to'g'ri o'zgartirishdan himoya qiladi.


---


## Savol 24



Quyidagi kodning natijasi nima?

```python
class Ota:
    def kim(self):
        return 'Ota'

class Farzand(Ota):
    pass

f = Farzand()
print(f.kim())
```



- [A] Xato beradi 
- [B] None 
- [C] Farzand 
- [D] Ota 


> **To'g'ri javob:** D 
> **Tushuntirish:** Farzand classida kim() yo'q → ota classdan qidiradi → 'Ota'.


---


## Savol 25



@dataclass da frozen=True nima qiladi?



- [A] Classni o'chiradi 
- [B] Obyektni immutable (o'zgarmas) qiladi 
- [C] Class atributlarini yashiradi 
- [D] Faqat string atributlar uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** @dataclass(frozen=True) — obyektni o'zgarmas qiladi. Atributga qayta qiymat bersak FrozenInstanceError.


---


## Savol 26



self ixtiyoriy nommi yoki majburiy?



- [A] Majburiy, faqat 'self' deb yozilishi kerak 
- [B] Ixtiyoriy nom, lekin 'self' ishlatish konventsiya 
- [C] Har doim 'this' deb yoziladi 
- [D] Har doim 'object' deb yoziladi 


> **To'g'ri javob:** B 
> **Tushuntirish:** self — konventsiya bo'yicha nom. Texnik jihatdan boshqa nom ham bo'ladi, lekin self standart.


---


## Savol 27



Instance atribut va class atributning farqi nima?



- [A] Hech qanday farq yo'q 
- [B] Instance atribut — har obyektga xos, class atribut — barcha obyektlar uchun umumiy 
- [C] Class atribut tezroq ishlaydi 
- [D] Instance atribut faqat __init__ da bo'ladi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Class atribut — barcha instansiyalarga umumiy. Instance atribut — faqat o'sha obyektga xos.


---


## Savol 28



Python da private atribut qanday e'lon qilinadi?



- [A] private self.x = 5 
- [B] self.x = 5 
- [C] self.__x = 5 
- [D] self._private_x = 5 


> **To'g'ri javob:** C 
> **Tushuntirish:** Ikki pastki chiziq __ — private atribut: self.__x. Tashqaridan to'g'ridan-to'g'ri kirish mumkin emas.


---


## Savol 29



Python da meros olish qanday yoziladi?



- [A] class Farzand extends Ota: 
- [B] class Farzand inherits Ota: 
- [C] class Farzand(Ota): 
- [D] class Farzand -> Ota: 


> **To'g'ri javob:** C 
> **Tushuntirish:** Python da meros olish: class FarzandClass(OtaClass):


---


## Savol 30



@dataclass dan foydalanish uchun nima import qilinadi?



- [A] from class import dataclass 
- [B] from dataclasses import dataclass 
- [C] import dataclass 
- [D] from python import dataclass 


> **To'g'ri javob:** B 
> **Tushuntirish:** from dataclasses import dataclass — to'g'ri import.


---


## Savol 31



Virtual environment nima uchun kerak?



- [A] Python ni o'rnatish uchun 
- [B] Har bir loyiha uchun alohida kutubxona versiyalarini boshqarish uchun 
- [C] Dasturni tezlashtirish uchun 
- [D] Faqat Windows uchun 


> **To'g'ri javob:** B 
> **Tushuntirish:** Loyiha A: Django 3.2, Loyiha B: Django 4.0 — virtual muhit bu konfliktni hal qiladi.


---


## Savol 32



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


## Savol 33



BotFather nima?



- [A] Telegram kompaniyasi rahbari 
- [B] Telegram da yangi botlar yaratish va boshqarish uchun rasmiy bot 
- [C] Bot xavfsizligi tizimi 
- [D] Telegram guruh administratori 


> **To'g'ri javob:** B 
> **Tushuntirish:** BotFather — Telegram ning rasmiy boti. Yangi bot yaratish, token olish, sozlash uchun ishlatiladi.


---


## Savol 34



Aiogram o'rnatish buyrug'i qaysi?



- [A] python install aiogram 
- [B] pip install aiogram 
- [C] pip install telegram-aiogram 
- [D] conda install aiogram 


> **To'g'ri javob:** B 
> **Tushuntirish:** pip install aiogram — to'g'ri o'rnatish buyrug'i.


---


## Savol 35



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