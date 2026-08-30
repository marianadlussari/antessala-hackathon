# Jornada do cliente dentro do Antessala · Índice de decisões (29 ago 2026)

> **Status: DECIDIDO em 29/08/2026** pela fundadora, item a item, após 3 simulações (`simulacoes-jornada.md`). Ainda **não promovido ao V3** — o cânone continua sendo `fontes/antessala-documento-consolidado-v3.html` até a próxima revisão dele (ver §5). Os documentos de PM e UX permanecem como memória da proposta; onde divergem das decisões, as decisões prevalecem.
>
> **Origem:** a pergunta *"qual a jornada do cliente dentro da ferramenta? O que ele vê? Quais informações fornece? Quais informações a IA coleta sozinha e como isso aparece pro usuário?"* — e a verificação na fonte de que o V3 define o **motor**, não a **jornada**.
>
> **Três documentos de apoio:**
> - `simulacoes-jornada.md` — 3 simulações (fictícias, declaradas) que testaram as decisões e produziram as regras R1–R10.
> - `jornada-produto-pm.md` — @pm (Morgan): atores, jornada ponta a ponta em 8 etapas, fronteira do MVP de 10 h, 7 pontos de decisão, perguntas para as entrevistas, riscos.
> - `jornada-superficie-ux.md` — @ux (Uma): 13 princípios de superfície, anatomia e wireframe do brief (com exemplo 100% fictício), comparativo de canais, telas de onboarding, interações pós-entrega, acessibilidade e tom, 26 perguntas de validação.
>
> **Convenção de origem, nos dois:** `[V3]` = decidido no V3 (seção citada) · `[E5]` = proposta nova, hipótese · `[E5-H]` (UX) = proposta que depende de hipótese sobre o ICP ainda não testada.

---

## 1 · O que o V3 já decide sobre a jornada (verificado na fonte)

| Elemento | Texto no V3 | Onde |
|---|---|---|
| Gatilho | "Reunião comercial identificada automaticamente no calendário" | Registro de decisão atual |
| Entrada | "Calendário + contexto interno + dados públicos" | Registro de decisão atual |
| Saída | "Readiness brief entregue automaticamente antes da reunião" | Registro de decisão atual |
| Fluxo | 8 passos: Gatilho · Identificação · Contexto interno · Pesquisa externa · Consolidação · Análise · Objetivo · Entrega | §8 Fluxo |
| Conteúdo do brief | 8 blocos: Why now · O que sabemos · O que mudou · Quem está na mesa · O que falta · Riscos · Perguntas críticas · Resultado esperado | §8 Saída |
| Confiança | CONFIRMADO / HIPÓTESE / DESCONHECIDO — "Fatos precisam de fonte. Hipóteses precisam de justificativa. Desconhecidos viram perguntas de discovery." | §8 Regra de confiança |
| Fronteira | 7 atividades da máquina; 3 do humano (confirmar dor/orçamento/urgência/política · negociar · decidir) | §8 Fronteira humano × máquina |
| Não construir agora | "Chatbot, AI SDR completo, CRM, forecast ou plataforma comercial generalista" | Registro de decisão atual |
| Compra | "Não depender de compra individual do closer" | §11 |

**O que o V3 NÃO define (e os dois documentos propõem):** provedor e escopo de calendário · canal e momento de entrega · superfície e formato do brief · onboarding (quem, o que fornece) · fontes concretas da pesquisa externa · triagem de "reunião de receita" · correção e feedback · pós-reunião · guardião de acesso (`README.md`: "não está no documento") · LGPD.

---

## 2 · Decisões a tomar — recomendação de cada especialista

| # | Decisão | @pm (Morgan) | @ux (Uma) | Convergem? |
|---|---|---|---|---|
| 1 | **Canal de entrega** | E-mail como canal primário + link para página web read-only. WhatsApp na visão (API oficial não cabe em 10 h) | **Duas camadas:** (1) evento-espelho **privado** no calendário do vendedor, 60 min antes — mesma permissão do gatilho, zero onboarding novo; (2) e-mail com o corpo completo no mesmo instante. Página por link não indexado só se sobrar tempo | **Parcial.** Ambos usam e-mail; a UX acrescenta o evento-espelho como camada 1. **Regra de segurança da UX (não negociável): nunca escrever em evento com convidado externo** |
| 2 | **Onboarding** | Híbrido: gestor contrata e configura a empresa (≤ 6 campos); cada vendedor concede o próprio calendário via OAuth | Calendário é o **único** passo obrigatório; nada de formulário sobre a empresa — "não pedir o que está no convite"; CRM/e-mail só depois do primeiro brief, com "Agora não" | **Divergem** no formulário do gestor: PM pede ~6 campos (o que vende, para quem, ticket, tipos de reunião); UX pede zero campos e corrige por heurística (tela 3: "desmarque o que não for comercial") |
| 3 | **Integrações do MVP** | **Só calendário** (Google). Estratégico: é a única configuração que demonstra o caso que AmpUp/Parsley/EchoIQ/SiftHub declaradamente não cobrem | Idem — "calendário como único passo obrigatório" | **Sim** |
| 4 | **Sem contexto interno (1ª conversa)** | DESCONHECIDO vira pergunta de discovery (regra do V3); o brief muda de **peso**, não de estrutura | Idem — "1ª conversa" é **selo**, não erro; *O que falta* expande, *Perguntas críticas* ganham destaque; nunca escrever "sem dados" | **Sim** |
| 5 | **Edição/correção do brief** | Read-only + "não bate" em 1 clique no brief inteiro; correção por fato depois | Read-only + "Algo errado aqui?" → página com `✗` por fato + "o certo é…" (versão mínima cabe nas 10 h) | **Parcial** — divergem na granularidade no MVP (brief inteiro vs. por fato) |
| 6 | **Feedback pós-reunião** | 1 pergunta ~1 h após: "ajudou? sim / não / **não li**" — "não li" separa canal errado de conteúdo ruim | Dois momentos: "Útil / Não ajudou" no rodapé do brief (imediato) + "Como foi?" 2 h após com "Avançou / Ficou igual / Não avançou", o brief se cobrando pelo próprio *Resultado esperado* | **Divergem** — PM quer 1 toque com opção "não li"; UX quer 2 toques em momentos distintos, sem "não li" |
| 7 | **LGPD / dados** | Escopo mínimo; fonte-por-fato como trilha de auditoria; direito de exclusão; retenção curta. **Precisa de revisão jurídica** | Tela "O que o Antessala vai fazer" com coluna **NUNCA** visível antes do clique; texto pronto para o guardião; base legal marcada `[E5-H]` | **Sim** (a UX materializa o que o PM define) |
| 8 | **Ordem dos 8 blocos** | Mantém a ordem do V3 | Troca **6 ↔ 7** (Perguntas críticas antes de Riscos): "O que falta" e "Perguntas" são o mesmo conteúdo em dois estados; reversível a custo zero | **Divergem** — mudar ordem do V3 é decisão da fundadora |
| 9 | **Superfície do gestor** | Relatório **mensal por e-mail**, nunca dashboard; sem win rate como resultado | Declarada como **lacuna** — "nada aqui define o que o dono/Head vê"; perguntas 24–25 da validação abrem isso | **Parcial** — PM propõe o mínimo; UX não desenhou |

### As 4 divergências que precisam da sua palavra

| Divergência | Opção A (PM) | Opção B (UX) | O que decide |
|---|---|---|---|
| **D1 · Evento-espelho no calendário como camada 1?** | Não — só e-mail | Sim — evento privado 60 min antes + e-mail | Custo: escopo de **escrita** no OAuth (a tela de permissões fica mais pesada). Ganho: chega onde a mão do vendedor já vai |
| **D2 · Gestor preenche formulário da empresa no onboarding?** | Sim, ≤ 6 campos | Não — heurística + correção em 1 toque | Custo A: atrito. Custo B: a triagem "reunião de receita" começa cega. As duas concordam que o vendedor **nunca** preenche |
| **D3 · Feedback: 1 toque com "não li" ou 2 momentos?** | 1 pergunta, 3 respostas, ~1 h após | Útil/Não ajudou imediato + Avançou/Igual/Não avançou 2 h após | A opção "não li" do PM só existe em A. O "brief se cobrando" da UX só existe em B. Podem ser combinadas: B + "não li" na primeira pergunta |
| **D4 · Trocar a ordem 6 ↔ 7 do V3?** | Não | Sim | Mexe no cânone. Reversível. A UX propõe testar na pergunta 8 da validação ("com 30 s, qual bloco você leria?") |

### ✅ Decisões da fundadora — 29 ago 2026 (prevalecem sobre as recomendações acima)

| # | Decisão | Decidido | Observação |
|---|---|---|---|
| 1 / D1 | Canal | **Evento-espelho privado no calendário + e-mail** (opção UX) | **Correção da fundadora: o brief chega sempre no dia anterior à reunião**, não 60 min antes — para o vendedor poder se organizar. Vale para as duas camadas. Regra de segurança mantida: nunca escrever em evento com convidado externo |
| 2 / D2 | Onboarding | **Gestor preenche formulário curto (≤ 6 campos, ≤ 3 min)** (opção PM); cada vendedor concede o próprio calendário via OAuth; o vendedor nunca preenche nada | As telas 0–5 da UX continuam válidas para o vendedor; entra uma tela de gestor antes |
| 6 / D3 | Feedback | **Dois momentos + "não li"**: rodapé do brief "Útil / Não ajudou / Não li" + ~2 h após a reunião "Avançou / Ficou igual / Não avançou" | Une o "não li" do PM ao brief-que-se-cobra da UX. Leitura sempre descritiva, nunca causal `[V3 §10]` |
| 8 / D4 | Ordem dos blocos | **Trocar 6 ↔ 7: Perguntas críticas antes de Riscos** (opção UX) | Altera a ordem do V3 §8 — **promover ao V3** na próxima revisão. Reversível |

| 3 | Integrações do MVP | **Só calendário** (Google) | Confirmado nas 3 simulações. Forma um sistema com D2 (6 campos do gestor) e D3/item 5 (feedback vira contexto interno) — é também o que destrava o guardião |
| 4 | 1ª conversa | **DESCONHECIDO vira pergunta; brief muda de peso; "1ª conversa" é selo** | Condição: **testar na demo com empresa "silenciosa"** (sem notícia pública) antes de fechar o pitch |
| 5 | Correção do brief | **Por fato** (opção UX), já no MVP | "Algo errado aqui?" → `✗` por fato + "o certo é…" |
| 7 | LGPD / dados | **Escopo mínimo; fonte-por-fato como auditoria; tela NUNCA; revisão jurídica antes de cliente pagante** | Condições: tela NUNCA avisa do consentimento do Google (R9); texto do guardião inclui a permissão de escrita |
| 9 | Superfície do gestor | **Relatório mensal por e-mail, agregado, sem win rate** | Sem briefs individuais e sem métricas por vendedor no MVP (R7, R8) |

### ✅ Regras derivadas das simulações — decididas em 29/08/2026

| # | Regra | Decidido |
|---|---|---|
| R1 | Reunião criada depois da véspera | Entrega **imediata, com selo "última hora"** |
| R2 | Véspera cai em fim de semana | **Dia útil** anterior |
| R3 | Hora do disparo na véspera | **18h** — validar na Trilha A ("quando você preparou?") |
| R4 | Evento sem nenhum convidado externo | **Nunca gera brief**, mesmo com título comercial |
| R5 | Correção do vendedor × fonte pública | **Correção vence**, marcada "registrado por {nome}, {data}"; fonte pública rebaixada só para aquela conta; sem propagação |
| R6 | "Não li" na pergunta das 2 h | Aparece **só quando o link do brief não foi aberto** |
| R7 | Relatório do gestor | **Agregado** no MVP; por vendedor só com opt-in visível ao próprio vendedor |
| R8 | Gestor vê briefs individuais? | **Não** no MVP — segunda superfície a desenhar depois |
| R9 | Aviso pré-consentimento do Google | Uma linha na tela NUNCA: "na próxima tela o Google vai pedir edição — só criamos eventos privados seus" |
| R10 | Ao desconectar | **Uma pergunta opcional**: "o que fez você desligar?" |


---

## 3 · Lacunas declaradas pelos dois (onde nenhum tem base)

1. **Quem é o guardião de acesso** — `README.md` já declara não mapeado; pergunta 9 da Trilha B + follow-up "e se fosse só o calendário?"
2. **Se o vendedor abre e-mail antes da reunião** — premissa de toda a recomendação de canal; se a Trilha A responder "WhatsApp", a decisão 1 cai
3. **Penetração de Slack/Teams em PME de 3–15 vendedores** — sem dado no kit
4. **Redação jurídica da base legal (LGPD)** e prazo de retenção
5. **Frequência/agregação** — um brief por reunião pode virar ruído em quem tem 6 reuniões/dia
6. **Superfície do gestor** (quem paga) — não desenhada
7. **Estimativa de esforço por integração** — é do @architect
8. **Verbatim do ICP continua em 0%** — todo `[E5-H]` sobe ou cai nas 5 entrevistas; nada disso deve virar código antes

---

## 4 · Riscos novos que a jornada expõe (não estão no §12 do V3)

| Risco | Fonte | Recomendação |
|---|---|---|
| **Guardião trava depois do "sim" comercial** | PM, risco 6 — "crítico e não mapeado" | Entrar no §12 do V3; pedir só calendário reduz a chance de acionar |
| **LGPD vira objeção de compra** | PM, risco 10 — "alto, não mapeado" | Entrar no §12 do V3; revisão jurídica antes de cliente pagante |
| **Brief vaza para o cliente** (escrita no evento original) | UX, §3.2 — "não é bug, é incidente" | Regra de segurança: nunca escrever em evento com convidado externo |
| **Brief de 1ª conversa sai vazio** | PM, risco 7 · UX, §4.2 | **Testar na demo antes de fechar o pitch** — se sair "não sabemos" três vezes, a fronteira defensável não existe |

---

## 5 · O que fazer agora (ordem)

1. ~~Fundadora decide as 9 linhas da tabela §2 e as 4 divergências~~ **Feito em 29/08/2026** (blocos ✅ acima).
2. Acrescentar ao `roteiro-entrevistas-primarias.md` as perguntas propostas (PM: 8 na Trilha A, 6 na Trilha B; UX: 26 em 7 blocos, com teste de 5 segundos usando o exemplo fictício).
3. Testar o brief de primeira conversa com dados reais **antes** de fechar o pitch.
4. Depois de aprovado, promover as decisões para uma seção nova do V3 — o V3 é o cânone; estes documentos não são.
