# Três simulações da jornada · Antessala (29 ago 2026)

> ⚠️ **SIMULAÇÃO.** Tudo abaixo é **fictício e declarado**: empresa cliente, vendedores, prospects, pessoas, datas, notícias, números e fontes foram inventados para testar a jornada **como decidida pela fundadora em 29/08/2026**. Nenhuma linha é resultado real do produto, nenhuma pode ir a slide como se fosse. O que a simulação produz de verdadeiro são as **perguntas que ela faz a jornada** — listadas ao final.
>
> **Decisões aplicadas (índice `jornada-do-cliente.md`):** D1 evento-espelho privado + e-mail, **entrega no dia anterior** · D2 gestor preenche ≤ 6 campos, vendedor só conecta o calendário · D3 feedback em 2 momentos + "não li" · D4 Perguntas críticas antes de Riscos · item 5 correção **por fato** · itens convergentes 3 (só calendário), 4 (1ª conversa = selo), 7 (LGPD escopo mínimo + tela NUNCA), 9 (gestor: relatório mensal por e-mail, sem win rate) — **em teste**.
>
> **Regra de rigor mantida:** em nenhuma simulação o produto afirma, sugere ou mede que aumentou conversão. Onde aparece "avançou", é registro descritivo do vendedor.

**Cenário-base fictício.** *Vetor Industrial Ltda.* — PME de Joinville que vende contratos de manutenção preditiva para indústrias; 8 vendedores; ticket médio R$ 48 mil/ano; CRM: RD Station CRM Basic (R$73/usuário — preço real, ENTREGA 2); sem SDR, sem sales intelligence. Gestora comercial: **Paula**. Vendedor: **Diego**. Guardião de acesso: ninguém formal — o Google Workspace é administrado pelo **Fábio**, contador terceirizado que criou as contas.

---

## SIMULAÇÃO 1 · Onboarding pelo gestor e o primeiro brief de primeira conversa

*Testa: D1, D2, item 3 (só calendário), item 4 (1ª conversa), item 7 (tela NUNCA).*

### Terça, 26/08 — Paula contrata (Etapa 0–1)

**O que Paula fornece (D2 — os 6 campos):**

| # | Campo | Resposta da Paula (fictícia) | Onde a IA usa |
|---|---|---|---|
| 1 | O que a empresa vende | "Contratos de manutenção preditiva para linhas industriais" | *Why now* e *Resultado esperado* — o avanço a buscar é sempre relativo ao que se vende |
| 2 | Para quem vende | "Gerentes de manutenção e diretores industriais, fábricas de 100 a 1.000 funcionários" | Triagem: convidado com cargo compatível pesa mais · *Quem está na mesa*: papel provável |
| 3 | Ticket médio | "R$ 48 mil/ano" | *Why now*: calibra o peso da reunião · relatório mensal |
| 4 | O que conta como reunião comercial | "Qualquer reunião com gente de fora que não seja fornecedor nosso" | Triagem: domínio externo **e** exclusão da lista de fornecedores |
| 5 | Domínios de fornecedores/parceiros a ignorar | "sensortech.com.br, contabil-fabio.com.br" | Triagem: anti-ruído |
| 6 | Time | 8 nomes + e-mails @vetorindustrial.com.br | Convites · domínio interno |

Tempo: 2 min 40 s. **Observação da simulação:** o campo 4 foi respondido de forma vaga ("gente de fora") — a triagem vai depender do campo 5 para não gerar brief para a reunião com o contador. **O formulário precisa de exemplo ao lado de cada campo**, senão o gestor responde genérico.

**O que Paula vê depois:** lista dos 8 vendedores com status "convidado". Nada mais. Não há brief para ela.

### Terça, 26/08, 17h10 — Diego conecta (Etapa 2)

Diego recebe o e-mail-convite, toca em "Conectar minha agenda", escolhe Google e vê a tela de permissões **já ajustada à D1** (escrita):

```
O que o Antessala vai fazer
LÊ      ✓ título, horário e participantes dos seus eventos futuros
ESCREVE ✓ cria um evento privado, só seu, com o brief — no dia anterior à reunião
NUNCA   ✗ altera, cancela ou responde seus eventos
        ✗ escreve em evento com convidado externo
        ✗ envia nada para o cliente
        ✗ lê eventos passados além de 90 dias
```

**Observação da simulação:** a D1 obriga o escopo de **escrita** no OAuth do Google (`calendar.events`), que na tela nativa do Google aparece como *"Ver, editar, compartilhar e excluir permanentemente todas as agendas que você pode acessar"*. **Essa frase é mais assustadora do que a nossa tela NUNCA** — e aparece *depois* dela. Isso não invalida a D1, mas exige que a tela NUNCA **avise antes**: "na próxima tela o Google vai pedir permissão de edição — nós só criamos eventos privados seus". Sem esse aviso, o vendedor desiste no consentimento do Google, não no nosso.

Tela 3 (triagem): o sistema encontrou 5 eventos nos próximos 7 dias e pré-marcou 3:

```
[x] qui 28/08 10h00 · Alvorada Alimentos (fictícia)   — domínio externo
[x] sex 29/08 15h00 · Metalúrgica Pinheiro (fictícia)  — domínio externo
[ ] sex 29/08 09h00 · Reunião semanal de vendas       — interno
[ ] seg 01/09 14h00 · Fábio (contabilidade)           — domínio na lista de fornecedores (campo 5)
[x] ter 02/09 11h00 · "Visita" (sem convidado)        — ???
```

**Observação da simulação:** o evento "Visita" sem convidado externo foi pré-marcado por heurística fraca (título + horário comercial) e **está errado** — é visita ao dentista. Diego desmarca. Isso mostra que a triagem por domínio externo é sólida e a triagem por título é ruído: **regra a decidir — evento sem nenhum convidado externo nunca gera brief, mesmo que o título pareça comercial.**

### Quarta, 27/08, 18h00 — o brief chega (D1: dia anterior)

**Passos 1–7 executados sozinhos**, sem Diego saber. Fontes consultadas (fictícias): `alvoradaalimentos.com.br` (site institucional) · consulta pública de CNPJ · 2 notícias regionais · perfis profissionais públicos dos 2 convidados · **contexto interno: zero** — nenhum evento anterior com esse domínio no calendário de Diego; sem CRM conectado (item 3).

**O que Diego vê na agenda** (camada 1 — evento-espelho privado, criado às 18h00 de quarta):

```
┌─ Google Agenda · qua 27/08 ──────────────────────────────┐
│ 18:00  Antessala · Alvorada Alimentos — amanhã 10h        │  ← evento privado, sem convidados
│        Avanço a buscar: sair com o volume de linhas e     │
│        o nome de quem assina. 1ª conversa.                │
│        Brief completo: [link não indexado]                │
└───────────────────────────────────────────────────────────┘
```

**O que Diego vê no e-mail** (camada 2), assunto: *"Alvorada amanhã 10h · 1ª conversa · pediram reunião após parar a linha 3"*

```
ANTESSALA · Amanhã, qui 28/08, 10h00 · 45 min · Google Meet ↗
ALVORADA ALIMENTOS (fictícia) — 1ª CONVERSA · nenhum histórico interno
Este brief é 100% pesquisa pública + o que o convite mostra.

▍POR QUE AGORA
Pediram a reunião 4 dias depois de uma parada não programada na linha 3
noticiada no jornal local. Ticket de referência da Vetor: R$ 48 mil/ano.
✓ CONFIRMADO  Jornal Regional (fictício), 23/08 ↗
≈ HIPÓTESE  a parada acelerou a decisão · porque o pedido de reunião veio
  por formulário 4 dias depois, sem contato anterior

▍O QUE SABEMOS
• Indústria de alimentos, ~420 funcionários, 2 plantas  ✓ CONFIRMADO  CNPJ público + site ↗
• Nenhum contato anterior da Vetor com esta conta  ? DESCONHECIDO → Q1

▍O QUE MUDOU
• Parada na linha 3 em 22/08  ✓ CONFIRMADO  Jornal Regional ↗
• Novo gerente de manutenção desde jun/26  ✓ CONFIRMADO  perfil público ↗

▍QUEM ESTÁ NA MESA
Marcelo T. · Gerente de Manutenção  ≈ HIPÓTESE usuário e iniciador · porque
  abriu o contato e está há 2 meses no cargo — tende a querer marcar posição
Lúcia F. · Compras  ≈ HIPÓTESE avaliadora de custo · porque Compras num 1º
  contato costuma indicar comparação de fornecedores
? DESCONHECIDO  ninguém da Diretoria Industrial no convite → R1, Q3

▍O QUE FALTA
? Quantas linhas e qual o custo/hora de parada  ? Quem assina contrato anual
? Se já têm manutenção preditiva com outro fornecedor  ? Prazo de decisão

▍PERGUNTAS CRÍTICAS                              ← (D4: antes de Riscos)
Q1 "Como vocês cuidam da manutenção hoje — time interno, contrato, os dois?"
Q2 "O que a parada da linha 3 custou, em horas ou em produção?"
Q3 "Além de vocês dois, quem precisa dizer sim para um contrato anual?"
Q4 "O que faria vocês manterem exatamente o que têm hoje?"

▍RISCOS
R1 Diretoria fora da mesa — decisão não fecha nesta conversa
R2 ≈ HIPÓTESE  comparação de fornecedores em curso · porque Compras está no convite
R3 ? DESCONHECIDO  se a parada já foi resolvida internamente → Q2

▍RESULTADO ESPERADO
Sair com o número de linhas, o custo da parada e o nome de quem assina.
Melhor desfecho: visita técnica à planta agendada com data.

9 fatos · 6 com fonte · 4 hipóteses justificadas · 5 desconhecidos, todos virados em pergunta
[ Útil ]  [ Não ajudou ]  [ Não li ]  ·  Algo errado aqui? Corrigir ↗
```

~310 palavras. Diego lê na quarta à noite, em casa, no celular. Quinta de manhã, no carro, abre o evento-espelho e relê só *Perguntas críticas* e *Resultado esperado*.

**O que a Simulação 1 mostra sobre os convergentes:**
- **Item 3 (só calendário) se sustenta** — o brief saiu útil sem CRM. Mas repare: os 6 campos da Paula (D2) fizeram trabalho que o CRM faria (ticket, público-alvo). **D2 e item 3 se apoiam mutuamente**: sem o formulário do gestor, o brief de 1ª conversa seria mais raso.
- **Item 4 (1ª conversa como selo) se sustenta** — o selo está no assunto do e-mail, no evento e no topo do brief; *O que falta* tem 4 itens e *Perguntas* tem 4. Não pareceu vazio. **Condição:** existia notícia pública recente. Ver Simulação 2 para o caso sem notícia.
- **Item 7 (tela NUNCA) se sustenta, com ajuste** — precisa avisar sobre a tela de consentimento do Google.

---

## SIMULAÇÃO 2 · Segunda reunião com a mesma conta, um fato errado e o feedback

*Testa: D1 (dia anterior — caso de reunião marcada em cima da hora), D3, item 5 (correção por fato), o que vira "contexto interno" sem CRM.*

### Quinta, 11/09 — o histórico que o calendário carrega

Diego teve a 1ª reunião com a Alvorada em 28/08. Duas horas depois, respondeu ao "Como foi?": **[Avançou]** + texto livre: *"Quem assina é o Rogério, diretor industrial. Eles têm 5 linhas. A parada custou 2 turnos."* Em 05/09 marcou a 2ª reunião — convite com Marcelo, Lúcia **e Rogério**.

**Contexto interno agora existe — sem CRM.** Vem de três lugares: o evento anterior no calendário (data, participantes), o brief anterior e **a resposta de feedback do Diego** (item 5 + D3 alimentando a conta). O brief de quarta 10/09 às 18h abre assim:

```
ALVORADA ALIMENTOS (fictícia) — 2ª CONVERSA · histórico interno: 1 reunião (28/08)

▍POR QUE AGORA
Rogério (diretor industrial, quem assina) entrou no convite. Na 1ª conversa,
Diego registrou 5 linhas e parada de 2 turnos.
✓ CONFIRMADO  convite de 05/09 ↗  ·  ✓ CONFIRMADO  registrado por Diego em 28/08 ↗

▍O QUE SABEMOS
• 5 linhas; parada de 22/08 custou 2 turnos  ✓ CONFIRMADO  registrado por Diego, 28/08
• Quem assina: Rogério M., Diretor Industrial  ✓ CONFIRMADO  registrado por Diego, 28/08
• ~120 funcionários  ✓ CONFIRMADO  base pública de empresas (fictícia), 09/09
  ...
```

### O fato errado (item 5 — correção por fato)

Diego sabe que a planta tem ~420 funcionários (estava certo no 1º brief); o 2º brief trouxe **"~120"** de outra fonte pública. Ele toca em *Algo errado aqui?* → página do brief com `✗` por fato → toca no `✗` de "~120 funcionários":

```
✗ "~120 funcionários"   CONFIRMADO · base pública de empresas, 09/09
  O certo é: [ ~420, duas plantas — a base pegou só a matriz ]
  [ Salvar ]  [ Só remover isso ]
```

**O que o sistema faz com isso — regra que a simulação obriga a decidir:**
- o fato passa a **"~420 funcionários · ✓ CONFIRMADO · corrigido por Diego em 10/09"** nos briefs seguintes;
- a fonte pública que deu 120 é **rebaixada** para essa conta (conflito registrado, não apagado);
- **a correção não se propaga para outras contas** — é conhecimento do Diego sobre a Alvorada, não regra geral.

**Observação da simulação:** aqui aparece a primeira tensão real da regra de confiança do V3. "Fatos precisam de fonte" — e a fonte agora é **uma pessoa**. É legítimo (é o `[E1]` da própria escala do dossiê), mas a interface precisa distinguir visualmente *fonte pública* de *registrado por vendedor*, senão o gestor lê "CONFIRMADO" e supõe que foi pesquisado. Proposta: prefixo **"registrado por"** sempre visível, como no exemplo.

### O caso que a D1 não cobre: reunião marcada em cima da hora

Sexta 12/09, 08h40: Marcelo manda WhatsApp para Diego — *"consegue às 11h hoje? Rogério só tem hoje"*. Diego cria o evento às 08h45. **"Dia anterior" já passou.**

Três comportamentos possíveis — **a fundadora precisa escolher um**:

| Opção | O que acontece | Custo |
|---|---|---|
| **A · Entrega imediata com selo "brief de última hora"** | Evento-espelho + e-mail às 08h52, selo no topo: *"reunião marcada há 7 min — brief feito agora, sem revisão de véspera"* | Pesquisa externa pode sair mais rasa (menos tempo); mas é exatamente o momento em que o vendedor mais precisa |
| **B · Não entrega** (regra "dia anterior" é estrita) | Diego entra sem brief | Produto falha justamente na reunião urgente |
| **C · Entrega imediata, sem selo** | Igual a A, sem avisar | Vendedor não sabe que o brief teve 5 minutos de pesquisa |

**Recomendação do orquestrador `[E5]`: A.** A regra "dia anterior" é o **padrão**, não o teto: *"sempre no dia anterior; se a reunião for criada depois disso, o quanto antes, com selo"*.

Segunda variante, mais comum: **reunião de segunda-feira 09h.** "Dia anterior" = domingo. Enviar no domingo às 18h invade o fim de semana do vendedor e provavelmente não é lido; enviar sexta às 18h é "dois dias antes". **Decisão a tomar:** dia anterior **útil** (sexta) ou **corrido** (domingo)? A simulação sugere **dia útil anterior, no fim da tarde (18h)** — e o horário 18h também é decisão em aberto (a UX propôs 60 min antes; a fundadora mudou para véspera; a hora da véspera ninguém definiu).

### O feedback (D3 — dois momentos + "não li")

- Quinta 10/09, 18h: brief chega. Diego não abre.
- Sexta 11h: reunião acontece — Diego entrou sem ler.
- Sexta 13h (2 h após): *"Como foi a Alvorada? Seu brief apontava: sair com data de visita técnica"* → **[Não li]** aparece aqui também? **Não** — na D3 o "não li" está no rodapé do brief, e Diego não abriu o brief. **Lacuna:** o sistema só descobre que Diego não leu se ele responder à 2ª pergunta. **Proposta:** a pergunta das 2 h ganha uma 4ª opção discreta, *"não li o brief"*, **só quando o link do brief não foi aberto** (o sistema sabe). Diego toca em [Avançou] e escreve: *"Visita técnica dia 19. Rogério quer proposta em 3 cenários."* → vira contexto interno da conta.

**O que a Simulação 2 mostra:**
- **Item 5 (por fato) se sustenta e revela valor além da correção**: a resposta de feedback é a forma mais barata de contexto interno que existe — **é o "CRM" do MVP sem CRM**. Isso reforça o item 3.
- **D1 precisa de duas regras de fallback** (reunião de última hora; véspera em fim de semana) e de um horário.
- **D3 precisa do "não li" nos dois momentos**, condicionado ao link não aberto.

---

## SIMULAÇÃO 3 · Trinta dias depois: a gestora, o guardião e o relatório mensal

*Testa: item 7 (LGPD e guardião), item 9 (relatório mensal por e-mail, sem win rate), sinais de churn.*

### O guardião aparece depois do "sim" (Etapa 2, lado do gestor)

Dia 02/09, 3 dos 8 vendedores ainda não conectaram. Um deles, **Renan**, respondeu ao convite: *"o Fábio disse que não é pra autorizar app nenhum no Google da empresa sem ele ver"*. Fábio — contador, administrador do Workspace — é o guardião que o `README.md` diz não estar mapeado. **Na simulação, ele existe e é externo à empresa.**

Paula usa o texto pronto da UX (§4.3) e manda para Fábio. Resposta dele, fictícia: *"Só agenda? Sem e-mail? Então libera, mas quero que dê pra desligar."* — o item 3 (só calendário) **é o que destrava o guardião**. Se o MVP pedisse e-mail, essa conversa teria outro final.

**Observação da simulação:** a permissão de **escrita** da D1 fez Fábio perguntar *"editar agenda pra quê?"*. A resposta — *"cria um evento privado do próprio vendedor, nunca mexe em evento com gente de fora"* — resolveu, mas **precisa estar no texto do guardião**, que hoje diz só "lê". **Ajuste obrigatório no texto da UX §4.3.**

### O relatório mensal (item 9) — sexta 26/09, 08h00, e-mail para Paula

Assunto: *"Antessala · setembro · 31 briefs, 6 de 8 vendedores ativos"*

```
VETOR INDUSTRIAL · setembro/2026 · relatório do Antessala

ATIVAÇÃO
6 de 8 vendedores conectaram a agenda (2 pendentes: Renan, Carla)
31 reuniões comerciais detectadas · 31 briefs entregues automaticamente (100%)
  — 4 de última hora (reunião criada no mesmo dia)

QUALIDADE
% de fatos com fonte: 71% (média por brief: 9 fatos, 6,4 com fonte)
Correções feitas pelos vendedores: 5 (em 4 briefs) — todas viraram contexto da conta
Briefs de 1ª conversa: 19 de 31 (61%)

USO
Lidos antes da reunião: 24 (77%)  ·  "Não li": 7
Considerados úteis: 20 · Não ajudou: 3 · sem resposta: 8
Gaps identificados antes da reunião: 112 desconhecidos virados em pergunta

O QUE ACONTECEU DEPOIS (registro dos vendedores, descritivo)
Avançou: 14 · Ficou igual: 7 · Não avançou: 3 · sem resposta: 7
⚠ Isto não mede efeito do brief. É o que os vendedores registraram.

TEMPO (autorrelato, 1x por vendedor)
"Quanto tempo você gastaria nisso?" — mediana: 25 min por reunião
→ 31 briefs × 25 min ≈ 13 h no mês, se a premissa valer

PARA VOCÊ DECIDIR
• 2 vendedores não conectaram — quer que eu reenvie o convite?
• 7 "não li": 5 são de reuniões de última hora — o brief chegou tarde demais
```

**O que Paula NÃO vê — e a simulação obriga a decidir:**
- **Nada por vendedor além de ativação.** O relatório acima é agregado. Se mostrar "Diego: 9 úteis · Renan: 0 lidos", o produto vira **ferramenta de controle**, e o vendedor que hoje concede o calendário de boa vontade passa a ver o Antessala como vigilância. **Decisão para a fundadora: relatório do gestor é agregado (recomendação `[E5]`) ou por vendedor?** O V3 diz que o champion quer "reduzir variação entre vendedores" — o que puxa para "por vendedor". A tensão é real.
- **Nenhum brief individual.** Paula não recebe cópia dos briefs (lacuna que a UX declarou nas perguntas 24–25). Se ela pedir — e a simulação sugere que ela vai pedir, porque quer ver "o que o Diego levou pra Alvorada" — é uma segunda superfície a desenhar.
- **Nenhum número de conversão.** "14 avançaram" está lá como descrição, com o aviso. Está de acordo com o V3 §10.

### Sinais de churn (Etapa 7)

Aos 30 dias: 2 nunca conectaram; 1 (Carla) conectou e desconectou na semana 2 — sem responder nada. **O sistema não sabe por quê.** Proposta `[E5]`: ao desconectar, uma única pergunta opcional, *"o que fez você desligar?"* — é o único momento em que o motivo de churn está fresco.

**O que a Simulação 3 mostra:**
- **Item 7 se sustenta e ganha corpo**: o guardião existe, é externo, e "só calendário" é o argumento que o convence. O texto do guardião precisa incluir a permissão de escrita.
- **Item 9 se sustenta**, mas expõe **duas decisões**: agregado vs. por vendedor; e se o gestor vê briefs individuais.
- **"Não li" (D3) tem valor diagnóstico real**: 5 dos 7 "não li" eram de última hora — dado que só existe porque o "não li" é uma opção separada de "não ajudou".

---

## O que as três simulações revelaram

### Os convergentes se sustentam? **Sim, os quatro — com condições.**

| Item | Veredito | Condição que a simulação expôs |
|---|---|---|
| **3 · Só calendário** | ✅ Sustenta nas 3 | Depende dos 6 campos do gestor (D2) para o brief de 1ª conversa não sair raso, e do feedback (D3 + item 5) para construir contexto interno sem CRM. **Os três formam um sistema.** É também o que destrava o guardião |
| **4 · 1ª conversa = selo** | ✅ Sustenta (Sim. 1) | Quando há notícia pública recente. **Caso não testado:** empresa sem nenhuma notícia, site pobre — o brief de 1ª conversa vira só CNPJ + perguntas genéricas. **Testar na demo com uma empresa "silenciosa".** |
| **7 · LGPD escopo mínimo + tela NUNCA** | ✅ Sustenta (Sim. 1 e 3) | A tela NUNCA precisa **avisar sobre o consentimento do Google** (que assusta mais) e o texto do guardião precisa **incluir a escrita** da D1 |
| **9 · Relatório mensal por e-mail** | ✅ Sustenta (Sim. 3) | Expõe a decisão **agregado vs. por vendedor** — que é a fronteira entre readiness e vigilância |

### Regras que ninguém tinha decidido e que as simulações obrigam a decidir

| # | Regra a decidir | Onde apareceu | Recomendação `[E5]` |
|---|---|---|---|
| R1 | **Reunião criada depois da véspera** (última hora) | Sim. 2 | Entrega imediata **com selo "última hora"** |
| R2 | **Véspera cai em fim de semana** | Sim. 2 | Dia **útil** anterior |
| R3 | **Horário do disparo na véspera** | Sim. 1 e 2 | 18h (fim do dia útil) — a validar na Trilha A: "quando você preparou?" |
| R4 | **Evento sem nenhum convidado externo** | Sim. 1 | Nunca gera brief, mesmo com título comercial |
| R5 | **Fato corrigido pelo vendedor × fonte pública** | Sim. 2 | Correção vence, marcada "registrado por {nome}, {data}"; fonte pública rebaixada só para aquela conta; sem propagação |
| R6 | **"Não li" na pergunta das 2 h** | Sim. 2 | Aparece só quando o link do brief não foi aberto |
| R7 | **Relatório do gestor: agregado ou por vendedor** | Sim. 3 | Agregado no MVP; por vendedor só com opt-in visível ao próprio vendedor |
| R8 | **Gestor vê briefs individuais?** | Sim. 3 | Não no MVP — é a segunda superfície que a UX não desenhou |
| R9 | **Aviso pré-consentimento do Google** (escopo de escrita) | Sim. 1 | Uma linha na tela NUNCA: "na próxima tela o Google vai pedir edição — só criamos eventos privados seus" |
| R10 | **Pergunta única ao desconectar** | Sim. 3 | "O que fez você desligar?" — opcional |

### Correções aos documentos dos especialistas que as suas decisões já exigem

| Documento | O que muda |
|---|---|
| `jornada-superficie-ux.md` | "60 min antes" → **"dia útil anterior, 18h"** em §2.2, §3.2, Tela 2, Tela 4, Tela 5 · texto do guardião (§4.3) ganha a linha de escrita · ordem 6↔7 passa de proposta a decidida · correção por fato (§5.3) passa de proposta a decidida |
| `jornada-produto-pm.md` | Decisão 4.1 (canal) → substituída pela D1 · 4.6 (feedback) → substituída pela D3 · Etapa 5 "véspera à noite **e** 30 min antes" → só véspera (R1 para exceções) |
| `jornada-do-cliente.md` | Registrar itens 3, 4, 5, 7, 9 como decididos + as regras R1–R10 como pendentes |
| V3 (cânone) | Na próxima revisão: ordem 6↔7 (D4) · guardião e LGPD no §12 |
