# Achados · Pesquisa pública · v3 — leitura direta de página (29 ago 2026)

## COMO A CONFIANÇA É CALCULADA (regra explícita)

| Nível | Critério |
|---|---|
| **100%** | Página aberta e lida diretamente, com data da consulta |
| **95%** | Confirmado no domínio do próprio emissor **+** segunda recuperação independente concordante |
| **90%** | Confirmado no domínio do emissor, recuperação única, sem contradição |
| **70%** | 3+ fontes secundárias independentes concordantes |
| **50%** | 2 fontes secundárias |
| **30%** | Fonte secundária única |
| **0%** | Sem fonte localizável |

**Histórico de método.** A v2 (30 ago 2026, sessão remota) tinha teto de 95%: a política de egresso impedia abrir qualquer página, e a verificação foi feita forçando a busca a retornar só o domínio do emissor. Esta v3 (29 ago 2026, terminal sem bloqueio) **abriu e leu as páginas** — WebFetch e Chrome real — e carimbou a data ao lado de cada número. Onde a página não abriu, a confiança **não subiu** e o motivo está registrado.

---

## CONFIANÇA POR DIMENSÃO *(não uso número único — ele esconde as diferenças)*

| Dimensão | Confiança | Base |
|---|---|---|
| Preço · categoria internacional | **100%** | apollo.io/pt/pricing e business.linkedin.com lidos em 29/08/2026 |
| Preço · Brasil (RD Station, Agendor, Ploomes) | **100%** | rdstation.com, agendor.com.br e ploomes.com/precos lidos em 29/08/2026 |
| Gong não publica preço | **95%** | gong.io, confirmado (v2); não relido nesta rodada |
| Concorrente direto AmpUp | **100%** | ampup.ai/meeting-prep lida em 29/08/2026 — **citação anterior corrigida** |
| Concorrentes Parsley · EchoIQ (MaxIQ) · SiftHub | **100%** | sites de cada um lidos em 29/08/2026 (v2: 60%) |
| Momentum · Voice of the Market 2026 | **95%** | página do emissor (momentum.io) lida + cópia sindicada independente lida; release canônico no BusinessWire **não abriu** (anti-bot) |
| Estatística dos 82% é inutilizável | **85%** | rastreamento de origem convergente (v2) |
| Preço Kommo em reais | **30%** | R$66 **não aparece em nenhuma página do domínio**; preço é em USD — ver tabela |
| Números de adoção/shelfware | **REMOVIDOS** | origem não rastreável após busca dirigida — ver seção "NÃO USE" |
| **Verbatim PT-BR do ICP** | **0%** | **estruturalmente indisponível — ver abaixo** |

**O núcleo que sustenta o critério "Potencial de negócio" está em 100%** (preço Brasil, preço internacional, concorrente direto). Uma dimensão não chega lá hoje por método nenhum, e eu não vou maquiá-la.

---

## ⚠️ CORREÇÕES DESTA RODADA (v3, 29 ago 2026) — leitura direta derrubou três registros

**1. Citação da AmpUp estava errada.** A v2 citava o título da página como *"AI Meeting Prep for Sales — 2 Min Briefs, Not 20 Min Research"*. **Essa frase não existe na página.** O meta title real é `"AI Meeting Prep for Sales Teams - 2-Min Briefs | AmpUp"`, o H1 é `"AI Meeting Prep for Sales Teams"` e o contraste declarado é com **"45+ Minutes of Research"** (*"Reps spend nearly an hour digging through CRM notes and old emails before important calls"*), não com 20 minutos. Numa banca, citar "2 min vs 20 min" seria citação incorreta de fonte primária. Corrigido na ENTREGA 5. A citação antiga vale **0%**.

**2. Implantação do RD Station: R$1.999 é do plano Advanced.** A v2 registrava "implantação opcional R$1.999" sem qualificar o plano. Na página: Basic/Pro têm implantação opcional de **R$849**; o R$1.999 é do **Advanced** — que não é a faixa do ICP. Corrigido na tabela.

**3. Ploomes: os dois lados da contradição estavam errados.** A v2 registrava "R$240/mês para 3 usuários vs. R$154,90–R$498,20 por usuário" e "o site declara não exibir preço". Lido em `ploomes.com/precos` (29/08/2026): **"R$85,00 /mês por usuário" · "Mínimo de 3 usuários"**. Nenhum dos números anteriores aparece na página; o "sob consulta" vale só para os **módulos** (Workflow, CPQ, Analytics, Assistente de IA), não para o plano base. Resolvido: 55% → 100%.

## ⚠️ CORREÇÕES DA v2 (mantidas)

**1. Preço do Gong.** Eu reportei "US$100–120/usuário/mês + taxa de plataforma US$5.000–15.000/ano" como se fosse dado. Verificado em gong.io: **a Gong não publica preço**; tudo é cotação. Aqueles valores são **estimativa de terceiros**, não tabela. Confiança cai de aparente para **40%**. Não use os números; use o fato de que o preço é fechado — que é o que interessa ao argumento.

**2. Números de adoção (42% sobrecarregados, 23% de ROI no 1º ano, <40% treinam).** Na v2 estavam a 40%, mantidos "para não perder o rastro". Nesta rodada a busca dirigida **não encontrou estudo nomeado para nenhum dos três** — e os releases da Gartner localizados por título trazem 50% e 70%, nunca 42%. **Removidos do documento**, mesmo tratamento dado à estatística dos 82%. Registro na seção "NÃO USE".

---

## VERBATIM: por que 0% e por que isso não sobe hoje

Não é falta de esforço nem restrição desta sessão. São dois bloqueios de natureza diferente:

1. **Reddit bloqueia o crawler da Anthropic no nível do publisher.** A busca retorna erro explícito de domínio inacessível. Nenhuma ferramenta minha alcança thread de r/sales — hoje ou em qualquer sessão.
2. **Em português, a conversa não existe publicamente.** Três buscas com formulações diferentes retornaram **apenas conteúdo de marketing de fornecedor** (Agendor, RD Station, VendaMais, Exact Sales). Zero fala espontânea de vendedor ou gestor brasileiro.

> **O bloqueio 2 é o achado, não o obstáculo.** Se o ICP brasileiro não fala publicamente dessa dor, ele provavelmente **não a nomeia**. Isso o coloca em consciência de *problema* ou abaixo — e significa que uma headline como "prepare melhor suas reuniões" fala uma língua que ele ainda não usa. Ele fala de **conversão, meta e inconsistência do time**. É a informação mais acionável deste documento inteiro, e ela veio justamente da busca vazia.

### O que consegui de fonte de praticante *(o mais próximo de verbatim disponível)*

Reviews de G2 e Capterra são indexáveis. As frases abaixo vêm de páginas de review identificadas, mas **eu não abri as páginas** — então a redação não é certificada. Tag própria: `[E2*]` = praticante identificado, URL conhecida, redação não verificada.

- `[E2*]` Economia relatada de **1–2 horas por dia** antes gastas "garimpando no Salesforce e no Sales Navigator" para achar contas qualificadas — reviews do ZoomInfo no G2
- `[E2*]` "O custo de pesquisa por conta era tão alto que a personalização só acontecia nas contas 'top' — todo o resto recebia mensagem enlatada" — G2
- `[E2*]` Ter a pesquisa organizada em um só lugar "reduziu o tempo de preparação antes das reuniões" — G2

**Uso permitido:** como evidência de que a dor existe na categoria. **Uso proibido:** como fala do seu ICP brasileiro. São perfis diferentes.

---

## ENTREGA 2 · ÂNCORA DE PREÇO *(lida na página, 29 ago 2026)*

### Brasil — o que a PME realmente paga

| Ferramenta | Preço (página, 29/08/2026) | Confiança | Nota |
|---|---|---|---|
| **RD Station CRM** | Free (máx. 4 usuários) · Basic **R$73**/usuário/mês (anual: R$65,70) · Pro **R$131**/usuário/mês (anual: R$117,90) · Advanced sob consulta | **100%** | **Pro e Advanced exigem mínimo de 4 usuários.** Implantação opcional: **R$849** (Basic/Pro) · R$1.999 (Advanced). *v2 registrava só "R$1.999" sem qualificar o plano.* Mínimo do Basic não localizado na página — lacuna |
| **Agendor** | Gratuito (até 3 usuários) · Pro **R$59** · Performance **R$83** · Corporativo **R$156** — por usuário/mês, visão mensal (anual: 10% off) | **100%** | R$83 agora **declarado direto na página**; a prova aritmética da v2 (R$332÷4 = R$415÷5) deixou de ser necessária — os totais não constam mais. Corporativo exige **mínimo de 10 usuários** |
| **Ploomes** | **R$85**/usuário/mês · **mínimo de 3 usuários** · módulos sob consulta | **100%** | *v2 registrava contradição (R$240/3 vs R$154,90–498,20) — nenhum dos dois consta da página. Ver correção 3.* Versão em inglês: "Ploomes Lite" US$22/usuário/mês |
| **Kommo** | Base **US$15** · Advanced **US$25** · Pro **US$45** — por usuário/mês, **assinatura mínima de 6 meses**, cobrança em USD ou BRL sem valor em R$ exibido | **100%** (USD) · **30%** (R$66) | *v2 registrava R$66/usuário/mês (fonte secundária única).* Quatro páginas do domínio lidas, inclusive a pt-BR: **R$66 não aparece em nenhuma.** ⚠️ Reajuste anunciado no blog oficial: a partir de **01/09/2026**, Base → US$25 e Advanced → US$35. **Sai das âncoras em reais** |

### Categoria internacional

| Ferramenta | Preço (página, 29/08/2026) | Confiança |
|---|---|---|
| **LinkedIn Sales Navigator** | Core **US$119,99**/mês/licença (US$1.079,88/ano) · Advanced **US$159,99**/mês/licença (US$1.799,88/ano) · Advanced Plus sob cotação. Página declara "may exclude VAT" e "pricing is subject to change" | **100%** |
| **Apollo.io** | Free US$0 · Basic **US$49** · Professional **US$79** · Organization **US$119** — por assento/mês, **cobrado anualmente** (toggle anual "economize 24%") · Organization exige **mínimo 3 assentos** · "preços excluem impostos" | **100%** (lido no Chrome real; a página `/pricing` não renderiza sem JavaScript) |
| **Gong** | **Sem preço público.** Só cotação. Licenças "Gong Foundation" + add-ons | **95%** (o fato, v2) / 40% (os valores estimados por terceiros) |

### A cunha estratégica que sai daqui

`[E4]` **Faixa de trabalho:** a PME brasileira do ICP paga hoje na ordem de **R$60 a R$130 por vendedor/mês** por ferramenta comercial de base — piso Agendor Pro R$59, núcleo R$73–R$85 (RD Basic, Agendor Performance, Ploomes), teto RD Pro R$131. *(Premissa declarada: RD Station, Agendor e Ploomes são representativos; os três lidos no próprio domínio em 29/08/2026, visão mensal.)*

Contra isso:

- **Sales Navigator custa ~US$120/assento/mês** — na ordem de **4x a 8x** o CRM inteiro que a PME já paga.
- **Mínimos de assento e de prazo são barreira real para time pequeno** — agora com cinco entradas lidas na página: Apollo Organization (**3 assentos**), RD Station Pro e Advanced (**4 usuários**), Ploomes (**3 usuários**), Agendor Corporativo (**10 usuários**), Kommo (**6 meses** de contrato mínimo, em dólar).
- **"Não publica preço" é padrão da categoria, com 3 casos lidos** — Gong, EchoIQ/MaxIQ e SiftHub. O único concorrente de meeting prep que publica preço (Parsley) cobra por conversa, não por assento.

> **A PME do ICP não está sem sales intelligence por descuido. A estrutura de preço da categoria a exclui.**
> Isso converte o anti-ICP "enterprise" do V3 em argumento de cunha: *existe uma faixa de empresa que tem a dor e está fora do alcance de preço de quem a resolve.* Sustentado por preço **lido na página**, não por opinião nem por recuperação de busca.

---

## ENTREGA 5 · EVIDÊNCIA DE CATEGORIA

> **EVIDÊNCIA DE CATEGORIA — não são resultados do Antessala.**

### O concorrente que precisa entrar no seu radar

**AmpUp** `[100%]` — `ampup.ai/meeting-prep`, lida em 29/08/2026. Meta title literal:

> **"AI Meeting Prep for Sales Teams - 2-Min Briefs | AmpUp"**

H1: *"AI Meeting Prep for Sales Teams"*. Subheadline: *"AI meeting prep that puts the high-fidelity context you need to win in front of you before every call, account history, likely objections, and winning plays, generated automatically in about two minutes."* O bloco do problema é **"45+ Minutes of Research"** — *"Reps spend nearly an hour digging through CRM notes and old emails before important calls."* (Um depoimento na mesma página cita "30-40 minutes"; a página não é internamente consistente — **use os minutos como promessa do concorrente, nunca como estatística de mercado.**)

> *Histórico: a v2 citava "AI Meeting Prep for Sales — 2 Min Briefs, Not 20 Min Research". Essa redação **não existe na página** em 29/08/2026. Confiança da citação antiga: 0%.*

Conteúdo do brief, segundo a página: *account history summary · previous objections and how they were handled · stakeholder map · suggested talking points based on deal stage · competitive intelligence · risk factors.* Fontes de dados declaradas: **"calls, CRM, and emails"**; integrações com **Gong, Chorus**, Salesforce, HubSpot, Google Calendar, Outlook.

**Isso é a promessa do Antessala, já no ar, com página de vendas pronta.** O V3 lista "briefing virar commodity" como risco **alto** — está confirmado, com nome, URL e data.

### Os outros três, agora lidos `[100%]` *(29/08/2026)*

| Concorrente | O que a página diz (literal) | Preço público | Mecanismo declarado |
|---|---|---|---|
| **Parsley** (`parsley.id`) | Seção **"Pre-Call Brief"**: *"Talking points and knowledge gaps ready before your call"*. Headline: *"The AI presales agent for LinkedIn and email"* | **Sim** — *"Flat 25¢ a conversation at every pack size"*, sem assinatura | O brief vem da conversa que o **próprio prospect** teve com o chatbot no link do vendedor — exige interação prévia |
| **EchoIQ** — *produto da MaxIQ* (`getmaxiq.com/echoiq`), não empresa | **"AI Meeting Briefs"** — *"Automated briefs surface deal history, key contacts, and account insights in seconds."* · *"Walk into every meeting fully prepped"* | **Não** — *"Usage Based, Not Seat Based"*; `/pricing` é formulário | Brief montado de **histórico de deal e conversas anteriores** |
| **SiftHub** (`sifthub.io`) | *"Pre-call briefs, post-call summaries, and sales-to-CS handovers are generated automatically **from CRM and call data**."* | **Não** — *"Request a quote!"* | Depende de **CRM e dados de call** existentes; perfil enterprise (entrada por "RFP Agent") |

*v2: os três estavam a 60%, citados por fonte secundária única.*

Adjacentes (não lidos nesta rodada): Fireflies, Avoma, Fathom, Otter, tl;dv, Fellow, Granola. **Novo adjacente lido:** o **Apollo** lista *"Insights de IA pré-reunião"* como recurso dos planos Professional (US$79) e Organization (US$119) — `apollo.io/pt/pricing`, 29/08/2026. A funcionalidade em si não foi lida; entra como adjacente até leitura.

### A fronteira que continua defensável — reforçada por leitura literal

`[E3]` **Os quatro concorrentes de meeting prep lidos declaram, cada um na própria página, que o brief é montado sobre artefato prévio**: gravação de call (AmpUp via Gong/Chorus), histórico de deal (EchoIQ), CRM + call data (SiftHub), chat prévio do prospect (Parsley). Gong, Otter e Fireflies idem. O Antessala, como o V3 desenha, precisa funcionar **na primeira conversa** — onde não há gravação, histórico de conta nem interação prévia. Some-se a isso a cunha de preço acima e o contexto fragmentado brasileiro (WhatsApp, e-mail, CRM parcial), e a diferenciação para de ser "fazemos briefing".

### Momentum · Voice of the Market 2026 `[95%]`

Release de 27 jan 2026, base de **>2.000 oportunidades B2B ativas em 150 setores**:

- **88%** dos times dizem usar IA · apenas **24%** têm IA funcionando **dentro do workflow de receita**
- Compradores estão **saindo de point solutions** e buscando consolidação
- "Para a maioria dos times, a IA vive fora do sistema de registro"

**Verificação (29/08/2026):** o release canônico no BusinessWire **não abriu** (interstício anti-bot; não contornado). Confirmado por (a) página do emissor `momentum.io/voice-of-the-market`, lida no Chrome real — *"The 2026 Voice of the Market Report from Momentum · Over 2,000 real B2B conversations"* — e (b) cópia sindicada independente lida (SalesTechStar, 27/01/2026): *"88% of teams claim AI adoption, but only 24% have embedded it into revenue workflows"* · *"drawing on more than 2,000 active B2B sales opportunities across 150 industries"*. Regra: emissor + segunda recuperação independente = 95%. **Não é 100%** porque a página canônica não foi lida.

⚠️ **Dois cuidados novos:** (1) a página do emissor também diz *"We analyzed 1,069 real B2B sales calls"* — o release esclarece que 1.000+ calls é a base do relatório **2025**, e 2.000+ oportunidades a do **2026**; cite a do 2026. (2) O site exibe o banner **"Momentum is now part of Salesforce!"** — a Momentum foi adquirida pela Salesforce.

**Leitura de duas mãos:** sustenta a tese de que IA solta não resolve — e ao mesmo tempo é a objeção mais dura que o Antessala vai ouvir, porque ele *é* mais um point solution. Prepare resposta.
*(Ressalva de método: é pesquisa publicada por fornecedor da categoria — hoje parte da Salesforce. Cite como "relatório da Momentum", nunca como dado neutro de mercado.)*

---

## ⚠️ NÃO USE

### A estatística dos 82% de decisores `[85%]`

Circula amplamente: *"82% dos decisores B2B acham que vendedores chegam despreparados"*. Parece feita para este pitch.

Rastreamento: atribuída a um estudo da *Biznology*, **sem estudo documentado localizável**, repetida entre blogs por anos com citação copiada. Uma das próprias páginas que a publica registra essa ressalva.

**Numa banca, uma pergunta de origem derruba o número e contamina o resto.** Fique com o que o V3 já tem com fonte nomeada: Salesforce State of Sales 2026, RD Station Panorama 2026, 6sense 2025.

### Os números de adoção/shelfware — REMOVIDOS em 29/08/2026

Constavam na v2 a 40%: "42% dos vendedores sobrecarregados com ferramentas" · "23% obtêm ROI no 1º ano" · "<40% das empresas treinam". Busca dirigida nesta rodada:

- **42%** — atribuição a "Gartner Sales Survey 2025" vinha só de compilação de terceiro (403 ao abrir). Releases da Gartner localizados por título trazem **50%** (16/09/2024) e **70%** (Seller Skills Survey 2024) — nunca 42%. gartner.com respondeu 403 em 3 tentativas. → **removido** (30%)
- **23%** — nenhum estudo nomeado; só outros "23%" de assuntos diferentes. → **removido** (0%)
- **<40%** — nenhum estudo nomeado. O mais próximo é um release da Gartner de 18/11/2025 sobre *"fewer than 40% of sellers will report AI agents improved productivity"* — assunto diferente, não aberto (403). → **removido** (0%)

**Substituto com metodologia nomeada, se o argumento de sobrecarga for necessário** `[E3]`: Allego, *"New Research: Poor Adoption of Sales Tools Causes Missed Quotas"*, 09/02/2022, lida em 29/08/2026 — *"Allego surveyed 330 B2B sales leaders"* · *"76% of companies said poor adoption of sales tools is a top reason teams miss their sales quotas"*. Ressalvas: fornecedor da categoria, amostra de **líderes** (comprador, não usuário), não brasileira, **4+ anos**. ⚠️ A mesma página traz um "82%" (*"trying to get reps to use the provided sales tools feels like a second job"*) que **não tem relação** com a estatística banida dos 82% de decisores — não misturar.

---

## CONFERÊNCIA DAS 6 URLs — feita em 29 ago 2026

| # | URL | Conferido | Veredito | Confiança |
|---|---|---|---|---|
| 1 | `rdstation.com/planos/crm/` | Basic R$73 · Pro R$131 · mín. 4 usuários | **Bate** · diverge na implantação (R$849 Basic/Pro; R$1.999 é Advanced) | 100% |
| 2 | `agendor.com.br/planos-precos` | Performance R$83/usuário | **Bate** — declarado direto; Pro R$59 e Corporativo R$156 são novos | 100% |
| 3 | `apollo.io/pricing` → `/pt/pricing` | US$49 / 79 / 119 · mín. 3 assentos | **Bate** (Chrome real) | 100% |
| 4 | `business.linkedin.com/sell/sales-navigator/compare-plans` | US$119,99 / US$159,99 | **Bate** | 100% |
| 5 | `ampup.ai/meeting-prep` | promessa "2 min vs 20 min" | **Diverge** — "2-Min Briefs" vs **"45+ Minutes"**; título é "for Sales Teams" | 100% (novo) / 0% (antigo) |
| 6 | `businesswire.com/news/home/20260127999573/en/` | Momentum 88% / 24% | **Bate** via emissor + cópia sindicada; canônica não abriu (anti-bot) | 95% |

---

## LOG DE BUSCA

### v2 (sessão remota, sem abrir página)

| Query | Resultado |
|---|---|
| RD Station CRM planos *(domínio rdstation.com)* | ✅ Confirmado + mínimo de 4 usuários |
| Agendor planos *(domínio agendor.com.br)* | ✅ Confirmado por aritmética |
| Apollo pricing *(domínio apollo.io)* | ✅ Confirmado |
| Sales Navigator plans *(domínio linkedin.com)* | ✅ Confirmado |
| Gong pricing *(domínio gong.io)* | ✅ Confirmado como cotação-only |
| AmpUp pre-call briefing *(domínio ampup.ai)* | ✅ Confirmado *(redação depois corrigida na v3)* |
| Momentum VoM 2026 *(domínio businesswire.com)* | ✅ Confirmado |
| Ploomes preços *(domínio ploomes.com)* | ⚠️ Contradição interna *(resolvida na v3)* |
| Reviews sobre tempo de pesquisa *(g2.com, capterra.com)* | 🟡 Paráfrase de praticante, redação não certificada |
| "chego/entrei despreparado" reunião vendedor | ❌ Só marketing de fornecedor |
| diretor comercial vendedores não pesquisam antes | ❌ Só marketing de fornecedor |
| r/sales prep time *(domínio reddit.com)* | ❌ **Reddit bloqueia o crawler da Anthropic** |
| origem da estatística dos 82% | ✅ Confirmada como não rastreável |

**Leitura de página bloqueada pelo egresso (11 domínios testados):** business.linkedin.com · reddit.com · old.reddit.com · apollo.io · g2.com · agendor.com.br · rdstation.com · costbench.com · en.wikipedia.org e outros.

### v3 (terminal, 29 ago 2026 — páginas abertas)

| Página | Resultado |
|---|---|
| rdstation.com/planos/crm/ · agendor.com.br/planos-precos · business.linkedin.com/…/compare-plans · ampup.ai/meeting-prep | ✅ Lidas (WebFetch) |
| apollo.io/pricing | ⚠️ Não renderiza sem JS (2 tentativas) → ✅ lida no **Chrome real** (`/pt/pricing`) |
| businesswire.com/…/20260127999573 | ❌ Timeout (4x WebFetch) · interstício anti-bot no Chrome — **não contornado** |
| momentum.io/voice-of-the-market | ✅ Lida (Chrome real) — 88/24 atrás de formulário |
| salestechstar.com (cópia sindicada do release) | ✅ Lida |
| telecomreseller.com (cópia sindicada) | ❌ Bloqueio Cloudflare — não contornado |
| parsley.id · getmaxiq.com/echoiq · sifthub.io (+ /pricing de cada) | ✅ Lidas |
| ploomes.com/pricing | ❌ 404 → ✅ `ploomes.com/precos` e `/en/pricing` lidas |
| kommo.com/pricing/ · /br/precos/compare-planos/ · blog/kommo-pricing/ · support (pt-br) | ✅ Lidas — nenhuma em R$ |
| kommo.com/br/precos/ | ❌ HTTP 500 (WebFetch); Chrome desconectou antes da tentativa |
| gartner.com (releases de sobrecarga) | ❌ 403 (3x) |
| allego.com (pesquisa de adoção 2022) | ✅ Lida |

---

## Próximo passo (Agora)

As 5 entrevistas (`roteiro-entrevistas-primarias.md`, Trilha B primeiro). É o **único** caminho para o verbatim — não por limitação minha, mas porque a conversa não existe publicamente em português.

## Pendências residuais desta rodada

- **Momentum a 95%**: só sobe a 100% com leitura humana do release no BusinessWire (anti-bot) — ou do PDF do relatório após preencher o formulário em momentum.io.
- **Kommo R$66**: `kommo.com/br/precos/` deu HTTP 500. Como o domínio inteiro vende em USD, a decisão (fora das âncoras em reais) não depende dessa página.
- **Apollo "Insights de IA pré-reunião"**: ler a funcionalidade para decidir se sobe de adjacente a concorrente direto.

## Se quiser aprofundar

Levar ao palco a cunha de preço em vez da promessa de briefing. A promessa de briefing já tem dono — quatro, na verdade, com página de vendas no ar e todos dependentes de artefato prévio. A cunha — *a empresa que tem a dor está fora do alcance de quem a resolve* — está sustentada por preço lido na página, com data, em cinco fornecedores.
