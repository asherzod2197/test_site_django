## Savol 1



Quyidagi kodning natijasi nima?

```python
for i in range(5):
    print(i)
```



- [A] 1 2 3 4 5 
- [B] 0 1 2 3 4 5 
- [C] 0 1 2 3 4 
- [D] 1 2 3 4 


> **To'g'ri javob:** C 
> **Tushuntirish:** range(5) → range(0, 5, 1). 0 dan 4 gacha: 0, 1, 2, 3, 4.


---


## Savol 2



OOP da 'Class' nima?



- [A] O'zgaruvchilar to'plami 
- [B] Funksiyalar to'plami 
- [C] Obyektlarni yaratish uchun qolip (shablon) 
- [D] Python moduli 


> **To'g'ri javob:** C 
> **Tushuntirish:** Class — obyektlar uchun qolip. Atributlar (ma'lumot) va metodlar (funksiya) ni birlashtiradi.


---


## Savol 3



Quyidagi kodda xato bormi?

```python
class Hayvon:
    pass
```



- [A] Ha, pass ishlatib bo'lmaydi 
- [B] Ha, atribut bo'lishi shart 
- [C] Yo'q — pass bo'sh class uchun to'g'ri 
- [D] Ha, class kichik harf bilan yozilishi kerak 


> **To'g'ri javob:** C 
> **Tushuntirish:** pass — hozircha bo'sh class yaratish uchun ishlatiladi. To'liq to'g'ri sintaksis.


---


## Savol 4



Bir classdan nechta obyekt yaratish mumkin?



- [A] Faqat bitta 
- [B] Faqat ikkita 
- [C] Istalgancha 
- [D] Faqat 100 ta 


> **To'g'ri javob:** C 
> **Tushuntirish:** Bir classdan istalgancha obyekt yaratish mumkin. Har biri mustaqil.


---


## Savol 5



Quyidagi kodning natijasi nima?

```python
class Salom:
    def ayt(self):
        return 'Assalomu alaykum!'

s = Salom()
print(s.ayt())
```



- [A] Xato beradi 
- [B] None 
- [C] Assalomu alaykum! 
- [D] ayt 


> **To'g'ri javob:** C 
> **Tushuntirish:** s.ayt() — Salom classining ayt metodini chaqiradi → 'Assalomu alaykum!'.


---


## Savol 6



Quyidagi kodning natijasi nima?

```python
class Odam:
    def __init__(self, ism):
        self.ism = ism

    def salom(self):
        return f'Salom, men {self.ism}!'

o = Odam('Sherzod')
print(o.salom())
```



- [A] Salom, men self.ism! 
- [B] Salom, men Sherzod! 
- [C] None 
- [D] Xato beradi 


> **To'g'ri javob:** B 
> **Tushuntirish:** self.ism = 'Sherzod'. salom() → 'Salom, men Sherzod!'.


---


## Savol 7



Quyidagi kodning natijasi nima?

```python
class Talaba:
    maktab = 'INHA'

t = Talaba()
t.ism = 'Ali'
print(t.maktab)
print(t.ism)
```



- [A] Xato beradi 
- [B] INHA, Ali 
- [C] None, Ali 
- [D] INHA, None 


> **To'g'ri javob:** B 
> **Tushuntirish:** t.maktab — class atributi → 'INHA'. t.ism — instance atributi → 'Ali'.


---


## Savol 8



Quyidagi kodning natijasi nima?

```python
class Bank:
    def __init__(self, balans):
        self.__balans = balans

b = Bank(100000)
print(b.__balans)
```



- [A] 100000 
- [B] None 
- [C] AttributeError 
- [D] 0 


> **To'g'ri javob:** C 
> **Tushuntirish:** __balans — private. Tashqaridan b.__balans → AttributeError.


---


## Savol 9



Quyidagi kodning natijasi nima?

```python
class Hayvon:
    def nafas_ol(self):
        return 'Nafas olmoqda'

class It(Hayvon):
    def vov(self):
        return 'Vov-vov!'

i = It()
print(i.nafas_ol())
print(i.vov())
```



- [A] Xato beradi 
- [B] Nafas olmoqda, Vov-vov! 
- [C] None, Vov-vov! 
- [D] Nafas olmoqda, None 


> **To'g'ri javob:** B 
> **Tushuntirish:** It classi Hayvon dan meros olgan → nafas_ol() ham ishlaydi.


---


## Savol 10



Quyidagi kodning natijasi nima?

```python
from dataclasses import dataclass

@dataclass
class Nuqta:
    x: float
    y: float

n = Nuqta(1.0, 2.0)
print(n.x, n.y)
```



- [A] Xato beradi 
- [B] 1.0 2.0 
- [C] None None 
- [D] x y 


> **To'g'ri javob:** B 
> **Tushuntirish:** @dataclass avtomatik __init__ yaratadi. Nuqta(1.0, 2.0) → x=1.0, y=2.0.


---


## Savol 11



Python da virtual muhit yaratish uchun qaysi modul ishlatiladi?



- [A] virtualenv 
- [B] venv 
- [C] env 
- [D] pyenv 


> **To'g'ri javob:** B 
> **Tushuntirish:** Python 3 da o'rnatilgan venv moduli: python -m venv muhit_nomi.


---


## Savol 12



Linux/Mac da virtual muhitni faollashtirish buyrug'i qaysi?



- [A] venv\Scripts\activate 
- [B] source myenv/bin/activate 
- [C] activate myenv 
- [D] python myenv/activate 


> **To'g'ri javob:** B 
> **Tushuntirish:** Linux/Mac: source myenv/bin/activate. Windows: myenv\Scripts\activate.


---


## Savol 13



Bot token nima?



- [A] Foydalanuvchi paroli 
- [B] Botni Telegram API orqali boshqarish uchun maxsus kalit (unikal identifikator) 
- [C] Bot nomi 
- [D] Telegram kanalining manzili 


> **To'g'ri javob:** B 
> **Tushuntirish:** Token — botning Telegram API ga ulanish uchun sir kalit. BotFather dan olinadi. Hech kimga berilmaydi.


---


## Savol 14



/start komandasi nima?



- [A] Botni o'chirish 
- [B] Foydalanuvchi bilan birinchi tanishish — botni ishga tushiruvchi standart komanda 
- [C] Faqat admin uchun 
- [D] Xabarlarni o'chirish 


> **To'g'ri javob:** B 
> **Tushuntirish:** /start — botni birinchi ishga tushirganda yoki qayta ishga tushirganda chaqiriladi.


---


## Savol 15



Echo bot ishlash printsipi qanday?



- [A] Bot serverga so'rov yuboradi, server qaytaradi 
- [B] Foydalanuvchi xabar → bot qabul qiladi → aynan o'sha xabarni yuboradi 
- [C] Bot ma'lumotlar bazasidan javob qidiradi 
- [D] Faqat buyruqlar ishlaydi 


> **To'g'ri javob:** B 
> **Tushuntirish:** Echo: user → bot: 'Salom' → bot → user: 'Salom'. Oddiy aks ettirish.


---


## Savol 16



range(5) va list(range(5)) ning farqi nima?



- [A] Hech qanday farq yo'q 
- [B] range(5) — range obyekti (lazy), list(range(5)) — [0,1,2,3,4] ro'yxati 
- [C] list(range(5)) tezroq ishlaydi 
- [D] range(5) xotiradan ko'p joy oladi 


> **To'g'ri javob:** B 
> **Tushuntirish:** range() — lazy evaluation. Faqat kerakli vaqtda qiymat hisoblanadi. list() — barcha qiymatlar xotirada.


---


## Savol 17



Real hayotdagi qaysi misol OOP ni eng yaxshi ifodalaydi?



- [A] Raqamlar ro'yxati 
- [B] Avtomobil — rangi, tezligi bor (atributlar), yuradi, to'xtaydi (metodlar) 
- [C] Matematik formula 
- [D] Fayl o'qish funksiyasi 


> **To'g'ri javob:** B 
> **Tushuntirish:** OOP real dunyo obyektlarini modellashtiradi. Avtomobil — atributlari va metodlari bor.


---


## Savol 18



Quyidagi kodning natijasi nima?

```python
class A:
    x = 10

class B:
    x = 20

print(A.x + B.x)
```



- [A] 10 
- [B] 20 
- [C] 30 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** A.x = 10, B.x = 20. 10 + 20 = 30.


---


## Savol 19



Quyidagi kodning natijasi nima?

```python
class Qush:
    qanotlar = 2

q1 = Qush()
q2 = Qush()
q1.qanotlar = 0
print(q1.qanotlar)
print(q2.qanotlar)
```



- [A] 0, 0 
- [B] 2, 2 
- [C] 0, 2 
- [D] 2, 0 


> **To'g'ri javob:** C 
> **Tushuntirish:** q1.qanotlar = 0 — q1 ga instance atribut. q2 class atributidan oladi → 2.


---


## Savol 20



Quyidagi kodning natijasi nima?

```python
class Hisoblagich:
    soni = 0

    def oshir(self):
        self.soni += 1

h = Hisoblagich()
h.oshir()
h.oshir()
h.oshir()
print(h.soni)
```



- [A] 0 
- [B] 1 
- [C] 3 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** oshir() har chaqirilganda h.soni ga 1 qo'shadi. 3 marta → 3.


---


## Savol 21



self parametri metodda qanday uzatiladi?



- [A] Dasturchi qo'lda uzatadi: obj.method(obj) 
- [B] Python avtomatik uzatadi: obj.method() chaqirilganda obj → self 
- [C] Faqat __init__ da uzatiladi 
- [D] return bilan qaytariladi 


> **To'g'ri javob:** B 
> **Tushuntirish:** obj.method() chaqirilganda Python avtomatik obj ni self sifatida uzatadi.


---


## Savol 22



hasattr() funksiyasi nima uchun ishlatiladi?



- [A] Atributni o'chirish 
- [B] Atribut mavjudligini tekshirish 
- [C] Atribut qiymatini olish 
- [D] Yangi atribut yaratish 


> **To'g'ri javob:** B 
> **Tushuntirish:** hasattr(obyekt, 'atribut_nomi') — atribut mavjud bo'lsa True, bo'lmasa False.


---


## Savol 23



Quyidagi kodning natijasi nima?

```python
class Konteyner:
    def __init__(self):
        self._qiymat = 42

k = Konteyner()
print(k._qiymat)
```



- [A] AttributeError 
- [B] None 
- [C] 42 
- [D] 0 


> **To'g'ri javob:** C 
> **Tushuntirish:** _qiymat — protected (konventsiya). Texnik jihatdan tashqaridan kirish mumkin → 42.


---


## Savol 24



Quyidagi kodning natijasi nima?

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

obj = C()
print(isinstance(obj, A))
print(isinstance(obj, B))
```



- [A] False, False 
- [B] True, False 
- [C] False, True 
- [D] True, True 


> **To'g'ri javob:** D 
> **Tushuntirish:** C → B → A meros zanjiri. isinstance(obj, A) → True. isinstance(obj, B) → True.


---


## Savol 25



@dataclass da default qiymat qanday beriladi?

```python
@dataclass
class Tovar:
    nomi: str
    narx: float = 0.0
```



- [A] Bu xato, default bo'lmaydi 
- [B] To'g'ri — narx = 0.0 default qiymat 
- [C] Default faqat int uchun 
- [D] Default faqat __init__ da beriladi 


> **To'g'ri javob:** B 
> **Tushuntirish:** @dataclass da standart qiymatlar: narx: float = 0.0 — to'g'ri sintaksis.


---


## Savol 26



Quyidagi kodning natijasi nima?

```python
class Robot:
    def __init__(self, nomi):
        self.nomi = nomi
        self.batareya = 100

    def ish_qil(self):
        self.batareya -= 10
        return f'{self.nomi}: {self.batareya}%'

r = Robot('R2D2')
r.ish_qil()
print(r.ish_qil())
```



- [A] R2D2: 100% 
- [B] R2D2: 90% 
- [C] R2D2: 80% 
- [D] Xato beradi 


> **To'g'ri javob:** C 
> **Tushuntirish:** Birinchi ish_qil() → 100-10=90. Ikkinchi ish_qil() → 90-10=80 → 'R2D2: 80%'.


---


## Savol 27



Atributni o'chirish uchun qaysi operator/funksiya ishlatiladi?



- [A] remove(atribut) 
- [B] delete atribut 
- [C] del obyekt.atribut 
- [D] clear(atribut) 


> **To'g'ri javob:** C 
> **Tushuntirish:** del obyekt.atribut — atributni o'chiradi. delattr(obyekt, 'nom') ham ishlatiladi.


---


## Savol 28



Quyidagi kodning natijasi nima?

```python
class Karta:
    def __init__(self, raqam):
        self.__raqam = raqam

    def __str__(self):
        return f'**** **** **** {self.__raqam[-4:]}'

k = Karta('1234567890123456')
print(k)
```



- [A] 1234567890123456 
- [B] **** **** **** 3456 
- [C] AttributeError 
- [D] None 


> **To'g'ri javob:** B 
> **Tushuntirish:** __str__ — print(k) chaqirilganda ishlaydi. self.__raqam[-4:] → '3456'.


---


## Savol 29



Quyidagi kodning natijasi nima?

```python
class Transport:
    def __init__(self, nomi, tezlik):
        self.nomi = nomi
        self.tezlik = tezlik

class Velosiped(Transport):
    def __init__(self, nomi, tezlik, g_soni):
        super().__init__(nomi, tezlik)
        self.g_soni = g_soni

v = Velosiped('Trek', 30, 21)
print(v.nomi, v.tezlik, v.g_soni)
```



- [A] Xato beradi 
- [B] Trek 30 21 
- [C] None None 21 
- [D] Trek None 21 


> **To'g'ri javob:** B 
> **Tushuntirish:** super().__init__(nomi, tezlik) ota classni chaqiradi. Barcha atributlar o'rnatiladi.


---


## Savol 30



@dataclass field() funksiyasi nima uchun ishlatiladi?



- [A] Maydoni o'chirish 
- [B] Murakkab default qiymatlar (list, dict) yoki qo'shimcha sozlamalar berish 
- [C] Faqat tip tekshirish 
- [D] Metodlar qo'shish 


> **To'g'ri javob:** B 
> **Tushuntirish:** field() — default_factory (list/dict uchun), compare, repr kabi sozlamalarni beradi.


---


## Savol 31



Virtual muhit papkasini git ga qo'shmaslik uchun nima qilinadi?



- [A] Papkani o'chirish 
- [B] .gitignore fayliga virtual muhit papkasini qo'shish 
- [C] requirements.txt o'chirish 
- [D] Git ishlatmaslik 


> **To'g'ri javob:** B 
> **Tushuntirish:** .gitignore ga venv/ yoki env/ qo'shiladi. Kutubxonalar requirements.txt orqali ulashiladi.


---


## Savol 32



Virtual muhit papkasini boshqa kompyuterga ko'chirish to'g'rimi?



- [A] Ha, eng yaxshi usul shu 
- [B] Yo'q — requirements.txt orqali qayta yaratish to'g'ri 
- [C] Faqat Windows da mumkin 
- [D] Faqat Docker da mumkin 


> **To'g'ri javob:** B 
> **Tushuntirish:** Virtual muhit papkasi ko'chirilmaydi. requirements.txt yozib, boshqa kompyuterda qayta o'rnatiladi.


---


## Savol 33



Telegram botning username qanday ko'rinishda bo'ladi?



- [A] istalgan nom 
- [B] @nom_bot yoki @nomBot — oxiri bot bilan tugashi shart 
- [C] faqat raqamlar 
- [D] @Bot_nom 


> **To'g'ri javob:** B 
> **Tushuntirish:** Bot username: bot yoki _bot bilan tugashi shart, masalan @MyProjectBot.


---


## Savol 34



Aiogram da foydalanuvchi yozgan matnni olish uchun nima ishlatiladi?



- [A] message.command 
- [B] message.text 
- [C] message.data 
- [D] message.content 


> **To'g'ri javob:** B 
> **Tushuntirish:** message.text — foydalanuvchi yozgan matn xabarini qaytaradi.


---


## Savol 35



Quyidagi kodda nima qilinmoqda?

```python
if message.text:
    await message.answer(message.text)
else:
    await message.answer('Faqat matn qabul qilaman!')
```



- [A] Xabarni o'chirish 
- [B] Matn bo'lsa qaytaradi, bo'lmasa xabar beradi 
- [C] Faqat rasm qabul qiladi 
- [D] Bot to'xtaydi 


> **To'g'ri javob:** B 
> **Tushuntirish:** if message.text — matn borligini tekshiradi. Matn bo'lsa qaytaradi, bo'lmasa muqobil javob.


---