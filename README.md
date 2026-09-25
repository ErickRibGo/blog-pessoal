# Portfólio — Erick Ribeiro

Portfólio estático com curadoria de projetos de engenharia de software, integrações e análise de dados. HTML, CSS e JavaScript, sem dependências de runtime no servidor.

## Executar localmente

Na raiz do projeto:

```powershell
python -m http.server 8765 --bind 127.0.0.1
```

Abra http://localhost:8765. As páginas também funcionam sem JavaScript; filtros e cópia do e-mail são melhorias progressivas.

## Editar o conteúdo

- `scripts/build_portfolio.py`: dados dos projetos e geração da auditoria.
- `scripts/presentation.py`: apresentação pública, diagramas e resumos de escopo.
- `css/portfolio.css`: apresentação responsiva.
- `js/portfolio.js`: filtros por competência e cópia do e-mail.
- `content/posts/`: conteúdo dos artigos em HTML, preservado e editável.
- `scripts/build_blog.py`: gera a listagem do blog e os dois artigos.
- `css/blog.css` e `js/blog.js`: leitura, busca, filtros e compartilhamento.

Após editar os dados ou a apresentação:

```powershell
python scripts/build_portfolio.py
```

Isso atualiza `index.html`, `cases.html` e `AUDITORIA-PROJETOS.md`. Não editar diretamente os dois HTMLs gerados.

Para atualizar o blog depois de editar artigos ou metadados:

```powershell
python scripts/build_blog.py
```

O gerador mantém os endereços dos artigos. O antigo `lobbystartup.html` encaminha para o filtro Startups. O tempo de leitura é estimado a 200 palavras por minuto; datas só aparecem quando existiam no conteúdo original. Busca ignora acentos e combina com o assunto selecionado. Sem JavaScript, os dois artigos continuam acessíveis.

## Proveniência dos visuais

A captura `images/pvt-dashboard.png` foi obtida do [README público do PVT](https://github.com/ErickRibGo/pvt-project-dashboard), a partir da [imagem publicada pelo autor](https://github.com/user-attachments/assets/e8a0285c-c54c-47ce-ae58-e1d827aae3e2). Ela representa dados de demonstração, não implantação em cliente.

O gráfico Retail usa taxas recalculadas do CSV do repositório. Os demais visuais são diagramas textuais identificados, baseados no código consultado; não são screenshots de aplicações em execução. A foto já fazia parte do site original.

## Verificação

Em 25/09/2026: navegação para cases, filtros Data e IA & Integrações, retorno a Todos, imagens carregadas e apresentação desktop/mobile conferidos no navegador. Home e cases não apresentaram overflow horizontal a 320 px. JavaScript passou em `node --check` e alterações passaram em `git diff --check`.

A auditoria distingue código observado de funcionalidades declaradas. Não foram executados testes ou serviços dos repositórios auditados. Cases comerciais aguardam material verificável antes de aparecerem no site.

## Publicação

Esta entrega não foi publicada. Publicar somente páginas, CSS, JavaScript, fontes e imagens necessários ao site. `.audit-sources` contém material de pesquisa local e é ignorado pelo Git; não enviar essa pasta ao hosting. O relatório de auditoria e os scripts de geração não são necessários para servir o portfólio.
