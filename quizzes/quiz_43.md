## Savol 1

`makemigrations` buyrug'i nima qiladi?

- [A] Ma'lumotlar bazasini to'liq o'chiradi va qayta yaratadi
- [B] `models.py` dagi o'zgarishlarni o'qib, migration fayl yaratadi — lekin DB ga hech narsa qilmaydi
- [C] Migration fayllarini o'qib, ma'lumotlar bazasini yangilaydi
- [D] Serverni qayta ishga tushiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `makemigrations` — faqat `migrations/` papkasida yangi Python fayl (`0001_initial.py`, `0002_...py` va h.k.) yaratadi. Bu fayl model o'zgarishlarini tasvirlaydi. Haqiqiy SQL va DB o'zgarishlari uchun `migrate` ishlatiladi.

---

## Savol 2

`migrate` buyrug'i nima qiladi?

- [A] Yangi migration fayllar yaratadi
- [B] Modellarni tekshiradi va xatolarni topadi
- [C] Mavjud migration fayllarni o'qib, SQL so'rovlar orqali ma'lumotlar bazasini yangilaydi
- [D] Faqat Django standart applarini o'rnatadi

> **To'g'ri javob:** C
> **Tushuntirish:** `migrate` — `migrations/` papkasidagi fayllarni ketma-ket o'qib, ularni hali qo'llanilmagan bo'lsa DB ga tatbiq etadi. Django qaysi migratsiyalar allaqachon bajarilganini `django_migrations` jadvalida kuzatib boradi.

---

## Savol 3

Birinchi marta loyiha yaratilganda `python manage.py migrate` buyrug'i nima qiladi?

- [A] Hech narsa — faqat foydalanuvchi modellari uchun ishlaydi
- [B] Xato beradi — avval `makemigrations` kerak
- [C] Django standart applarining (`auth`, `admin`, `sessions` va h.k.) jadvallarini yaratadi
- [D] Faqat `db.sqlite3` faylini yaratadi, jadvallar bo'lmaydi

> **To'g'ri javob:** C
> **Tushuntirish:** `INSTALLED_APPS` dagi standart Django applar (`django.contrib.auth`, `django.contrib.admin` va h.k.) allaqachon o'z migration fayllariga ega. Birinchi `migrate` ularni DB ga qo'llab, `users`, `auth_permission`, `django_session` kabi jadvallarni yaratadi.

---

## Savol 4

Quyidagi buyruq nima chiqaradi agar hech qanday o'zgarish bo'lmasa?

```bash
$ python manage.py makemigrations
```

- [A] `Error: nothing to migrate`
- [B] `No changes detected`
- [C] Bo'sh migration fayl yaratadi
- [D] Serverni to'xtatadi

> **To'g'ri javob:** B
> **Tushuntirish:** Agar `models.py` dagi o'zgarishlar oxirgi migration bilan mos kelsa, Django `No changes detected` xabarini chiqaradi va hech qanday fayl yaratmaydi. Bu xatolik emas — shunchaki o'zgarish yo'qligini bildiradi.

---

## Savol 5

Migration fayllarining to'g'ri ketma-ketligi qaysi?

```
0001_initial.py
0002_add_email_field.py
0003_alter_name_max_length.py
```

- [A] Fayllar har safar qayta yoziladi — faqat bitta fayl bo'ladi
- [B] Har bir o'zgarish uchun yangi fayl qo'shiladi, oldingilari saqlanadi
- [C] Faqat oxirgi fayl ishlaydi, qolganlar o'chadi
- [D] Fayllar orden muhim emas — ixtiyoriy tartibda bajariladi

> **To'g'ri javob:** B
> **Tushuntirish:** Migration fayllar ketma-ket to'planib boradi — har bir `makemigrations` yangi raqamlangan fayl yaratadi. Django ularni `0001 → 0002 → 0003` tartibida bajaradi. Bu tarix sifatida saqlanadi va o'chirib bo'lmaydi (agar DB bilan sinxronlashtirilmagan bo'lsa).

---

## Savol 6

`python manage.py showmigrations` buyrug'i nima ko'rsatadi?

- [A] Faqat xatolik bo'lgan migratsiyalarni
- [B] Barcha migration fayllar ro'yxatini va qaysilari bajarilganini (`[X]`) yoki bajarilmaganini (`[ ]`) ko'rsatadi
- [C] Migration fayllarining SQL kodini ko'rsatadi
- [D] Faqat so'nggi migratsiyani ko'rsatadi

> **To'g'ri javob:** B
> **Tushuntirish:** `showmigrations` — monitoring vositasi. `[X]` — bajarilgan, `[ ]` — bajarilmagan. Barcha applar bo'yicha migratsiyalar holati ko'rinadi. Bu `migrate` dan oldin qaysi migratsiyalar qo'llanilganligini tekshirish uchun foydali.

---

## Savol 7

Quyidagi buyruq nima qiladi?

```bash
$ python manage.py sqlmigrate blog 0001
```

- [A] Migration ni bajaradi
- [B] `blog` appining `0001` migration i uchun bajariladigan SQL so'rovlarni ko'rsatadi — lekin DB ga hech narsa qilmaydi
- [C] Migration ni bekor qiladi
- [D] Migration faylini o'chiradi

> **To'g'ri javob:** B
> **Tushuntirish:** `sqlmigrate` — migration bajariladigan SQL ni ko'rish imkonini beradi (`CREATE TABLE`, `ALTER TABLE` va h.k.). Bu debug va audit uchun juda foydali. Haqiqiy o'zgartirish qilmaydi — faqat ko'rsatadi.

---

## Savol 8

Model ga yangi maydon qo'shildi. Qanday tartibda harakat qilish kerak?

```python
# models.py ga qo'shildi:
telefon = models.CharField(max_length=20, blank=True)
```

- [A] Faqat `migrate` yetarli
- [B] Faqat `makemigrations` yetarli
- [C] `makemigrations` → so'ng `migrate`
- [D] Serverni qayta ishga tushirish yetarli

> **To'g'ri javob:** C
> **Tushuntirish:** Har doim ikki qadam: 1) `makemigrations` — o'zgarishni migration fayliga yozadi. 2) `migrate` — shu faylni o'qib, DB dagi jadvalga yangi ustun qo'shadi. Birinchi qadamsiz ikkinchisi DB ni yangilay olmaydi.

---

## Savol 9

`migrations/__init__.py` faylining vazifasi nima?

- [A] Birinchi migratsiya faylini saqlaydi
- [B] `migrations` papkasini Python paketi sifatida belgilaydi — bo'sh fayl
- [C] Barcha migratsiyalarni boshqaradi
- [D] Ma'lumotlar bazasi ulanishini saqlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `__init__.py` — papkani Python paketi (modul) sifatida belgilash uchun zarur bo'sh fayl. Bu Python ning standart mexanizmi. `migrations/` papkasidagi bu fayl bo'lmasa, Django migratsiya fayllarini import qila olmaydi.

---

## Savol 10

Quyidagi migratsiya faylida `dependencies` nima anglatadi?

```python
class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]
    operations = [...]
```

- [A] Tashqi kutubxonalar ro'yxati
- [B] Bu migratsiya bajarilishidan oldin qaysi migratsiya bajarilgan bo'lishi kerakligini bildiradi
- [C] App larga bog'liqlik
- [D] Ma'lumotlar bazasi drayverini belgilaydi

> **To'g'ri javob:** B
> **Tushuntirish:** `dependencies` — migratsiyalar tartibi va bog'liqligini belgilaydi. `('blog', '0001_initial')` — bu migratsiya faqat `blog` appining `0001` migration i bajarilgandan keyin ishga tushadi. Bu ketma-ketlikni kafolatlaydi.

---

## Savol 11

`python manage.py migrate blog zero` buyrug'i nima qiladi?

- [A] `blog` appini o'chiradi
- [B] `blog` appining barcha migratsiyalarini bekor qiladi — jadvallar o'chadi
- [C] Faqat `0001` migratsiyani bekor qiladi
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `migrate appnomi zero` — rollback (qaytarish). `blog` appiga tegishli barcha migratsiyalarni bekor qilib, yaratilgan jadvallarni o'chiradi. `zero` — "hech qanday migratsiya qo'llanilmagan holat" degani. Faqat `reverse` qo'llab-quvvatlaydigan migratsiyalar uchun ishlaydi.

---

## Savol 12

Bir migration faylini qo'lda o'chirish natijasi nima bo'lishi mumkin?

- [A] Hech narsa — Django avtomatik qayta yaratadi
- [B] Django va ma'lumotlar bazasi o'rtasida nomuvofiqlik yuzaga keladi — xato va nosozliklar
- [C] Faqat admin panelda muammo bo'ladi
- [D] Keyingi `makemigrations` avtomatik tuzatadi

> **To'g'ri javob:** B
> **Tushuntirish:** Migration fayllarini qo'lda o'chirish xavfli! `django_migrations` jadvalida shu fayl bajarilgan deb belgilangan bo'lsa, Django holatni noto'g'ri tushunadi. Natijada `InconsistentMigrationHistory` yoki `Table already exists` kabi xatolar chiqadi.

---

## Savol 13

`makemigrations --name` parametri nima uchun ishlatiladi?

```bash
$ python manage.py makemigrations blog --name add_phone_field
```

- [A] Appni nomini o'zgartiradi
- [B] Migration fayliga odatiy avtomatik nom o'rniga tushunarli nom beradi: `0002_add_phone_field.py`
- [C] Migration ni bajaradi va nomini belgilaydi
- [D] Faqat test uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `--name` — migration fayl nomini belgilash imkonini beradi. Masalan: `0002_add_phone_field.py`. Bu keyinchalik migration tarixini o'qishni osonlashtiradi. Belgilanmasa Django avtomatik nom beradi: `0002_maqola_telefon.py`.

---

## Savol 14

`python manage.py migrate blog 0002` buyrug'i nima qiladi?

- [A] `0002` migratsiyani qaytaradi (rollback)
- [B] Faqat `0002` gacha bo'lgan migratsiyalarni qo'llaydi — `0003` va undan keyingilar bajarilmaydi
- [C] Faqat `0002` ni bajaradi, qolganlarni o'tkazib yuboradi
- [D] Xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** `migrate appnomi raqam` — ko'rsatilgan migratsiyagacha qo'llaydi yoki qaytaradi. Agar `0003` allaqachon bajarilgan bo'lsa, `0002` ga qaytaradi (rollback). Agar `0001` gacha bajarilgan bo'lsa, `0002` ni qo'llaydi. Muayyan versiyaga o'tish uchun ishlatiladi.

---

## Savol 15

`squashmigrations` buyrug'i nima maqsadda ishlatiladi?

- [A] Migration fayllarni ziplash
- [B] Ko'p sonli migration fayllarni bitta yoki kamroq faylga birlashtirish — eski tarixni soddalashtirish
- [C] Migration fayllarni o'chirish
- [D] Migration larni test qilish

> **To'g'ri javob:** B
> **Tushuntirish:** Vaqt o'tishi bilan migration fayllar ko'payib ketadi (masalan, 100+ ta). `squashmigrations` ularni bitta optimallashtirilgan faylga jamlaydi. Bu loyiha unib-o'sgandan keyin `makemigrations` vaqtini va tarix hajmini kamaytiradi.

---

## Savol 16

Quyidagi xatolik qanday holatda yuzaga keladi?

```
django.db.utils.OperationalError: table "blog_maqola" already exists
```

- [A] `models.py` da xato bor
- [B] `migrate` ikki marta ishga tushirildi — lekin bu odatda bo'lmaydi, chunki Django kuzatib boradi
- [C] Migration faylli o'chirib, `migrate` qayta ishlatildi — DB dagi jadval saqlanib qolgan, lekin Django uni yo bilmaydi
- [D] `makemigrations` ishlatilmagan

> **To'g'ri javob:** C
> **Tushuntirish:** Bu xatolik `django_migrations` jadvali bilan haqiqiy DB o'rtasidagi nomuvofiqlikdan kelib chiqadi. Ko'pincha migration fayllar o'chirilganda yoki `migrate` ni chetlab `CREATE TABLE` qo'lda bajarilganda paydo bo'ladi. Yechim: `--fake` yoki `--fake-initial` parametrlaridan foydalanish.

---

## Savol 17

`--fake` parametri qanday holatda ishlatiladi?

```bash
$ python manage.py migrate blog --fake
```

- [A] Ma'lumotlar bazasini o'zgartirmasdan, migratsiyalarni bajarilgan deb belgilaydi
- [B] Test rejimida migratsiyani bajaradi
- [C] Migration ni tezlashtiradi
- [D] Migration ni bekor qiladi

> **To'g'ri javob:** A
> **Tushuntirish:** `--fake` — `django_migrations` jadvalida migratsiyani bajarilgan deb yozadi, lekin haqiqiy SQL ishlatmaydi. Agar DB da jadval allaqachon bor bo'lsa-yu, Django bilmasa, shu buyruq orqali sinxronlashtiriladi. Ehtiyotkorlik bilan ishlatish kerak.

---

## Savol 18

`RunPython` nima va migratsiya faylida qanday ishlatiladi?

```python
def populate_data(apps, schema_editor):
    Maqola = apps.get_model('blog', 'Maqola')
    Maqola.objects.create(sarlavha='Birinchi maqola')

class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(populate_data),
    ]
```

- [A] Faqat jadval yaratish uchun
- [B] Migratsiya ichida ixtiyoriy Python kodi bajarish imkonini beradi — data migration uchun ishlatiladi
- [C] Modelni import qilish uchun
- [D] Faqat test ma'lumotlari uchun

> **To'g'ri javob:** B
> **Tushuntirish:** `RunPython` — migratsiya davomida Python kodi bajarish imkonini beradi. **Data migration** (schema o'zgarishi bilan birga ma'lumotlarni ham ko'chirish/to'ldirish) uchun ishlatiladi. `apps.get_model()` orqali model tarix versiyasiga murojaat qilinadi.

---

## Savol 19

Ikki dasturchi bir vaqtda `models.py` ga o'zgartirish kiritib, har biri `makemigrations` qildi. Natijada nima bo'ladi?

- [A] Hech qanday muammo yo'q — Django avtomatik birlashtiradi
- [B] Migration conflict (ziddiyat) yuzaga keladi — ikkita migration bir xil ota-migratsiyaga bog'liq bo'lib qoladi
- [C] Faqat birinchi migration saqlanadi
- [D] Ikkinchi `makemigrations` xato beradi

> **To'g'ri javob:** B
> **Tushuntirish:** Ikkala dasturchi `0003` ni ota sifatida ko'rsatgan `0004_a.py` va `0004_b.py` yaratsa — conflict. Yechim: `python manage.py makemigrations --merge` buyrug'i ikkala migration ni birlashtiruvchi yangi fayl yaratadi.

---

## Savol 20

Quyidagi to'liq stsenariyda qaysi qadam **noto'g'ri**?

```
1. models.py ga yangi Model qo'shildi
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py runserver
```

- [A] 1-qadam — model `INSTALLED_APPS` siz ham ishlaydi
- [B] Barcha qadamlar to'g'ri — bu standart Django ish jarayoni
- [C] 3-qadam — `migrate` dan oldin server ishga tushirilishi kerak
- [D] 2-qadam — `makemigrations` kerak emas, `migrate` o'zi aniqlaydi

> **To'g'ri javob:** B
> **Tushuntirish:** Bu to'liq to'g'ri va standart Django ish jarayoni: model yoziladi → migration yaratiladi → DB yangilanadi → server ishga tushiriladi. Faqat bitta shart: model appning `INSTALLED_APPS` da ro'yxatdan o'tgan bo'lishi kerak — bu esa 1-qadam oldidan bajarilgan deb qabul qilinadi.

---