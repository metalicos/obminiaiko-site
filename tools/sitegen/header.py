import sys, os
S=sys.argv[1]
BASE='https://metalicos.github.io/obminiaiko-site/'
CURRENT=' aria-current="page"'
def page(path, title, desc, body, current, prefix):
    nav=[('', 'Головна', 'home'), ('support/', 'Підтримка', 'support'),
         ('privacy/', '<span class="long">Конфіденційність</span><span class="short">Приватність</span>', 'privacy')]
    links=''.join('<a href="%s"%s>%s</a>' % ((prefix + h) or './', CURRENT if k == current else '', t) for h, t, k in nav)
    html=f'''<!doctype html>
<html lang="uk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#F4F6F3" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#08130F" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{BASE}{path}">
<meta property="og:type" content="website">
<meta property="og:locale" content="uk_UA">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:image" content="{BASE}assets/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{prefix}assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{prefix}assets/img/apple-touch-icon.png">
<link rel="stylesheet" href="{prefix}assets/style.css?v=4">
</head>
<body>
<a class="skip" href="#main">Перейти до змісту</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{prefix or './'}" aria-label="Обміняйко — головна"><img src="{prefix}assets/img/icon-512.png" alt="" width="36" height="36"><span class="brand-name">Обміняйко</span></a>
    <nav class="nav" aria-label="Розділи">{links}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <span>© 2026 Обміняйко. Розрахунок орієнтовний — остаточну суму визначає кантор.</span>
    <nav aria-label="Нижнє меню">{links}</nav>
  </div>
</footer>
</body>
</html>
'''
    target = os.path.join(S, path) if path.endswith('.html') else os.path.join(S, path, 'index.html')
    os.makedirs(os.path.dirname(target), exist_ok=True)
    open(target, 'w').write(html)
