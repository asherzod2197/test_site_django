## Savol 1

Django MVT arxitekturasida harflar nimani anglatadi?

- [A] Model – View – Transfer  
- [B] Module – View – Template  
- [C] Model – View – Template  
- [D] Model – Visual – Template  

> **To'g'ri javob:** C  
> **Tushuntirish:** MVT — Model (ma'lumotlar bazasi bilan ishlash), View (biznes mantiq), Template (HTML ko'rinish) so'zlarining qisqartmasi. Django ning asosiy arxitektura patterni shu uchta qismdan iborat.

---

## Savol 2

MVT da **Model** qanday vazifani bajaradi?

- [A] HTML sahifalarni ko'rsatadi  
- [B] Foydalanuvchi so'rovlarini qayta ishlaydi  
- [C] Ma'lumotlar bazasi jadvallarini va ular bilan ishlash mantiqini belgilaydi  
- [D] URL yo'naltirishni boshqaradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** Model — ma'lumotlar bazasining Python ko'rinishi. Har bir Model klassi bitta jadvalga mos keladi. Model orqali ma'lumot qo'shish, o'qish, yangilash va o'chirish (CRUD) amalga oshiriladi.

---

## Savol 3

MVT da **View** qanday vazifani bajaradi?

- [A] Faqat HTML sahifalarni yaratadi  
- [B] So'rovni qabul qilib, Model dan ma'lumot olib, Template ga uzatadi va javob qaytaradi  
- [C] Faqat ma'lumotlar bazasi bilan ishlaydi  
- [D] URL manzillarni belgilaydi  

> **To'g'ri javob:** B  
> **Tushuntirish:** View — loyihaning "miya"si. Foydalanuvchi so'rovini (request) qabul qiladi, kerakli ma'lumotni Model dan oladi, uni Template ga uzatadi va tayyor HTML sahifani javob (response) sifatida qaytaradi.

---

## Savol 4

MVT da **Template** qanday vazifani bajaradi?

- [A] Ma'lumotlar bazasini boshqaradi  
- [B] Biznes mantiqni bajaradi  
- [C] Foydalanuvchiga ko'rsatiladigan HTML sahifani shakllantiradi  
- [D] So'rovlarni yo'naltiradi  

> **To'g'ri javob:** C  
> **Tushuntirish:** Template — foydalanuvchi ko'radigan qism (presentation layer). U HTML, CSS va Django Template Language (DTL) dan iborat. View uzatgan ma'lumotlarni HTML sahifaga joylashtiradi.

---

## Savol 5

Django da Model qaysi faylda yoziladi?

- [A] `views.py`  
- [B] `urls.py`  
- [C] `settings.py`  
- [D] `models.py`  

> **To'g'ri javob:** D  
> **Tushuntirish:** Har bir Django ilovasida `models.py` fayli bo'lib, unda ma'lumotlar bazasi modellari (jadvallar) Python klasslari ko'rinishida yoziladi. Bu klasslar `django.db.models.Model` dan meros oladi.

---

## Savol 6

Quyidagi kod nima vazifasini bajaradi?

```python
class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    matn = models.TextField()
```

- [A] HTML sahifa yaratadi  
- [B] `sarlavha` va `matn` ustunlariga ega `Maqola` jadvali modelini belgilaydi  
- [C] URL manzil belgilaydi  
- [D] View funksiyasini yaratadi  

> **To'g'ri javob:** B  
> **Tushuntirish:** Bu kod `Maqola` nomli Model klassini yaratadi. `CharField` — qisqa matn, `TextField` — uzun matn uchun. `makemigrations` va `migrate` buyruqlari bilan bu model ma'lumotlar bazasida jadvalga aylanadi.

---

## Savol 7

Django View funksiyasi albatta nima qaytarishi kerak?

- [A] Python lug'ati (dictionary)  
- [B] HTML matn  
- [C] `HttpResponse` yoki uning kenja sinflari  
- [D] JSON ob'ekt  

> **To'g'ri javob:** C  
> **Tushuntirish:** Har bir Django View funksiyasi `HttpResponse` yoki uning kenja sinflaridan birini (masalan, `JsonResponse`, `HttpResponseRedirect`) qaytarishi shart. Aks holda xato yuzaga keladi.

---

## Savol 8

`render()` funksiyasi qanday vazifani bajaradi?

- [A] Ma'lumotlar bazasiga yozuv qo'shadi  
- [B] Template faylini ma'lumotlar bilan to'ldirib, `HttpResponse` qaytaradi  
- [C] URL manzilga yo'naltiradi  
- [D] Foydalanuvchini tizimga kiritadi  

> **To'g'ri javob:** B  
> **Tushuntirish:** `render(request, 'template.html', context)` — bu Django da eng ko'p ishlatiladigan funksiya. U template faylini topib, `context` dagi ma'lumotlarni unga joylashtiradi va tayyor HTML ni `HttpResponse` sifatida qaytaradi.

---

## Savol 9

Django Template Language (DTL) da o'zgaruvchini HTML ga chiqarish uchun qaysi sintaksis ishlatiladi?

- [A] `<% o'zgaruvchi %>`  
- [B] `{{ o'zgaruvchi }}`  
- [C] `<? o'zgaruvchi ?>`  
- [D] `${ o'zgaruvchi }`  

> **To'g'ri javob:** B  
> **Tushuntirish:** Django Template Language da ikki jingalak qavs `{{ }}` o'zgaruvchi qiymatini HTML ga chiqarish uchun ishlatiladi. Masalan, `{{ maqola.sarlavha }}` — maqola sarlavhasini ko'rsatadi.

---

## Savol 10

Django Template Language da `if-else` shartini yozish uchun qaysi sintaksis to'g'ri?

- [A] `{{ if shart }} ... {{ endif }}`  
- [B] `<% if shart %> ... <% endif %>`  
- [C] `{% if shart %} ... {% endif %}`  
- [D] `{# if shart #} ... {# endif #}`  

> **To'g'ri javob:** C  
> **Tushuntirish:** DTL da mantiqiy teglar uchun `{% %}` (figurali qavs + foiz) sintaksisi ishlatiladi. `{% if %}`, `{% for %}`, `{% block %}` kabi barcha template teglar shu sintaksisda yoziladi.

---

## Savol 11

MVT da foydalanuvchi brauzerdan so'rov yuborganda qanday tartibda qayta ishlanadi?

- [A] Template → View → Model → Javob  
- [B] Model → Template → View → Javob  
- [C] So'rov → URL → View → Model → Template → Javob  
- [D] So'rov → Model → View → Template → Javob  

> **To'g'ri javob:** C  
> **Tushuntirish:** To'liq jarayon: Foydalanuvchi so'rov yuboradi → URL dispatcher tegishli View ni topadi → View Model dan ma'lumot oladi → Ma'lumot Template ga uzatiladi → Tayyor HTML javob sifatida qaytariladi.

---

## Savol 12

`context` nima va u qanday ishlatiladi?

- [A] Ma'lumotlar bazasi ulanish sozlamalari  
- [B] View dan Template ga uzatiladigan Python lug'ati (dictionary)  
- [C] URL manzillar ro'yxati  
- [D] Model maydonlari to'plami  

> **To'g'ri javob:** B  
> **Tushuntirish:** `context` — View funksiyasida Template ga uzatiladigan ma'lumotlar lug'ati. Masalan, `context = {'maqolalar': Maqola.objects.all()}` — barcha maqolalarni Template ga uzatadi va `{{ maqolalar }}` orqali HTML da ishlatiladi.

---

## Savol 13

Django Template da izoh (comment) yozish uchun qaysi sintaksis ishlatiladi?

- [A] `// bu izoh`  
- [B] `<!-- bu izoh -->`  
- [C] `{# bu izoh #}`  
- [D] `{{ # bu izoh }}`  

> **To'g'ri javob:** C  
> **Tushuntirish:** DTL da izohlar `{# ... #}` sintaksisida yoziladi. Bu izohlar HTML sahifada ko'rinmaydi va brauzerga yuborilmaydi. HTML izoh `<!-- -->` ham ishlatilishi mumkin, lekin u brauzerga yuboriladi.

---

## Savol 14

Django da Class-Based View (CBV) va Function-Based View (FBV) ning asosiy farqi nima?

- [A] CBV faqat ma'lumotlar bazasi bilan, FBV faqat Template bilan ishlaydi  
- [B] CBV klasslar orqali, FBV funksiyalar orqali yoziladi; CBV qayta ishlatish va meros olishni osonlashtiradi  
- [C] FBV yangi, CBV eski usul hisoblanadi  
- [D] Hech qanday farq yo'q, faqat yozilish uslubi farqli  

> **To'g'ri javob:** B  
> **Tushuntirish:** FBV oddiy Python funksiyasi sifatida, CBV esa klass sifatida yoziladi. CBV `ListView`, `DetailView`, `CreateView` kabi tayyor klasslardan meros olib, kod miqdorini kamaytiradi va qayta ishlatishni osonlashtiradi.

---

## Savol 15

Django da Template inheritance (shablon merosi) nima uchun ishlatiladi?

- [A] Bir modeldan boshqa model meros olishi uchun  
- [B] Asosiy HTML tuzilmani (header, footer) bir joyda yozib, boshqa sahifalardan undan foydalanish uchun  
- [C] View funksiyalarini qayta ishlatish uchun  
- [D] Ma'lumotlar bazasi jadvallarini birlashtirish uchun  

> **To'g'ri javob:** B  
> **Tushuntirish:** Template inheritance `{% extends 'base.html' %}` va `{% block %}` teglari orqali amalga oshiriladi. `base.html` da umumiy tuzilma (navigatsiya, footer) bir marta yoziladi, boshqa templatelar undan meros olib faqat o'zgaruvchan qismlarni to'ldiradi.

---