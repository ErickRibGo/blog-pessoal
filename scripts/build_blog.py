"""Gera o blog a partir dos artigos preservados em content/posts."""
from pathlib import Path
from html import escape, unescape
import re
import math

ROOT = Path(__file__).resolve().parents[1]
posts = [
    dict(slug='startups', category='Startups', title='Minha estratégia para lançar 12 startups em 12 meses',
         excerpt='Um experimento sobre velocidade, escopo e aprendizado na construção de produtos digitais.', image='startup.jpg',
         alt='Imagem de capa do artigo sobre startups', date='2025-10-20', date_label='20 out. 2025'),
    dict(slug='xadrez', category='Filosofia', title='Xadrez e Filosofia',
         excerpt='O que o tabuleiro ensina sobre estratégia, ego e paciência — nos negócios e fora deles.', image='xadrez.jpg',
         alt='Imagem de capa do artigo sobre xadrez', date=None, date_label=None),
]
for p in posts:
    p['body'] = (ROOT/'content/posts'/f'{p["slug"]}.html').read_text(encoding='utf-8')
    text = unescape(re.sub('<[^>]+>', ' ', p['body']))
    p['minutes'] = max(1, math.ceil(len(text.split()) / 200))
    p['url'] = f'post-{p["slug"]}.html'

def header(title, description):
    return f'''<!doctype html><html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} — Erick Ribeiro</title><meta name="description" content="{escape(description)}">
<meta name="theme-color" content="#f5f3ed"><meta property="og:title" content="{escape(title)} — Erick Ribeiro"><meta property="og:description" content="{escape(description)}">
<link rel="icon" href="images/perfil-icon.png"><link rel="stylesheet" href="css/portfolio.css"><link rel="stylesheet" href="css/blog.css"><script src="js/blog.js" defer></script>
</head><body class="editorial"><a class="skip" href="#main">Pular para o conteúdo</a>
<header class="top"><a class="brand" href="index.html" aria-label="Erick Ribeiro, início">erick<span>ribeiro.</span></a><nav aria-label="Navegação principal"><a href="index.html#projects">Projetos</a><a href="index.html#about">Sobre</a><a href="blog.html" aria-current="page">Blog</a><a class="nav-contact" href="mailto:erickribeirogon@gmail.com">Vamos conversar ↗</a></nav></header>'''

footer='''<footer><span>© 2026 Erick Ribeiro · Ideias em construção.</span><a href="index.html">Portfólio ↗</a><a href="https://www.linkedin.com/in/erick-ribeiro-515992228/">LinkedIn ↗</a><a href="#main">Voltar ao início ↑</a></footer></body></html>'''

def meta(p):
    date = f'<time datetime="{p["date"]}">{p["date_label"]}</time><span aria-hidden="true">·</span>' if p['date'] else ''
    return f'<div class="reading-meta">{date}<span>{p["minutes"]} min de leitura estimada</span></div>'

cards=[]
for i,p in enumerate(posts):
    cards.append(f'''<article class="journal-card" data-category="{p['category'].lower()}" data-search="{escape(p['title']+' '+p['excerpt']+' '+p['category'])}"><a class="journal-cover" href="{p['url']}" tabindex="-1" aria-hidden="true"><img src="images/{p['image']}" alt="" width="900" height="600"><span class="cover-index">0{i+1} / {p['category'].upper()}</span></a><div class="journal-card-body"><p class="eyebrow">{p['category']}</p><h2><a href="{p['url']}">{p['title']}</a></h2><p class="journal-excerpt">{p['excerpt']}</p><div class="journal-bottom">{meta(p)}<a class="read-link" href="{p['url']}" aria-label="Ler {p['title']}">Ler artigo ↗</a></div></div></article>''')

blog=header('Blog', 'Reflexões de Erick Ribeiro sobre construção de produtos, startups, estratégia e filosofia.')+'''
<main id="main"><section class="journal-hero"><div><p class="eyebrow">O caderno de Erick Ribeiro</p><h1>Entre o código<br>e as <em>ideias.</em></h1></div><div class="journal-intro"><span class="journal-symbol" aria-hidden="true">✳</span><p>Reflexões sobre construir produtos, tomar decisões e aprender pelo caminho.</p><span>STARTUPS / ESTRATÉGIA / FILOSOFIA</span></div></section>
<section class="journal-library" aria-labelledby="articles-heading"><div class="library-top"><h2 id="articles-heading">Artigos<span class="article-count">02</span></h2><div class="journal-search" hidden><label for="article-search">Buscar no blog</label><input id="article-search" type="search" placeholder="Título ou assunto…" autocomplete="off"></div></div><div class="journal-toolbar" hidden><div class="journal-filters" role="group" aria-label="Filtrar artigos por assunto"><button type="button" data-topic="todos" aria-pressed="true">Todos</button><button type="button" data-topic="startups" aria-pressed="false">Startups</button><button type="button" data-topic="filosofia" aria-pressed="false">Filosofia</button></div><p class="results-count" role="status" aria-live="polite">2 artigos</p></div><div class="journal-grid">'''+''.join(cards)+'''</div><div class="journal-empty" hidden><span aria-hidden="true">↳</span><h3>Nenhum artigo por aqui.</h3><p>Tente outro termo ou explore todos os assuntos.</p><button type="button" id="clear-search">Limpar busca e filtros</button></div></section>
<aside class="journal-end"><div><p class="eyebrow">Das ideias à implementação</p><h2>Veja o que estou construindo.</h2><p>Projetos de software, integrações e dados — com as decisões por trás de cada solução.</p></div><a class="button" href="index.html#projects">Explorar projetos ↗</a></aside></main>'''+footer
(ROOT/'blog.html').write_text(blog,encoding='utf-8')

for p in posts:
    headings=[]
    def section_heading(match):
        tag, text = match.groups()
        anchor=f'section-{len(headings)+1}'
        label=unescape(re.sub('<[^>]+>','',text))
        headings.append((anchor,label,tag))
        return f'<{tag} id="{anchor}">{text}</{tag}>'
    body=re.sub(r'<(h[23])>(.*?)</\1>',section_heading,p['body'],flags=re.S)
    toc=''.join(f'<li class="toc-{tag}"><a href="#{anchor}">{escape(label)}</a></li>' for anchor,label,tag in headings)
    other=next(x for x in posts if x!=p)
    article=header(p['title'],p['excerpt'])+f'''<div class="reading-progress" aria-hidden="true"><span></span></div><main id="main" class="article-main"><nav class="breadcrumb" aria-label="Caminho da página"><a href="blog.html">← Todos os artigos</a><span>/</span><a href="blog.html?categoria={p['category'].lower()}">{p['category']}</a></nav><article><header class="article-header"><p class="eyebrow">{p['category']}</p><h1>{p['title']}</h1><p class="article-deck">{p['excerpt']}</p><div class="article-byline"><img src="images/perfil_completo.jpg" alt="" width="42" height="42"><div><span>Erick Ribeiro</span>{meta(p)}</div></div></header><figure class="article-cover"><img src="images/{p['image']}" alt="{p['alt']}" width="1200" height="700"></figure><div class="article-layout"><aside class="article-toc"><nav aria-label="Neste artigo"><p class="eyebrow">Neste artigo</p><ol>{toc}</ol></nav><button type="button" class="copy-article" hidden>Copiar link ↗</button><span class="share-status" role="status"></span></aside><div class="article-prose" id="article-content">{body}<div class="author-note"><img src="images/perfil_completo.jpg" alt="" width="56" height="56"><div><strong>Erick Ribeiro</strong><p>Engenharia de software, produtos e ideias em construção.</p><a href="index.html#about">Conheça meu trabalho ↗</a></div></div></div></div></article><aside class="next-article"><p class="eyebrow">Continue a leitura</p><a href="{other['url']}"><span>{other['title']}</span><span aria-hidden="true">↗</span></a><p>{other['excerpt']}</p></aside></main>'''+footer
    (ROOT/p['url']).write_text(article,encoding='utf-8')

# Mantém o endereço antigo utilizável, sem o layout duplicado e quebrado.
(ROOT/'lobbystartup.html').write_text('''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url=blog.html?categoria=startups"><title>Startups — Erick Ribeiro</title></head><body><p><a href="blog.html?categoria=startups">Abrir artigos sobre startups →</a></p></body></html>''',encoding='utf-8')
print('Blog e dois artigos gerados; conteúdo original preservado.')
