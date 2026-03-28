## Savol 1

Django shablonida o'zgaruvchi qiymatini chiqarish uchun qaysi sintaksis ishlatiladi?

- [A] `<% ism %>`
- [B] `{{ ism }}`
- [C] `{# ism #}`
- [D] `{% ism %}`

> **To'g'ri javob:** B
> **Tushuntirish:** Django shablon tizimida uch xil maxsus belgi bor: `{{ }}` — o'zgaruvchi qiymatini chiqarish uchun, `{% %}` — teg (mantiq, shart, tsikl) uchun, `{# #}` — izoh (comment) uchun. `<% %>` — Ruby/ERB sintaksisi, Django da ishlatilmaydi.

---

## Savol 2

Quyidagi shablonda `{{ maqola.sarlavha }}` qanday ishlaydi?

```html
<!-- views.py dan: {'maqola': maqola_obj} -->
<h1>{{ maqola.sarlavha }}</h1>
```

- [A] `maqola` degan so'zni, keyin `sarlavha` degan so'zni chiqaradi
- [B] `maqola` kontekst o'zgaruvchisining `sarlavha` atributini (yoki dict kalitini) chiqaradi
- [C] `maqola.sarlavha` ni hisoblaydi
- [D] Xato beradi — nuqta ishlatilmaydi

> **To'g'ri javob:** B
> **Tushuntirish:** Django shablon tizimida nuqta (`.`) quyidagilarni ketma-ket tekshiradi: 1) obyekt atributi (`obj.attr`), 2) dict kaliti (`dict['kalit']`), 3) ro'yxat indeksi (`list[0]`), 4) chaqiriladigan metod (`obj.metod()`). Mos kelgani ishlatiladi.

---

## Savol 3

`{% if %}` bloki qanday yoziladi?

```html
{% if foydalanuvchi.is_authenticated %}
    <p>Xush kelibsiz, {{ foydalanuvchi.username }}!</p>
{% else %}
    <p>Iltimos, kiring.</p>
{% endif %}
```

- [A] `{% endif %}` o'rniga `{% /if %}` yozilishi kerak
- [B] `{% else %}` qo'llab-quvvatlanmaydi
- [C] To'g'ri — `{% if %}`, `{% else %}`, `{% endif %}` standart sintaksis
- [D] Xato — `if` da qavs ishlatilishi kerak: `{% if (shart) %}`

> **To'g'ri javob:** C
> **Tushuntirish:** Django da barcha blok teglar yopilishi shart: `{% if %}...{% endif %}`, `{% for %}...{% endfor %}`, `{% block %}...{% endblock %}`. `{% else %}` va `{% elif %}` ixtiyoriy. Qavslar shart emas — Python dan farqli.

---

## Savol 4

Quyidagi `{% for %}` tsikli nima chiqaradi?

```html
{% for meva in mevalar %}
    <li>{{ meva }}</li>
{% endfor %}
```

`mevalar = ['olma', 'nok', 'uzum']` bo'lsa:

- [A] Faqat `olma`
- [B] `<li>olma</li>`, `<li>nok</li>`, `<li>uzum</li>` — uchta `<li>` elementi
- [C] `['olma', 'nok', 'uzum']`
- [D] Xato — `for` da `in` ishlatilmaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `{% for element in royxat %}` — har bir element uchun blok takrorlanadi. `mevalar` da 3 ta element bor, shuning uchun 3 ta `<li>` yaratiladi. `{% endfor %}` blok oxirini belgilaydi. `forloop.counter`, `forloop.first`, `forloop.last` kabi maxsus o'zgaruvchilar ham mavjud.

---

## Savol 5

`{% for %}` ichidagi `forloop.counter` nima qaytaradi?

```html
{% for maqola in maqolalar %}
    <p>{{ forloop.counter }}. {{ maqola.sarlavha }}</p>
{% endfor %}
```

- [A] `0` dan boshlangan indeks
- [B] `1` dan boshlangan joriy iteratsiya raqami
- [C] Elementlar umumiy soni
- [D] Oxirgi element indeksi

> **To'g'ri javob:** B
> **Tushuntirish:** `forloop.counter` — `1` dan boshlanadi. `forloop.counter0` — `0` dan boshlanadi. `forloop.revcounter` — oxiridan sanaydi. `forloop.first` — birinchi iteratsiyada `True`. `forloop.last` — oxirgi iteratsiyada `True`. Bular `{% for %}` ichida avtomatik mavjud.

---

## Savol 6

`{% empty %}` tegi qachon ishlaydi?

```html
{% for maqola in maqolalar %}
    <li>{{ maqola.sarlavha }}</li>
{% empty %}
    <li>Hozircha maqola yo'q.</li>
{% endfor %}
```

- [A] Har doim `{% empty %}` bloki ham chiqadi
- [B] `maqolalar` bo'sh (`[]`) yoki `None` bo'lsa, `{% empty %}` bloki ko'rsatiladi
- [C] Faqat `None` da ishlaydi
- [D] `{% empty %}` Django da yo'q

> **To'g'ri javob:** B
> **Tushuntirish:** `{% empty %}` — ro'yxat bo'sh bo'lganida muqobil kontent ko'rsatish uchun. `maqolalar.count() == 0` yoki bo'sh `QuerySet` bo'lsa, `{% empty %}` bloki render qilinadi. `{% for %}` oddiy ishlasa, `{% empty %}` e'tiborga olinmaydi. Kod soddalashtiradi.

---

## Savol 7

Shablon filtrlari qanday ishlatiladi?

```html
{{ matn | upper }}
{{ sana | date:"d.m.Y" }}
{{ narx | floatformat:2 }}
```

- [A] `|` — Python `or` operatori
- [B] `|` — filtr operatori; o'zgaruvchi qiymatini o'zgartiradi yoki formatlaydi
- [C] `|` — ikki qiymatni birlashtiradi
- [D] Xato — filtrlarda qo'shtirnoq ishlatilmaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `{{ qiymat | filtr_nomi }}` yoki `{{ qiymat | filtr_nomi:argument }}` — filtr sintaksisi. `upper` — katta harfga; `date:"d.m.Y"` — sana formatlash; `floatformat:2` — 2 ta kasr o'rin. Filtrlar zanjirlanishi mumkin: `{{ matn | lower | truncatewords:10 }}`.

---

## Savol 8

Quyidagi filtrlardan qaysi biri matnni qisqartiradi?

```html
{{ maqola.matn | truncatewords:20 }}
```

- [A] Matndagi 20 ta belgini qoldiradi
- [B] Matndagi **20 ta so'zni** qoldiradi, qolganini `...` bilan almashtiradi
- [C] 20 ta qatorni qoldiradi
- [D] 20 ta paragrafni qoldiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `truncatewords:20` — dastlabki **20 ta so'z** ko'rsatiladi, qolganlari o'rniga `...` qo'yiladi. `truncatechars:100` — 100 ta **belgi** ga qisqartiradi. Maqolalar ro'yxatida to'liq matni o'rniga qisqa ko'rinish uchun foydali.

---

## Savol 9

`{{ qiymat | default:"Noma'lum" }}` qachon `"Noma'lum"` chiqaradi?

- [A] Har doim
- [B] `qiymat` `False`, bo'sh string, `None`, `0`, bo'sh ro'yxat — ya'ni "falsy" qiymat bo'lganida
- [C] Faqat `qiymat` `None` bo'lganida
- [D] Hech qachon — bu sintaksis xato

> **To'g'ri javob:** B
> **Tushuntirish:** `default` filtri — qiymat "falsy" bo'lganda (`None`, `""`, `0`, `False`, `[]`, `{}`) zaxira qiymat ko'rsatadi. Faqat `None` uchun `default_if_none` filtri ishlatiladi. `{{ ism | default:"Mehmon" }}` — ism bo'sh bo'lsa `"Mehmon"` chiqadi.

---

## Savol 10

`{% block %}` va `{% extends %}` qanday maqsadda ishlatiladi?

```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head><title>{% block title %}Sayt{% endblock %}</title></head>
<body>
    {% block content %}{% endblock %}
</body>
</html>

<!-- blog/royxat.html -->
{% extends 'base.html' %}

{% block title %}Maqolalar{% endblock %}
{% block content %}
    <h1>Barcha maqolalar</h1>
{% endblock %}
```

- [A] `extends` — JavaScript fayllarni ulash uchun
- [B] `extends` — bosh shablondan meros olish; `block` — ota-shablondagi o'rnini bola shablon to'ldiradi
- [C] `block` — HTML blok elementi yaratadi
- [D] `extends` ixtiyoriy — `block` yolg'iz ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** Django ning kuchli xususiyati — shablon merosi. `base.html` — asosiy skelet (header, footer, CSS). `{% block nom %}` — bola shablon to'ldiradigan joy. `{% extends 'base.html' %}` — bola shablon ota-shablondan meros oladi. Kod takrorlanishi oldini oladi (DRY).

---

## Savol 11

`{% extends %}` tegi shablonning qayerida bo'lishi kerak?

- [A] `{% block %}` dan keyin
- [B] Shablonning **birinchi satri** da — undan oldin hech narsa bo'lmasligi kerak
- [C] `</body>` oldida
- [D] Istalgan joyda

> **To'g'ri javob:** B
> **Tushuntirish:** `{% extends %}` — **shart ravishda birinchi satrda** bo'lishi kerak. Undan oldin hech qanday HTML, bo'sh joy yoki boshqa teg bo'lmasligi kerak. Aks holda Django xato beradi yoki kutilmagan natija chiqadi. Bu qat'iy talab.

---

## Savol 12

`{% include %}` tegi nima qiladi?

```html
<!-- bosh.html -->
{% include 'partials/navbar.html' %}
<main>
    {% block content %}{% endblock %}
</main>
{% include 'partials/footer.html' %}
```

- [A] Boshqa shablon faylini import qiladi (Python import kabi)
- [B] Ko'rsatilgan shablon faylini render qilib, joriy joyga qo'yadi
- [C] Faqat JavaScript fayllar uchun
- [D] Boshqa view ni chaqiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `{% include 'fayl.html' %}` — ko'rsatilgan shablonni render qilib, joriy shablonga joylashtiradi. Joriy kontekst avtomatik uzatiladi. Takrorlanadigan qismlar (navbar, footer, sidebar, karta) uchun ishlatiladi. `{% extends %}` dan farqi: `include` qism, `extends` meros.

---

## Savol 13

`{{ matn | safe }}` filtri nima qiladi va qachon xavfli?

```html
{{ maqola.matn | safe }}
```

- [A] Matnni shifrlaydi
- [B] HTML teglarga escape qo'yishni o'chirib, raw HTML chiqaradi — foydalanuvchi kiritgan ma'lumotlarda XSS xavfi bor
- [C] Matnni xavfsiz serverga yuboradi
- [D] Faqat admin uchun

> **To'g'ri javob:** B
> **Tushuntirish:** Django standart ravishda barcha o'zgaruvchilarni escape qiladi (`<` → `&lt;`). `| safe` bu himoyani o'chiradi — raw HTML chiqadi. Agar foydalanuvchi kiritgan ma'lumot bo'lsa, `<script>alert('XSS')</script>` kabi hujumlar mumkin. Faqat ishonchli ma'lumotlar uchun ishlatilng.

---

## Savol 14

`{% csrf_token %}` nima uchun kerak?

```html
<form method="post" action="/saqlash/">
    {% csrf_token %}
    <input type="text" name="sarlavha">
    <button type="submit">Saqlash</button>
</form>
```

- [A] Formani chiroyli qiladi
- [B] Cross-Site Request Forgery hujumidan himoya — Django POST so'rovini tasdiqlash uchun yashirin token qo'shadi
- [C] Faqat HTTPS da ishlaydi
- [D] Formani JavaScript bilan yuborish uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `{% csrf_token %}` — yashirin `<input type="hidden" name="csrfmiddlewaretoken" value="...">` qo'shadi. Django har POST so'rovda bu tokenni tekshiradi. Token bo'lmasa `403 Forbidden` qaytariladi. `method="post"` bilan ishlatiladigan **barcha formalarda majburiy**.

---

## Savol 15

`{% load %}` tegi qachon kerak?

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">

{% load humanize %}
{{ son | intcomma }}
```

- [A] Barcha shablonlarda avtomatik yuklanadi
- [B] Standart bo'lmagan shablon teglari va filtrlarini (`static`, `humanize` va h.k.) shablonga yuklaydi
- [C] Python modullarini import qiladi
- [D] `settings.py` dagi sozlamalarni yuklaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `{% load %}` — qo'shimcha shablon kutubxonalarini yuklaydi. `{% load static %}` — `{% static %}` tegini faollashtiradi (CSS, JS, rasm yo'llari uchun). `{% load humanize %}` — `intcomma`, `naturalday` kabi filtrlarni. `{% load %}` fayl boshida yoziladi.

---

## Savol 16

`{% static %}` tegi qanday ishlaydi?

```html
{% load static %}
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

- [A] Rasmni ma'lumotlar bazasidan oladi
- [B] `settings.py` dagi `STATIC_URL` bilan `'images/logo.png'` yo'lini birlashtiradi: masalan `/static/images/logo.png`
- [C] Rasmni base64 ga aylantiradi
- [D] Faqat production da ishlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `{% static 'fayl/yoli' %}` → `STATIC_URL + 'fayl/yoli'` → masalan `/static/images/logo.png`. `STATIC_URL = '/static/'` bo'lsa. Bu yol hardcode qilmaslik imkonini beradi — `STATIC_URL` o'zgarsa, barcha shablonlar avtomatik yangilanadi. `{% load static %}` oldin yozilishi shart.

---

## Savol 17

Quyidagi shablonda `{% if %}` da qanday operatorlar ishlatilishi mumkin?

```html
{% if yosh >= 18 and mamlakat == "UZ" %}
    <p>Kirish mumkin</p>
{% elif yosh < 18 %}
    <p>Yoshingiz yetarli emas</p>
{% else %}
    <p>Mamlakat mos emas</p>
{% endif %}
```

- [A] Faqat `==` va `!=`
- [B] `==`, `!=`, `<`, `>`, `<=`, `>=`, `and`, `or`, `not`, `in`, `not in`
- [C] Faqat `and` va `or`
- [D] Python operatorlarining barchasi — shu jumladan `is`, `is not`

> **To'g'ri javob:** B
> **Tushuntirish:** Django shablon tizimi quyidagilarni qo'llab-quvvatlaydi: taqqoslash (`==`, `!=`, `<`, `>`, `<=`, `>=`), mantiq (`and`, `or`, `not`), a'zolik (`in`, `not in`). **Ishlamaydiganlar:** `is`, `is not`, matematik amallar (`+`, `-`, `*`), `//`. Murakkab hisoblashlar view da bajarilishi kerak.

---

## Savol 18

`{{ sana | date:"l, j-F Y" }}` chiqarishi nima bo'ladi? (`sana = 2024-03-15`)

- [A] `2024-03-15`
- [B] `Friday, 15-March 2024`
- [C] `15/03/2024`
- [D] `March 15, 2024`

> **To'g'ri javob:** B
> **Tushuntirish:** `date` filtri PHP date formatlash sintaksisiga o'xshaydi: `l` — to'liq hafta kuni nomi (`Friday`), `j` — nol siz kun raqami (`15`), `F` — to'liq oy nomi (`March`), `Y` — to'rt xonali yil (`2024`). `d` — nol bilan kun (`01-31`), `m` — raqamli oy (`01-12`), `y` — ikki xonali yil.

---

## Savol 19

Quyidagi shablon fragmenti qanday xatoga ega?

```html
{% extends 'base.html' %}
{% load static %}

{% block content %}
    <img src="{% static 'img/banner.jpg' %}">
    {% for maqola in maqolalar %}
        <h2>{{ maqola.sarlavha }}</h2>
    {% endfor %}
    {# Bu yerda eski kontent bor edi #}
{% endblock %}
```

- [A] `{% load static %}` `{% extends %}` dan oldin bo'lishi kerak edi
- [B] `{# ... #}` izoh sintaksisi noto'g'ri
- [C] Xato yo'q — to'g'ri yozilgan
- [D] `{% block %}` da `{% load %}` ishlatilmaydi

> **To'g'ri javob:** C
> **Tushuntirish:** Kod to'liq to'g'ri. `{% extends %}` — birinchi satrda ✓. `{% load static %}` — `{% extends %}` dan keyin yozish mumkin ✓. `{% static %}` `{% block %}` ichida ishlaydi ✓. `{# ... #}` — to'g'ri izoh sintaksisi ✓. `{% for %}...{% endfor %}` — to'g'ri yopilgan ✓.

---

## Savol 20

Quyidagi to'liq shablon to'g'ri render qilinib, brauzerda qanday ko'rinadi?

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}{{ blog.nomi }} — Bosh sahifa{% endblock %}

{% block content %}
<div class="container">
    <h1>{{ blog.nomi }}</h1>

    {% if maqolalar %}
        {% for maqola in maqolalar %}
        <article>
            <h2>{{ maqola.sarlavha | title }}</h2>
            <p>{{ maqola.matn | truncatewords:30 }}</p>
            <small>
                {{ maqola.yaratilgan | date:"d.m.Y" }} |
                {{ maqola.muallif | default:"Noma'lum muallif" }}
            </small>
            <a href="{% url 'blog:detail' maqola.pk %}">Ko'proq o'qi</a>
        </article>
        {% endfor %}
    {% else %}
        <p>Hozircha maqola mavjud emas.</p>
    {% endif %}
</div>
{% endblock %}
```

`kontekst = {'blog': blog_obj, 'maqolalar': [maqola1, maqola2]}` bo'lsa, **noto'g'ri** xulosa qaysi?

- [A] Sahifa `<title>` tegi `blog.nomi` ni o'z ichiga oladi
- [B] Har bir maqola sarlavhasi `Title Case` ga aylantiriladi
- [C] `{% else %}` bloki ko'rsatiladi — chunki ro'yxatda 2 ta element bor
- [D] Har bir maqola matni 30 so'zdan keyin qisqartiriladi

> **To'g'ri javob:** C
> **Tushuntirish:** `maqolalar` da 2 ta element bor — bu "truthy" qiymat. Shuning uchun `{% if maqolalar %}` `True` bo'lib, `{% for %}` tsikli ishlaydi va `{% else %}` bloki **ko'rsatilmaydi**. Qolgan xulosalar to'g'ri: `| title` → Title Case, `| truncatewords:30` → 30 so'z, `{% block title %}` → `<title>` ichiga.

---