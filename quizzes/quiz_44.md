## Savol 1

Django da `view` nima vazifani bajaradi?

- [A] Ma'lumotlar bazasi jadvalini yaratadi
- [B] HTTP so'rovini (`request`) qabul qilib, HTTP javobini (`response`) qaytaradi
- [C] HTML shablonlarni saqlaydi
- [D] Foydalanuvchi parolini tekshiradi

> **To'g'ri javob:** B
> **Tushuntirish:** View — Django MVC/MVT arxitekturasining "V" qismi. Brauzer so'rov yuboradi → URL uni view ga yo'naltiradi → view mantiqni bajaradi → `HttpResponse` yoki `render()` orqali javob qaytaradi. Bu Django ning asosiy ma'lumot oqimi.

---

## Savol 2

Quyidagi eng sodda view kodi nima qaytaradi?

```python
from django.http import HttpResponse

def salom(request):
    return HttpResponse("Salom, Dunyo!")
```

- [A] HTML fayl
- [B] `"Salom, Dunyo!"` matnini o'z ichiga olgan HTTP javob
- [C] `None`
- [D] JSON ma'lumot

> **To'g'ri javob:** B
> **Tushuntirish:** `HttpResponse` — eng sodda javob turi. Ichiga istalgan matn, HTML yoki boshqa kontent uzatiladi. Brauzer bu javobni oladi va ko'rsatadi. `render()` ishlatilmasa, shablon yo'q — faqat sof matn yoki HTML string qaytariladi.

---

## Savol 3

`render()` funksiyasi qanday ishlaydi?

```python
from django.shortcuts import render

def bosh_sahifa(request):
    return render(request, 'blog/index.html', {'sarlavha': 'Xush kelibsiz'})
```

- [A] Faqat `request` ni qaytaradi
- [B] `blog/index.html` shablonini `{'sarlavha': 'Xush kelibsiz'}` konteksti bilan birlashtiradi va `HttpResponse` qaytaradi
- [C] JSON formatida qaytaradi
- [D] Shablonni ma'lumotlar bazasiga saqlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `render(request, shablon_yoli, kontekst)` — uchta argument: `request` (HTTP so'rov), shablon yo'li, va kontekst (dict). Shablon ichida `{{ sarlavha }}` yozilgan joyga `'Xush kelibsiz'` qo'yiladi. Natija `HttpResponse` ga o'ralgan HTML.

---

## Savol 4

URL konfiguratsiyasi qaysi faylda boshlanadi?

- [A] `views.py`
- [B] `models.py`
- [C] `settings.py` dagi `ROOT_URLCONF` orqali ko'rsatilgan fayl (odatda `mysite/urls.py`)
- [D] `wsgi.py`

> **To'g'ri javob:** C
> **Tushuntirish:** `settings.py` da `ROOT_URLCONF = 'mysite.urls'` yoziladi. Django har bir so'rovni shu fayldan boshlaydi. `mysite/urls.py` — asosiy URL marshrutlash nuqtasi. App ning URL lari esa `include()` orqali ulanadi.

---

## Savol 5

Quyidagi URL konfiguratsiyasida qanday xato bor?

```python
from django.urls import path
from . import views

urlpatterns = [
    path('bosh/', views.bosh_sahifa),
    path('haqida/', views.haqida),
]
```

- [A] `path` import qilinmagan
- [B] `views` import qilinmagan
- [C] Xato yo'q — to'g'ri yozilgan
- [D] `urlpatterns` nomi noto'g'ri

> **To'g'ri javob:** C
> **Tushuntirish:** Kod to'liq to'g'ri. `path()` — URL pattern va view ni bog'laydi. `from . import views` — bir papkadagi `views.py` import qilinadi. `urlpatterns` — Django ning majburiy ro'yxat nomi, boshqacha nom berib bo'lmaydi.

---

## Savol 6

`path()` funksiyasida `name` parametri nima uchun kerak?

```python
path('maqolalar/', views.maqolalar_royxati, name='maqolalar-royxati')
```

- [A] URL ni qisqartiradi
- [B] View ga qo'shimcha argument uzatadi
- [C] URL ga ism beradi — shablon va `reverse()` da shu ism bilan murojaat qilish mumkin
- [D] Faqat admin panel uchun kerak

> **To'g'ri javob:** C
> **Tushuntirish:** `name` — URL nomlanishi. Shablonda `{% url 'maqolalar-royxati' %}`, Python kodida `reverse('maqolalar-royxati')` orqali ishlatiladi. URL o'zgartirilsa ham, nom orqali murojaatlar avtomatik yangilanadi. Bu "hardcoded URL" muammosini hal qiladi.

---

## Savol 7

Quyidagi kodda `include()` nima qiladi?

```python
# mysite/urls.py
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
]
```

- [A] `blog` va `shop` applarini o'rnatadi
- [B] `blog/` dan boshlanadigan so'rovlarni `blog/urls.py` ga, `shop/` dan boshlaganlarni `shop/urls.py` ga yo'naltiradi
- [C] Ikkala URL ni bitta faylga birlashtiradi
- [D] App larni `INSTALLED_APPS` ga qo'shadi

> **To'g'ri javob:** B
> **Tushuntirish:** `include()` — URL larni app bo'yicha ajratish imkonini beradi. `blog/` prefiksi bilan kelgan so'rov `blog/urls.py` ga uzatiladi, u yerda qolgan qism (`/maqolalar/`, `/yangi/` va h.k.) tekshiriladi. Bu modularlikni ta'minlaydi.

---

## Savol 8

Brauzerda `http://localhost:8000/blog/maqolalar/` so'ralsa, quyidagi konfiguratsiyada qaysi view chaqiriladi?

```python
# mysite/urls.py
urlpatterns = [
    path('blog/', include('blog.urls')),
]

# blog/urls.py
urlpatterns = [
    path('maqolalar/', views.royxat, name='royxat'),
    path('yangi/', views.yangi, name='yangi'),
]
```

- [A] `views.yangi`
- [B] Hech qaysi — `404` xatosi
- [C] `views.royxat`
- [D] Asosiy `urls.py` dagi view

> **To'g'ri javob:** C
> **Tushuntirish:** Django qidirishi: `/blog/maqolalar/` → asosiy `urls.py` da `blog/` mos keladi → qolgan `maqolalar/` `blog/urls.py` ga uzatiladi → `maqolalar/` pattern `views.royxat` ga mos keladi → shu view chaqiriladi.

---

## Savol 9

URL da o'zgaruvchi qism qanday belgilanadi?

```python
path('maqola/<int:maqola_id>/', views.maqola_detail, name='maqola-detail')
```

- [A] `<int:maqola_id>` — URL dagi raqamli qismni `maqola_id` nomi bilan view ga uzatadi
- [B] `<int:maqola_id>` — faqat regex uchun
- [C] `maqola_id` — URL ning qismi sifatida ko'rinadi
- [D] Faqat `str` turi ishlatilishi mumkin

> **To'g'ri javob:** A
> **Tushuntirish:** `<int:maqola_id>` — URL converter. `int` — faqat butun sonlarni qabul qiladi. `/maqola/5/` so'rovi kelganda, `5` ni `maqola_id=5` sifatida view ga uzatadi. `str`, `slug`, `uuid`, `path` kabi boshqa konverterlar ham mavjud.

---

## Savol 10

Quyidagi view to'g'ri yozilganmi?

```python
def maqola_detail(request, maqola_id):
    maqola = Maqola.objects.get(id=maqola_id)
    return render(request, 'blog/detail.html', {'maqola': maqola})
```

- [A] Xato — `maqola_id` parametri `request` dan oldin yozilishi kerak
- [B] Xato — `Maqola.objects.get()` ishlatilmaydi
- [C] To'g'ri — URL dan kelgan `maqola_id` view parametriga mos keladi
- [D] Xato — `render()` da `maqola_id` ham uzatilishi kerak

> **To'g'ri javob:** C
> **Tushuntirish:** `request` har doim birinchi parametr. URL dan kelgan `maqola_id` ikkinchi parametr sifatida qabul qilinadi. `Maqola.objects.get(id=maqola_id)` — shu `id` li maqolani topadi. Agar topilmasa `DoesNotExist` xatosi chiqadi — shuning uchun `get_object_or_404()` tavsiya etiladi.

---

## Savol 11

`get_object_or_404()` nima uchun ishlatiladi?

```python
from django.shortcuts import get_object_or_404

def maqola_detail(request, pk):
    maqola = get_object_or_404(Maqola, pk=pk)
    return render(request, 'blog/detail.html', {'maqola': maqola})
```

- [A] Obyektni ma'lumotlar bazasiga saqlaydi
- [B] Obyekt topilmasa `DoesNotExist` o'rniga `404 Not Found` HTTP javobi qaytaradi
- [C] Obyektni 404 soniya saqlaydi (kesh)
- [D] Faqat admin uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `get_object_or_404()` — `objects.get()` xavfsiz versiyasi. Agar obyekt topilmasa, Django `404 Not Found` sahifasini ko'rsatadi. `objects.get()` bilan esa `DoesNotExist` exception chiqib, `500 Server Error` ga olib kelishi mumkin. Foydalanuvchiga to'g'ri xato ko'rsatish uchun ishlatiladi.

---

## Savol 12

Quyidagi URL patternlardan qaysi biri `/maqola/django-haqida/` so'roviga mos keladi?

```python
# A variant
path('maqola/<int:id>/', views.detail)

# B variant
path('maqola/<slug:slug>/', views.detail)

# C variant
path('maqola/<str:nom>/', views.detail)

# D variant
path('maqola/<uuid:uid>/', views.detail)
```

- [A] Faqat A
- [B] B va C
- [C] Faqat D
- [D] Faqat A va D

> **To'g'ri javob:** B
> **Tushuntirish:** `django-haqida` — harf, tire va raqamlardan iborat. `<int:>` — faqat raqam (mos kelmaydi). `<slug:>` — harf, raqam, tire va pastki chiziq (mos keladi). `<str:>` — tire (`-`) bo'lmagan stringlar uchun, lekin `path` separatori `/` bo'lmasa ishlaydi (mos keladi). `<uuid:>` — UUID format (mos kelmaydi).

---

## Savol 13

`HttpResponse` va `redirect()` ning farqi nima?

```python
from django.http import HttpResponse
from django.shortcuts import redirect

# 1-usul
return HttpResponse("Saqlandi!")

# 2-usul
return redirect('maqolalar-royxati')
```

- [A] Ikkalasi bir xil
- [B] `HttpResponse` — matn/HTML ko'rsatadi; `redirect()` — brauzer ni boshqa URL ga yo'naltiradi (302 yoki 301)
- [C] `redirect()` — matn ko'rsatadi; `HttpResponse` — yo'naltiradi
- [D] `redirect()` faqat tashqi saytlar uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `HttpResponse` — joriy so'rovga javob berib, brauzerga kontent ko'rsatadi. `redirect()` — `302 Found` HTTP statusi bilan brauzerga yangi manzilga murojaat qilishni buyuradi. Forma yuborilgandan keyin `redirect()` ishlatish — POST/Redirect/GET naqshini amalga oshiradi va sahifa qayta yuklanganda formani ikki marta yuborishni oldini oladi.

---

## Savol 14

Quyidagi `app_name` nima vazifani bajaradi?

```python
# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.royxat, name='royxat'),
    path('<int:pk>/', views.detail, name='detail'),
]
```

- [A] App nomini o'zgartiradi
- [B] URL nomlarini namespace (nom maydoni) bilan ajratadi — `blog:royxat`, `blog:detail` ko'rinishida ishlatiladi
- [C] Faqat admin panel uchun
- [D] `include()` ni bekor qiladi

> **To'g'ri javob:** B
> **Tushuntirish:** `app_name` — URL namespace. Bir nechta app da bir xil nom (`royxat`, `detail`) bo'lishi mumkin. `app_name = 'blog'` deb belgilanganida, shablonda `{% url 'blog:royxat' %}`, kodda `reverse('blog:royxat')` ko'rinishida aniq ko'rsatiladi. Nom to'qnashuvini oldini oladi.

---

## Savol 15

Quyidagi view qanday HTTP metodini qabul qiladi?

```python
def yangi_maqola(request):
    if request.method == 'POST':
        sarlavha = request.POST.get('sarlavha')
        # saqlash...
        return redirect('maqolalar-royxati')
    return render(request, 'blog/yangi.html')
```

- [A] Faqat `POST`
- [B] Faqat `GET`
- [C] Ham `GET` ham `POST` — metodga qarab turlicha ishlaydi
- [D] Hech qaysi — metod tekshirilmagan

> **To'g'ri javob:** C
> **Tushuntirish:** `request.method == 'POST'` — forma yuborilganini tekshiradi. `POST` bo'lsa — ma'lumotlarni saqlaydi va yo'naltiradi. `GET` bo'lsa (ya'ni `POST` emas) — bo'sh formani ko'rsatadi. Bu Django da forma bilan ishlashning standart naqshi.

---

## Savol 16

`re_path()` qachon ishlatiladi?

```python
from django.urls import re_path

urlpatterns = [
    re_path(r'^maqola/(?P<yil>[0-9]{4})/$', views.arxiv),
]
```

- [A] Barcha URL larda `path()` o'rniga
- [B] `path()` konverterlari yetarli bo'lmaganda — murakkab regex pattern talab qilinganida
- [C] Faqat admin URL lari uchun
- [D] Static fayllar uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `path()` — sodda, o'qilishi qulay, standart konverterlar bilan (`int`, `str`, `slug`, `uuid`). `re_path()` — to'liq regex imkoniyati, murakkab patternlar uchun. Masalan, faqat 4 xonali yil uchun `[0-9]{4}` yozish mumkin. Odatda `path()` afzal — `re_path()` faqat zaruriyatda.

---

## Savol 17

Quyidagi konfiguratsiyada `/` (bosh sahifa) URL qanday aniqlanadi?

```python
urlpatterns = [
    path('', views.bosh_sahifa, name='bosh'),
    path('haqida/', views.haqida, name='haqida'),
]
```

- [A] `path('/')` yozilishi kerak edi — xato
- [B] `path('')` — bo'sh string bosh sahifani ifodalaydi (`http://localhost:8000/`)
- [C] `path('index/')` yozilishi kerak
- [D] Bosh sahifa avtomatik aniqlanadi

> **To'g'ri javob:** B
> **Tushuntirish:** `path('')` — bo'sh string, ya'ni prefiks yo'q. `http://localhost:8000/` manziliga so'rov kelganda `views.bosh_sahifa` chaqiriladi. `path('/')` — xato, Django dagi URL patternlarda bosh `/` yozilmaydi.

---

## Savol 18

`request.GET` va `request.POST` ning farqi nima?

```python
# URL: /qidirish/?q=django&sahifa=2
def qidirish(request):
    so'z = request.GET.get('q')         # 'django'
    sahifa = request.GET.get('sahifa')  # '2'
```

- [A] `request.GET` — faqat GET metodini tekshiradi; `request.POST` — metodni o'zgartiradi
- [B] `request.GET` — URL dagi query string parametrlari (`?key=value`); `request.POST` — forma orqali yuborilgan ma'lumotlar
- [C] Ikkalasi bir xil
- [D] `request.GET` — HTML fayl, `request.POST` — JSON

> **To'g'ri javob:** B
> **Tushuntirish:** `request.GET` — `?` dan keyingi parametrlar (`QueryDict`). Qidiruv, filtr, sahifalash uchun. `request.POST` — forma `method="POST"` bilan yuborilgan ma'lumotlar. `request.GET.get('kalit', 'standart')` — kalit topilmasa standart qiymat qaytaradi.

---

## Savol 19

Quyidagi view da `context_object_name` o'rniga ko'rsatish uchun nima kerak?

```python
def maqolalar(request):
    barcha_maqolalar = Maqola.objects.all()
    return render(request, 'blog/royxat.html', {
        'maqolalar': barcha_maqolalar
    })
```

Shablonda:
```html
{% for m in ??? %}
    <h2>{{ m.sarlavha }}</h2>
{% endfor %}
```

- [A] `barcha_maqolalar`
- [B] `Maqola`
- [C] `maqolalar`
- [D] `royxat`

> **To'g'ri javob:** C
> **Tushuntirish:** `render()` ga uzatilgan `dict` ning **kaliti** (`'maqolalar'`) shablonda o'zgaruvchi nom sifatida ishlatiladi. `barcha_maqolalar` — Python dagi o'zgaruvchi nomi, lekin u `'maqolalar'` kaliti ostida uzatilgan. Shablon `context dict` ning kalitlarini ko'radi.

---

## Savol 20

Quyidagi URL pattern qanday qiymatlarni qabul qiladi?

```python
path('arxiv/<int:yil>/<int:oy>/', views.arxiv, name='arxiv')
```

- [A] Faqat bitta `yil` parametrini
- [B] `yil` va `oy` — ikkita butun son; masalan `/arxiv/2024/3/`
- [C] Faqat string qiymatlarni
- [D] UUID formatidagi qiymatlarni

> **To'g'ri javob:** B
> **Tushuntirish:** URL da ikkita `<int:>` converter bor. `/arxiv/2024/3/` so'rovi kelganda, `yil=2024` va `oy=3` sifatida view ga uzatiladi. View esa `def arxiv(request, yil, oy):` ko'rinishida ikkalasini qabul qiladi. Nomlar URL va view parametrlarida mos bo'lishi shart.

---

## Savol 21

Quyidagi view da muammo bormi?

```python
def maqola_ochirish(request, pk):
    maqola = get_object_or_404(Maqola, pk=pk)
    maqola.delete()
    return redirect('maqolalar-royxati')
```

- [A] `delete()` metodi yo'q
- [B] Ha — GET so'rovi bilan ham o'chirishga imkon beradi, bu xavfli; faqat `POST` da o'chirish kerak
- [C] `redirect()` o'rniga `HttpResponse` kerak
- [D] Xato yo'q — to'g'ri yozilgan

> **To'g'ri javob:** B
> **Tushuntirish:** Har qanday GET so'rovi (masalan, `<a href="/maqola/5/ochirish/">`) bilan ma'lumot o'chirilishi xavfli — CSRF va tasodifiy o'chirish xavfi. To'g'ri yondashuv: `if request.method == 'POST': maqola.delete()` — faqat forma yuborilganda o'chirish. Shablonda esa `<form method="post">` bilan tasdiqlanadi.

---

## Savol 22

`{% url %}` shablon tegi qanday ishlaydi?

```html
<a href="{% url 'blog:detail' maqola.pk %}">{{ maqola.sarlavha }}</a>
```

- [A] URL ni to'g'ridan-to'g'ri yozadi
- [B] `blog` namespace dagi `detail` nomli URL ni `maqola.pk` argumenti bilan generatsiya qiladi
- [C] Faqat tashqi URL lar uchun
- [D] `maqola.pk` ni matn sifatida chiqaradi

> **To'g'ri javob:** B
> **Tushuntirish:** `{% url 'blog:detail' maqola.pk %}` → Django `reverse('blog:detail', args=[maqola.pk])` ni chaqirib, masalan `/blog/5/` URL ini generatsiya qiladi. `app_name = 'blog'` va `name='detail'` bo'lishi shart. URL o'zgartirilsa ham shablon avtomatik yangilanadi.

---

## Savol 23

`reverse()` funksiyasi nima qiladi?

```python
from django.urls import reverse

url = reverse('blog:royxat')
# natija: '/blog/'
```

- [A] URL ni teskari qiladi (aylantiradi)
- [B] URL nomi orqali haqiqiy URL manzilini qaytaradi — shablonning Python kod ekvivalenti
- [C] Brauzer ni orqaga qaytaradi
- [D] URL ni o'chiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `reverse()` — `{% url %}` ning Python kod versiyasi. View ichida, `redirect(reverse('blog:royxat'))` yoki test kodlarida ishlatiladi. Argumentlar kerak bo'lsa: `reverse('blog:detail', args=[5])` yoki `reverse('blog:detail', kwargs={'pk': 5})`.

---

## Savol 24

Quyidagi to'liq URLconf to'g'rimi?

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('api/', include('api.urls')),
]
```

- [A] Xato — `admin.site.urls` uchun ham `include()` kerak
- [B] Xato — `include()` faqat bir marta ishlatilishi mumkin
- [C] To'g'ri — standart Django loyiha URL konfiguratsiyasi
- [D] Xato — `path('admin/', ...)` oxirgi bo'lishi kerak

> **To'g'ri javob:** C
> **Tushuntirish:** Bu standart va to'g'ri yozuv. `admin.site.urls` — Django ning o'zi `include()` ni ichida ishlatganligi uchun to'g'ridan-to'g'ri yoziladi. `include()` — ixtiyoriy sonda ishlatilishi mumkin. URL larning tartibi muhim: Django yuqoridan pastga tekshiradi.

---

## Savol 25

`path()` da `kwargs` parametri nima uchun?

```python
path('arxiv/', views.arxiv, name='arxiv', kwargs={'tur': 'yangilik'})
```

- [A] URL parametrlarini olish uchun
- [B] View ga qo'shimcha doimiy (static) argument uzatish uchun — URL o'zida ko'rinmaydi
- [C] URL ni nomlab chiqarish uchun
- [D] `name` parametrini bekor qiladi

> **To'g'ri javob:** B
> **Tushuntirish:** `kwargs` — view ga qo'shimcha argument, lekin URL da ko'rinmaydi. `views.arxiv` `def arxiv(request, tur):` ko'rinishida qabul qiladi va `tur='yangilik'` qiymatini oladi. Bir xil view ni turli konfiguratsiyalar bilan ishlatganda foydali.

---

## Savol 26

Quyidagi view da `HttpResponseNotFound` qachon ishlaydi?

```python
from django.http import HttpResponse, HttpResponseNotFound

def maqola(request, pk):
    try:
        maqola = Maqola.objects.get(pk=pk)
        return render(request, 'blog/detail.html', {'maqola': maqola})
    except Maqola.DoesNotExist:
        return HttpResponseNotFound('<h1>Maqola topilmadi</h1>')
```

- [A] Har doim
- [B] `pk` bo'lsa
- [C] `Maqola.DoesNotExist` xatosi chiqsa — shu `pk` li maqola bazada yo'q bo'lsa
- [D] Hech qachon

> **To'g'ri javob:** C
> **Tushuntirish:** `objects.get()` mos yozuv topilmasa `DoesNotExist` exception chiqaradi. `except` bloki uni ushlab, `HttpResponseNotFound` (404 status kodi bilan) qaytaradi. Bu `get_object_or_404()` ning qo'lda yozilgan versiyasi — ikkalasi bir xil natija beradi.

---

## Savol 27

Quyidagi `urls.py` da `include()` ga string o'rniga to'g'ridan-to'g'ri `urlpatterns` uzatilsa nima bo'ladi?

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.royxat),
]

# mysite/urls.py
from blog import urls as blog_urls

urlpatterns = [
    path('blog/', include(blog_urls)),
]
```

- [A] Xato — `include()` faqat string qabul qiladi
- [B] To'g'ri — `include()` string (modul yo'li) yoki `urlpatterns` ro'yxatini qabul qiladi
- [C] `app_name` bo'lmasa ishlaydi, bo'lsa xato
- [D] Faqat test muhitida ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `include()` uch xil formatni qabul qiladi: 1) `'blog.urls'` — string (modul yo'li), 2) `blog_urls` — to'g'ridan-to'g'ri `urlpatterns` ro'yxati yoki modul, 3) `(pattern_list, app_namespace)` — tuple. String ko'rinishi ko'proq ishlatiladi — lozy import imkoniyati bor.

---

## Savol 28

Quyidagi view da `request.user` nima?

```python
def profil(request):
    if request.user.is_authenticated:
        return render(request, 'profil.html', {'user': request.user})
    return redirect('login')
```

- [A] URL dagi foydalanuvchi nomi
- [B] Joriy so'rov yuborgan foydalanuvchi obyekti (`User` modeli) — kirgan bo'lsa haqiqiy, kirmagan bo'lsa `AnonymousUser`
- [C] Faqat admin foydalanuvchisi
- [D] `request.POST` dagi `user` maydoni

> **To'g'ri javob:** B
> **Tushuntirish:** `request.user` — Django `AuthenticationMiddleware` tomonidan qo'shiladi. Kirgan foydalanuvchi `User` obyektini, kirmagan foydalanuvchi `AnonymousUser` ni ifodalaydi. `is_authenticated` — kirganmi-yo'qmi tekshiradi. Bu Django authentication sistemasining asosi.

---

## Savol 29

`@login_required` dekorator nima qiladi?

```python
from django.contrib.auth.decorators import login_required

@login_required
def maxfiy_sahifa(request):
    return render(request, 'maxfiy.html')
```

- [A] Sahifani parol bilan himoyalaydi
- [B] Kirmagan foydalanuvchini login sahifasiga yo'naltiradi; kirgan foydalanuvchi view ga kirishi mumkin
- [C] Faqat admin kirishi mumkin
- [D] So'rovni shifrlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `@login_required` — agar foydalanuvchi `is_authenticated` bo'lmasa, `settings.py` da `LOGIN_URL` ga (odatda `/accounts/login/`) yo'naltiradi. Kirganidan so'ng asl sahifaga qaytaradi. `login_url='/kirish/'` argument bilan boshqa URL belgilanishi mumkin.

---

## Savol 30

Quyidagi URL patternlar qaysi tartibda tekshiriladi va `/maqola/yangi/` so'rovi qaysi view ga tushadi?

```python
urlpatterns = [
    path('maqola/<int:pk>/', views.detail, name='detail'),
    path('maqola/yangi/', views.yangi, name='yangi'),
    path('maqola/<slug:slug>/', views.slug_detail, name='slug-detail'),
]
```

- [A] `views.detail` — chunki birinchi
- [B] `views.yangi` — chunki `yangi` int emas, birinchi pattern mos kelmaydi, ikkinchisi mos keladi
- [C] `views.slug_detail` — chunki `yangi` slug formatida
- [D] Xato — ikkita pattern mos keladi

> **To'g'ri javob:** B
> **Tushuntirish:** Django yuqoridan pastga tekshiradi. `maqola/<int:pk>/` — `yangi` butun son emas, `int` converter mos kelmaydi → o'tkazib yuboradi. `maqola/yangi/` — to'g'ri mos keladi → `views.yangi` chaqiriladi. Uchinchi patternga yetib bormaydi. URL tartibini to'g'ri belgilash muhim!

---

## Savol 31

`JsonResponse` qachon ishlatiladi?

```python
from django.http import JsonResponse

def api_maqolalar(request):
    ma'lumot = {
        'maqolalar': [
            {'id': 1, 'sarlavha': 'Django'},
            {'id': 2, 'sarlavha': 'Python'},
        ]
    }
    return JsonResponse(ma'lumot)
```

- [A] Faqat Django REST Framework bilan
- [B] Javobni JSON formatida qaytarish uchun — API endpoint larda, AJAX so'rovlarda
- [C] HTML sahifalar uchun
- [D] Faqat `GET` metodida

> **To'g'ri javob:** B
> **Tushuntirish:** `JsonResponse` — `dict` ni JSON ga aylantiradi, `Content-Type: application/json` headerini qo'shadi va `HttpResponse` qaytaradi. API endpoint lar, AJAX (JavaScript) so'rovlari yoki frontend bilan aloqa uchun ishlatiladi. `safe=False` — `dict` bo'lmagan (`list`) ma'lumotlar uchun.

---

## Savol 32

Quyidagi ko'rinishda `namespace` qanday ishlatiladi?

```python
# mysite/urls.py
urlpatterns = [
    path('blog/', include('blog.urls', namespace='blog')),
    path('forum/', include('forum.urls', namespace='forum')),
]
```

Shablonda forum ning `royxat` URL ini qanday chaqirish kerak?

- [A] `{% url 'royxat' %}`
- [B] `{% url 'forum.royxat' %}`
- [C] `{% url 'forum:royxat' %}`
- [D] `{% url 'royxat' namespace='forum' %}`

> **To'g'ri javob:** C
> **Tushuntirish:** Namespace `ikki nuqta` (`:`) bilan ajratiladi: `namespace:url_nomi`. `{% url 'forum:royxat' %}` — `forum` namespace dagi `royxat` nomli URL. Bu `blog` va `forum` da bir xil `royxat` nomi bo'lsa ham to'qnashuv chiqmasligini ta'minlaydi.

---

## Savol 33

Quyidagi to'liq view + URL juftligi to'g'ri ishlaydi va `/foydalanuvchi/ali/` manziliga javob beradi?

```python
# views.py
def foydalanuvchi_profili(request, username):
    return HttpResponse(f"{username} ning profili")

# urls.py
urlpatterns = [
    path('foydalanuvchi/<str:username>/', views.foydalanuvchi_profili),
]
```

- [A] Xato — `str` converter URL da ishlatilmaydi
- [B] Xato — `username` parametri nomi mos kelmaydi
- [C] To'g'ri — `/foydalanuvchi/ali/` so'rovi `username='ali'` bilan view ni chaqiradi
- [D] Xato — `HttpResponse` da `f-string` ishlatilmaydi

> **To'g'ri javob:** C
> **Tushuntirish:** `<str:username>` — `/` dan tashqari ixtiyoriy string (harf, raqam, `-`, `_` va h.k.) qabul qiladi. `/foydalanuvchi/ali/` → `username='ali'` → `"ali ning profili"` matni qaytariladi. URL va view dagi `username` nomi mos — to'g'ri.

---

## Savol 34

`path()` konverterlari qanday ishlaydi? To'g'ri juftlikni toping.

```
1. <int:pk>
2. <str:nom>
3. <slug:slug>
4. <uuid:uid>
5. <path:fayl_yoli>
```

- [A] `<path:>` — faqat harf va raqamlar
- [B] `<slug:>` — UUID format
- [C] `<path:>` — `/` belgisini ham o'z ichiga olgan to'liq yo'l (`fayl/ichki/papka/nomi`)
- [D] `<str:>` — faqat kichik harflar

> **To'g'ri javob:** C
> **Tushuntirish:** `<path:>` — boshqa konverterlardan farqli, `/` belgisini ham qabul qiladi. Fayl yo'llari yoki ichki marshrutlash uchun. Qolganlar: `<int:>` — butun son, `<str:>` — `/` siz string, `<slug:>` — `[a-z0-9_-]`, `<uuid:>` — `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` format.

---

## Savol 35

Quyidagi view da `405 Method Not Allowed` qachon qaytariladi?

```python
from django.views.decorators.http import require_POST

@require_POST
def saqlash(request):
    # faqat POST
    ma'lumot = request.POST.get('nom')
    return HttpResponse("Saqlandi")
```

- [A] Hech qachon
- [B] `GET`, `PUT`, `DELETE` yoki boshqa non-POST metod bilan so'rov kelganda
- [C] Faqat brauzerdan so'rov kelganda
- [D] Ma'lumot bo'sh bo'lganida

> **To'g'ri javob:** B
> **Tushuntirish:** `@require_POST` dekorator — view ni faqat `POST` so'rovini qabul qilishga cheklaydi. Agar `GET` yoki boshqa metod bilan so'rov kelsa, Django avtomatik `405 Method Not Allowed` javob qaytaradi. `@require_GET`, `@require_http_methods(['GET', 'POST'])` ham mavjud.

---

## Savol 36

Quyidagi kod nima qiladi?

```python
# mysite/urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- [A] Static CSS/JS fayllarini ulaydi
- [B] Faqat production uchun
- [C] `MEDIA_URL` orqali yuklangan fayllar (`ImageField` va h.k.) ga URL orqali kirishni ta'minlaydi — faqat development uchun
- [D] `MEDIA_ROOT` papkasini yaratadi

> **To'g'ri javob:** C
> **Tushuntirish:** `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` — development da yuklangan fayllarni (`/media/rasmlar/fayl.jpg`) URL orqali ko'rish imkonini beradi. **Faqat `DEBUG=True` da ishlaydi** — production da Nginx/Apache bu vazifani bajaradi. `urlpatterns` ga `+` bilan qo'shiladi.

---

## Savol 37

Quyidagi view da `status` parametri nima uchun?

```python
def xato_sahifa(request):
    return render(request, 'xato.html', status=403)
```

- [A] Sahifani 403 soniya keyin ko'rsatadi
- [B] HTTP javob status kodini `403 Forbidden` ga o'rnatadi — brauzer va server uchun muhim
- [C] Faqat log uchun
- [D] `render()` da `status` parametri yo'q

> **To'g'ri javob:** B
> **Tushuntirish:** `render()` ning `status` parametri HTTP javob status kodini belgilaydi. Standart — `200 OK`. `status=403` — `Forbidden`, `status=404` — `Not Found`, `status=500` — `Server Error`. Brauzerlar, qidiruv tizimlari va API klientlar uchun to'g'ri status muhim.

---

## Savol 38

`include()` da 2-tuple formatidan foydalanish qanday ko'rinadi?

```python
urlpatterns = [
    path('blog/', include(('blog.urls', 'blog'))),
]
```

- [A] Xato — `include()` tuple qabul qilmaydi
- [B] To'g'ri — `(urls_modul, app_namespace)` tuple: `blog.urls` moduli `'blog'` namespace bilan ulanadi
- [C] Ikkinchi element `app_name` ni bekor qiladi
- [D] Faqat eski Django versiyalarida ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `include(('blog.urls', 'blog'))` — tuple formatida namespace berish. `blog.urls` da `app_name` yozilmagan bo'lsa ham namespace belgilanadi. Bu `include('blog.urls', namespace='blog')` bilan teng. `app_name` `blog.urls` da belgilangan bo'lsa — namespace argument shart emas.

---

## Savol 39

Quyidagi loyiha strukturasida URL fayllar qanday bog'langan?

```
mysite/
    mysite/
        urls.py        ← ROOT_URLCONF
    blog/
        urls.py        ← include bilan ulanadi
    shop/
        urls.py        ← include bilan ulanadi
    users/
        urls.py        ← include bilan ulanadi
```

So'rov `/shop/mahsulotlar/5/` kelganda qaysi fayllarga murojaat qilinadi?

- [A] Faqat `mysite/urls.py`
- [B] Faqat `shop/urls.py`
- [C] Avval `mysite/urls.py` → so'ng `shop/urls.py`
- [D] Barcha `urls.py` fayllar tekshiriladi

> **To'g'ri javob:** C
> **Tushuntirish:** Django ketma-ket tekshiradi: 1) `mysite/urls.py` da `shop/` prefiksi mos keladi → `include('shop.urls')` chaqiriladi. 2) `shop/urls.py` da `mahsulotlar/5/` qolgan qism tekshiriladi → mos view topiladi. `blog/urls.py` va `users/urls.py` ga umuman murojaat qilinmaydi.

---

## Savol 40

Quyidagi to'liq loyiha URL konfiguratsiyasida `/blog/5/` manziliga so'rov kelganda nima chiqadi?

```python
# mysite/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]

# blog/urls.py
app_name = 'blog'
urlpatterns = [
    path('', views.royxat, name='royxat'),
    path('<int:pk>/', views.detail, name='detail'),
    path('yangi/', views.yangi, name='yangi'),
]

# blog/views.py
def detail(request, pk):
    maqola = get_object_or_404(Maqola, pk=pk)
    return render(request, 'blog/detail.html', {'maqola': maqola, 'pk': pk})
```

- [A] `royxat` view chaqiriladi
- [B] `yangi` view chaqiriladi
- [C] `detail` view `pk=5` bilan chaqiriladi va `blog/detail.html` shabloni `maqola` va `pk` konteksti bilan render qilinadi
- [D] `404` xatosi

> **To'g'ri javob:** C
> **Tushuntirish:** `/blog/5/` → `mysite/urls.py` da `blog/` mos → `blog/urls.py` ga `5/` uzatiladi → `<int:pk>/` patternga mos → `views.detail(request, pk=5)` chaqiriladi → `Maqola` pk=5 bilan olinadi → `blog/detail.html` shabloni `{'maqola': ..., 'pk': 5}` konteksti bilan render qilinadi → `HttpResponse` qaytariladi.

---