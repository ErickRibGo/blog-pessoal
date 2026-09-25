"""Gera páginas estáticas da curadoria; execute da raiz com Python 3."""
from pathlib import Path
from html import escape as e

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://github.com/ErickRibGo/'
projects = [
dict(id='pvt', name='PVT Project Dashboard', repo='pvt-project-dashboard', category='Full Stack / Product', status='MVP', complexity='Média', featured=True,
 stack='React · TypeScript · Node.js · Express · Prisma · PostgreSQL · Vitest',
 problem='Consolidar horas, avanço físico e faturamento para identificar projetos que precisam de atenção.',
 description='Dashboard full stack que transforma dados de projetos em indicadores de consumo de horas, avanço e saúde, com regras de negócio centralizadas em uma API TypeScript.',
 skills='Frontend tipado, consumo de API REST, modelagem relacional, separação de camadas e tradução de regras operacionais em indicadores.',
 architecture='React → API Express → controller com Zod → service → repository Prisma → PostgreSQL.',
 evidence='O frontend usa useState, useEffect e useMemo, filtros, resumo, tabela e barras de progresso. A API calcula indicadores; o repository agrega apontamentos, marcos e faturamentos. Há testes Vitest das regras de saúde.',
 limits='A integração TOTVS RM é planejada: os dados vêm de seed, não de sincronização real. Sem autenticação, CRUD completo ou paginação. A interface se concentra em App.tsx; não constitui uma biblioteca extensa de componentes. O banco usa Decimal, mas o repository converte valores para number.',
 missing='Demo pública, validação visual em dispositivos e teclado, resultados de uso e execução registrada dos testes. Documentar autoria e contexto do case sem sugerir vínculo comercial não comprovado.',
 screenshots='Painel completo com dados de demonstração; filtro de críticos; estado de erro e nova tentativa; visualização mobile da tabela.',
 cta='Explorar o case full stack', sources=['frontend/src/App.tsx','backend/src/services/projects.service.ts','backend/src/repositories/prisma-projects.repository.ts','backend/src/controllers/projects.controller.ts','backend/src/services/projects.service.spec.ts','backend/package.json']),
dict(id='jungle', name='Case Jungle', repo='case_jungle', category='Backend / Architecture', status='Case técnico', complexity='Alta', featured=True,
 stack='TypeScript · NestJS · Bun · PostgreSQL · TypeORM · SQS · Docker',
 problem='Processar operações de apostas sem duplicar efeitos financeiros e manter consistência entre saldo, transações e ledger.',
 description='Serviço transacional com API e consumo de mensagens, idempotência persistente, valores decimais exatos e padrões inbox/outbox para coordenar operações financeiras.',
 skills='Modelagem de domínio, concorrência, transações SQL, integração assíncrona, observabilidade e desenho de testes de consistência.',
 architecture='HTTP / SQS → serviço de aplicação → domínio Money / Wallet / WagerTransaction → transação PostgreSQL (saldo + ledger + inbox + outbox) → worker SQS. Docker Compose inclui LocalStack e Nginx.',
 evidence='WagerService usa advisory lock e SELECT FOR UPDATE. O schema contém constraints, ledger imutável por trigger e reconciliação diferida. Workers implementam publicação da outbox e consumo de SQS. Testes incluem 50 entregas repetidas e duas apostas concorrentes. Money encapsula decimal.js.',
 limits='Execução configurada em Bun, inclusive Bun.sleep e bun:test; não anunciar como runtime Node.js validado. NoopAuthGuard sempre permite acesso. SQS local não comprova implantação AWS. Existência dos testes não significa que foram executados nesta auditoria. Código muito comprimido e uso de any reduzem legibilidade e tipagem nas fronteiras.',
 missing='Execução reproduzível dos testes com PostgreSQL/LocalStack, evidência de falhas e recuperação, revisão do consumidor SQS e autenticação antes de uso real. Não há evidência de escala ou produção.',
 screenshots='Diagrama de transação; sequência de replay idempotente com o mesmo saldo; ledger conciliado; resultado real dos testes de concorrência, depois de executados.',
 cta='Ver arquitetura e decisões', sources=['ARCHITECTURE.md','src/application/wager.service.ts','src/workers/sqs.worker.ts','src/workers/outbox.worker.ts','src/domain/money.ts','src/database/migrations/001_initial.sql','src/http/noop-auth.guard.ts','test/integration/concurrency.test.ts','Dockerfile']),
dict(id='retail', name='Retail Fraud Detection', repo='retail-fraud-detection', category='Data / Business Intelligence', status='Análise exploratória', complexity='Média', featured=True,
 stack='Python · pandas · NumPy · matplotlib · seaborn',
 problem='Investigar padrões associados a fraude em transações de varejo e apoiar hipóteses de triagem operacional.',
 description='Análise exploratória de 100.000 transações de varejo, com verificação de dados, visualizações e investigação de hipóteses sobre transações internacionais, dispositivos e valores anômalos.',
 skills='Qualidade de dados, estatística descritiva, visualização, formulação de hipóteses e comunicação de implicações para o negócio.',
 architecture='CSV → pandas / NumPy → estatísticas e agrupamentos → matplotlib / seaborn → interpretação no README.',
 evidence='Recontagem independente do CSV: 100.000 registros, 21 colunas e nenhuma célula vazia. Internacionais: 34.219 fraudes em 49.801 operações (68,71%); domésticas: 13.289 em 50.199 (26,47%). Mobile: 51,93%; Tablet: 45,65%; Desktop: 44,92%. O script verifica nulos, descreve distribuições e produz boxplots, contagens e correlações.',
 limits='Não há treinamento de modelo de machine learning no script analisado. Associações exploratórias não demonstram causalidade, poder preditivo fora da amostra ou redução de fraude. As conclusões do README são mais fortes que a evidência: correlação quase nula não elimina outras relações. O script usa caminho absoluto da máquina do autor.',
 missing='Origem e natureza do dataset, licença, dicionário de variáveis, caminho relativo reproduzível, análise de incerteza e validação das recomendações. Remover marcadores de citação quebrados do README.',
 screenshots='Taxa de fraude por origem com denominadores; comparação por dispositivo; boxplot dos valores; matriz de correlação com legenda legível.',
 cta='Ver análise e evidências', sources=['Notebook/analise_fraude.py','README.md','analise_fraude.ipynb']),
dict(id='chat', name='Chat Furioso', repo='ChatBot-Furia', category='AI Application / Interactive Web', status='Protótipo integrado', complexity='Média', featured=True,
 stack='React · JavaScript · Vite · CSS · Webhook n8n',
 problem='Oferecer uma experiência de conversa temática para fãs de esports.',
 description='Interface conversacional em React conectada a um webhook n8n, com histórico de mensagens, feedback de carregamento, rolagem automática e identidade visual animada.',
 skills='Estado em React, interação assíncrona, integração HTTP, feedback de interface e experiência conversacional.',
 architecture='React App → askGPT → POST ao webhook n8n → campo output da resposta. O README declara OpenAI dentro do fluxo externo; esse workflow não está no repositório.',
 evidence='useState controla mensagens, input, loading, splash e popup; useRef/useEffect fazem auto-scroll. O CSS tem animações e media query. O cliente envia chatInput ao n8n. Placar, torcida e barra de 80% são constantes no JSX.',
 limits='OpenAI está documentado, mas o código versionado não comprova o modelo ou a execução do workflow. Status de partida é simulado, não uma API ao vivo. App.jsx concentra a interface. askGPT não verifica response.ok e converte falhas em texto; o histórico local não é enviado na requisição. Express instalado não comprova backend próprio.',
 missing='Export sanitizado do workflow n8n, modelo/provedor confirmado, teste ponta a ponta, demo, acessibilidade do chat e modal, componentes menores e tratamento explícito de erros HTTP.',
 screenshots='Conversa com resposta real identificada; estado de loading; erro de serviço; layout mobile; popup rotulado como simulação.',
 cta='Explorar a experiência', sources=['src/App.jsx','src/openai.js','src/App.css','README.md']),
dict(id='fan', name='Know Your Fan', repo='know-your-fan', category='APIs / Systems Integration', status='Protótipo com pendências', complexity='Média', featured=True,
 stack='React · JavaScript · Vite · Express · IdAnalyzer · Webhook n8n',
 problem='Estruturar o cadastro de fãs e condicionar o envio dos dados a uma etapa de verificação documental.',
 description='Protótipo de integração de sistemas que conecta um formulário React a uma etapa de verificação documental e ao envio de dados para um webhook n8n.',
 skills='Formulários, estado, upload em base64, consumo de serviços externos e encadeamento de etapas assíncronas.',
 architecture='Fluxo no cliente: React → POST /api/idanalyzer → retorno ao React → checagem de success e nome → POST do React ao n8n. Existe um servidor Express separado que chama o módulo IdAnalyzer. Não é uma cadeia serverless funcional comprovada.',
 evidence='FanForm.js implementa upload, chamada da API, comparação do primeiro nome e envio posterior ao webhook. server.js define a rota Express. api/idanalyzer.js exporta verifyDocument(imageBase64), não um handler HTTP de Vercel.',
 limits='O backend usa require/module.exports em pacote type:module e referencia axios/body-parser ausentes das dependências diretas. Há uma credencial hardcoded: revogar/rotacionar e migrar para variável de ambiente. Não reproduzir seu valor. A validação e o disparo do webhook ficam no cliente, portanto não formam uma barreira confiável de identidade. CPF é validado por formato, não pelos dígitos verificadores. README declara Vercel, mas deploy funcional não foi comprovado.',
 missing='Corrigir contrato do handler e módulos/dependências, mover a decisão de validação para o servidor, workflow n8n sanitizado, demo validada e evidência de tratamento seguro dos documentos. Até isso ocorrer, apresentar como estudo de integração, não como validação de identidade pronta para produção.',
 screenshots='Formulário sem dados pessoais reais; seleção de arquivo fictício; erro de validação; confirmação após fluxo corrigido; diagrama distinguindo cliente, API e serviço externo.',
 cta='Entender a integração', sources=['src/components/FanForm.js','api/idanalyzer.js','server.js','package.json','README.md']),
dict(id='edp', name='Projeto EDP', repo='projeto_EDP', branch='master', category='Business Automation / Python', status='MVP em revisão', complexity='Média', featured=False,
 stack='Python · pandas · openpyxl · Streamlit · FastAPI',
 problem='Estruturar pedidos de insumos de agências, validar códigos e manter histórico com protocolo.',
 description='MVP de automação de suprimentos com validação de agências, registro de pedidos em Excel, protocolo e interface de acompanhamento em Streamlit.',
 skills='Modelagem de processo operacional, validação, persistência em arquivos e separação entre regras, entrada/saída e interfaces.',
 architecture='CLI / interface Streamlit → regras de validação e protocolo → pandas/openpyxl → Excel. A camada FastAPI está presente, mas bloqueada por conflitos de merge.',
 evidence='cli_simulator.py estrutura o atendimento; excel_store.py carrega DE-PARA e regrava pedidos; há core, dashboard, web e services separados.',
 limits='app/api/server.py contém marcadores de merge e não é Python válido. CLI simula atendimento, não integração WhatsApp. Excel é regravado a cada pedido e não comprova segurança para escrita concorrente. Não afirmar implantação na EDP ou ganho operacional medido.',
 missing='Resolver merge, verificar fluxo completo e e-mail, concorrência da persistência, contexto de autoria/uso e métricas reais. Candidato a sexto destaque após reparo e demonstração.',
 screenshots='Pedido com agência fictícia, protocolo gerado, dashboard filtrado e fluxo antes/depois sem quantificar ganhos não medidos.',
 cta='Ver o MVP de automação', sources=['app/cli_simulator.py','app/io/excel_store.py','app/api/server.py','app/dashboard/app_streamlit.py','README.md']),
dict(id='chronos', name='Chronos Pomodoro', repo='chronos-pomodoro', category='Frontend / Learning', status='Em desenvolvimento', complexity='Baixa no estado atual', featured=False,
 stack='React · TypeScript · Vite · CSS Modules · Lucide',
 problem='Interface inicial para organizar sessões de foco; o comportamento do temporizador ainda não está implementado.',
 description='Estudo de frontend em React e TypeScript, com componentes de layout, entrada tipada e estilos modulares para uma interface Pomodoro em desenvolvimento.',
 skills='Componentização inicial, composição de layout e tipagem de props com React.ComponentProps.',
 architecture='App → Container / Logo / Menu / CountDown / DefaultInput; CSS Modules e variáveis de tema.',
 evidence='CountDown retorna 00:00 fixo. DefaultInput combina id com React.ComponentProps, mas só encaminha id/type. Menu usa links # e ícones sem nome acessível. App ainda contém lorem5. O tamanho do contador usa clamp.',
 limits='Não há estado funcional do timer, histórico ou configuração implementada. Label associado ao input é um ponto positivo, mas navegação por ícones precisa de nomes acessíveis. CSS fluido é evidência parcial, não verificação de responsividade ou UX concluída.',
 missing='Timer com pausa/retomada, estado e persistência, navegação real, props encaminhadas corretamente, acessibilidade por teclado, telas mobile e README próprio. Não usar como principal prova de frontend: PVT é mais forte.',
 screenshots='Interface atual identificada como estudo; após implementação, estados de foco, pausa e histórico, incluindo mobile.',
 cta='Acompanhar o código', sources=['src/App.tsx','src/components/CountDown/index.tsx','src/components/Menu/index.tsx','src/components/DefaultInput/index.tsx','src/components/CountDown/styles.module.css']),
]

def repo(p): return BASE+p['repo']
def sources(p):
    return ''.join(f'<li><a href="{repo(p)}/blob/{p.get("branch","main")}/{s}">{e(s)}</a></li>' for s in p['sources'])

from presentation import render
render(projects)

report='''# Curadoria técnica dos projetos

Data: 25/09/2026. Base: código público de ErickRibGo, READMEs e dataset baixados nesta sessão. A auditoria anterior não foi fornecida. Revisão estática; não certifica execução, produção, autoria individual ou resultados comerciais. Complexidade é julgamento relativo do escopo implementado, não classificação de senioridade.

## Seleção e posicionamento

Seis Featured Projects: PVT, Case Jungle, Retail Fraud Detection, Chat Furioso, Know Your Fan e MMORPG em Python. O MMORPG foi incluído por solicitação do autor, que confirmou o backend integralmente em Python; seu código ainda não foi inspecionado. Os dois últimos entram como protótipos com limitações explícitas; Know Your Fan não deve ter CTA de demo antes das correções. EDP é candidato a sexto após resolver o merge e demonstrar o fluxo. Não preencher sete posições com projetos sem evidência.

Posicionamento: Software Engineer / Automation Engineer — Technology, Data & AI, com capacidade Full Stack. A trajetória editorial conecta JavaScript → TypeScript → React → APIs → Backend → Automation → Data → AI; não representa cronologia profissional comprovada.

PVT é a principal prova de React/TypeScript e Node.js, inclusive para empresas com essa stack. Jungle aprofunda backend/arquitetura, mas executa em Bun. Retail comprova análise de dados, não ML. Chat comprova integração n8n, enquanto OpenAI é declaração do README sem workflow versionado. Não há evidência suficiente para anunciar sistemas de IA em produção.

## Matriz de competência

| Projeto | Competência principal | Complexidade aparente | Decisão |
|---|---|---|---|
'''
for p in projects:
    report+=f'| {p["name"]} | {p["category"]} | {p["complexity"]} | {"Featured — " if p["featured"] else "More Projects — "}{p["status"]} |\n'
report+='''| SAP Data Automation | Business / Data Automation, ainda não verificável | Indeterminada | Aguardar código |
| Kinetra IA | Uso de IA não verificável | Indeterminada | Aguardar implementação |
| MMORPG em Python | Backend Python, informado pelo autor | Indeterminada | Featured com escopo atribuído ao autor; aguarda código |
| Captação de leads | Automação comercial não verificável | Indeterminada | Commercial Projects, após evidência |
| Lojas e landing pages | Entrega comercial não verificável | Indeterminada | Commercial Projects, após evidência |

## Cases analisados
'''
for p in projects:
    report+=f'\n### {p["name"]}\n\n'
    for label,key in [('Problema','problem'),('Competências','skills'),('Tecnologias','stack'),('Complexidade aparente','complexity'),('Descrição profissional sugerida','description'),('Arquitetura','architecture'),('Evidências','evidence'),('Limitações','limits'),('Informações faltantes','missing'),('Screenshots recomendados','screenshots'),('CTA','cta')]:
        report+=f'**{label}:** {p[key]}\n\n'
    report+=f'**GitHub:** [{p["repo"]}]({repo(p)}). **Live Demo:** não identificada; omitir botão.\n\n**Fontes:** '+', '.join(f'[{s}]({repo(p)}/blob/{p.get("branch","main")}/{s})' for s in p['sources'])+'.\n'
report+='''
## Projetos sem evidência suficiente

### SAP Data Automation
O repositório público [Automa-o-SAP---Extrair-dados-de-consumo](https://github.com/ErickRibGo/Automa-o-SAP---Extrair-dados-de-consumo) existe, mas a API GitHub retornou “This repository is empty”. Não é possível determinar extração, processamento, bibliotecas, integração SAP ou problema operacional preciso. Nome do repositório não comprova SAP GUI Scripting, API, RPA ou Python. Solicitar script sanitizado, entrada/saída, etapa manual substituída e evidência de execução. Screenshots futuros: fluxo de extração e saída anonimizada. CTA futuro: “Ver automação de dados”; descrição só após verificação. Live Demo não identificada.

### Kinetra IA
[kinetra-ia](https://github.com/ErickRibGo/kinetra-ia) contém apenas README.md com o título. Objetivo, arquitetura, tecnologias, modelo de IA e maturidade funcional não são verificáveis. Maturidade do artefato público: repositório inicial. Não confundir isso com conclusão sobre uma versão privada. Solicitar código, jornada, provedor/modelo, limites e demo. Screenshot útil: entrada → saída real com contexto. CTA futuro: “Explorar produto”, apenas quando houver produto verificável. Não publicar descrição especulativa.

### MMO Python
Não localizado entre os 13 repositórios públicos retornados pela conta. O autor confirmou posteriormente que desenvolveu todo o backend em Python. A classificação MMORPG e essa contribuição vêm do relato do autor, não de inspeção. O case foi adicionado à home sem atribuir frameworks, sistemas de jogo ou capacidade de rede não confirmados. Solicitar código do loop principal, entidades, estado/persistência e camada de rede, se houver. Avaliar separação entre simulação, renderização e comunicação. Não afirmar multiplayer, concorrência ou servidor sem evidência. Screenshot útil: estado do mundo e diagrama dos sistemas; vídeo pode explicar melhor transições. GitHub e Live Demo não identificados; CTA atual “Conversar sobre o projeto”; não há botão GitHub ou demo sem endereço informado.

### Automação de captação de leads
Não foi identificado repositório público correspondente. A existência de pastas de prospecção de Lucio na máquina não comprova relação com projetos de Erick; não as utilizei como fonte. Solicitar autoria, origem dos dados, etapas, deduplicação, integração CRM e exemplo anonimizado. Competência potencial: automação comercial; tecnologias, arquitetura, complexidade e resultados ficam pendentes. Screenshot: fluxo sanitizado e entrada/saída de exemplo. CTA futuro “Ver fluxo de automação”; GitHub e demo não identificados.

### Lojas e landing pages para clientes
O pedido informa essa experiência, mas não fornece nomes, URLs, escopo ou autoria. Categoria separada Commercial Projects criada sem inventar clientes. Antes de publicar cada case: identificar problema comercial, contribuição pessoal, stack real, entrega e URL autorizada; métricas somente com fonte. Screenshots: desktop/mobile e jornada principal, sem dados de clientes. CTA “Visitar site” se ativo, ou “Ver case” se houver material. GitHub pode ser privado: não inventar link. Complexidade e descrição dependem de cada entrega.

## Avaliação de frontend e leitura pelo recrutador

PVT é a evidência principal: tipagem do contrato, estado assíncrono, filtros, cálculos de resumo, erro/retry, tabela e barras. CSS possui breakpoints de 900 e 600 px; comportamento visual não foi certificado nesta revisão. Extrair componentes reutilizáveis, anunciar seleção dos filtros e revisar semântica das barras fortaleceriam a apresentação.

Chronos comprova composição inicial e props tipadas, mas contador fixo e navegação vazia impedem apresentá-lo como produto concluído. Labels existentes não compensam links de ícones sem nome acessível. Não há gerenciamento de estado funcional do timer a avaliar.

Chat tem estado e animação, porém pouca decomposição em componentes e dados de partida estáticos. Know Your Fan comprova intenção e encadeamento da integração, não um backend serverless pronto. Sua arquitetura observada retorna ao cliente antes do webhook; não apresentar IdAnalyzer → n8n como conexão direta de servidor.

## Organização aplicada ao site

Hero com posicionamento de engenharia → seis Featured Projects com filtros e evidências visuais → abordagem de trabalho → More Projects (EDP e Chronos, compactos) → contato e GitHub. Blog preservado em blog.html; artigos mantidos. Cada destaque abre um case com problema, stack, arquitetura, evidência e limites. Captura real do PVT proveniente do README; demais visuais identificados como diagramas ou gráfico de dados. Sem métricas inventadas ou botões de demo sem destino verificado.

A categoria comercial está planejada no backlog, mas foi retirada da página pública até haver cases documentados. SAP, Kinetra e leads não ocupam cards públicos sem evidência. O MMORPG aparece por solicitação expressa do autor, com a origem das informações indicada. O material detalhado desta auditoria serve como backlog editorial; as páginas públicas resumem o que o código sustenta.

## Prioridades para fortalecer a candidatura

1. PVT: demo com seed, teste do fluxo e revisão de acessibilidade; principal cartão de visita React/TypeScript/Node.
2. Jungle: executar testes unitários e de integração, registrar decisões e limites de produção; demonstrar idempotência e concorrência sem prometer escala medida.
3. Know Your Fan: rotacionar credencial exposta, corrigir contrato HTTP e backend e verificar integração antes de disponibilizar demo.
4. Chat: versionar workflow sanitizado e comprovar provedor/modelo; rotular status fictício.
5. EDP: resolver conflitos de merge e demonstrar o fluxo; pode completar o sexto destaque de automação Python.
6. Retail: tornar execução portátil, documentar dataset e moderar inferências exploratórias.
7. Completar evidências comerciais e dos repositórios vazios antes de promovê-los.

## Verificação da entrega

Página local inspecionada no navegador em desktop (1440 px) e mobile (390 px), com cinco cards Featured. Conferidos o CTA para o case PVT, o acesso ao blog e a apresentação dos artigos. Verificação estática de links locais, imagens, âncoras e IDs passou; git diff --check sem erros. A base Retail foi recontada com csv da biblioteca padrão do Python. O parser ast confirmou SyntaxError na linha 1 da API EDP. Os testes e serviços externos dos repositórios auditados não foram executados. O site não foi publicado.
'''
(ROOT/'AUDITORIA-PROJETOS.md').write_text(report,encoding='utf-8')
print('Gerados index.html, cases.html e AUDITORIA-PROJETOS.md')

