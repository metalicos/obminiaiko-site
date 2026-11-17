# Обміняйко — сайт

Сайт застосунку «Обміняйко» для iPhone: головна, підтримка й політика конфіденційності для App Store.

- Головна: https://metalicos.github.io/obminiaiko-site/
- Підтримка: https://metalicos.github.io/obminiaiko-site/support/
- Політика конфіденційності: https://metalicos.github.io/obminiaiko-site/privacy/

Статичний HTML/CSS без збирача, cookies, аналітики й сторонніх шрифтів (Unbounded і Manrope — локально, ліцензія SIL OFL, див. `assets/fonts/OFL-*.txt`). Публікується GitHub Pages з гілки `main`.

## Як оновити сайт

Сторінки генеруються скриптом (текст — у `tools/sitegen/content.py`, шапка й підвал — у `tools/sitegen/header.py`):

```sh
python3 tools/sitegen/content.py .
```

Перевірка верстки на ширині телефона (WebKit, повна висота сторінки):

```sh
swiftc -O tools/websnap/main.swift -o /tmp/websnap
/tmp/websnap "file://$PWD/index.html" /tmp/home.png 393        # 320, 375, 393…
```

Після зміни `assets/style.css` збільште `?v=` у `header.py`, щоб браузери не брали стару версію з кешу.
