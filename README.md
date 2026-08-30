# Antessala · Hackathon

Repositório do grupo para o **Antessala — Meeting Readiness Agent**: agente autônomo que detecta uma reunião comercial no calendário, pesquisa empresa e participantes e entrega um *readiness brief* antes da conversa, para PMEs brasileiras com 3–15 vendedores.

## Como ler este repositório (ordem sugerida)

| Ordem | Arquivo | Para quê |
|---|---|---|
| 1 | `contexto-antessala.md` | Produto, ICP, anti-ICP e a regra de rigor — 5 minutos |
| 2 | `DOSSIE-HANDOFF.md` | Estado do trabalho, o que está verificado, tarefas abertas, regras de evidência |
| 3 | `jornada-do-cliente.md` | A jornada dentro da ferramenta — decisões tomadas em 29/08/2026 (+ `simulacoes-jornada.md`) |
| 4 | `achados-pesquisa-publica.md` · `achados-gatilhos-mercado.md` | Preços, concorrentes, gatilhos e tamanho de mercado — cada número com fonte, data e confiança |
| 5 | `roteiro-entrevistas-primarias.md` | O que falta: 5 entrevistas (única fonte de verbatim brasileiro) |
| — | `Kit-ICP-Antessala.pdf` | Tudo acima diagramado, para ler no celular |
| — | `fontes/antessala-documento-consolidado-v3.html` | O **V3** — documento canônico do produto; tudo que não está nele é hipótese |

## Regras que valem para qualquer contribuição

1. **Toda afirmação carrega tag de evidência** `[E1]`–`[E5]` e, se for número, fonte com URL + data.
2. **Nunca afirmar que o Antessala aumenta win rate ou conversão.** Mecanismo defensável: *preparo raso → oportunidade subaproveitada → perda invisível*.
3. **O que não está no V3 é hipótese** (`[E5]`) até a fundadora decidir — as decisões ficam registradas em `jornada-do-cliente.md`.
4. "Não sei" é resposta válida. Reporte a confiança real, nunca a desejada.

## Regerar o PDF depois de editar qualquer `.md`

```bash
pip install markdown          # só na primeira vez
python3 build_pdf.py          # acha o Chrome sozinho (macOS, Linux, Windows)
# se não achar: CHROME_PATH="/caminho/do/chrome" python3 build_pdf.py
```

---

# Kit de Deep Research de ICP · Antessala

## Essência

- O V3 já resolveu **produto, ICP, fluxo, narrativa e métricas**. O que falta não é definição — é **evidência**.
- Das lacunas abertas, duas valem **40% da nota** do hackathon. As outras valem quase nada agora.
- Seu prompt original falhou por design: pedia números que ninguém tem e frases que ninguém disse.
- Com o relógio do hackathon rodando, o caminho é: **prompt enxuto (~40 min) + 5 entrevistas**, não pesquisa completa.

---

## O corte de prioridade

Os critérios de julgamento do V3 cruzados com o que o documento declara em aberto:

| Critério | Peso | Status no V3 | Ação |
|---|---|---|---|
| Produto e funcionamento | 25% | ✅ resolvido (fluxo de 8 passos, saída do brief) | nada |
| Autonomia | 20% | ✅ resolvido (fronteira humano × máquina) | nada |
| Pitch | 15% | ✅ frase-âncora e frase de compra prontas | nada |
| **Problema e oportunidade** | **20%** | ⚠️ falta **verbatim** e custo atual | **prompt · entrega 1** |
| **Potencial de negócio** | **20%** | ⚠️ falta **disposição a pagar** | **prompt · entrega 2 + Trilha B** |

**40% da nota depende exatamente do que falta.** Todo o resto é polimento.

---

## Os 5 erros do prompt original

| # | Erro | Correção |
|---|---|---|
| 1 | `80%+ da base sente`, `intensidade 8/10` | 4 proxies observáveis → nota **com a conta à mostra** |
| 2 | Faixa etária, renda pessoal, formação (molde B2C) | **Unidade de compra** + firmografia com sinais de orçamento |
| 3 | `Casos de sucesso validados` | **Evidência de categoria**, rotulada como de terceiros — o produto não tem clientes |
| 4 | Fato, citação e palpite no mesmo bullet | **Escala E1–E5** obrigatória em toda linha |
| 5 | `Confiança esperada: 85%+` | Confiança **real reportada**; "não sei" é resposta premiada |

---

## Os arquivos

| Arquivo | O que é | Quando usar |
|---|---|---|
| **`prompt-versao-hackathon.md`** | Prompt enxuto, contexto do V3 já embutido, 6 entregas priorizadas | **Agora.** ~40 min de execução |
| `roteiro-entrevistas-primarias.md` | Duas trilhas: 3 usuários + 2 compradores | Hoje, em paralelo |
| `contexto-antessala.md` | Bloco 1 preenchido a partir do V3 | Para alimentar o prompt mestre depois |
| `prompt-deep-research-icp.md` | Prompt mestre, 15 blocos | Depois do hackathon, pesquisa completa |
| `achados-pesquisa-publica.md` | Preços, concorrentes e evidência de categoria — lidos na página em 29/08/2026 | Para responder "quanto custa" e "quem já faz isso" na banca |
| `achados-gatilhos-mercado.md` | 8 gatilhos observáveis em dado público BR + tamanho de mercado (faixa e cadeia de cálculo) | Entregas 4 e 6 |
| `jornada-do-cliente.md` (+ `jornada-produto-pm.md`, `jornada-superficie-ux.md`, `simulacoes-jornada.md`) | Jornada dentro da ferramenta — o que o V3 não definia; decidida em 29/08 | Promover ao V3 na próxima revisão |
| `contexto/perfil_empresa.md` · `contexto/dossie_pessoa.md` · `contexto/dossie_pessoa_2.md` | **Gabaritos do MVP**: o nosso lado (o que vendemos / não fazemos) e o lado deles (2 pessoas reais, termos literais com link — gabarito 1 = retrato do ICP com rastro escasso; gabarito 2 = contraste com presença forte, porte acima do ICP) | O que o prompt do agente tem que acertar; regra: termo sem link não entra |
| `Kit-ICP-Antessala.pdf` | Tudo diagramado | Para circular no time |

---

## As 3 travas que o prompt carrega

1. **Citação sem URL não existe** — vira `LACUNA` com plano de fechamento.
2. **Todo `%` precisa de fonte com metodologia**, ou não entra.
3. **Achou 1 onde pedi 3? Entrega 1.** Nunca preenche por simetria de template.

E a regra de negócio embutida: **dor sem workaround é dor tolerada** — não vira compra. O prompt classifica em quente/morna/fria e manda descartar as frias do topo.

---

## Duas coisas que o prompt busca e você ainda não tem

**Âncora de preço.** O V3 diz que preço é hipótese. Mas o *pricing público* de Sales Navigator, Apollo, Clay, Gong e dos copilots de CRM é rastreável em minutos. Isso te dá faixa defensável para responder "quanto custa" na banca sem ter cliente — a resposta vira "a categoria cobra X por vendedor/mês, com esta fonte", não um chute.

**O guardião.** O V3 mapeia usuário, champion e comprador — mas o Antessala pede **calendário, e-mail e CRM**. Quem aprova esse acesso não está no documento, e é justamente quem pode travar a venda. A pergunta 9 da Trilha B existe para isso.

---

## Erros comuns / alertas

- **Não rode em ferramenta sem busca web.** Vai gerar um documento lindo e ficcional — exatamente o risco de alucinação que o V3 lista como crítico.
- **Não traduza verbatim em inglês como fala nativa BR.** Fala de AE americano no r/sales não é fala de gestor de PME brasileira.
- **Não deixe case de concorrente virar case seu**, nem por descuido de formatação. Num Q&A de banca isso é fatal.
- **Respeite a regra de rigor do V3.** Se a pesquisa sugerir ganho de conversão, apresente como cenário com premissa explícita — nunca como promessa.

---

## Próximo passo (Agora)

Colar `prompt-versao-hackathon.md` numa ferramenta com busca web e rodar. Foco nas entregas 1 e 2 — são as que valem nota.

## Depois

Disparar 10 convites de entrevista. Priorizar a Trilha B (comprador econômico): são as duas conversas que sustentam o critério de potencial de negócio.

## Se quiser aprofundar

Montar um slide único de "Painel de Evidências" — afirmação, tag, fonte, confiança. É o slide que mostra método em vez de opinião, e o único que sobrevive a uma banca cética.
