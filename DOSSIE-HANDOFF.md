# Dossiê de Handoff · Pesquisa de ICP do Antessala

> **Atualização 30/08/2026:** este dossiê cobre a fase de pesquisa (até 29/08). A entrega do hackathon está em `entrega/`; o consolidado vigente é a **V4** (`fontes/antessala-documento-consolidado-v4.html`). As tarefas abertas abaixo (entrevistas, promoção da jornada) continuam válidas para depois do evento.
>
> Para retomar este trabalho no **Claude Code via terminal**, onde não há bloqueio de rede.
> Tudo o que foi feito, o que ficou aberto, e como continuar sem perder rigor.
>
> **Atualização 29 ago 2026 (terminal):** Tarefas 1, 2 e 4 executadas — páginas abertas e lidas, três registros corrigidos, shelfware removido, gatilhos e tamanho de mercado entregues. Detalhe em `achados-pesquisa-publica.md` (v3) e `achados-gatilhos-mercado.md`. **Nova frente fechada:** a jornada do cliente dentro da ferramenta não estava definida no V3 — decidida item a item em `jornada-do-cliente.md` (+ 3 docs), pendente promoção ao V3. O que resta da pesquisa é a Tarefa 3 (entrevistas).

---

## 1 · Como usar este dossiê

1. Clone o repositório e entre na branch (comandos na seção 6).
2. Abra o Claude Code no terminal, dentro da pasta do projeto.
3. **Cole o prompt de arranque da seção 2** como primeira mensagem.
4. Siga a ordem das tarefas da seção 5. Elas estão priorizadas por impacto.

Tempo estimado para fechar tudo o que é fechável sem entrevista: **~45 minutos.** *(Feito em 29/08/2026.)*

---

## 2 · PROMPT DE ARRANQUE *(cole isto no terminal)*

```
Estou retomando a pesquisa de ICP do Antessala. Leia primeiro estes arquivos
da raiz do repositório antessala-hackathon para se situar:

- DOSSIE-HANDOFF.md        (este dossiê — estado, tarefas, regras)
- achados-pesquisa-publica.md  (o que já foi verificado e com que confiança)
- contexto-antessala.md    (produto, ICP travado, anti-ICP, regra de rigor)

CONTEXTO: o Antessala é um agente autônomo de readiness comercial para PMEs
brasileiras com comercial estruturado (3-15 vendedores, sem SDR/RevOps de
research, sem stack de sales intelligence). Está em estágio pré-cliente, zero
casos próprios. Vai a um hackathon.

O QUE JÁ FOI FEITO: pesquisa pública com preços da categoria e concorrentes
lidos na página de cada fornecedor em 29/08/2026 (100% nas dimensões
verificáveis; Momentum a 95%). Verbatim brasileiro continua em 0% — só
entrevista resolve.

SUA PRIMEIRA TAREFA: a partir dos verbatim das entrevistas (Tarefa 3 do
dossiê), classificar cada um por papel e dor (quente/morna/fria), inserir
como [E1] em prompt-versao-hackathon.md e regerar o painel de evidências.

REGRAS INEGOCIÁVEIS (estão detalhadas na seção 7 do dossiê):
1. Toda afirmação carrega tag de evidência E1-E5.
2. Citação sem URL + data + autor não existe: vira LACUNA.
3. Todo % precisa de fonte com metodologia, ou não entra.
4. Nunca preencher campo por simetria de template.
5. Nunca atribuir ao Antessala resultado de concorrente.
6. Nunca afirmar que o produto aumenta win rate ou conversão.
7. "Não sei" é resposta válida e premiada. Reporte a confiança real, nunca
   uma confiança-alvo.

Comece confirmando o que entendeu e qual será o primeiro passo.
```

---

## 3 · Estado do projeto

**Repositório:** `marianadlussari/antessala-hackathon` (privado, do grupo) · **Branch:** `main`

> Migrado em 29/08/2026 de `marianadlussari/estudos` (pasta `icp-antessala/`, branch `claude/deep-icp-research-jsc6un`), onde o histórico anterior permanece.

| Arquivo (raiz do repositório) | O que é | Status |
|---|---|---|
| `DOSSIE-HANDOFF.md` | Este dossiê | ✅ atualizado 29/08 |
| `achados-pesquisa-publica.md` | Resultado da pesquisa, com confiança por dimensão | ✅ **v3** — 6 URLs conferidas, pendências fechadas |
| `achados-gatilhos-mercado.md` | Entregas 4 e 6: 8 gatilhos observáveis em dado público BR + tamanho de mercado (faixa, cadeia de cálculo, lacunas) | ✅ novo 29/08 — confiança real 78% / 62% |
| `jornada-do-cliente.md` | Índice da jornada: o que o V3 decide vs. o que faltava; 9 decisões + 10 regras derivadas, **decididas pela fundadora em 29/08** | ✅ decidido — **pendente promoção ao V3** |
| `simulacoes-jornada.md` | 3 simulações (fictícias, declaradas) que testaram as decisões e expuseram as regras R1–R10 | ✅ 29/08 |
| `jornada-produto-pm.md` | Jornada ponta a ponta (8 etapas), fronteira do MVP, 7 pontos de decisão, perguntas para entrevistas, riscos — @pm | ✅ proposta; decisões da fundadora prevalecem (nota no topo) |
| `jornada-superficie-ux.md` | Superfície do brief: princípios, wireframe + exemplo fictício, canais, telas de onboarding, interações, acessibilidade, 26 perguntas de validação — @ux | ✅ proposta; decisões da fundadora prevalecem (nota no topo) |
| `contexto-antessala.md` | Bloco de contexto extraído do V3 | ✅ |
| `prompt-versao-hackathon.md` | Prompt enxuto, contexto embutido, 6 entregas | ✅ |
| `prompt-deep-research-icp.md` | Prompt mestre, 15 blocos, pesquisa completa | ✅ |
| `roteiro-entrevistas-primarias.md` | 2 trilhas: 3 usuários + 2 compradores | ✅ pronto para usar |
| `README.md` | Diagnóstico e corte de prioridade | ✅ |
| `build_pdf.py` | Gera o PDF do kit (portátil, acha o Chrome sozinho) | ✅ testado no macOS em 29/08 |
| `fontes/antessala-documento-consolidado-v3.html` | Documento V3 original | ✅ arquivado |
| `Kit-ICP-Antessala.pdf` | Tudo diagramado | ✅ regerado 29/08 |

---

## 4 · Painel de evidências *(atualizado 29 ago 2026 — leitura direta de página)*

### ✅ Verificado — pode ir para o pitch

| Achado | Confiança | Origem |
|---|---|---|
| RD Station CRM: Basic **R$73** · Pro **R$131** /usuário/mês (visão mensal) · Pro e Advanced exigem **mín. 4 usuários** · implantação opcional **R$849** (Basic/Pro) | 100% | rdstation.com, lida 29/08 |
| Agendor: Pro **R$59** · Performance **R$83** · Corporativo R$156 (mín. 10) /usuário/mês | 100% | agendor.com.br, lida 29/08 |
| Ploomes: **R$85**/usuário/mês · **mín. 3 usuários** | 100% | ploomes.com/precos, lida 29/08 |
| Apollo: Free · Basic **US$49** · Professional **US$79** · Organization **US$119** assento/mês, anual · Org exige **mín. 3 assentos** | 100% | apollo.io/pt/pricing, lida 29/08 (Chrome) |
| Sales Navigator: Core **US$119,99** · Advanced **US$159,99** /mês/licença | 100% | business.linkedin.com, lida 29/08 |
| **Gong não publica preço** — só cotação | 95% | gong.io |
| **AmpUp** é concorrente direto; meta title: *"AI Meeting Prep for Sales Teams - 2-Min Briefs"*; contraste com **"45+ Minutes of Research"**; puxa de calls/CRM/e-mails (Gong, Chorus) | 100% | ampup.ai/meeting-prep, lida 29/08 |
| **Parsley · EchoIQ (produto da MaxIQ) · SiftHub** são concorrentes de meeting prep — todos dependentes de artefato prévio (chat do prospect · histórico de deal · CRM + call data) | 100% | sites de cada um, lidos 29/08 |
| Momentum *Voice of the Market 2026*: **88%** dizem usar IA, só **24%** dentro do workflow de receita (>2.000 oportunidades, 150 setores) | 95% | momentum.io (emissor) + cópia sindicada lida; release canônico não abriu (anti-bot) |
| A estatística dos **82% de decisores** não tem origem rastreável — **não usar** | 85% | rastreamento convergente |

### ❌ Não verificado — não levar ao slide

| Item | Confiança | Problema |
|---|---|---|
| Valores em dólar do Gong (US$100-120/usuário + plataforma US$5-15k) | 40% | Estimativa de terceiros. A Gong não publica preço |
| Kommo **R$66**/usuário/mês | 30% | Não aparece em nenhuma página do domínio (4 lidas). Kommo vende em **USD** (15/25/45), mín. 6 meses, reajuste em 01/09/2026 |
| Adoção/shelfware: 42% sobrecarregados · 23% de ROI no 1º ano · <40% treinam | **removidos** | Nenhum estudo nomeado localizado; Gartner traz 50%/70%, não 42%. Substituto com metodologia: Allego 2022 (330 líderes, 76%) — ver achados |
| **Verbatim do ICP brasileiro** | **0%** | Não existe publicamente. Só entrevista resolve |

### ⚠️ Corrigido nesta rodada (registros da v2 que a página derrubou)

| Registro antigo | O que a página diz | Onde |
|---|---|---|
| AmpUp: *"…2 Min Briefs, Not 20 Min Research"* | Frase não existe; contraste real é **45+ min** | ampup.ai |
| RD Station: "implantação opcional R$1.999" | R$1.999 é do **Advanced**; Basic/Pro = **R$849** | rdstation.com |
| Ploomes: "R$240/3 usuários vs R$154,90–498,20" | Nenhum dos dois; é **R$85/usuário, mín. 3** | ploomes.com/precos |

### 🔑 A cunha estratégica que saiu da pesquisa

`[E4]` A PME do ICP paga hoje **~R$60 a R$130 por vendedor/mês** em ferramenta comercial (piso Agendor Pro R$59; núcleo R$73–R$85; teto RD Pro R$131 — três fornecedores lidos na página). Contra isso: Sales Navigator custa ~US$120/assento/mês (4x a 8x o CRM inteiro), Apollo exige 3 assentos, RD Station Pro exige 4, Ploomes exige 3, Kommo exige 6 meses em dólar, e Gong, EchoIQ e SiftHub nem publicam preço.

> **A PME do ICP não está sem sales intelligence por descuido — a estrutura de preço da categoria a exclui.**
> Isso converte o anti-ICP "enterprise" em argumento de cunha, sustentado por preço lido na página: *existe uma faixa de empresa que tem a dor e está fora do alcance de quem a resolve.*

### 🔎 O achado sobre consciência

Três buscas em português retornaram **apenas marketing de fornecedor** — zero fala espontânea de vendedor ou gestor brasileiro. Leitura: **o ICP não nomeia essa dor.** Ele está em consciência de *problema* ou abaixo, e fala de **conversão, meta e inconsistência do time** — não de "preparação de reunião". Isso muda a copy inteira.

### 🧱 O achado sobre a fronteira

Os quatro concorrentes de meeting prep lidos (AmpUp, Parsley, EchoIQ, SiftHub) declaram na própria página que o brief é montado sobre **artefato prévio** — gravação, histórico de deal, CRM ou chat anterior do prospect. Nenhum resolve a **primeira conversa** com conta sem histórico. A fronteira do V3 saiu reforçada por leitura literal, não por interpretação.

---

## 5 · Tarefas em aberto, em ordem

### ✅ TAREFA 1 · Confirmar 6 URLs — **feita em 29/08/2026**

Resultado: 5 de 6 a 100%; Momentum a 95% (release canônico atrás de anti-bot — não contornado). Duas divergências corrigidas com histórico (AmpUp, RD Station). Tabela completa com datas em `achados-pesquisa-publica.md`, seção "CONFERÊNCIA DAS 6 URLs".

### ✅ TAREFA 2 · Fechar as pendências de 40–60% — **feita em 29/08/2026**

- Parsley, EchoIQ (produto da MaxIQ), SiftHub: **confirmados** nos sites → 100%.
- Ploomes: contradição **resolvida** — R$85/usuário/mês, mín. 3 → 100%.
- Adoção/shelfware: origem não encontrada → **removidos do documento**.
- Kommo: R$66 não existe no domínio; preço é em USD → fora das âncoras em reais.

### TAREFA 3 · Entrevistas *(única forma de sair do 0% de verbatim)* — **PRÓXIMA**

Usar `roteiro-entrevistas-primarias.md`. Meta do V3: **3 usuários + 2 compradores econômicos**.
Priorizar a **Trilha B** (comprador) — é a que sustenta o critério "Potencial de negócio".
Depois, colar os verbatim no `prompt-versao-hackathon.md` como `[E1]` e regerar o painel.

### ✅ TAREFA 4 · Gatilhos observáveis e tamanho de mercado — **feita em 29/08/2026**

Entregas 4 e 6 do `prompt-versao-hackathon.md`, em `achados-gatilhos-mercado.md`. Resultado: **8 gatilhos** observáveis em dado público brasileiro (2 candidatos rejeitados por não serem observáveis: "meta não batida" e "corte de headcount"); tamanho de mercado **~21 mil a ~77 mil empresas, base ~42 mil como TETO** (universo IBGE CEMPRE 2024 lido na API do SIDRA a 100%; filtros de maturidade do Panorama RD Station com viés declarado; o último filtro — "sem stack de sales intelligence" — **não tem fonte** e está declarado como lacuna). Confiança real: 78% (gatilhos) / 62% (mercado). Não é TAM em receita.

### ✅ JORNADA DO CLIENTE — decidida em 29/08/2026; pendente promoção ao V3

O V3 define o motor (fluxo, blocos, confiança, fronteira), não a jornada. Em `jornada-do-cliente.md`: 9 decisões + 10 regras (R1–R10), decididas pela fundadora após 3 simulações. **Próximos passos:** (a) promover ao V3 — nova seção de jornada, ordem 6↔7 no §8, guardião e LGPD no §12; (b) acrescentar ao roteiro as perguntas propostas por PM e UX; (c) **testar o brief de 1ª conversa na demo com uma empresa "silenciosa" antes de fechar o pitch**.

### Pendências residuais (não bloqueiam)

- Momentum: ler o release no BusinessWire manualmente (anti-bot) ou baixar o PDF em momentum.io → 100%.
- Apollo lista "Insights de IA pré-reunião" nos planos US$79+: ler a funcionalidade para decidir se é concorrente direto.
- `kommo.com/br/precos/` deu HTTP 500 — irrelevante para a decisão, que já está tomada pelo restante do domínio.

---

## 6 · Setup e comandos

```bash
# 1. Clonar (repositório privado do grupo — peça acesso à Mariana)
git clone https://github.com/marianadlussari/antessala-hackathon.git
cd antessala-hackathon

# 2. Dependência do gerador de PDF (só na primeira vez)
pip install markdown

# 3. Regerar o PDF depois de qualquer alteração nos .md
python3 build_pdf.py
```

**Sobre o PDF:** `build_pdf.py` procura Chrome/Chromium sozinho (Linux, macOS e Windows) e só depende do módulo `markdown` (a versão anterior deste dossiê pedia também `pypdfium2` e `pillow`, que o script não importa). Se não achar o Chrome, defina o caminho:

```bash
CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" python3 build_pdf.py
```

Para incluir um documento novo no PDF, adicione o arquivo à lista `DOCS` no topo de `build_pdf.py`.

```bash
# 4. Commit e push
git add -A
git commit -m "Confirma precos nas fontes oficiais"
git push origin main
```

---

## 7 · Regras de rigor *(o contrato que não pode ser quebrado)*

### Escala de evidência — tag obrigatória em toda afirmação

| Tag | Significa |
|---|---|
| `[E1]` | Fala primária: entrevista ou transcrição real |
| `[E2]` | Verbatim público com URL, data e autor identificável |
| `[E2*]` | Praticante identificado, URL conhecida, **redação não certificada** (página não aberta) |
| `[E3]` | Dado secundário de fonte nomeada |
| `[E4]` | Inferência a partir de E1–E3 |
| `[E5]` | Hipótese não testada |

### Regra de cálculo da confiança

| Nível | Critério |
|---|---|
| 100% | Página aberta e lida diretamente, com data da consulta |
| 95% | Confirmado no domínio do emissor + segunda recuperação independente |
| 90% | Confirmado no domínio do emissor, recuperação única |
| 70% | 3+ fontes secundárias independentes concordantes |
| 50% | 2 fontes secundárias |
| 30% | Fonte secundária única |
| 0% | Sem fonte localizável |

### Proibições

1. Citação sem URL + data + autor → `LACUNA`, nunca invenção.
2. Percentual sem fonte com metodologia → fora.
3. Campo preenchido por simetria de template → fora. Achou 1 onde pedia 3, entrega 1.
4. Verbatim em inglês apresentado como fala nativa brasileira → fora. Listas separadas.
5. Case de concorrente apresentado como resultado do Antessala → fora, nem por descuido de formatação.
6. Afirmar aumento de win rate ou conversão → fora. É hipótese. O mecanismo defensável é *preparo raso → oportunidade subaproveitada → perda invisível*.
7. Perseguir uma meta de confiança → fora. Reporte a real.

### Regra de negócio

> **Dor sem workaround é dor tolerada.** Se ninguém já gasta tempo ou dinheiro resolvendo, não vira compra. Classifique em quente / morna / fria e mantenha as frias fora do topo.

---

## 8 · Armadilhas conhecidas

| Armadilha | Por quê |
|---|---|
| A estatística dos **82% de decisores** | Origem não rastreável. Uma pergunta de banca derruba e contamina o resto |
| **Valores em dólar do Gong** | A Gong não publica preço. São estimativas de terceiros |
| Citar a AmpUp como **"2 min vs 20 min"** | A página diz **"45+ Minutes"**. A frase antiga não existe — citação incorreta de fonte primária |
| Os números de **shelfware** (42% / 23% / <40%) | Removidos: sem estudo nomeado. Gartner publica 50% e 70%, não 42% |
| **Kommo a R$66** | Não existe no domínio; a Kommo vende em dólar com contrato mínimo de 6 meses |
| Traduzir review do **G2 como fala brasileira** | AE americano ≠ gestor de PME brasileira. Perfis diferentes |
| Vender "**fazemos briefing**" | AmpUp, Parsley, EchoIQ e SiftHub já têm página de vendas com essa promessa. A diferenciação é preço + Brasil + autonomia + primeira conversa |
| Citar a **Momentum como dado neutro** | É pesquisa publicada por fornecedor da categoria — hoje parte da Salesforce. Cite como "relatório da Momentum" |
| Somar **usuário e comprador** na mesma estatística | Sentem dores diferentes — e a diferença é o dado |
| Rodar prompt de pesquisa **sem acesso web** | Gera documento impecável e 100% ficcional |

---

## 9 · Definition of done

A pesquisa está pronta quando:

- [x] As 6 URLs da Tarefa 1 estão conferidas, com data de consulta ao lado de cada número *(29/08/2026 — 5 a 100%, Momentum a 95%)*
- [x] Nada abaixo de 70% de confiança aparece em slide *(shelfware e Kommo R$66 removidos/rebaixados)*
- [ ] Existem no mínimo **5 verbatim `[E1]`** vindos das entrevistas
- [ ] Cada verbatim tem papel do entrevistado e classificação de dor (quente/morna/fria)
- [x] O painel de evidências tem uma linha por afirmação, com tag e fonte
- [x] O documento declara a **confiança real por dimensão**, não um número único
- [x] Nenhuma afirmação de causalidade sobre conversão sobreviveu à revisão
- [x] O PDF foi regerado e commitado *(29/08/2026)*

---

## 10 · Contexto de por que este dossiê existe

A pesquisa foi executada numa sessão remota do Claude Code na web cujo ambiente tem **política de egresso restritiva**: o proxy responde `403` para praticamente todo host (testado em 11 domínios, inclusive Wikipedia). Foi possível **buscar**, não **abrir página**.

A verificação foi então feita forçando cada consulta a retornar apenas o domínio do emissor — o que valida a fonte e levou as dimensões verificáveis de 45% para 90–95%, mas não substitui ler a página. Daí a Tarefa 1 — **executada em 29/08/2026 no terminal**, onde a leitura direta levou essas dimensões a 100% e, de quebra, derrubou três registros que a busca havia validado (AmpUp, RD Station, Ploomes). Lição registrada: **confirmação no domínio do emissor valida a fonte, não o número.**

Uma limitação **não** se resolve com rede: o Reddit bloqueia o crawler da Anthropic no nível do publisher, e em português a conversa sobre esta dor não existe publicamente. Verbatim só sai de entrevista — em qualquer ambiente.
