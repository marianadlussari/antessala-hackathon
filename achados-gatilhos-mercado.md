# Achados · Gatilhos observáveis e tamanho de mercado (29 ago 2026)

> Entregas 4 e 6 do `prompt-versao-hackathon.md` (Tarefa 4 do dossiê). Complementa `achados-pesquisa-publica.md`. Mesma régua de confiança e mesmas tags E1–E5.

**Analista:** Atlas (@analyst) · **Data de execução:** 29 ago 2026 · **Todas as consultas web feitas em 29/08/2026.**

---

## AUTO-AUDITORIA (leia antes de usar qualquer número)

| Item | Resultado |
|---|---|
| Afirmações com URL verificável | **19** |
| Páginas que eu **abri e li** (confiança 100% no que reproduzo) | **9** — API SIDRA/IBGE (5 chamadas), InfoJobs, LinkedIn Jobs BR, CRM Hub, CUT (reprodução do release IBGE), Meio&Mensagem, RD Station (2 páginas do domínio do emissor) |
| Páginas que tentei abrir e **falharam** (403 / socket hang up / conteúdo JS) | **8** — agenciadenoticias.ibge.gov.br, catho.com.br, facebook.com/ads/library (2x), trends.builtwith.com, gov.br dados-publicos-cnpj, cnpj-metadados.pdf (binário), PDF CEMPRE 2024 |
| Linhas sem tag de evidência | **0** |
| Gatilhos entregues | **8 aceitos + 2 rejeitados explicitamente** (o prompt sugeria 6 candidatos; 2 deles não sobrevivem ao teste de observabilidade pública no Brasil) |
| Confiança real do documento | **Entrega 4: 78%** (a *observabilidade* está bem sustentada; o *mecanismo causal* de cada gatilho é `[E4]`/`[E5]` em todos os casos). **Entrega 6: 62%** (o universo é `[E3]` a 100%; os dois filtros de maturidade vêm de uma amostra com viés conhecido; o terceiro filtro não tem fonte). |

**Aviso de rigor (dossiê §7, regra 6):** nada neste documento afirma ou insinua que o Antessala aumenta win rate ou conversão. Os gatilhos indicam **momento de orçamento e de atenção**, não probabilidade de fechamento.

---

## AS 3 COISAS QUE ESTE DOCUMENTO **NÃO** RESOLVE

1. **Nenhum gatilho foi validado como preditivo de compra.** Todos os mecanismos ("por que destrava orçamento") são inferência minha `[E4]` ou hipótese `[E5]`. Não achei nenhum estudo brasileiro que correlacione qualquer um destes eventos com compra de ferramenta comercial. Só entrevista com comprador econômico fecha isso.
2. **A janela de ação de cada gatilho é hipótese `[E5]` sem exceção.** Não existe base pública brasileira que meça "quantos dias depois de abrir vaga de vendedor a empresa compra software".
3. **O filtro final do ICP — "sem stack de sales intelligence implantado" — não tem fonte.** Ver LACUNA-1. O número de mercado que entrego é, por isso, um **teto**, não uma estimativa do ICP fechado.

---
---

# ENTREGA 4 · Gatilhos observáveis em dado público brasileiro

## 4.1 · Tabela-resumo

| # | Gatilho | Onde observar no Brasil | Fonte / URL | Data da consulta | Tag | Confiança na **observabilidade** |
|---|---|---|---|---|---|---|
| G1 | Empresa abre vaga de **vendedor / consultor comercial** | InfoJobs · Catho · LinkedIn Jobs · Gupy (portal + páginas de carreira indexadas) · Indeed BR | https://www.infojobs.com.br/vagas-de-consultor-comercial.aspx · https://br.linkedin.com/jobs/sdr-vagas · https://portal.gupy.io/ | 29/08/2026 | `[E2]` | **100%** (abri InfoJobs e LinkedIn e li os contadores) |
| G2 | Empresa abre vaga de **SDR / pré-vendas** | LinkedIn Jobs BR · InfoJobs · Gupy · Indeed BR | https://br.linkedin.com/jobs/sdr-vagas | 29/08/2026 | `[E2]` | **100%** (página aberta) |
| G3 | **A vaga nomeia o CRM/stack** que a empresa usa | Texto das vagas em InfoJobs/Catho/LinkedIn/Gupy · agregador CRM Hub | https://crmhub.com.br/vagas | 29/08/2026 | `[E2]` | **90%** (abri o CRM Hub e vi ferramenta + empresa nomeadas na vaga) |
| G4 | **Abertura de filial, mudança de porte, mudança de CNAE, alteração de capital social** | Dados Abertos do CNPJ da Receita Federal (base completa, atualização mensal) | https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/dados-abertos/cadastros · https://arquivos.receitafederal.gov.br/ | 29/08/2026 | `[E3]` | **85%** (dataset e periodicidade confirmados; **não consegui abrir o PDF de leiaute** — lista de campos não certificada) |
| G5 | Empresa **começou ou intensificou mídia paga** | Biblioteca de Anúncios da Meta (consulta pública, sem login) · Centro de Transparência de Anúncios do Google | https://www.facebook.com/ads/library/ · https://adstransparency.google.com | 29/08/2026 | `[E3]` | **70%** (3+ fontes secundárias concordantes, incluindo o blog da RD Station; **a Meta bloqueou meu acesso direto**) |
| G6 | **Adoção ou troca de ferramenta detectável no site** (script de RD Station, HubSpot, etc.) | BuiltWith (varredura contínua + linha do tempo histórica) · Wappalyzer | https://builtwith.com · https://www.wappalyzer.com | 29/08/2026 | `[E3]` | **50%** (2 fontes secundárias; a página de estatísticas do BuiltWith não carregou para mim) |
| G7 | **Troca de liderança comercial** (novo Head/Diretor de Vendas) | Perfil público no LinkedIn + página da empresa no LinkedIn + post de anúncio | https://www.linkedin.com | 29/08/2026 | `[E4]` | **50%** — observável **manualmente**, caso a caso. Não achei feed público estruturado. Detecção em escala é justamente a feature paga (alerta de job change do Sales Navigator) que o ICP não tem |
| G8 | **Rodada de investimento / aporte** | Distrito (relatórios públicos) · NeoFeed · Startups.com.br · Brazil Journal · ABVCAP | https://www.distrito.me/conteudo/reports · https://neofeed.com.br | 29/08/2026 | `[E3]` | **70%** na observabilidade, **mas cobertura do ICP é BAIXA** — ver 4.3 |

## 4.2 · Detalhamento por gatilho

### G1 · Vaga aberta para vendedor / consultor comercial

- **Evento:** a empresa publica vaga para função de venda direta.
- **Onde observar (verificado):** abri `infojobs.com.br/vagas-de-consultor-comercial.aspx` em 29/08/2026 e o título da página trazia **"10.356 Vagas de Emprego de Consultor Comercial"**. A busca é **pública, sem login**, e cada vaga exibe: empresa (com link para o perfil), cidade/UF, data de publicação ("Hoje", "Ontem", "27 ago"), salário ou "A combinar", experiência exigida, modelo de trabalho. `[E2]` · confiança 100%.
- **Volume comparativo (fonte secundária, não abri as páginas):** Catho — 93.048 vagas de "Vendedor" e 6.575 de "Consultor comercial"; InfoJobs — 14.806 de "Vendedor". `[E3]` · confiança 30% (recuperação única, e a Catho me devolveu 403 quando tentei abrir).
- **Por que destrava orçamento:** contratar vendedor é a decisão que converte "quero crescer" em despesa aprovada; a mesma reunião de aprovação costuma abrir espaço para ferramenta de suporte ao vendedor. **`[E4]` — inferência minha, não testada.**
- **Janela de ação:** `[E5]` hipótese, sem fonte. Sugiro tratar como "enquanto a vaga estiver ativa + ~60 dias" e **testar**, não afirmar.
- **Ressalva séria:** o volume bruto é dominado por varejo e vendas transacionais — que são **anti-ICP** explícito. O gatilho só serve com filtro cruzado de porte e setor (Entrega 6). Sem esse filtro, ele gera ruído, não lista.

### G2 · Vaga aberta para SDR / pré-vendas

- **Onde observar (verificado):** abri `br.linkedin.com/jobs/sdr-vagas` em 29/08/2026; o título exibia **"10.000+ Sdr vagas em Brasil"**. A listagem é navegável sem login (login exigido só para ver tudo/criar alerta). Cada anúncio mostra cargo, empresa, cidade/UF e recência ("Há 7 horas", "Há 1 mês"). `[E2]` · confiança 100% **quanto ao que a página exibe**.
- **⚠️ Alerta metodológico:** o contador do LinkedIn ("10.000+") é aproximado e inclui correspondência fuzzy. **Não use esse número como tamanho de mercado.** Outras recuperações da mesma busca deram "+ de 2.000 vagas de Sdr em: Brasil". A divergência é do próprio LinkedIn. Confiança no **número**: 30%.
- **Por que importa mais que G1:** vaga de SDR indica que a empresa está separando prospecção de fechamento — sinal de estruturação comercial, que é exatamente o corte do ICP. `[E4]`
- **Contra-sinal, e é importante:** o ICP travado é "**sem** SDR/RevOps de research". Uma empresa que acabou de contratar SDR pode estar migrando **para fora** do ICP, não para dentro. Este gatilho é ambíguo por construção e eu não tenho dado para desambiguá-lo. **`[E5]`**

### G3 · A vaga nomeia o CRM que a empresa usa

- **Onde observar (verificado):** abri `crmhub.com.br/vagas` em 29/08/2026 — **"1.158 vagas ativas"**, **"160 publicadas hoje"**, atualização diária. As vagas nomeiam ferramenta **e** empresa contratante. Exemplos reproduzidos da página: *"Analista de CRM Sênior (Salesforce) | Bilíngue (Espanhol)"* — Orbia (São Paulo, SP); *"Especialista Hubspot"* — Grupo AG Capital; *"Product Owner | Zendesk"* — Vericode. `[E2]` · confiança 90%.
- **Por que este é o gatilho mais operacional dos oito:** ele resolve, de graça e em texto público, a pergunta que o ICP exige responder — *qual stack a empresa tem hoje*. Uma vaga que pede "experiência com RD Station CRM ou Pipedrive" e **não** cita Sales Navigator, Apollo, Gong ou ZoomInfo é evidência textual de empresa com CRM e **sem** stack de sales intelligence. `[E4]`
- **Limite honesto:** a ausência de menção não prova ausência de ferramenta. É sinal, não prova. `[E4]`
- **Janela de ação:** `[E5]`.

### G4 · Movimentação cadastral na Receita Federal

- **Evento:** abertura de novo estabelecimento (filial), mudança de porte, inclusão de CNAE secundária, alteração de capital social, mudança de situação cadastral.
- **Onde observar:** **Dados Abertos do CNPJ da Receita Federal**, base completa em CSV, **atualização mensal**, dividida em tabelas de *empresas*, *estabelecimentos*, *sócios* e *Simples*. A tabela de estabelecimentos traz dados cadastrais por unidade (matriz/filial), nome fantasia, CNAE e endereço. Download: `dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj` e `arquivos.receitafederal.gov.br`. `[E3]` · confiança 85%.
- **Por que não é 100%:** tentei abrir o leiaute oficial (`gov.br/receitafederal/dados/cnpj-metadados.pdf`) e recebi PDF binário ilegível; a página `dados-publicos-cnpj` derrubou a conexão. **A existência, a periodicidade mensal e as quatro tabelas estão confirmadas; a lista exata de campos não está certificada por mim.** Quem for usar em produção precisa abrir o leiaute.
- **Por que destrava orçamento:** abrir filial ou subir de porte normalmente vem com meta nova e time novo. `[E4]`
- **Vantagem estrutural deste gatilho:** é o **único** da lista que é (a) gratuito, (b) exaustivo sobre todo o universo de empresas brasileiras, (c) cruzável com CNPJ, e (d) casável 1:1 com o recorte de porte e CNAE da Entrega 6. Os outros sete são amostrais ou manuais.

### G5 · Empresa começou ou intensificou mídia paga

- **Onde observar:** **Biblioteca de Anúncios da Meta** (`facebook.com/ads/library`) — base pública de anúncios ativos em Facebook, Instagram, Messenger e Audience Network, **consultável por nome de anunciante, sem login**, com filtro de país (Brasil), plataforma, tipo de mídia e período; exibe criativo e data de início da veiculação. **Centro de Transparência de Anúncios do Google** (`adstransparency.google.com`) — anunciantes verificados, buscáveis por nome de empresa ou site, com formatos e regiões de veiculação. `[E3]` · confiança 70%.
- **Base da confiança 70%:** 3+ fontes secundárias independentes e concordantes, incluindo o **blog da própria RD Station** (`rdstation.com/blog/marketing/biblioteca-de-anuncios/`), Neil Patel BR e Nuvemshop. **A Meta me devolveu 403 nas duas tentativas de abrir a Ad Library** — não certifiquei o comportamento da ferramenta com meus próprios olhos.
- **Por que destrava orçamento:** investir em mídia gera volume de lead; volume de lead sem preparo é exatamente o mecanismo do produto (*preparo raso → oportunidade potencialmente subaproveitada*). `[E4]`
- **Ancoragem cruzada disponível:** o Panorama RD Station 2026 reporta que **82%** dependem de plataformas de terceiros (redes sociais, WhatsApp, mídia paga) e **62%** não acompanham taxas de conversão do funil `[E3]` (ver Entrega 6 para fonte e metodologia).

### G6 · Adoção ou troca de ferramenta detectável no site

- **Onde observar:** **BuiltWith** — varredura contínua de domínios com **linha do tempo histórica** de tecnologias (permite ver *quando* o script entrou ou saiu); **Wappalyzer** — snapshot do stack, com RD Station e HubSpot entre as tecnologias catalogadas. `[E3]` · confiança **50%** (duas fontes secundárias; a página `trends.builtwith.com/analytics/RD-Station` não renderizou para mim — ficou em "Loading…").
- **Por que importa:** a troca de CRM é um dos gatilhos que o prompt pediu, e esta é a **única forma pública que encontrei de detectá-la sem entrar na empresa** — pelo script de marketing/CRM no site. `[E4]`
- **Limite grave:** detecta automação de marketing no site (RD Station Marketing, HubSpot, ActiveCampaign). **Não detecta CRM interno sem pegada no site** — que é justamente o caso do RD Station CRM, Agendor, Ploomes e Pipedrive na maioria das PMEs. O gatilho tem cobertura parcial e enviesada. Não prometa cobertura total.

### G7 · Troca de liderança comercial

- **Onde observar:** perfil público no LinkedIn (mudança de cargo), página da empresa e post de anúncio de contratação. `[E4]` · confiança **50%**.
- **Por que só 50%:** o evento é visível, mas **não achei nenhum feed público, gratuito e estruturado no Brasil que emita esse sinal em escala.** Monitorar N empresas exige checagem manual — ou uma ferramenta paga de alerta de job change. **Há uma ironia útil aqui:** o gatilho mais citado como "óbvio" só é operacionalizável por quem já comprou a categoria que o ICP não compra.
- **Uso recomendado:** gatilho de **conta específica** (quando já existe lista curta), não de geração de lista.

### G8 · Rodada de investimento

- **Onde observar:** relatórios públicos do **Distrito** (`distrito.me/conteudo/reports`), **NeoFeed**, **Startups.com.br**, **Brazil Journal**, **ABVCAP**. `[E3]` · confiança 70% na existência e periodicidade das fontes.
- **Ordem de grandeza (fonte secundária, não abri o relatório):** startups brasileiras captaram **US$ 2,14 bi em 2024**, em **386 rodadas**, segundo dados do Distrito. `[E3]` · confiança 30% (recuperação única, via Startups.com.br).
- **⚠️ Cobertura do ICP: BAIXA — e isso é o achado.** 386 rodadas/ano contra um universo de dezenas de milhares de empresas no ICP (Entrega 6). Além disso, startup com aporte tende a comprar stack e contratar RevOps — ou seja, **migra para o anti-ICP**. Este gatilho é popular em deck e **quase irrelevante para este ICP específico**. Mantenho na lista por transparência, com a recomendação de **não usá-lo como canal principal**.

## 4.3 · Gatilhos que o prompt pediu e que eu **rejeito** por não serem observáveis

Registro os dois porque a ausência é informação, não fracasso.

| Candidato do prompt | Veredito | Motivo | Tag |
|---|---|---|---|
| **Virada de trimestre com meta não batida** | **NÃO OBSERVÁVEL publicamente para o ICP** | PME de capital fechado não tem obrigação de publicar resultado comercial. Quem publica trimestre é S.A. de capital aberto — que é anti-ICP. Não existe fonte pública brasileira que exponha meta batida/não batida por CNPJ | `[E4]` |
| **Corte de headcount mantendo meta** | **NÃO OBSERVÁVEL por empresa** | O Brasil não tem equivalente ao WARN Act americano (aviso público de demissão em massa). O **Novo CAGED** publica microdados mensais de admissão e desligamento, mas o Ministério do Trabalho declara que os dados são divulgados **"sem identificação dos empregadores ou trabalhadores"** — só por município, CNAE e CBO. Serve como termômetro setorial, **nunca** como sinal de conta. Fonte: `gov.br/trabalho-e-emprego/.../microdados-rais-e-caged`, consultado em 29/08/2026 | `[E3]` |

**Nota de uso do CAGED:** ele ainda tem valor como **sinal de janela de mercado** — admissões nas CBOs comerciais por setor e mês indicam quando o setor está contratando vendedor. Isso informa *quando* fazer campanha, não *para quem*. Confiança 85% na descrição do dado, 0% em qualquer uso por empresa.

---
---

# ENTREGA 6 · Tamanho de mercado

> **Objetivo:** quantas empresas brasileiras plausivelmente batem no ICP. Cadeia explícita, cada elo com fonte. Onde não há fonte, `[E5]` declarado.

## 6.1 · Base: universo de empresas por porte (dado primário, lido por mim)

**Fonte:** IBGE · **Estatísticas do Cadastro Central de Empresas (CEMPRE)**, tabela SIDRA **7528**, variável 2585 ("Número de empresas e outras organizações"), Brasil, **ano de referência 2024**.
**Como obtive:** consulta direta à API do SIDRA em **29/08/2026**, URL `https://apisidra.ibge.gov.br/values/t/7528/n1/all/v/2585/p/2024/c319/all/c2703/all`. **Li a resposta da API do próprio IBGE.**
**Tag:** `[E3]` (dado secundário de fonte nomeada — o emissor é o IBGE) · **Confiança: 100%** no número reproduzido.

| Faixa de pessoal ocupado | Total | **Entidades empresariais** | Adm. pública | Sem fins lucrativos |
|---|---:|---:|---:|---:|
| **Total** | 10.607.110 | **9.486.025** | 59.399 | 1.061.686 |
| 0 a 4 | 9.020.033 | 8.003.006 | 41.374 | 975.653 |
| 5 a 9 | 888.339 | 833.415 | 2.649 | 52.275 |
| 10 a 19 | 411.455 | 392.706 | 2.225 | 16.524 |
| **20 a 29** | 107.121 | **100.671** | 1.165 | 5.285 |
| **30 a 49** | 76.615 | **70.786** | 1.344 | 4.485 |
| **50 a 99** | 52.204 | **47.071** | 1.732 | 3.401 |
| **100 a 249** | 27.938 | **23.194** | 2.644 | 2.100 |
| 250 a 499 | 11.278 | 7.889 | 2.496 | 893 |
| 500 ou mais | 12.127 | 7.287 | 3.770 | 1.070 |

**Verificação cruzada independente:** o release do CEMPRE **2023** do IBGE (divulgado em **13/11/2025**) informa **10,0 milhões** de empresas e organizações formais ativas, com **93,1% de 0 a 9 pessoas · 5,9% de 10 a 49 · 0,8% de 50 a 249 · 0,2% de 250 ou mais**. Reproduzido de `cut.org.br/noticias/ibge-empresas-contrataram-mais-...-55e5`, consultado em 29/08/2026 (a página oficial da Agência IBGE me devolveu 403). O total de 2024 (10,6 mi) é coerente com 10,0 mi em 2023. `[E3]` · confiança 70% nesta segunda linha (é reprodução de release, não o release aberto por mim) — mas ela **concorda** com o dado da API, que é o que uso.

**O CEMPRE 2024 foi publicado em 2026** (edição de 74 páginas, formato digital, catálogo da Biblioteca IBGE). `[E3]` · confiança 70%.

### Premissa P1 — faixa de pessoal ocupado como proxy de "3 a 15 vendedores"

> **A faixa de 20 a 249 pessoas ocupadas é o proxy do ICP.** Racional: com time comercial representando tipicamente 10% a 20% do quadro, 3 vendedores implicam ~20-30 pessoas e 15 vendedores implicam ~100-150 pessoas.
> **Tag: `[E5]` — hipótese minha. Não achei nenhuma fonte brasileira que publique a razão vendedores/quadro total por porte.** Este é o elo mais frágil de toda a cadeia e a primeira pergunta que uma banca faz. Ver LACUNA-2.

## 6.2 · Filtro setorial (dado primário, lido por mim)

**Mesma fonte e mesma consulta**, cruzando faixa de pessoal com seção/divisão CNAE 2.0 (URLs: `.../c319/all/c12762/116910,117363,117484,117555` e `.../c12762/117608,117666,117673,117714` e `.../c12762/117376,117438`). Consultadas em 29/08/2026. `[E3]` · **confiança 100%** nos números.

Empresas por seção CNAE, somando as faixas **20-29 + 30-49 + 50-99 + 100-249**:

| Seção / divisão CNAE | 20-249 pessoas | Entra no filtro B2B? |
|---|---:|---|
| C · Indústrias de transformação | **48.343** | sim |
| G46 · Comércio **por atacado** | **13.648** | sim |
| H · Transporte, armazenagem e correio | **15.409** | sim |
| J · Informação e comunicação | **7.602** | sim |
| K · Atividades financeiras e de seguros | **3.074** | sim |
| L · Atividades imobiliárias | **1.656** | sim |
| M · Atividades profissionais, científicas e técnicas | **11.667** | sim |
| N · Atividades administrativas e serviços complementares | **32.354** | sim |
| **Subtotal filtro B2B** | **133.753** | — |
| G47 · Comércio **varejista** | 36.184 | **não** (transacional = anti-ICP) |
| G45 · Comércio/reparação de veículos | 6.904 | **não** |
| Demais seções (A, B, D, E, F, I, P, Q, R, S…) | ≈ 64.881 | fora do recorte base |
| **Todas as seções · entidades empresariais · 20-249** | **241.722** | universo máximo |

### Premissa P2 — quais setores contam como "ticket médio-alto com alguma consultividade"

> Incluí C, G46, H, J, K, L, M, N. Excluí varejo (G47), veículos (G45), alojamento e alimentação, educação, saúde, construção e agro.
> **Tag: `[E4]` — inferência minha a partir da definição de anti-ICP do V3 ("vendas transacionais de baixo valor unitário").** Nenhuma fonte brasileira classifica CNAE por consultividade de venda. Um recorte diferente move o resultado em ±40%. Por isso entrego faixa, não número único.

## 6.3 · Filtro de maturidade comercial (fonte nomeada, com viés declarado)

**Fonte:** RD Station · **Panoramas de Marketing e Vendas**.

**Metodologia, verificada no domínio do emissor** (`rdstation.com/pesquisas/panorama-marketing-vendas/edicao-2026/introducao/`, consultada em 29/08/2026 — **página aberta por mim**): **2.790 profissionais de Marketing e Vendas do Brasil**, **nível de confiança 95%**, **margem de erro 2,5%**, estudo 100% nacional. Perfil dos respondentes: sócio/CEO/proprietário 26% · lideranças de Mkt/Vendas 21% · analistas 20% · vendedores 10% · freelancers/autônomos 7% · SDRs 5% · outros 11%. Complementado por dados de ferramenta: 97 milhões de negociações no RD Station CRM em 2025. `[E3]` · confiança 100% na metodologia.

### Premissa P3 — adoção de CRM como proxy de "comercial estruturado"

| Dado | Valor | Fonte | Tag | Confiança |
|---|---|---|---|---|
| Empresas brasileiras que **operam sem CRM** | **54%** → logo **46% têm CRM** | Panorama RD Station 2026, via Meio & Mensagem, matéria de **26/05/2026** (`meioemensagem.com.br/marketing/empresas-querem-crescer-em-2026-mas-nao-bateram-metas-em-2025`), consultada 29/08/2026 | `[E3]` | **70%** (li a matéria; o número não estava exposto na página do emissor, que é landing page de captura) |
| Empresas que **usam CRM** (edição anterior) | **42%** (58% não usam) | Panoramas RD Station 2025, `rdstation.com/pesquisas/panoramas-rdstation-2025/vendas/maturidade-times/`, **1.504 respondentes**, consultada 29/08/2026 — **página do emissor, aberta por mim** | `[E3]` | **90%** |
| Empresas com **processo de vendas bem estruturado, previsível, escalável e sustentável** | **37%** | mesma página, Panoramas 2025 | `[E3]` | **90%** |

> **Uso CRM (46%) como proxy de "comercial estruturado".** `[E4]`.
> **Alternativa mais fiel e mais dura:** os **37%** com processo estruturado. Se a banca apertar, use 37% — o número cai ~20%.

### Premissa P4 — ausência de pré-vendas como proxy de "sem SDR/RevOps de research"

| Dado | Valor | Fonte | Tag | Confiança |
|---|---|---|---|---|
| Empresas com **equipe de pré-venda responsável pela prospecção, com SDRs e BDRs** | **31%** → logo **69% NÃO têm** | Panoramas RD Station 2025, mesma página, **1.504 respondentes, resposta múltipla** | `[E3]` | **90%** |

> Ausência de SDR/BDR é o proxy mais próximo que existe em dado público brasileiro para "sem função dedicada de research". **`[E4]`** — SDR não é RevOps de research, mas é o indicador mais adjacente disponível.

### ⚠️ Viés desta fonte — declare junto com o número

A amostra da RD Station é composta por profissionais do ecossistema de marketing e vendas digital, boa parte deles cliente ou orbitando a RD. **É plausível que ela superestime a maturidade média das empresas brasileiras** — e também que **subestime a adoção de CRM na faixa de 20-249 pessoas especificamente**, já que 26% dos respondentes são sócio/CEO/proprietário, perfil concentrado em empresas menores. **Os dois vieses puxam em direções opostas e eu não sei qual domina.** Confiança na aplicação desses percentuais à faixa de 20-249: **50%**.

## 6.4 · A cadeia de cálculo, passo a passo

```
CENÁRIO BASE
  Universo IBGE CEMPRE 2024, seções C+G46+H+J+K+L+M+N, 20 a 249 pessoas ........  133.753   [E3] 100%
  × 46% com CRM (proxy de comercial estruturado, Panorama RD 2026) .............   61.526   [E3] 70% / proxy [E4]
  × 69% sem equipe de pré-venda (Panoramas RD 2025) ............................   42.453   [E3] 90% / proxy [E4]
  × % sem stack de sales intelligence ..........................................  SEM FONTE  [E5]  → LACUNA-1
  ────────────────────────────────────────────────────────────────────────────────────────
  RESULTADO BASE .......................................................... ~42.000 empresas (TETO)

CENÁRIO CONSERVADOR
  Setores estritos C+G46+J+M, faixa 20 a 99 pessoas ............................   72.068   [E3] 100%
  × 42% com CRM (Panoramas RD 2025, número mais baixo das duas edições) ........   30.269
  × 69% sem pré-venda ..........................................................   20.885
  ────────────────────────────────────────────────────────────────────────────────────────
  RESULTADO CONSERVADOR ................................................... ~21.000 empresas

CENÁRIO ALTO
  Todas as seções, entidades empresariais, 20 a 249 pessoas ....................  241.722   [E3] 100%
  × 46% com CRM ................................................................  111.192
  × 69% sem pré-venda ..........................................................   76.723
  ────────────────────────────────────────────────────────────────────────────────────────
  RESULTADO ALTO .......................................................... ~77.000 empresas
```

### Premissas declaradas por cenário

| Cenário | Premissa de setor | Premissa de porte | Premissa de CRM | Tag dominante |
|---|---|---|---|---|
| Conservador ~21.000 | só indústria, atacado, TIC e serviços profissionais | 20 a 99 pessoas (≈ 3 a 10 vendedores) | 42% (edição 2025) | `[E4]` |
| **Base ~42.000** | 8 seções B2B | 20 a 249 pessoas (≈ 3 a 15 vendedores) | 46% (edição 2026) | `[E4]` |
| Alto ~77.000 | todas as seções | 20 a 249 pessoas | 46% (edição 2026) | `[E4]` |

## 6.5 · Resultado

> ### **Faixa: ~21.000 a ~77.000 empresas brasileiras. Base: ~42.000.**
> ### **Confiança real: 62%.**

**Como declarar em banca, exatamente nestes termos:**

> "O universo é dado do IBGE e eu o li na API do SIDRA: **133.753 empresas brasileiras com 20 a 249 pessoas ocupadas em setores B2B** — esse número tem 100% de confiança. Sobre ele apliquei dois filtros de maturidade do Panorama RD Station, que é pesquisa de fornecedor com viés declarado e amostra de 2.790 respondentes. Isso me dá **~42 mil empresas como teto do ICP, numa faixa de 21 a 77 mil**. Chamo de teto porque o último filtro do ICP — 'sem stack de sales intelligence' — **não tem fonte pública brasileira**, e eu não vou inventá-lo."

### O que este número **não** é

- **Não é TAM em receita.** Não multipliquei por preço. Fazer isso exigiria assumir ticket e taxa de conversão — nenhum dos dois validado (dossiê §4: "Empresas pagariam por briefing isolado — NÃO COMPROVADO").
- **Não é mercado endereçável.** É universo que **cabe na definição**, não que compre.
- **Não é estimativa de demanda.** Nenhum elo mede intenção de compra.

### Duas triangulações de sanidade (faça você mesmo a conta)

1. **Base instalada de CRM.** A cadeia implica ~111 mil empresas com CRM na faixa 20-249 (cenário alto). A RD Station — líder de mercado — declara ter **50.000 clientes em 2024** / **mais de 60 mil empresas clientes**, mas isso é **todos os portes e 40+ países** (`administradores.com.br`, `[E3]`, confiança 30%, recuperação única). Somando Ploomes, Agendor, Pipedrive, HubSpot, Salesforce, Kommo, Zoho, Bitrix, Moskit e outros, 111 mil na faixa 20-249 é **plausível, porém no limite superior**. Isso reforça que **o cenário alto é otimista** e que o risco da cadeia é para baixo.
2. **A cunha de preço já verificada no dossiê (§4, 90-92%).** A PME do ICP paga hoje **R$ 70 a R$ 130 por vendedor/mês** em ferramenta comercial, enquanto o Sales Navigator custa ~US$ 120/assento/mês. Isso sustenta *qualitativamente* que a penetração de sales intelligence nessa faixa é baixa — o que é a **direção** do filtro que falta, mas **não é o percentual dele**. Não converta em número.

---
---

# LACUNAS

| # | O que não consegui fundamentar | Impacto | O que fecharia |
|---|---|---|---|
| **LACUNA-1** | **Percentual de PMEs brasileiras sem stack de sales intelligence.** Não existe pesquisa pública brasileira que meça penetração de sales intelligence (não CRM) por porte. Sem isso, o número da Entrega 6 é teto, não estimativa | **Alto** — é o último filtro do ICP | Pesquisa própria com amostra de 100+ PMEs, ou dado de fornecedor (ZoomInfo/Apollo/LinkedIn) que não é publicado por região |
| **LACUNA-2** | **Razão vendedores/quadro total por porte no Brasil.** A conversão "3 a 15 vendedores → 20 a 249 pessoas ocupadas" é hipótese `[E5]` minha. Nem IBGE nem RAIS publicam essa razão | **Alto** — define o universo inteiro | RAIS/CAGED por CBO comercial cruzado com porte do estabelecimento (dado existe em microdado identificado, mas não é público); ou 10 entrevistas com gestores medindo a razão |
| **LACUNA-3** | **Nenhum gatilho foi validado como preditivo.** Todos os "por que destrava orçamento" são `[E4]`/`[E5]` | **Alto** — muda a priorização dos 8 | Entrevistas Trilha B (comprador econômico) do `roteiro-entrevistas-primarias.md`: perguntar *"o que aconteceu na empresa nos 90 dias antes de você comprar a última ferramenta comercial?"* |
| **LACUNA-4** | **Janela de ação de todos os 8 gatilhos.** `[E5]` sem exceção | Médio | Só teste de campo (medir resposta por dias desde o evento) |
| **LACUNA-5** | **Lista exata de campos dos Dados Abertos do CNPJ.** Confirmei dataset, periodicidade mensal e as 4 tabelas; **não consegui abrir o leiaute oficial** (PDF binário) | Médio | Baixar `gov.br/receitafederal/dados/cnpj-metadados.pdf` e ler — 5 minutos numa máquina que renderize PDF |
| **LACUNA-6** | **Números do Panorama RD Station 2026 no domínio do emissor.** O 54% sem CRM só consegui via Meio & Mensagem; a página da RD é landing page de captura | Médio | Preencher o formulário em `rdstation.com/pesquisas/panorama-marketing-vendas/edicao-2026/` e ler o relatório completo — sobe de 70% para 90-95% |
| **LACUNA-7** | **Comportamento real da Biblioteca de Anúncios da Meta e do BuiltWith.** Ambos bloquearam ou não renderizaram para mim | Baixo | Abrir num navegador comum |
| **LACUNA-8** | **Contagem confiável de vagas na Catho.** Devolveu 403; só tenho os números via snippet de busca | Baixo | Abrir num navegador comum |

---

# LOG DE BUSCA
*(todas em 29/08/2026 · queries vazias e páginas bloqueadas registradas)*

### Buscas realizadas (WebSearch)

| # | Query | Resultado |
|---|---|---|
| 1 | IBGE Cadastro Central de Empresas CEMPRE 2023 número de empresas por faixa de pessoal ocupado | ✅ localizou release e catálogo IBGE |
| 2 | Receita Federal dados abertos CNPJ arquivos estabelecimentos download público | ✅ localizou dados.gov.br e arquivos.receitafederal.gov.br |
| 3 | IBGE agência de notícias CEMPRE 2023 empresas ativas faixas de pessoal ocupado 2023 | ✅ trouxe a distribuição percentual |
| 4 | SIDRA tabela CEMPRE 2023 empresas por faixas de pessoal ocupado assalariado | ⚠️ genérica; resolvida depois pela API |
| 5 | RD Station Panorama de Vendas 2026 adoção de CRM empresas brasileiras percentual metodologia | ✅ 54% sem CRM + metodologia |
| 6 | Novo CAGED microdados layout variáveis CNPJ município CBO seção disponibilidade pública | ✅ **confirmou anonimização dos empregadores** (achado que rejeitou 1 gatilho) |
| 7 | "Gupy" maior plataforma de recrutamento Brasil número de vagas empresas 2025 | ⚠️ **PARCIALMENTE VAZIA** — retornou aporte e headcount da Gupy, **não** o número de vagas |
| 8 | Biblioteca de Anúncios Meta Ad Library Brasil consulta pública | ✅ 3+ fontes secundárias concordantes |
| 9 | Distrito Inside Report investimentos startups brasileiras 2026 | ✅ ordem de grandeza (386 rodadas / US$ 2,14 bi em 2024) |
| 10 | Gupy portal de vagas público "vagas.gupy.io" página de carreiras indexada Google | ⚠️ **PARCIALMENTE VAZIA** — confirmou portal.gupy.io e indexação; não confirmou o subdomínio |
| 11 | "Centro de Transparência de Anúncios" Google anunciantes verificados consulta pública Brasil | ✅ adstransparency.google.com disponível no Brasil |
| 12 | Catho Vagas.com InfoJobs número de vagas vendedor consultor comercial 2026 | ✅ contadores por portal |
| 13 | vagas SDR pré-vendas Brasil quantidade LinkedIn Gupy 2026 | ⚠️ contadores do LinkedIn **divergentes entre si** (2.000 vs 10.000+) — registrado |
| 14 | BuiltWith Wappalyzer detectar RD Station HubSpot site empresa brasileira | ✅ ambos catalogam RD Station |
| 15 | Receita Federal dados abertos CNPJ layout campos data início atividade situação cadastral capital social | ✅ localizou o PDF de leiaute (que depois não abriu) |
| 16 | Sebrae pequenas empresas uso de tecnologia digital vendas CRM percentual 2025 2026 | ⚠️ **VAZIA PARA O MEU FIM** — Sebrae/ABDI publica Índice de Maturidade Digital (IMD 37 pontos, 7 mil MPEs, coleta mai-jun/2025), mas **sem percentual de adoção de CRM**. Não uso |
| 17 | infojobs vagas "RD Station CRM" OR "Pipedrive" OR "HubSpot" requisito vaga vendedor | ✅ levou ao CRM Hub |
| 18 | lista de expositores feira B2B Brasil pública Feicon Fispal Agrishow | ⚠️ **INCONCLUSIVA** — listas existem, mas não consegui abrir nenhuma renderizada. **Gatilho de feira setorial descartado da tabela final por falta de verificação** |
| 19 | RD Station número de clientes empresas Brasil 2025 2026 base instalada CRM | ⚠️ 50 mil (2024) e "mais de 60 mil" — fonte secundária única, confiança 30% |
| 20 | "Panorama de Vendas" RD Station 2026 tamanho do time de vendas número de vendedores | ⚠️ **VAZIA** — **não existe dado público de tamanho médio de time de vendas no Brasil.** Origem direta da LACUNA-2 |
| 21 | IBGE CEMPRE 2024 divulgação Estatísticas do Cadastro Central de Empresas 2024 | ✅ confirmou publicação do CEMPRE 2024 em 2026 |
| 22 | Meta "Biblioteca de Anúncios" transparency.meta.com consulta sem login | ✅ confirmou acesso sem cadastro (fontes secundárias) |

### Páginas abertas com sucesso (WebFetch)

| URL | O que extraí |
|---|---|
| `apisidra.ibge.gov.br/values/t/7528/n1/all/v/2585/p/2024/c319/all` | empresas por faixa de pessoal, 2024 |
| `apisidra.ibge.gov.br/.../c319/all/c2703/all` | idem × natureza jurídica |
| `apisidra.ibge.gov.br/.../c319/all/c12762/116910,117363,117484,117555` | seções C, G, H, J |
| `apisidra.ibge.gov.br/.../c319/all/c12762/117608,117666,117673,117714` | seções K, L, M, N |
| `apisidra.ibge.gov.br/.../c319/all/c12762/117376,117438` | divisões 46 atacado e 47 varejo |
| `servicodados.ibge.gov.br/api/v3/agregados/7528/metadados` | IDs de classificações e categorias |
| `infojobs.com.br/vagas-de-consultor-comercial.aspx` | 10.356 vagas · campos públicos por vaga |
| `br.linkedin.com/jobs/sdr-vagas` | "10.000+ Sdr vagas em Brasil" · campos públicos |
| `crmhub.com.br/vagas` | 1.158 vagas ativas · ferramenta + empresa nomeadas |
| `rdstation.com/pesquisas/.../edicao-2026/introducao/` | metodologia 2.790 respondentes, MoE 2,5%, NC 95% |
| `rdstation.com/pesquisas/panoramas-rdstation-2025/vendas/maturidade-times/` | 42% CRM · 31% pré-venda · 37% processo estruturado · n=1.504 |
| `meioemensagem.com.br/marketing/empresas-querem-crescer-em-2026-...` | 54% sem CRM e demais % · publicada 26/05/2026 |
| `cut.org.br/noticias/ibge-empresas-contrataram-...-55e5` | reprodução do release CEMPRE 2023 |
| `istoedinheiro.com.br/brasil-tinha-10-milhoes-de-empresas-...` | 10 mi empresas 2023 · release de 13/11/2025 |

### Páginas que **falharam** (registrado por honestidade)

| URL | Erro |
|---|---|
| `agenciadenoticias.ibge.gov.br/.../45117-empresas-contrataram-mais...` | HTTP 403 |
| `catho.com.br/vagas/vendedor/` | HTTP 403 |
| `facebook.com/ads/library/` (2 tentativas) | socket hang up / 403 |
| `facebook.com/business/help/2405092116183307` | redirect não seguido |
| `trends.builtwith.com/analytics/RD-Station` | página em "Loading…" |
| `gov.br/receitafederal/.../dados-publicos-cnpj` | socket hang up |
| `gov.br/receitafederal/dados/cnpj-metadados.pdf` | PDF binário ilegível |
| `agenciadenoticias.ibge.gov.br/media/.../e1be873...pdf` (CEMPRE 2024) | HTTP 403 |
| `dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj` | página sem conteúdo renderizado |
| `feicon.com.br/pt-br/Expositores.html` | landing page, lista não renderizada |
| `rdstation.com/pesquisas/panorama-marketing-vendas/edicao-2026/` | landing page de captura, sem os % |

---

# PAINEL DE EVIDÊNCIAS

| # | Afirmação | Tag | Fonte | Data consulta | Confiança |
|---|---|---|---|---|---|
| 1 | 10.607.110 empresas e organizações ativas no Brasil em 2024; 9.486.025 são entidades empresariais | `[E3]` | IBGE · CEMPRE · SIDRA t/7528 v/2585 (API lida) | 29/08/2026 | **100%** |
| 2 | 241.722 entidades empresariais com 20 a 249 pessoas ocupadas (2024) | `[E3]` | idem | 29/08/2026 | **100%** |
| 3 | 133.753 empresas com 20-249 pessoas nas seções C, G46, H, J, K, L, M, N | `[E3]` dado + `[E4]` recorte | idem | 29/08/2026 | **100%** no dado · `[E4]` no recorte |
| 4 | CEMPRE 2023: 10,0 mi de empresas; 93,1% de 0-9 · 5,9% de 10-49 · 0,8% de 50-249 · 0,2% de 250+ | `[E3]` | Release IBGE 13/11/2025, reproduzido por CUT e IstoÉ Dinheiro | 29/08/2026 | 70% |
| 5 | 54% das empresas brasileiras operam sem CRM (46% têm) | `[E3]` | Panorama RD Station 2026, via Meio & Mensagem, 26/05/2026 | 29/08/2026 | 70% |
| 6 | 42% usam CRM · 31% têm equipe de pré-venda com SDR/BDR · 37% têm processo estruturado (n=1.504) | `[E3]` | Panoramas RD Station 2025, domínio do emissor | 29/08/2026 | 90% |
| 7 | Metodologia Panorama 2026: 2.790 respondentes · MoE 2,5% · NC 95% | `[E3]` | rdstation.com (domínio do emissor, página aberta) | 29/08/2026 | **100%** |
| 8 | InfoJobs exibe 10.356 vagas de Consultor Comercial, busca pública sem login, com empresa/cidade/data | `[E2]` | infojobs.com.br | 29/08/2026 | **100%** |
| 9 | LinkedIn Jobs BR exibe "10.000+ Sdr vagas em Brasil", navegável sem login | `[E2]` | br.linkedin.com/jobs | 29/08/2026 | **100%** na exibição · 30% no número |
| 10 | CRM Hub lista 1.158 vagas ativas nomeando ferramenta de CRM e empresa contratante | `[E2]` | crmhub.com.br/vagas | 29/08/2026 | 90% |
| 11 | Dados Abertos do CNPJ: base pública em CSV, atualização mensal, tabelas de empresas/estabelecimentos/sócios/Simples | `[E3]` | gov.br/receitafederal · dados.gov.br | 29/08/2026 | 85% |
| 12 | Microdados do Novo CAGED são divulgados **sem identificação dos empregadores** | `[E3]` | gov.br/trabalho-e-emprego · microdados-rais-e-caged | 29/08/2026 | 85% |
| 13 | Biblioteca de Anúncios da Meta é consultável publicamente, sem login, com filtro de país | `[E3]` | 3+ fontes secundárias, incl. blog RD Station | 29/08/2026 | 70% |
| 14 | Centro de Transparência de Anúncios do Google está disponível no Brasil em adstransparency.google.com | `[E3]` | blog.google (intl/pt-br) + secundárias | 29/08/2026 | 70% |
| 15 | BuiltWith mantém linha do tempo histórica de tecnologias; Wappalyzer e BuiltWith detectam RD Station e HubSpot | `[E3]` | wappalyzer.com + builtwith.com (via secundárias) | 29/08/2026 | 50% |
| 16 | Startups brasileiras: US$ 2,14 bi em 386 rodadas em 2024 (Distrito) | `[E3]` | Startups.com.br citando Distrito | 29/08/2026 | 30% |
| 17 | RD Station: 50.000 clientes em 2024 / "mais de 60 mil empresas clientes" (todos os portes, 40+ países) | `[E3]` | administradores.com.br | 29/08/2026 | 30% |
| 18 | CEMPRE 2024 foi publicado em 2026 | `[E3]` | Catálogo Biblioteca IBGE | 29/08/2026 | 70% |
| 19 | Sebrae/ABDI: IMD nacional 37 pontos, 7 mil MPEs, coleta mai-jun/2025 — **sem dado de CRM** | `[E3]` | Sebrae/PR · Agência Sebrae | 29/08/2026 | 50% · **não usado na cadeia** |
| 20 | Mercado ICP: ~21.000 a ~77.000 empresas, base ~42.000 (teto) | `[E4]` | Cadeia 6.4 acima | 29/08/2026 | **62%** |
| 21 | Todos os mecanismos "por que destrava orçamento" dos 8 gatilhos | `[E4]`/`[E5]` | inferência do analista | — | **0% de validação empírica** |
| 22 | Janela de ação de todos os gatilhos | `[E5]` | hipótese | — | **0%** |

---

**Fim.** Entreguei 8 gatilhos onde o prompt sugeria 6 candidatos, e **rejeitei 2 dos 6 sugeridos** por não serem observáveis em dado público brasileiro. Não completei nenhuma tabela por simetria. O número de mercado é um teto declarado, não uma estimativa fechada.
