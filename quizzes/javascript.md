# JavaScript Asoslari — Test

## Savol 1

Quyidagi JavaScript kodining natijasi nima?

```javascript
console.log(typeof null);
```

- [A] `"null"`
- [B] `"undefined"`
- [C] `"object"`
- [D] `"boolean"`

> **To'g'ri javob:** C
> **Tushuntirish:** Bu JavaScript'ning mashhur xatolaridan biri. `typeof null` — `"object"` qaytaradi. Bu tilning dastlabki versiyasidagi bug bo'lib, orqaga muvofiqlik uchun saqlab qolindi.

---

## Savol 2

Quyidagi kod nima chiqaradi?

```javascript
let x = 10;
let y = "10";
console.log(x == y);
console.log(x === y);
```

- [A] `true true`
- [B] `true false`
- [C] `false true`
- [D] `false false`

> **To'g'ri javob:** B
> **Tushuntirish:** `==` (loose equality) turlarni o'zgartiradi va solishtiradi, shuning uchun `10 == "10"` — `true`. `===` (strict equality) turlarni ham tekshiradi: `number !== string`, shuning uchun `false`.

---

## Savol 3

Quyidagi kodning natijasi nima?

```javascript
const arr = [1, 2, 3];
arr.push(4);
console.log(arr.length);
```

- [A] `3`
- [B] `4`
- [C] `5`
- [D] Xatolik chiqadi

> **To'g'ri javob:** B
> **Tushuntirish:** `const` massivning o'zgaruvchisini qayta tayinlashni taqiqlaydi, lekin massiv ichidagi elementlarni o'zgartirishga ruxsat beradi. `push(4)` elementni qo'shadi, natija `[1,2,3,4]`, uzunligi `4`.

---

## Savol 4

Quyidagi kodda nima sodir bo'ladi?

```javascript
setTimeout(() => console.log("A"), 0);
console.log("B");
```

- [A] `A` keyin `B`
- [B] `B` keyin `A`
- [C] Faqat `B`
- [D] Faqat `A`

> **To'g'ri javob:** B
> **Tushuntirish:** `setTimeout` callback'ni event loop'ning keyingi tsikliga joylashtiradi, hatto delay 0 bo'lsa ham. Sinxron kod (`console.log("B")`) avval bajariladi, keyin asinxron callback.

---

## Savol 5

`Array.isArray([1, 2, 3])` qanday natija beradi?

- [A] `true`
- [B] `false`
- [C] `undefined`
- [D] `"array"`

> **To'g'ri javob:** A
> **Tushuntirish:** `Array.isArray()` metodi argument massiv ekanligini tekshiradi va `true` yoki `false` qaytaradi. `[1, 2, 3]` massiv bo'lgani uchun `true`.

---

## Savol 6

Quyidagi kodning natijasi nima?

```javascript
const obj = { a: 1, b: 2, c: 3 };
const { a, ...rest } = obj;
console.log(rest);
```

- [A] `{ a: 1 }`
- [B] `{ b: 2, c: 3 }`
- [C] `[2, 3]`
- [D] `undefined`

> **To'g'ri javob:** B
> **Tushuntirish:** Destructuring bilan `a` alohida olinadi, `...rest` esa qolgan barcha xususiyatlarni yangi objektga yig'adi: `{ b: 2, c: 3 }`.
