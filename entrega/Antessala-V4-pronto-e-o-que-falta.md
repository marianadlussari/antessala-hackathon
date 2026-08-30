# Antessala · V4 — o que está pronto e o que falta para o pitch

*Retorno do Agente Néctar · 30/08/2026, 13h10 · pitch às 15h*

---

## 1 · Néctar (a essência em 5 linhas)

- A V4 está **pronta como documento**: tese, ICP, evidências auditadas, arquitetura, custo unitário, Q&A. É o melhor material do grupo.
- A nota do hackathon (V4 §1) é: Problema 20% · Negócio 20% · **Produto e funcionamento 25%** · **Autonomia 20%** · Pitch 15%.
- **45% da nota depende de mostrar um fluxo que roda** ("entrada → execução → saída", "trabalho humano efetivamente substituído").
- A V4 tem uma contradição interna: §14 manda *"construir fluxo autônomo"*; §15 já ensaia *"escolhemos validar antes de escrever código"*.
- O que falta não é texto. É **a demo, o brief real e o ensaio**.

---

## 2 · O que está PRONTO (verificado na V4)

| Peça | Onde na V4 | Status |
|---|---|---|
| Tese, problema, frase-âncora e frase de compra | §2, §3, §7 | ✅ |
| ICP travado + anti-ICP + usuário/champion/comprador | §5, §6 | ✅ |
| Critérios de nota do júri (pesos) | §1 | ✅ — novo, orienta tudo |
| Auditoria de evidências: **usar** 6sense (94% · ~80% · 4.000+); **não usar** "82%" e "Gong 50%" | §4 | ✅ — conferi o 6sense na fonte primária: 94%, 77%, "more than 4,000 buyers", 12/11/2025 |
| Arquitetura: Etapa 0 + 5 etapas + portão de confiança | §7C | ✅ — absorve o doc do colega; substitui minha proposta de arquivo separado |
| Coletores, prioridade, política de dados, resposta sobre LinkedIn/LGPD | §7D | ✅ |
| Custo por brief: R$ 0,40–0,80 · Claude US$1/5 e US$2/10 por MTok · Tavily US$0,008/crédito | §7E | ✅ — **preços conferidos hoje**, estão certos |
| MVP: fluxo de 8 passos, 8 blocos, CONFIRMADO/HIPÓTESE/DESCONHECIDO, fronteira humano×máquina | §8 | ✅ |
| Métricas sem prometer causalidade | §10 | ✅ |
| 6 respostas de Q&A | §15 | ✅ — 1 precisa mudar (ver abaixo) |

---

## 3 · O que FALTA (em ordem de peso na nota)

### 🔴 1. A demo — 45% da nota
- **Não tenho esse dado:** não sei o que o colega já tem rodando. É a primeira pergunta a fazer a ele.
- Se **roda**: a resposta §15 *"Por que não construíram?"* fica errada. Trocar por: *"Construímos o fluxo mínimo — calendário → pesquisa → brief com fonte — e provamos que a economia fecha."*
- Se **não roda até 14h30**: demo = brief montado à mão (Pessoa A do plano) + comparação lado a lado "pesquisa manual × Antessala". Não é autopilot, mas é "saída" concreta.
- **Não faça isso:** mostrar slides de arquitetura no lugar da demo. Arquitetura não pontua em "funcionamento".

### 🔴 2. O brief real de uma empresa-exemplo
- Sem ele, o slide 5 do plano ("o brief em tela cheia") está vazio.
- **Não tenho esse dado:** não sei se a empresa já foi escolhida. O plano dizia "5 minutos, agora".
- Candidatos já pesquisados no repo: `contexto/dossie_pessoa.md` (OGM — retrato do ICP, rastro escasso = teste da "empresa silenciosa") e `contexto/dossie_pessoa_2.md` (Fórmula Distribuidora — presença forte, porte acima do ICP).

### 🟠 3. Alinhar "CRM" × "calendário" entre demo e Q&A
- V4 diz: *gatilho principal = CRM; calendário como alternativa* (§TL;DR, §8).
- Q&A §15 diz: *"O Antessala dispara sozinho pelo CRM"*.
- A demo (se houver) dispara pelo **calendário** — não há integração de CRM construída.
- Um jurado atento pergunta "cadê o CRM?". Regra simples: **o Q&A descreve o que a demo mostra**. Dizer "calendário hoje, CRM na sequência".

### 🟠 4. Dois números sem fonte dentro da V4
- §4, linha *"times com enablement formal ganham ~49% dos negócios previstos contra ~42,5% sem"* — **sem fonte nomeada**. Pela regra da própria V4 ("se um jurado pedir a fonte, não há"): achar a fonte ou cortar.
- §4, *"quando o comprador não havia ranqueado (6%), o primeiro fornecedor ganhou só 57%"* — plausível (mesmo relatório 6sense), mas **eu não verifiquei**. Só usar se alguém abrir o relatório e confirmar.

### 🟡 5. As palavras do desafio
- O júri vai procurar "**oportunidades**" e "**abordagens**" no brief. Os 8 blocos não usam essas palavras.
- Saída barata: no slide do brief, rotular a Etapa 4 · Análise como *"oportunidades e abordagens"*. Zero mudança de produto.

### 🟡 6. Entrevistas (3 usuários + 2 compradores, §9.5)
- Continua em **zero**. Não cabe antes das 15h.
- No pitch, entra como "próximos testes" — com honestidade, vira força: *"é a nossa principal incógnita e já temos o roteiro"*.

### ⚪ 7. Bookkeeping (depois do pitch)
- V4 ainda não está no repo (`fontes/` tem só a V3). Incluir + linha no `DOSSIE-HANDOFF.md` §3 — com seu ok.
- Decisões da jornada (véspera 18h, 6 campos do gestor, feedback D3) não entraram na V4. Você decidiu que são detalhe técnico para o pitch; ficam para a V5.

---

## 4 · Plano até as 15h (microetapas)

**Agora (13h10 → 14h00)**
1. Perguntar ao colega: *"o que roda de ponta a ponta agora?"* → decide o item 1.
2. Confirmar a empresa-exemplo → destrava o brief real (item 2).
3. Cortar ou sourcear os dois números do item 4 (5 minutos).
4. Reescrever a resposta *"Por que não construíram?"* conforme o item 1.

**Depois (14h00 → 15h00)**
5. Ensaio 3× cronometrado; na 3ª, jurado hostil com as 6 perguntas do §15.
6. Decorar a linha de sobrevivência: *"6sense, Buyer Experience Report 2025, mais de 4.000 compradores"*.

**Se quiser aprofundar (pós-hackathon)**
7. Entrevistas com o roteiro pronto (`roteiro-entrevistas-primarias.md`).
8. V5: fundir decisões da jornada + V4 no repo.

---

## 5 · Erros comuns que derrubam no Q&A (evite)

- Dizer "aumenta conversão" — a V4 proíbe; a resposta certa está no §15.
- Citar "82% dos decisores" — folclore, sem fonte.
- Responder "CRM" quando a demo mostra calendário.
- Preencher lacuna com número redondo ("~80%" vira "77%" se alguém abrir o relatório — a V4 já explica; use a explicação).

---

## 6 · Check rápido (3 perguntas, responda de cabeça)

1. Qual % da nota depende de algo funcionando? → **45%**
2. Qual é a única estatística que sobrevive a "de onde veio?" → **6sense 2025, 4.000+ compradores**
3. O que responder a "preparação aumenta conversão?" → **"Não há prova causal publicada; o comprador chega decidido; é isso que medimos."**

---

**Próximo passo claro:** mandar mensagem ao colega agora — *"o que roda de ponta a ponta?"* — e me dizer a resposta. Tudo o mais depende dela.
