# Jornada UX · Antessala · A superfície do readiness brief

> **Autoria:** Uma (@ux-design-expert) · 29 ago 2026
> **Pergunta que originou o documento:** *"o que o cliente vê? como o que a IA coleta aparece pro usuário?"*
> **Lacuna atacada:** o V3 define o **conteúdo** do brief (8 blocos + 3 tags de confiança) e o **fluxo** (8 passos). Não define a **superfície**: canal, formato, hierarquia, tamanho, comportamento das tags, o que é tocável, como o usuário reage. As palavras "tela", "interface" e "Slack" têm **zero ocorrência** no V3.

> ✅ **DECISÕES DA FUNDADORA (29/08/2026) — prevalecem sobre as recomendações deste documento.** Registro completo em `jornada-do-cliente.md`. O que muda aqui:
> - **Momento da entrega:** não é "60 min antes". É **no dia útil anterior, às 18h**; reunião criada depois disso recebe o brief **imediatamente, com selo "última hora"** (R1–R3). As menções abaixo foram alinhadas.
> - **Onboarding:** o **gestor preenche um formulário curto (≤ 6 campos)** antes das telas do vendedor (D2). As telas 0–5 valem para o vendedor, que continua não preenchendo nada.
> - **Ordem dos blocos 6 ↔ 7** (§2.1): **decidida**, não mais proposta — promover ao V3.
> - **Correção por fato** (§5.3): **decidida** para o MVP.
> - **Feedback** (§5): dois momentos **+ "Não li"** no rodapé do brief; nas 2 h após, "não li" aparece só se o link não foi aberto (D3, R6).
> - **Tela 2 (permissões):** ganha o aviso *"na próxima tela o Google vai pedir permissão de edição — só criamos eventos privados seus"* (R9).
> - **Relatório do gestor:** agregado, sem briefs individuais no MVP (R7, R8).

## Como ler as marcações (Artigo IV · No Invention)

| Marca | Significado |
|---|---|
| `[V3]` | Está escrito no Documento Consolidado V3. É decisão já tomada. |
| `[E5]` | **Proposta minha**, derivada de evidência (achados-pesquisa-publica.md, sobretudo ENTREGA 5 e VERBATIM) ou de prática de UX. **Não é decisão** — é candidata a validação. |
| `[E5-H]` | Proposta que depende de uma **hipótese ainda não testada** sobre o ICP. Marcada separadamente porque cai primeiro se a entrevista contradisser. |

**Duas regras que valem em cada pixel deste documento:**
1. Nenhuma tela, headline, botão ou microcópia afirma que o Antessala aumenta win rate ou conversão. `[V3 · regra de rigor]`
2. Todo dado do exemplo é **fictício e declarado**. Nenhuma empresa, pessoa, URL ou notícia real.

---

# 1 · Princípios de superfície

Doze princípios. Cada um com origem e com a consequência de design que ele obriga.

### P1 · A entrega tem que acontecer sem ser aberta `[V3]` → consequência `[E5]`
O V3 define o produto como agente que entrega "**sem que ninguém peça**" e a restrição do hackathon é autonomia — "um chatbot que espera o vendedor pedir algo é uma direção mais fraca". `[V3]`
**Consequência de superfície `[E5]`:** a superfície primária é **push**, não *pull*. Um web app onde o vendedor precisa lembrar de entrar transfere de volta para o humano o único trabalho que o produto prometeu assumir — e isso é visível na demo, porque a banca vê o clique.

### P2 · A primeira linha responde "por que essa reunião importa" `[V3]`
O bloco 1 da tabela de saída do V3 é **Why now** — "por que essa reunião existe e qual o contexto da oportunidade". `[V3]`
**Consequência `[E5]`:** as primeiras ~90 caracteres (o que sobrevive na prévia de notificação, de e-mail e de WhatsApp) precisam ser o Why now condensado. Se o preview mostrar "Olá! Seu briefing está pronto", o produto gastou o único ativo de atenção que tinha.

### P3 · Todo CONFIRMADO carrega fonte tocável, na mesma linha `[V3]`
"Fatos precisam de fonte." `[V3]` E "% de fatos com fonte" é métrica declarada do MVP. `[V3]`
**Consequência `[E5]`:** a fonte não vai para rodapé nem para nota de fim. Vai **colada ao fato**, com origem e data, e é clicável. Rodapé de fontes é padrão de relatório; aqui o fato é lido isolado, no meio de outros, por alguém andando.

### P4 · Toda HIPÓTESE mostra o "porque" antes de o usuário perguntar `[V3]`
"Hipóteses precisam de justificativa." `[V3]`
**Consequência `[E5]`:** hipótese sem justificativa visível é indistinguível de alucinação — e "fatos errados ou alucinação" é risco **crítico** no V3. A justificativa entra na mesma linha, em texto menor, começando por "porque".

### P5 · DESCONHECIDO vira pergunta, nunca lacuna vazia `[V3]`
"Desconhecidos viram perguntas de discovery." `[V3]`
**Consequência `[E5]`:** é proibido renderizar "Orçamento: —" ou "Não encontrado". O mesmo dado ausente é renderizado como item acionável no bloco *Perguntas críticas*. Campo vazio comunica falha do produto; pergunta comunica trabalho feito.

### P6 · A primeira conversa é o estado padrão, não o estado vazio `[E5]`
Os quatro concorrentes de meeting prep lidos em 29/08/2026 declaram, cada um na própria página, que o brief é montado **sobre artefato prévio**: AmpUp puxa de "calls, CRM, and emails" (integrações Gong/Chorus); EchoIQ de "deal history"; SiftHub "from CRM and call data"; Parsley da conversa que o próprio prospect teve com o chatbot. `[E5 · ENTREGA 5]`
**Consequência `[E5]`:** onde eles mostram estado vazio, o Antessala mostra seu melhor argumento. O brief de primeira conversa não é uma versão degradada — é a versão que a concorrência não tem. O design precisa dar a ele um layout próprio e digno, não um "sem dados disponíveis".

### P7 · Falar a língua que o ICP usa — que não é "preparação" `[E5]`
Achado da seção VERBATIM: três buscas em português retornaram **apenas conteúdo de marketing de fornecedor**; zero fala espontânea de vendedor ou gestor brasileiro. A leitura registrada é que **o ICP não nomeia essa dor** — ele fala de **conversão, meta e inconsistência do time**. `[E5 · VERBATIM]`
**Consequência `[E5]`:** headline de onboarding não é "prepare melhor suas reuniões". É a reunião concreta, o cliente concreto, o que está em jogo naquela conversa. E o brief nunca se autodenomina "sua preparação".
**Limite explícito:** usar o vocabulário do ICP **não** autoriza prometer o resultado do ICP. Podemos dizer "as reuniões que decidem o seu mês"; não podemos dizer "aumente sua conversão". `[V3 · regra de rigor]`

### P8 · Nenhum pixel promete conversão `[V3]`
"Não afirmar que o Antessala aumenta win rate sem evidência primária." `[V3]`
**Consequência `[E5]`:** proibido na interface — "aumente sua taxa de fechamento", "feche mais negócios", contadores de "negócios ganhos com Antessala", badges de performance. Permitido — "o que você já deveria saber, o que falta descobrir e qual avanço buscar", que é a promessa literal do MVP no V3.

### P9 · Útil em 90 segundos, no celular, em pé `[E5]`
O usuário é AE de PME entre uma reunião e outra. A régua da categoria já está pública: o concorrente direto AmpUp vende "**2-Min Briefs**" no próprio meta title. `[E5 · ENTREGA 5]` *(usar como promessa do concorrente, nunca como estatística de mercado — a página não é internamente consistente sobre os minutos.)*
**Consequência `[E5]`:** orçamento de leitura ≈ **350–450 palavras** no corpo principal. Cada bloco em 1–3 linhas. Tudo que exceder isso vai para "ver mais", nunca para o corpo.

### P10 · A superfície nunca decide — ela devolve perguntas `[V3]`
A fronteira humano × máquina do V3 dá ao Antessala: detectar, pesquisar, consolidar, identificar gaps e riscos, criar hipóteses, **sugerir perguntas**, definir objetivo provável. Dá ao humano: confirmar dor, orçamento, urgência e política interna; conduzir a negociação; **tomar a decisão comercial**. `[V3]`
**Consequência `[E5]`:** a interface oferece **perguntas**, não falas prontas. Nada de "diga isto:". Nada de botão "gerar proposta". O verbo do produto é *perguntar*, não *responder pelo vendedor*. Isso também é o que separa readiness de "texto gerado por IA" — o risco de commoditização listado como **alto** no V3.

### P11 · Entregar dentro do fluxo que já existe `[E5]`
Relatório Momentum · Voice of the Market 2026 (base >2.000 oportunidades B2B): **88%** dos times dizem usar IA, apenas **24%** têm IA dentro do workflow de receita — "para a maioria dos times, a IA vive fora do sistema de registro". `[E5 · 95%]` *(pesquisa publicada por fornecedor da categoria, hoje parte da Salesforce — citar como "relatório da Momentum", nunca como dado neutro.)*
**Consequência `[E5]`:** mais um destino para onde ir é exatamente o modo de falhar descrito ali. A superfície primária deve morar onde a mão do vendedor já vai antes da call — o convite do calendário e a caixa de e-mail.

### P12 · Onboarding pede uma coisa `[V3 gatilho]` + `[E5 execução]`
O V3 define entrada como "Calendário + contexto interno + dados públicos" e gatilho como "reunião comercial identificada automaticamente no calendário". `[V3]`
**Consequência `[E5]`:** **calendário é o único passo obrigatório.** E-mail e CRM são adiáveis para depois do primeiro brief. Cada campo obrigatório extra é uma chance de o usuário nunca ver o produto funcionando — e o produto só convence funcionando.

### P13 · Cor nunca carrega significado sozinha `[E5]`
As três tags de confiança são semânticas. Se forem só verde/amarelo/cinza, quebram em: modo escuro de cliente de e-mail (que inverte cores), WhatsApp (sem cor nenhuma), descrição de evento de calendário (texto puro), daltonismo e print em preto e branco — e **printar e mandar no grupo do time é o comportamento de compartilhamento mais provável** `[E5-H]`.
**Consequência `[E5]`:** a tag é sempre **palavra + símbolo**; cor é reforço opcional. WCAG 1.4.1 (uso de cor).

---

# 2 · Anatomia do readiness brief

## 2.1 Ordem dos blocos — o que mantenho e o que proponho mudar

| # | Ordem V3 | Ordem que recomendo | Mudou? |
|---|---|---|---|
| 1 | Why now | Why now | — |
| 2 | O que sabemos | O que sabemos | — |
| 3 | O que mudou | O que mudou | — |
| 4 | Quem está na mesa | Quem está na mesa | — |
| 5 | O que falta | O que falta | — |
| 6 | Riscos | **Perguntas críticas** | trocado `[E5]` |
| 7 | Perguntas críticas | **Riscos** | trocado `[E5]` |
| 8 | Resultado esperado | Resultado esperado | — |

**Uma única troca: 6 ↔ 7.** `[E5]`
**Justificativa:** a regra de confiança do próprio V3 diz que "**desconhecidos viram perguntas de discovery**". *O que falta* e *Perguntas críticas* são, literalmente, o mesmo conteúdo em dois estados — gap e gap convertido em ação. Separá-los com *Riscos* no meio quebra a única cadeia causal explícita do documento. Colados, o vendedor lê "isto eu não sei → então eu pergunto isto", que é a operação mental que ele vai executar na sala.
**Efeito colateral positivo:** *Riscos* passa a encostar em *Resultado esperado*, o que também faz sentido — o risco é o que pode impedir o avanço que o bloco seguinte define.
**Reversível:** se a validação (§7) mostrar que o vendedor procura riscos antes de perguntas, volta-se à ordem V3 sem custo. Nenhum bloco foi criado, removido ou renomeado.

**O que eu NÃO mudei e por quê:** houve tentação de subir *Resultado esperado* para o topo (é a linha mais acionável do brief). Não subi: a promessa do MVP no V3 é ordenada — "o que ele **já deveria saber**, o que ainda **precisa descobrir** e qual **avanço** aquela conversa precisa produzir" — e termina no avanço. Em vez de reordenar, resolvi por **envelope**: a prévia (§2.2) repete a frase do bloco 8. É repetição de bloco existente, não bloco novo. `[E5]`

## 2.2 O envelope — os 90 caracteres que decidem tudo

Em qualquer canal, a primeira coisa vista não é o brief: é a prévia. `[E5]`

```
┌────────────────────────────────────────┐
│  Antessala                      13:47  │
│  14h30 · Nortex · contrato de renov…   │  ← linha 1 = Why now condensado
│  Avanço a buscar: agendar piloto       │  ← linha 2 = Resultado esperado
└────────────────────────────────────────┘
```

Regra de composição `[E5]`: **linha 1 = quem + quando + por que agora** · **linha 2 = o avanço**. Nada de saudação, nada de nome de feature, nada de "seu briefing está pronto".

## 2.3 Wireframe — corpo do brief (mobile, ~40 colunas)

```
╔════════════════════════════════════════╗
║ ANTESSALA                              ║
║ Hoje 14h30 · 45 min · Google Meet ↗    ║  ← link da call no topo:
╠════════════════════════════════════════╣     o motivo real de o
║ NORTEX DISTRIBUIDORA                   ║     vendedor abrir isto
║ 1ª conversa · sem histórico interno    ║
╠════════════════════════════════════════╣
║ ▍POR QUE AGORA                         ║  1
║ Pediram reunião depois de baixar o     ║
║ comparativo de frete. Janela de        ║
║ renovação do contrato atual: out/26.   ║
║ ✓ CONFIRMADO  fonte: form do site ↗    ║
║ ≈ HIPÓTESE  a janela pressiona a       ║
║   decisão · porque o contrato públic…  ║
╠════════════════════════════════════════╣
║ ▍O QUE SABEMOS                         ║  2
║ • Distribuidora regional, ~180 func.   ║
║   ✓ CONFIRMADO  LinkedIn ↗ 26/08       ║
║ • 3 CDs no Sul e Sudeste               ║
║   ✓ CONFIRMADO  site institucional ↗   ║
║ • Nenhum contato anterior registrado   ║
║   ? DESCONHECIDO → virou pergunta Q1   ║
╠════════════════════════════════════════╣
║ ▍O QUE MUDOU                           ║  3
║ • Novo CD anunciado em ago/26          ║
║   ✓ CONFIRMADO  release da empresa ↗   ║
║ • Diretoria de Operações trocou em     ║
║   jun/26                               ║
║   ✓ CONFIRMADO  LinkedIn ↗             ║
╠════════════════════════════════════════╣
║ ▍QUEM ESTÁ NA MESA                     ║  4
║ ┌────────────────────────────────────┐ ║
║ │ R. Ambrósio · Dir. Operações       │ ║
║ │ ≈ HIPÓTESE decisora                │ ║
║ │   porque abriu o contato e o tema  │ ║
║ │   é custo operacional              │ ║
║ │ ✓ no cargo há 3 meses  LinkedIn ↗  │ ║
║ ├────────────────────────────────────┤ ║
║ │ C. Vasques · Coord. Logística      │ ║
║ │ ≈ HIPÓTESE usuário/influenciador   │ ║
║ ├────────────────────────────────────┤ ║
║ │ ? DESCONHECIDO  ninguém de         │ ║
║ │   Financeiro no convite            │ ║
║ │   → virou risco R1 e pergunta Q3   │ ║
║ └────────────────────────────────────┘ ║
╠════════════════════════════════════════╣
║ ▍O QUE FALTA                           ║  5
║ ? Volume mensal de expedição           ║
║ ? Quem assina um contrato deste porte  ║
║ ? Se já usam outro fornecedor hoje     ║
╠════════════════════════════════════════╣
║ ▍PERGUNTAS CRÍTICAS                    ║  6 (era 7)
║ Q1 "Como vocês resolvem isso hoje?"    ║
║ Q2 "Quantas expedições por mês, e      ║
║     quanto isso mudou com o novo CD?"  ║
║ Q3 "Além de vocês dois, quem mais      ║
║     precisa dizer sim?"                ║
╠════════════════════════════════════════╣
║ ▍RISCOS                                ║  7 (era 6)
║ R1 Ninguém de Financeiro na mesa       ║
║ R2 Podem estar comparando fornecedores ║
║    ≈ HIPÓTESE porque baixaram um       ║
║      comparativo, não um material de   ║
║      topo                              ║
╠════════════════════════════════════════╣
║ ▍RESULTADO ESPERADO                    ║  8
║ Sair com o volume mensal e com o nome  ║
║ de quem assina. Piloto agendado seria  ║
║ o melhor desfecho.                     ║
╠════════════════════════════════════════╣
║  [ Foi útil ]      [ Não ajudou ]      ║  ← §5
║  Algo errado aqui? Corrigir ↗          ║
╚════════════════════════════════════════╝
```

## 2.4 Como as três tags aparecem

`[E5]` — a **forma**; `[V3]` — o **significado**.

| Tag | Renderização | Regra obrigatória | Fallback texto puro |
|---|---|---|---|
| **CONFIRMADO** | `✓ CONFIRMADO` + fonte + data, colados ao fato | **Nunca aparece sem fonte.** Sem fonte, o fato é rebaixado a HIPÓTESE ou removido | `[CONFIRMADO] fonte: LinkedIn, 26/08` |
| **HIPÓTESE** | `≈ HIPÓTESE` + a afirmação + linha "porque …" em corpo menor | **Nunca aparece sem o "porque".** Sem justificativa, não entra | `[HIPOTESE] ... porque ...` |
| **DESCONHECIDO** | `? DESCONHECIDO` + **para onde foi** (`→ virou pergunta Q1` / `→ virou risco R1`) | **Nunca aparece como campo vazio.** Todo desconhecido tem destino | `[?] ... -> pergunta Q1` |

Detalhes de renderização `[E5]`:
- **Símbolo antes da palavra** (`✓` `≈` `?`) para varredura visual rápida; a palavra garante o significado quando o símbolo não renderiza.
- **Fonte tocável** = texto do fato + `↗` linkado. O alvo tem ≥44×44 px. O rótulo do link é o nome da fonte, nunca "clique aqui" (WCAG 2.4.4).
- **Data ao lado da fonte, sempre.** Sem data, o vendedor não sabe se "trocou de diretoria" é de junho ou de 2019.
- **Contagem visível `[E5]`:** um rodapé opcional "12 fatos · 9 com fonte" alimenta diretamente a métrica "% de fatos com fonte" `[V3]` e transforma rigor em elemento de interface — que é justamente o que os quatro concorrentes lidos **não** exibem em suas páginas `[E5 · ENTREGA 5]`.

## 2.5 EXEMPLO ILUSTRATIVO — brief preenchido

> ⚠️ **EXEMPLO ILUSTRATIVO · 100% FICTÍCIO.** Empresa, pessoas, datas, notícias e fontes foram inventadas para demonstrar o formato. Nada aqui foi pesquisado, nada corresponde a organização ou pessoa real. As "fontes" são marcadores de posição — em produção seriam URLs verificáveis. Não usar em pitch como se fosse saída real do sistema; se for ao pitch, manter este aviso visível.

---

**ANTESSALA · Hoje, 14h30 · 45 min**
**NORTEX DISTRIBUIDORA (fictícia)** — 1ª conversa · nenhum histórico interno

**▍POR QUE AGORA**
Eles pediram a reunião três dias depois de baixar o comparativo de custo de frete no seu site. O contrato logístico atual deles vence em out/26.
`✓ CONFIRMADO` origem do contato: formulário do site, 26/08/26 *(fonte fictícia)*
`≈ HIPÓTESE` a janela de renovação está pressionando a decisão — *porque* pediram contato a dois meses do vencimento e entraram por material de comparação, não por material de topo de funil

**▍O QUE SABEMOS**
- Distribuidora regional de material de construção, ~180 funcionários — `✓ CONFIRMADO` perfil público da empresa, 26/08 *(fictício)*
- 3 centros de distribuição, Sul e Sudeste — `✓ CONFIRMADO` site institucional *(fictício)*
- Nenhum contato anterior registrado com esta conta — `? DESCONHECIDO` **→ Q1**

**▍O QUE MUDOU**
- Novo CD anunciado em ago/26 — `✓ CONFIRMADO` comunicado da empresa, 12/08 *(fictício)*
- Direção de Operações mudou em jun/26 — `✓ CONFIRMADO` perfil público *(fictício)*
- `≈ HIPÓTESE` o novo CD aumentou a complexidade de expedição — *porque* o comunicado cita "ampliação da malha", mas nenhum número foi publicado

**▍QUEM ESTÁ NA MESA**
| Pessoa (fictícia) | Papel | Leitura |
|---|---|---|
| Renata Ambrósio | Diretora de Operações | `≈ HIPÓTESE` decisora — *porque* abriu o contato e o tema é custo operacional · `✓ CONFIRMADO` no cargo há 3 meses |
| Caio Vasques | Coord. de Logística | `≈ HIPÓTESE` usuário e influenciador técnico — *porque* o cargo opera o processo que a solução toca |
| — | Financeiro | `? DESCONHECIDO` ninguém do Financeiro no convite **→ R1 e Q3** |

**▍O QUE FALTA**
`?` Volume mensal de expedição · `?` Quem assina contrato deste porte · `?` Se já operam com outro fornecedor hoje · `?` Se o novo CD tem prazo de estabilização

**▍PERGUNTAS CRÍTICAS**
**Q1** "Como vocês resolvem isso hoje — é interno ou terceirizado?"
**Q2** "Quantas expedições por mês, e o quanto isso mudou depois do CD novo?"
**Q3** "Além de você e do Caio, quem mais precisa dizer sim para algo assim andar?"
**Q4** "O que faria vocês continuarem exatamente como estão?"

**▍RISCOS**
**R1** Ninguém do Financeiro na mesa — decisão pode não fechar nesta conversa
**R2** `≈ HIPÓTESE` estão comparando fornecedores — *porque* o material baixado foi um comparativo
**R3** `? DESCONHECIDO` prazo real da renovação — se for antes de out/26, o ritmo muda **→ Q2**

**▍RESULTADO ESPERADO**
Sair com o volume mensal e com o nome de quem assina. Melhor desfecho possível: piloto de um CD agendado com data.

`10 fatos · 6 com fonte · 3 hipóteses justificadas · 4 desconhecidos, todos virados em pergunta`
`[ Foi útil ] [ Não ajudou ] · Algo errado? Corrigir`

---

**Leitura do exemplo:** ~330 palavras. Cabe em uma tela e meia de celular. Nenhum bloco precisou de dado interno — é exatamente o cenário de primeira conversa em que os quatro concorrentes lidos não têm o que montar `[E5 · ENTREGA 5]`.

---

# 3 · Comparativo de canais de entrega

## 3.1 Tabela

Escala: **A** alto / **M** médio / **B** baixo. Todas as leituras são `[E5]`.

| Canal | Atrito de onboarding | Lido antes da reunião | Formatação + fonte tocável | Viável em 10 h | Riscos principais |
|---|---|---|---|---|---|
| **Convite do calendário** (evento-espelho / descrição) | **Nenhum adicional** — mesma conexão do gatilho `[V3]` | **A** — o vendedor abre o convite para pegar o link da call; o brief fica no caminho da mão | **M** — texto puro + URLs clicáveis; sem cor, sem tabela | **A** — mesma API do gatilho, só acrescenta escopo de escrita | **Crítico:** editar o evento original **vaza o brief para os convidados externos**. Só evento-espelho privado. Limite prático de tamanho na descrição |
| **E-mail** | **B** — o endereço já vem do calendário; zero campo novo | **M** — caixa cheia; depende do assunto e do horário do disparo | **A** — HTML, hierarquia, links nomeados, alvo de toque; **modo escuro inverte cores** (ver P13) | **A** — um provedor transacional, sem aprovação de terceiros | Cair em Promoções/Spam. Dados de terceiros persistidos em servidor de e-mail. Reencaminhamento sem controle |
| **WhatsApp** | **A** — número + opt-in +, na API oficial, **template aprovado** para mensagem iniciada pelo negócio | **A** — o canal mais aberto do vendedor brasileiro `[E5-H]` | **B** — negrito/itálico apenas; sem tabela; link sem rótulo; texto longo colapsa em "Ler mais" | **B** — aprovação de template e verificação de número não cabem em 10 h de forma confiável | **LGPD sensível:** dado de terceiro no app **pessoal** do vendedor, fora do controle da empresa. Percepção de spam. Se o vendedor sair, o histórico sai com ele |
| **Slack / Teams** | **A** — depende do **guardião de TI** instalar o app no workspace | **M/A** onde o hábito existe | **A** — blocos, botões nativos (feedback em 1 toque) | **M** — webhook é trivial, app com botões e OAuth não | `[E5-H]` **A PME do ICP pode simplesmente não ter workspace ativo** — hipótese não testada. Teams puxa aprovação corporativa. Brief em canal compartilhado expõe dado de conta ao time inteiro |
| **Web app** | **A** — cadastro, login, senha esquecida | **B** — é *pull*: exige lembrar de entrar. Contradiz "sem que ninguém peça" `[V3]` | **A** — controle total | **M** — construível, mas **come as 10 h** que deveriam ir para o fluxo autônomo `[V3 · prioridade 3]` | É exatamente "a IA que vive fora do sistema de registro" (Momentum, 24%) `[E5]`. Mais um login para a PME administrar |

## 3.2 Recomendação `[E5]`

**Camada 1 — entrega (push): evento-espelho privado no calendário, criado no dia útil anterior à reunião, às 18h** *(decisão da fundadora, 29/08; a proposta original era 60 min antes — reunião criada depois da véspera recebe o brief imediatamente, com selo "última hora")*.
Zero onboarding novo (mesma permissão do gatilho), chega no momento exato e mora onde a mão do vendedor já vai. Resolve P1, P11 e P12 de uma vez.
**Regra inegociável:** **nunca** editar o evento original quando houver convidado de domínio externo. Cria-se um evento **novo, privado, sem convidados**, no calendário do vendedor, com título `Antessala · <Empresa> 14h30`. O vazamento do brief para o cliente é o pior fracasso possível deste produto — não é bug, é incidente.

**Camada 2 — corpo completo: e-mail, disparado no mesmo instante.**
É onde cabem hierarquia, tabela de participantes, links de fonte nomeados e os botões de feedback. Assunto = a linha de prévia do §2.2 (Why now condensado), nunca "Seu briefing está pronto".

**Camada 3 (opcional, se sobrar tempo) — página do brief por link não indexado.**
Destino do `↗` "ver fontes" e das ações de correção. Token não adivinhável, `noindex`, sem login. Não é o canal de entrega; é o lugar onde o brief é *aprofundado* e *corrigido*.

**Fora do MVP de 10 h:**
- **WhatsApp** — melhor canal de leitura do Brasil `[E5-H]`, pior canal de LGPD e de aprovação. Vira **pergunta de entrevista** (§7), não linha de código.
- **Slack/Teams** — dependência de guardião de TI que o V3 declara **"ainda não mapeado"**. Construir integração antes de saber se o workspace existe é apostar.
- **Web app como destino principal** — o modo de falhar descrito pelo relatório da Momentum.

**Por que dois canais e não um:** o calendário garante o **momento**; o e-mail garante a **forma** (fonte tocável, P3; contraste e hierarquia, §6). Nenhum dos dois entrega os dois sozinho. E o custo marginal do segundo é baixo — o mesmo conteúdo, dois renderizadores.

---

# 4 · Onboarding — o que o usuário vê e o que ele fornece

Meta `[E5]`: **do primeiro clique ao primeiro brief agendado em menos de 90 segundos, com 1 decisão obrigatória.**

## Tela 0 · A promessa (linguagem do ICP — P7)

```
┌────────────────────────────────────────┐
│                                        │
│   ANTESSALA                            │
│                                        │
│   As reuniões que decidem o seu mês    │
│   começam com o contexto que muda a    │
│   conversa.                            │
│                                        │
│   O Antessala olha sua agenda, faz a   │
│   pesquisa sozinho e te manda o que    │
│   você já deveria saber, o que ainda   │
│   falta descobrir e qual avanço aquela │
│   conversa precisa produzir.           │
│                                        │
│   Você não precisa pedir.              │
│                                        │
│   [  Conectar minha agenda  ]          │
│                                        │
│   Leva 1 minuto. Um passo só.          │
└────────────────────────────────────────┘
```
Texto derivado da promessa literal do MVP no V3. Não diz "preparação" (P7), não promete conversão (P8).

## Tela 1 · Conectar calendário — o único passo obrigatório

```
┌────────────────────────────────────────┐
│  1 de 2                                │
│                                        │
│  Onde está sua agenda?                 │
│                                        │
│  [  Google Calendar          ]         │
│  [  Microsoft / Outlook      ]         │
│                                        │
│  É o único acesso obrigatório.         │
│  E-mail e CRM ficam para depois —      │
│  se você quiser.                       │
└────────────────────────────────────────┘
```

## Tela 2 · Permissões, em português de gente

```
┌────────────────────────────────────────┐
│  O que o Antessala vai fazer           │
│                                        │
│  LÊ                                    │
│  ✓ título, horário e participantes dos │
│    seus eventos futuros                │
│                                        │
│  ESCREVE                               │
│  ✓ cria um evento privado só seu, com  │
│    o brief, no dia anterior à reunião  │
│                                        │
│  NUNCA                                 │
│  ✗ altera, cancela ou responde seus    │
│    eventos                             │
│  ✗ escreve em evento com convidado     │
│    externo                             │
│  ✗ envia nada para o cliente           │
│  ✗ lê eventos passados                 │
│                                        │
│  Você desconecta quando quiser, num    │
│  clique, e apagamos o que guardamos.   │
│                                        │
│  Na próxima tela o Google vai pedir    │
│  permissão de edição de agenda — só    │
│  criamos eventos privados seus.        │
│                                        │
│  [  Continuar  ]   Ver detalhes ↗      │
└────────────────────────────────────────┘
```
`[E5]` A coluna **NUNCA** é o elemento mais importante desta tela e por isso é a mais longa. Conceder acesso à agenda é a barreira real; a objeção não se resolve com política de privacidade em link, resolve-se com a lista do que não fazemos, visível antes do clique.

## Tela 3 · Confirmar quais reuniões contam (10 segundos)

```
┌────────────────────────────────────────┐
│  2 de 2                                │
│  Achei 4 reuniões comerciais nos       │
│  próximos 7 dias.                      │
│                                        │
│  [x] qui 14h30 · Nortex (fictícia)     │
│  [x] sex 09h00 · Meridiano (fictícia)  │
│  [ ] sex 16h00 · Alinhamento interno   │
│  [x] seg 11h00 · Costa & Lima (fict.)  │
│                                        │
│  Desmarque o que não for comercial.    │
│  Eu aprendo com isso.                  │
│                                        │
│  [  Pronto  ]                          │
└────────────────────────────────────────┘
```
`[E5]` Detecção automática por heurística (participante de domínio externo + horário comercial + ausência de palavras de reunião interna) `[V3 · passo 1 do fluxo]`. O usuário **corrige**, não preenche. É a diferença entre 10 segundos e um formulário.

## Tela 4 · Onde receber

```
┌────────────────────────────────────────┐
│  Onde te mando?                        │
│                                        │
│  ✓ E-mail  vendedor@empresa.com.br     │
│    (peguei da sua agenda)              │
│                                        │
│  [x] Colocar também na minha agenda,   │
│      no dia anterior a cada reunião    │
│                                        │
│  [  Começar  ]                         │
└────────────────────────────────────────┘
```

## Tela 5 · Confirmação — o produto já está trabalhando

```
┌────────────────────────────────────────┐
│  Pronto.                               │
│                                        │
│  Sua próxima reunião comercial é       │
│  quinta, 14h30, com a Nortex.          │
│  Seu brief chega quinta, 13h30.        │
│                                        │
│  Não precisa fazer mais nada.          │
│                                        │
│  ─────────────────────────────────     │
│  Quer que eu use o histórico interno   │
│  também? (opcional, 30 s)              │
│  [ Conectar e-mail ]  [ Conectar CRM ] │
│  [ Agora não ]                         │
└────────────────────────────────────────┘
```
`[E5]` **CRM e e-mail entram aqui, depois do compromisso, e sempre com "Agora não" como saída legítima.** Pedir CRM antes do primeiro brief é copiar a dependência de artefato prévio que a §6 deste plano usa como diferencial contra a concorrência.

## 4.1 O que NÃO pedir — nunca

`[V3 · "sem que ninguém peça"]` + `[E5 · execução]`

| Não pedir | Por quê |
|---|---|
| Nome da empresa do prospect | Está no domínio do e-mail dos participantes do evento |
| Quem são os participantes | Está no convite |
| Objetivo da reunião | É o bloco 8 — **é saída do produto, não entrada** `[V3]` |
| Setor, ICP, persona, "conte sobre seu negócio" | Formulário de onboarding disfarçado de personalização |
| Upload de deck, playbook ou material | É a dependência de artefato prévio dos concorrentes `[E5]` |
| Cartão de crédito | Antes de o primeiro brief provar algo, não há o que cobrar |
| CRM como pré-requisito | Ver §4.2 |

## 4.2 Estado vazio — a primeira reunião sem contexto interno

**Este é o estado mais importante do produto, não o pior.** `[E5 · ENTREGA 5]`

Os quatro concorrentes lidos em 29/08/2026 declaram na própria página que montam o brief sobre artefato prévio — AmpUp sobre "calls, CRM, and emails"; EchoIQ sobre "deal history"; SiftHub "from CRM and call data"; Parsley sobre o chat prévio do prospect. Sem esse artefato, eles não têm o que renderizar. O Antessala, como o V3 desenha, precisa funcionar **na primeira conversa**.

**Como renderizar `[E5]`:**

```
┌────────────────────────────────────────┐
│ NORTEX DISTRIBUIDORA (fictícia)        │
│ ── 1ª conversa ──                      │
│ Nenhum histórico interno com esta      │
│ conta. Este brief é 100% pesquisa      │
│ pública + o que o convite mostra.      │
│                                        │
│ Por isso "O que falta" está grande —   │
│ e por isso as perguntas abaixo valem   │
│ mais que o resto.                      │
└────────────────────────────────────────┘
```

Três regras:
1. **Nunca escrever "sem dados"**. Escrever *o que existe* e *de onde veio*.
2. **O bloco *O que falta* expande** e as *Perguntas críticas* ganham destaque — o brief muda de peso, não de tamanho.
3. **A frase "1ª conversa" é um selo, não um aviso de erro.** No pitch, é o slide de diferenciação; na interface, é a mesma frase.

## 4.3 A tela do guardião de acesso

O V3 registra o guardião como **"ainda não mapeado"** — quem aprova acesso a calendário, e-mail e CRM. `[V3]` Portanto esta tela é uma **proposta a validar**, não uma decisão. `[E5-H]`

```
┌────────────────────────────────────────┐
│  Precisa de aprovação da sua empresa?  │
│                                        │
│  [ Copiar texto para enviar ao gestor ]│
│  [ Enviar por e-mail ]                 │
└────────────────────────────────────────┘
```

**Texto pronto, para o vendedor encaminhar (rascunho `[E5]`):**

> **Assunto: aprovação de acesso — Antessala (agenda)**
>
> Quero testar uma ferramenta que lê minha agenda e me manda, antes de cada reunião comercial, um resumo do que já se sabe sobre a empresa e o que ainda falta descobrir.
>
> **O que ela acessa:** título, horário e participantes dos meus eventos futuros.
> **O que ela escreve:** um evento privado só meu, com o resumo, no dia anterior à reunião. Para isso o Google pede permissão de edição de agenda — ela só cria eventos privados meus.
> **O que ela não faz:** não altera nem cancela meus eventos, não escreve em eventos com convidados externos, não envia nada para clientes, não acessa e-mail nem CRM.
> **Dados:** ficam em [local], podem ser apagados a qualquer momento revogando o acesso em [caminho].
> **Base legal (LGPD):** dados de participantes de reunião tratados para preparação da própria reunião — **a redação precisa de validação jurídica antes de ir ao ar** `[E5-H]`.
>
> Se preferir, revogo em um clique.

`[E5]` O que este texto faz de diferente: responde na ordem que um gestor de PME pergunta — *o que entra, o que sai, o que não acontece, como desliga*. Não é uma política de privacidade; é um pedido de autorização com escopo fechado.

---

# 5 · Interações depois da entrega

Regra que atravessa esta seção `[V3]`: o Antessala pesquisa, consolida, levanta hipóteses e sugere perguntas. **Confirmar, negociar e decidir é do humano.** Nenhuma interação proposta aqui move essa fronteira.

Segunda regra `[V3 · §10]`: **coletar não é atribuir.** "Reunião → próxima etapa" e "dias até proposta" são explicitamente "validar depois"; win rate é "não atribuir causalidade no hackathon". Capturar o dado é legítimo; ler causalidade nele, não.

## 5.1 As quatro interações, por ordem de prioridade

| # | Interação | Atrito | Métrica do V3 que alimenta | No MVP de 10 h? |
|---|---|---|---|---|
| 1 | **Útil / Não ajudou** | 1 toque | "% de briefings considerados úteis" `[V3]` | **Sim** |
| 2 | **Corrigir um fato** | 1 toque + texto livre | "% de fatos com fonte" + risco crítico de alucinação `[V3]` | **Sim, versão mínima** |
| 3 | **Registrar o que aconteceu** | 1 toque | "Reunião → próxima etapa" `[V3 · validar depois]` | Sim, se sobrar tempo |
| 4 | **Responder ao brief / pedir mais** | texto livre | — | **Não** — vira chatbot, direção mais fraca `[V3]` |

## 5.2 Útil / Não ajudou — dois links, zero telas

```
Este brief te ajudou?
[  Sim  ]     [  Não  ]
```
`[E5]` Implementação: dois links `GET` assinados no e-mail e no evento. Um toque grava e abre uma página de agradecimento de uma linha — **sem formulário, sem login, sem "conte mais"**. Se o usuário clicar "Não", aí sim uma única pergunta opcional aparece: *"O que faltou?"*, com "pular" à mostra.
**Por que essa e não NPS/estrelas:** a métrica do V3 é binária — "% de briefings considerados **úteis**". Escala de 5 pontos produz um número que ninguém sabe ler com n pequeno.

## 5.3 Corrigir um fato — o antídoto do risco crítico

O V3 classifica "fatos errados ou alucinação" como risco **crítico**, com resposta "fonte obrigatória e separação entre confirmado, hipótese e desconhecido". `[V3]` A correção humana é a terceira perna disso `[E5]`.

**Versão mínima (cabe nas 10 h):** um link "Algo errado aqui?" no rodapé → página com o brief renderizado, cada fato com um `✗` ao lado → toque abre um campo de uma linha ("o certo é…") → salva.

```
┌────────────────────────────────────────┐
│ ✗  "~180 funcionários"                 │
│    CONFIRMADO · perfil público, 26/08  │
│                                        │
│    O certo é: [ 340, contando os CDs ] │
│    [ Salvar ]   [ Só remover isso ]    │
└────────────────────────────────────────┘
```

Três efeitos `[E5]`:
1. O fato corrigido vira contexto interno permanente da conta — o brief seguinte já nasce melhor. É o começo do "contexto persistente" que o V3 aponta como resposta ao risco "CRM + ChatGPT ser bom o bastante".
2. Toda correção é um **rótulo de erro** para calibrar o pipeline de pesquisa.
3. Correções por brief é o indicador de qualidade mais honesto que o MVP consegue produzir — e o único que não depende do que o usuário *acha*.

## 5.4 Registrar o resultado — sem prometer causalidade

Disparo 2 h **depois** do fim da reunião, no mesmo canal `[E5]`:

```
┌────────────────────────────────────────┐
│  Como foi a Nortex?                    │
│                                        │
│  Seu brief apontava:                   │
│  "sair com o volume mensal e o nome    │
│   de quem assina"                      │
│                                        │
│  [ Avançou ]  [ Ficou igual ]          │
│  [ Não avançou ]                       │
│                                        │
│  Descobriu algo que eu deveria saber?  │
│  [ ................ ]  (opcional)      │
└────────────────────────────────────────┘
```

`[E5]` Por que assim:
- O brief **se cobra**: o *Resultado esperado* volta como pergunta. O produto se expõe ao próprio critério — comportamento que a interface dos concorrentes lidos não exibe.
- Três botões, não campo aberto. O texto livre é opcional e alimenta o contexto interno da conta.
- **Leitura permitida:** "% de reuniões que avançaram entre as que receberam brief", declarado como **descritivo**. **Leitura proibida:** qualquer afirmação de que o brief causou o avanço. `[V3 · métricas §10]`
- **Nunca mostrar ao usuário um placar do tipo "você avançou 78% das reuniões com Antessala".** É a promessa de causalidade proibida, vestida de dashboard. `[V3]`

## 5.5 O que fica de fora, de propósito

- **Chat sobre o brief** — "um chatbot que espera o vendedor pedir algo é uma direção mais fraca para este desafio". `[V3]`
- **Edição livre do texto do brief** — corrigir um fato é sinal; reescrever o brief é trabalho, e o produto existe para tirar trabalho.
- **Compartilhar com o time em um clique** — atraente, mas espalha dado de conta e dado pessoal sem controle. Depois de LGPD resolvida. `[E5]`

## 5.6 Métricas do V3 e onde cada uma nasce na interface

| Métrica `[V3]` | Onde a superfície a produz `[E5]` |
|---|---|
| % de briefs entregues automaticamente | Log de disparo; nenhum elemento de UI necessário |
| % de fatos com fonte | Rodapé "10 fatos · 6 com fonte" (§2.4) |
| % de briefings considerados úteis | Botão Útil / Não ajudou (§5.2) |
| Gaps críticos identificados antes da reunião | Contagem de `? DESCONHECIDO` convertidos em Q, + o campo "descobriu algo?" (§5.4) |
| Minutos de preparação evitados | Pergunta única, **uma vez por usuário**, na tela de agradecimento: *"quanto tempo você teria gasto nisso?"* — registrar como **autorrelato**, nunca como medição `[E5]` |
| Reunião → próxima etapa | Três botões (§5.4) — **validar depois** `[V3]` |
| Dias até proposta · Win rate | **Não instrumentar no MVP.** Nenhuma superfície. `[V3]` |

---

# 6 · Acessibilidade e tom

## 6.1 Tela pequena, em movimento

`[E5]`
- **Corpo ≥16 px** (abaixo disso o iOS dá zoom no toque e quebra o layout). Títulos de bloco em maiúsculas pequenas com peso, não em corpo maior — economiza altura.
- **Largura de linha 35–45 caracteres.** Acima disso, leitura em pé no elevador falha.
- **Nada de tabela larga no e-mail.** A tabela de participantes vira **cartões empilhados** abaixo de 480 px (o wireframe §2.3 já mostra assim).
- **Alvos de toque ≥44×44 px**, com ≥8 px entre "Foi útil" e "Não ajudou" — dois botões juntos e pequenos produzem métrica errada.
- **Texto real, nunca imagem de texto.** Imagem bloqueada por padrão em cliente de e-mail = brief em branco. O brief precisa ser **100% legível com imagens desligadas**.
- **Modo escuro:** testar em Gmail iOS/Android e Outlook, que invertem cores de forma diferente. Daí P13 — a tag nunca depende de cor.
- **Ordem do DOM = ordem de leitura**, para leitor de tela. Blocos como `<h2>`, itens como lista.
- **Assunto do e-mail ≤ 45 caracteres** para sobreviver ao corte em tela pequena.

## 6.2 Contraste das tags

`[E5]` Alvos: texto ≥ **4.5:1**; símbolo/borda ≥ **3:1** (WCAG 1.4.3 e 1.4.11). Cor só reforça — o par palavra+símbolo carrega o significado sozinho (WCAG 1.4.1).

| Tag | Peso visual pretendido | Nota |
|---|---|---|
| `✓ CONFIRMADO` | discreto | é o estado esperado; não deve competir com o fato |
| `≈ HIPÓTESE` | médio, distinto | precisa ser percebido **antes** de a frase ser lida como verdade |
| `? DESCONHECIDO` | alto | é o item que gera ação; pode ser o elemento mais marcado do brief |

`[E5]` Evitar a dupla verde/vermelho como único diferenciador (deuteranopia é o caso mais comum). Preferir diferença de **peso e forma** — a hierarquia acima já funciona em preto e branco, que é como o brief vai aparecer se alguém printar.

## 6.3 Tom de voz

**Sim:**
- Segunda pessoa, frase curta, verbo na frente. *"Pediram a reunião três dias depois de baixar o comparativo."*
- Número sempre com fonte e data.
- Incerteza dita, não escondida. *"Não sei quem assina — pergunte."*
- O vocabulário do ICP: **meta, oportunidade, conversa, avanço, quem decide**. `[E5 · VERBATIM]`

**Não:**
- **"Preparação" como headline** — palavra que o ICP não usa para nomear a própria dor. `[E5 · VERBATIM]` Dentro do brief, descrevendo a reunião, tudo bem; como promessa de topo, não.
- **Jargão de IA** — "insights", "powered by AI", "análise inteligente". O V3 precisa que o produto pareça *trabalho feito*, não *texto gerado por IA* — que é o risco de commodity.
- **Promessa de conversão em qualquer lugar.** `[V3]`
- **Empolgação.** Nada de "Ótima notícia!". O usuário está a caminho de uma reunião.
- **Afirmação sem tag.** Toda frase do brief pertence a um dos três estados. Se não pertence, não entra.

---

# 7 · Perguntas de validação para as entrevistas

> **Disciplina do roteiro existente:** perguntar sobre o passado, não sobre o futuro; **não mencionar o Antessala até o fim**. Tudo aqui entra **depois** das perguntas comportamentais da Trilha A — nunca antes.

## 7.1 Antes de mostrar qualquer coisa — canal (comportamento, não preferência)

`[E5]`
1. "Nos 10 minutos antes da sua última reunião importante, **qual foi o último app que você abriu**?" *(mede o canal real; não pergunta qual ele preferiria)*
2. "Como você entra numa call — pelo convite do calendário, por link no WhatsApp, por e-mail?" *(valida a Camada 1 da recomendação §3.2)*
3. "Quantos e-mails **não lidos** você tem agora?" *(calibra a chance de leitura da Camada 2 — pergunta que o entrevistado responde olhando a tela)*
4. "Você usa WhatsApp de trabalho no seu número pessoal?" *(a resposta define se WhatsApp é canal ou é problema — §3.1)*
5. "Sua empresa usa Slack ou Teams? Você abriria lá?" *(testa a hipótese `[E5-H]` que mantém Slack fora do MVP)*
6. "Você já mandou print de alguma coisa no grupo do time hoje?" *(testa o comportamento de compartilhamento que sustenta P13)*

## 7.2 Mostrar o brief — teste de 5 segundos

Entregar o exemplo §2.5 **impresso ou em tela de celular**. Mostrar por 5 segundos. Tirar. Perguntar:
7. "O que você lembra?" *(valida P2 e a hierarquia; se ninguém lembrar do Why now, o topo está errado)*
8. "Se você tivesse **30 segundos** antes de entrar, qual bloco leria?" *(valida a ordem — e a troca 6↔7)*
9. "Onde seu olho foi primeiro?"

## 7.3 Com o brief na mão — conteúdo e confiança

10. "Lê em voz alta o que você **já sabia**." *(mede novidade real; risco de commodity)*
11. "Tem alguma coisa aqui que você **não acreditaria**? Por quê?" *(mede confiança; se for a hipótese, a justificativa está fraca — P4)*
12. "O que significa isto?" — apontando para `≈ HIPÓTESE` **sem explicar**. *(as tags só funcionam se forem autoexplicativas)*
13. "Você clicaria em alguma fonte? Em qual?" *(valida P3 — se ninguém clica, a fonte é ritual, não recurso)*
14. "Este bloco diz que não sabemos quem assina. Isso te incomoda ou te ajuda?" *(o teste direto de P5 — desconhecido como pergunta)*
15. "Falta alguma coisa que você teria procurado?" *(gaps de cobertura)*
16. "Tem coisa demais aqui?" *(P9 — orçamento de leitura)*
17. "Está escrito na sua língua? O que você diria diferente?" *(P7 — coleta vocabulário nativo, que é justamente o que a pesquisa pública não conseguiu obter)*

## 7.4 Estado de primeira conversa

Mostrar a versão §4.2 (sem histórico interno):
18. "Este é o brief de um cliente com quem você nunca falou. Serve para alguma coisa?" *(testa o diferencial de §4.2 diretamente com o usuário)*
19. "Você faria essas perguntas? Reescreveria alguma?"

## 7.5 Confiança, acesso e o guardião

20. "Para isso funcionar, ele precisa ler sua agenda. **Qual sua primeira preocupação?**" *(o roteiro já ensina: preocupação, não interesse)*
21. "**Quem** na sua empresa precisaria aprovar isso?" *(a pergunta que fecha o "guardião ainda não mapeado" do V3 — é a lacuna mais barata de resolver e ninguém resolveu)*
22. "Já negaram acesso a alguma ferramenta pra você? O que aconteceu?" *(comportamento passado, não hipótese)*
23. "Se um fato aqui estivesse **errado**, o que você faria?" *(valida §5.3; observar se procura um botão — e onde)*

## 7.6 Para o comprador econômico (Trilha B)

24. "Se seus vendedores recebessem isto antes de cada reunião, **o que você iria querer ver**?" *(cuidado: pergunta hipotética — usar só para detectar se ele pede um painel de time, o que muda a superfície)*
25. "Você ia querer receber uma cópia dos briefs do time?" *(testa se existe uma segunda superfície, de gestor, que este documento não cobre)*
26. "Qual número você olha toda segunda?" *(já no roteiro — aqui serve para escolher as palavras do onboarding, P7)*

## 7.7 O que NÃO perguntar

- "Você usaria?" / "Pagaria por isso?" — o roteiro já bane, com razão.
- "Prefere e-mail ou WhatsApp?" — preferência declarada não prevê comportamento. As perguntas 1–5 respondem isso melhor.
- "Gostou do layout?" — o entrevistado passa a te agradar. Perguntar o que ele **lembra** e o que ele **faria**, nunca se gostou.

---

# 8 · Resumo das decisões e o que cada uma custa

| Item | Marca | Reversível? |
|---|---|---|
| 8 blocos, conteúdo e nomes | `[V3]` | não é decisão minha |
| Três tags de confiança e suas regras | `[V3]` | não é decisão minha |
| Troca de ordem 6 ↔ 7 (Perguntas antes de Riscos) | `[E5]` | sim, custo zero |
| Prévia de 2 linhas (Why now + Resultado esperado) | `[E5]` | sim |
| Canal 1: evento-espelho privado no calendário | `[E5]` | sim |
| Canal 2: e-mail com o corpo completo | `[E5]` | sim |
| Nunca escrever em evento com convidado externo | `[E5]` | **não — é regra de segurança** |
| WhatsApp e Slack fora do MVP de 10 h | `[E5]` | sim, após entrevistas |
| Calendário como único passo obrigatório | `[E5]` | sim |
| CRM e e-mail só depois do primeiro brief | `[E5]` | sim |
| Estado "1ª conversa" como selo, não como erro | `[E5]` | sim |
| Útil/Não ajudou + Corrigir fato no MVP | `[E5]` | sim |
| Nenhum placar de causalidade na interface | `[V3]` | **não** |
| Tag = palavra + símbolo, cor só reforça | `[E5]` | sim |

## Lacunas que este documento não resolve

1. **Superfície do gestor.** O V3 separa usuário e comprador econômico, mas nada aqui define o que o **dono/Head de Vendas** vê. Ele é quem paga. Perguntas 24–25 abrem isso; o desenho não existe.
2. **Redação jurídica da base legal LGPD.** O texto do guardião (§4.3) é rascunho de UX, não peça jurídica.
3. **Frequência.** Um brief por reunião pode virar ruído em quem tem 6 reuniões/dia. Não há regra de agregação proposta.
4. **Marca visual.** Cor, tipografia e identidade não estão definidos — este documento define estrutura, hierarquia e comportamento, que precedem isso.
5. **Verbatim do ICP continua em 0%.** Todo `[E5-H]` deste documento cai ou sobe nas 5 entrevistas do roteiro. Nenhum deles deve virar código antes disso.

---

*Documento de trabalho · Uma (@ux-design-expert) · 29 ago 2026 · Antessala V3*
