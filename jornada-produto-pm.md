# Jornada do cliente dentro do Antessala
**Documento de definição de produto · @pm (Morgan) · 29 ago 2026**

> **Status deste documento.** O V3 (29/08/2026) define o **motor**: gatilho, fluxo de 8 passos, 8 blocos do brief, regra de confiança e fronteira humano × máquina. O V3 **não define a jornada**: canal de entrega, superfície, onboarding, quem concede acesso, quais fontes concretas são consultadas e o que acontece depois da reunião. Este documento preenche essa lacuna **como proposta**, não como registro de decisão.
>
> **Convenção de origem — respeitada em toda linha:**
> - `[V3]` = decidido no V3, com a seção citada. Pode ser apresentado como decisão do projeto.
> - `[E5]` = **proposta nova desta rodada**. É hipótese. Não pode ser apresentada em banca como decisão tomada, e não pode entrar no V3 sem aprovação explícita.
>
> **Regra de rigor herdada `[V3 · §3 "Formulações a evitar"]`:** nenhuma linha deste documento afirma que o Antessala aumenta win rate ou conversão. O mecanismo defensável é **preparo raso ou ausente → oportunidade potencialmente subaproveitada → perda invisível**.

---

> ✅ **DECISÕES DA FUNDADORA (29/08/2026) — prevalecem sobre as recomendações deste documento.** Registro completo em `jornada-do-cliente.md`. O que muda aqui:
> - **4.1 Canal → D1:** evento-espelho privado no calendário **+** e-mail (não só e-mail). Entrega **no dia útil anterior, às 18h**; reunião criada depois recebe o brief imediatamente com selo "última hora" (R1–R3). O "30 min antes" da Etapa 5 cai.
> - **4.2 Onboarding → D2:** híbrido confirmado; gestor preenche ≤ 6 campos.
> - **4.3 Integrações:** só calendário — **confirmado**.
> - **4.4 Primeira conversa:** confirmado; testar na demo com empresa "silenciosa" (sem notícia pública).
> - **4.5 Correção → item 5:** **por fato** já no MVP (não "brief inteiro").
> - **4.6 Feedback → D3:** dois momentos ("Útil / Não ajudou / Não li" no brief + "Avançou / Igual / Não avançou" 2 h após), não uma pergunta só.
> - **4.7 LGPD:** confirmado; texto do guardião inclui a permissão de escrita.
> - **Etapa 6 / relatório do gestor:** mensal, **agregado**, sem briefs individuais (R7, R8).

## 0 · O que o V3 já decidiu sobre a jornada (verificado na fonte)

Antes de propor, o que já está travado. Tudo abaixo é `[V3]`:

| Elemento | Texto no V3 | Seção |
|---|---|---|
| Gatilho | "Reunião comercial identificada automaticamente no calendário" | TL;DR · Registro de decisão atual |
| Entrada | "Calendário + contexto interno + dados públicos" | TL;DR · Registro de decisão atual |
| Saída | "Readiness brief entregue automaticamente antes da reunião" | TL;DR · Registro de decisão atual |
| Fluxo | 8 passos: Gatilho · Identificação · Contexto interno · Pesquisa externa · Consolidação · Análise · Objetivo · Entrega | §8 · Fluxo |
| Conteúdo do brief | 8 blocos: Why now · O que sabemos · O que mudou · Quem está na mesa · O que falta · Riscos · Perguntas críticas · Resultado esperado | §8 · Saída do readiness brief |
| Confiança | CONFIRMADO / HIPÓTESE / DESCONHECIDO. "Fatos precisam de fonte. Hipóteses precisam de justificativa. Desconhecidos viram perguntas de discovery." | §8 · Regra de confiança |
| O que a máquina faz sozinha | detectar reunião · pesquisar conta e participantes · buscar histórico · consolidar · identificar gaps e riscos · criar hipóteses e perguntas · definir objetivo provável | §8 · Fronteira humano × máquina |
| O que fica com o humano | confirmar dor, orçamento, urgência e política interna · conduzir negociação · tomar decisão comercial | §8 · Fronteira humano × máquina |
| Restrição de autonomia | "Um chatbot que espera o vendedor pedir algo é uma direção mais fraca para este desafio" | §1 · O desafio recebido |
| Não construir agora | "Chatbot, AI SDR completo, CRM, forecast ou plataforma comercial generalista" | TL;DR · Registro de decisão atual |
| Quem compra | "Não depender de compra individual do closer" · "Priorizar dono, Diretor Comercial ou Head de Vendas em PME estruturada" | §11 · Modelo de negócio |

**O que o V3 declaradamente NÃO resolve e este documento propõe:** canal, superfície, onboarding, fontes concretas, permissões, correção do brief, pós-reunião, privacidade. O `README.md:66` registra explicitamente: *"o Antessala pede calendário, e-mail e CRM — quem aprova esse acesso não está no documento"*.

---

## 1 · Atores

Papéis do V3 `[V3 · §6 "Quem usa e quem sente o negócio no mês"]`, com a coluna de jornada acrescentada `[E5]`.

| Ator | Quem é | Motivação (V3) | Onde aparece na jornada `[E5]` | Risco se ignorado |
|---|---|---|---|---|
| **Usuário — AE / vendedor** | AE, closer, executivo de contas, consultor comercial, vendedor de campo `[V3 §6]` | "Entrar em reuniões importantes com contexto, riscos, gaps e objetivo claro sem precisar reconstruir tudo sozinho" `[V3 §6]` | Etapas 2 (conecta o próprio calendário), 3, 4, 5, 6. **É o único ator que pode conceder o calendário dele.** | Compra sem adoção: o gestor assina, o vendedor nunca conecta |
| **Champion — gerente comercial** | Gerente comercial ou líder de vendas próximo da execução `[V3 §6]` | "Reduzir variação entre vendedores e tornar a preparação menos dependente dos melhores performers" `[V3 §6]` | Etapas 0, 1, 2 (ativa o time), 6 (é quem olha consistência), 7 | Sem ele, a ativação vira tarefa individual e morre |
| **Comprador econômico — dono / Diretor Comercial / Head de Vendas** | `[V3 §6]` | "Evitar oportunidades subaproveitadas, melhorar execução do pipeline e proteger receita relevante do mês" `[V3 §6]` | Etapas 0, 6, 7. **Não é usuário diário.** | Sem prova de uso e de utilidade, não renova |
| **Guardião de acesso** | **NÃO MAPEADO.** `README.md:66`: "quem aprova acesso a calendário, e-mail e CRM não está no documento" | — | Etapa 2 · bloqueia ou libera a conexão | **É quem pode travar a venda depois do "sim" comercial** |

> **Sobre o guardião: não tenho base para afirmar quem é.** Em PME de 3–15 vendedores ele pode ser o próprio dono, um TI terceirizado, um contador/administrativo, ou ninguém formalmente. O V3 não diz, a pesquisa pública não diz, e inventar isso seria violação do Art. IV. **O que seria preciso saber:** (a) existe TI interno? (b) o Google Workspace / Microsoft 365 do cliente tem política de apps de terceiros? (c) quem historicamente aprovou o último acesso desse tipo? A **pergunta 9 da Trilha B** do roteiro existente já foi escrita exatamente para fechar isso.

---

## 2 · Jornada ponta a ponta

### Etapa 0 · Aquisição e decisão de compra

| O que o usuário faz/fornece | O que a IA coleta/faz sozinha (fonte concreta) | O que o usuário vê (conteúdo + canal) | Origem |
|---|---|---|---|
| Comprador econômico (dono/DC/Head) é abordado; não é o closer que compra | Nada. Ainda não há acesso a nada. | Pitch: "seus vendedores estão entrando nas reuniões que mais valem o mês sem o contexto que muda o resultado — e você não vê os negócios que isso custa" | `[V3]` §11 Modelo de negócio + §7 Frase de compra |
| Comprador responde: quantos vendedores, existe alguém que prepara reunião hoje, qual CRM | Nada | Qualificação de fit conduzida por humano | `[V3]` §5 ICP (sinais de alto fit) / `[E5]` o formato da qualificação |
| — | **Proposta `[E5]`:** antes da assinatura, gerar **1 brief-amostra** de uma reunião real futura do próprio comprador, a partir de um único evento de calendário informado manualmente | Brief-amostra por e-mail/PDF, antes de qualquer integração | `[E5]` |

**Por que o brief-amostra `[E5]`:** o V3 lista "briefing virar commodity" como risco **alto** `[V3 §12]` e a ENTREGA 5 confirma quatro concorrentes com página de vendas no ar. Argumento de venda não diferencia; artefato diferencia. Custo: uma execução manual do motor. **Risco:** se o brief-amostra sair genérico ou com um fato errado, mata a venda na entrada — é a materialização do risco crítico "fatos errados ou alucinação" `[V3 §12]`.

---

### Etapa 1 · Onboarding

| O que o usuário faz/fornece | O que a IA coleta/faz sozinha (fonte concreta) | O que o usuário vê (conteúdo + canal) | Origem |
|---|---|---|---|
| Gestor informa: nome da empresa, o que ela vende, para quem vende, ticket médio aproximado, quais tipos de reunião contam como "de receita" | Nada ainda — é input humano deliberado | Formulário web curto (proposta: ≤ 6 campos, ≤ 3 min) | `[E5]` |
| Gestor lista os vendedores (nome + e-mail corporativo) | Deriva o domínio corporativo do cliente — usado depois para separar participante interno de externo | Lista do time na tela, com status "convidado / conectado" | `[E5]` |
| Vendedor recebe convite | — | E-mail de convite com 1 botão: "conectar meu calendário" | `[E5]` |
| — | **Nada é pesquisado antes do primeiro evento detectado** | — | `[E5]`, derivado de `[V3 §1]` autonomia: o produto não deve pedir trabalho ao usuário |

**Tensão declarada.** O V3 exige autonomia `[V3 §1]`, mas o onboarding é inevitavelmente humano: alguém precisa conceder acesso e alguém precisa dizer o que a empresa vende. **Não há como a máquina descobrir sozinha o que conta como "reunião de receita" nesse cliente.** Este é o único ponto da jornada em que o produto pede trabalho, e ele deve ser explicitamente curto. `[E5]`

---

### Etapa 2 · Conexões e permissões

| O que o usuário faz/fornece | O que a IA coleta/faz sozinha (fonte concreta) | O que o usuário vê (conteúdo + canal) | Origem |
|---|---|---|---|
| Cada vendedor autoriza **OAuth do próprio calendário** (Google Calendar ou Microsoft 365 / Outlook Calendar) — escopo de **leitura** | Passa a ler: título, descrição, horário, lista de convidados, organizador, link da call, eventos anteriores com os mesmos convidados | Tela de consentimento nativa do Google/Microsoft + tela de confirmação "conectado, seu primeiro brief chega antes da próxima reunião" | `[E5]` — o V3 diz "calendário" (TL;DR · Entrada) mas **não diz qual provedor nem qual escopo** |
| Gestor (ou guardião) aprova o app no workspace, se a política exigir | — | Fluxo administrativo do Google Workspace / Microsoft 365 | `[E5]` |
| **Opcional, não no MVP:** conexão de CRM | Leria: oportunidade, estágio, valor, notas, histórico da conta | — | `[E5]` — V3 cita "contexto interno" `[V3 §8 Fluxo, passo 3]` sem nomear sistema |
| **Opcional, não no MVP:** conexão de e-mail | Leria: thread com os participantes daquela conta | — | `[E5]` — alto impacto em LGPD, ver §4.7 |

**Fato de mercado relevante `[E5, apoiado em ENTREGA 5]`:** AmpUp declara integrações com Gong, Chorus, Salesforce, HubSpot, Google Calendar e Outlook. Ou seja, **a barra de integração da categoria é alta e já está estabelecida.** Competir por número de conectores é competir onde o concorrente já ganhou. A cunha do Antessala não está aí.

---

### Etapa 3 · Primeiro brief

| O que o usuário faz/fornece | O que a IA coleta/faz sozinha (fonte concreta) | O que o usuário vê (conteúdo + canal) | Origem |
|---|---|---|---|
| **Nada.** Não pede, não abre app, não digita | **Passo 1 · Gatilho:** varre o calendário conectado e detecta reunião futura | — | `[V3]` §8 Fluxo, passo 1 |
| — | **Triagem `[E5]`:** classifica se é "reunião de receita". Sinais propostos: existe convidado com domínio externo ao do cliente · duração ≥ 30 min · não é evento recorrente interno | — | `[E5]` — o V3 diz "reunião comercial identificada automaticamente" (TL;DR) mas **não define o critério de identificação** |
| — | **Passo 2 · Identificação:** empresa a partir do **domínio de e-mail dos convidados externos**; pessoas a partir de nome + domínio | — | `[V3]` §8 passo 2 / `[E5]` o método (domínio) |
| — | **Passo 3 · Contexto interno:** no MVP, o que o próprio calendário carrega — título, descrição, anexos do evento, convites anteriores com o mesmo domínio | — | `[V3]` §8 passo 3 / `[E5]` a fonte concreta |
| — | **Passo 4 · Pesquisa externa:** site institucional da empresa · notícias públicas recentes · consulta pública de CNPJ (base da Receita Federal exposta por serviços públicos) · perfis profissionais públicos dos participantes | — | `[V3]` §8 passo 4 + TL;DR "dados públicos" / `[E5]` a lista concreta de fontes |
| — | **Passos 5–7:** consolida, remove redundância, identifica gaps/riscos/hipóteses, formula perguntas, define o avanço que a reunião precisa produzir | — | `[V3]` §8 passos 5, 6, 7 |
| — | **Passo 8 · Entrega:** envia automaticamente antes da reunião | **Brief nos 8 blocos**, cada fato com tag CONFIRMADO / HIPÓTESE / DESCONHECIDO e fonte | `[V3]` §8 passo 8 + Saída do readiness brief + Regra de confiança |
| — | — | **Canal e antecedência:** ~~e-mail, com link para versão web read-only; disparo proposto na véspera à noite e 30 min antes~~ → **DECIDIDO 29/08 (D1, R1–R3):** evento-espelho privado no calendário + e-mail, no dia útil anterior às 18h; última hora = imediato com selo | `[E5]` — ver decisão 4.1 |

**Alerta de conformidade `[E5]`:** raspar LinkedIn logado viola os termos de uso da plataforma e é exatamente o que o Sales Navigator monetiza (US$119,99–159,99/licença/mês, ENTREGA 2). **Recomendação:** no MVP, usar apenas o que buscador público retorna sobre a pessoa, sem sessão autenticada, e registrar a fonte por fato. Se o brief não conseguir dizer quem é o participante, o bloco "Quem está na mesa" deve declarar **DESCONHECIDO** — que é exatamente o que a regra de confiança do V3 manda `[V3 §8 Regra de confiança]`.

---

### Etapa 4 · Uso recorrente

| O que o usuário faz/fornece | O que a IA coleta/faz sozinha (fonte concreta) | O que o usuário vê (conteúdo + canal) | Origem |
|---|---|---|---|
| Nada. Continua trabalhando no calendário como sempre | Monitora continuamente o calendário; gera brief a cada reunião de receita detectada | Um brief por reunião, no canal escolhido | `[V3]` TL;DR (entrega automática) / `[E5]` a cadência |
| Marca/desmarca reunião | Recalcula: reunião cancelada → não envia; reunião remarcada → reprograma o envio; convidado adicionado → atualiza "Quem está na mesa" | Brief atualizado, ou silêncio se cancelou | `[E5]` |
| **Sinaliza "não é reunião de receita"** (1 clique no rodapé do brief) | Deixa de gerar para eventos daquele padrão | Confirmação simples | `[E5]` — controle de ruído |
| — | **Não no MVP `[E5]`:** aprender com o histórico de feedback do próprio usuário | — | `[E5]` |

**Risco central desta etapa `[E5]`:** o brief que chega sempre vira ruído, e ruído é desinstalado. O V3 lista "PME não perceber urgência" como risco **crítico** `[V3 §12]`. Uma jornada que dispara brief para toda reunião do calendário converte um produto de alto valor por reunião em spam. **A triagem não é detalhe técnico — é a diferença entre adoção e churn.**

---

### Etapa 5 · Antes, durante e depois da reunião

| Momento | O que o usuário faz/fornece | O que a IA coleta/faz sozinha | O que o usuário vê (conteúdo + canal) | Origem |
|---|---|---|---|---|
| **Antes (véspera)** | Lê ou não lê | Já entregou | Brief completo, 8 blocos, por e-mail | `[V3]` §8 Saída / `[E5]` o canal e o momento |
| **Antes (30 min)** | Lê no celular, geralmente em deslocamento | Nada novo — mesmo conteúdo, formato curto | **Proposta `[E5]`:** versão curta — objetivo da reunião + 3 perguntas críticas + 1 risco. Cabe em uma tela | `[E5]` |
| **Durante** | Conduz a reunião. Confirma dor, orçamento, urgência e política interna; negocia; decide | **Nada.** O V3 põe explicitamente esses três itens do lado humano | Nada. **Sem copiloto em call no MVP** | `[V3]` §8 Fronteira humano × máquina + TL;DR "Não construir agora" |
| **Depois** | Responde 1 pergunta | Registra a resposta | ~~Proposta: e-mail curto ~1h após o fim: "o brief ajudou nesta conversa? sim / não / não li"~~ → **DECIDIDO 29/08 (D3):** "Útil / Não ajudou / Não li" no rodapé do brief **+** "Avançou / Ficou igual / Não avançou" ~2 h após, com "não li" se o link não foi aberto | `[E5]`, alimenta a métrica `[V3 §10]` "% de briefings considerados úteis · mensurável rapidamente" |

**Limite explícito.** O V3 classifica "reunião → próxima etapa" e "dias até proposta" como **"validar depois"**, não como métrica do MVP `[V3 §10]`. A jornada pode **instrumentar** o campo, mas o hackathon **não pode apresentar avanço de pipeline como resultado medido**.

---

### Etapa 6 · Feedback e métricas

| Ator | O que fornece | O que a IA coleta/faz sozinha | O que vê (conteúdo + canal) | Origem |
|---|---|---|---|---|
| Vendedor | 1 clique de utilidade por brief | Agrega | Nada além da confirmação | `[E5]` / métrica em `[V3 §10]` |
| Vendedor | Opcional: "este fato está errado" + campo livre | Registra a correção com o fato e a fonte associados | Confirmação | `[E5]` — mitigação direta do risco crítico "fatos errados ou alucinação" `[V3 §12]` |
| Gestor / comprador | Nada | Calcula: % de briefs entregues automaticamente · % de fatos com fonte · % de briefs considerados úteis · gaps críticos identificados antes da call · minutos de preparação evitados (estimativa com premissa explícita) | **Proposta `[E5]`:** um e-mail mensal, não um dashboard. Quem compra não é usuário diário `[V3 §6]` | Métricas: `[V3]` §10 · Canal e formato: `[E5]` |

**Regra de honestidade no relatório do gestor `[V3 §10 "Leitura correta"]`:** "O MVP consegue provar automação, qualidade da saída e trabalho substituído. Impacto em avanço e conversão continua sendo hipótese a testar." O relatório mensal **não pode** exibir win rate como resultado do produto.

---

### Etapa 7 · Renovação ou churn

| O que o usuário faz/fornece | O que a IA coleta/faz sozinha | O que o usuário vê | Origem |
|---|---|---|---|
| Comprador decide manter ou cortar | Consolida o histórico de uso e utilidade do período | Relatório de renovação com os números do §10 e **nenhuma alegação de causalidade** | `[E5]` / métricas `[V3 §10]` |
| — | **Sinais de churn `[E5]`:** vendedor desconectou o calendário · taxa de "não li" alta · zero cliques de utilidade por 30 dias · nenhuma reunião de receita detectada (fit errado) | Alerta interno, não para o cliente | `[E5]` |

**Previsor de churn mais provável `[E5]`:** não é preço, é irrelevância — brief que chega e não é lido. O roteiro de entrevistas já tem a pergunta certa para investigar isso na Trilha B: *"Me conta a última ferramenta comercial que vocês cancelaram. Por quê?"*

---

## 3 · Fronteira do MVP de 10 horas vs. produto completo

Coerente com o não-escopo do V3: *"Não construir agora: chatbot, AI SDR completo, CRM, forecast ou plataforma comercial generalista"* `[V3 · TL;DR]`.

### Cabe nas 10 horas

| Item da jornada | Etapa | Por que cabe |
|---|---|---|
| Conexão OAuth de **um** calendário (Google) | 2 | Um provedor, escopo de leitura |
| Detecção automática de reunião futura | 3 | `[V3 §8 passo 1]` — é o gatilho, não é opcional |
| Triagem por domínio externo + duração | 3 | Regra determinística, poucas linhas |
| Identificação de empresa por domínio | 3 | `[V3 §8 passo 2]` |
| Pesquisa externa: site, notícias, CNPJ público, perfil profissional público | 3 | `[V3 §8 passo 4]` |
| Contexto interno **a partir do próprio calendário** | 3 | Mantém o passo 3 do V3 vivo sem conector de CRM |
| Consolidação, análise, objetivo | 3 | `[V3 §8 passos 5–7]` — núcleo do LLM |
| Brief nos 8 blocos com tag de confiança e fonte por fato | 3 | `[V3 §8 Saída + Regra de confiança]` — **inegociável, é o antídoto do risco crítico de alucinação** |
| Entrega automática por e-mail + link web read-only | 3 | `[V3 §8 passo 8]` |
| Feedback binário de utilidade (1 clique) | 6 | Alimenta `[V3 §10]` "% de briefings considerados úteis" |
| Contador de % de briefs entregues automaticamente e % de fatos com fonte | 6 | `[V3 §10]` — são as duas métricas que provam **autonomia** (20% da nota) |

### Fica como visão

| Item | Por quê |
|---|---|
| Conector de CRM (RD Station, Agendor, Ploomes, HubSpot, Salesforce) | Cada conector é projeto próprio; e a demo da **primeira conversa** — a fronteira defensável — não precisa dele |
| Leitura de caixa de e-mail | Maior ganho de contexto **e** maior exposição LGPD. Não se resolve em 10h |
| WhatsApp como canal | API oficial exige número, aprovação de template e verificação de negócio — inviável no relógio do hackathon |
| App web logado, histórico de briefs, busca | O V3 já exclui "plataforma comercial generalista" |
| Painel do gestor em tempo real | Comprador não é usuário diário `[V3 §6]`; e-mail mensal resolve mais barato |
| Correção fato a fato com reaprendizado | O registro da correção cabe; o aprendizado não |
| Instrumentação de reunião → próxima etapa | `[V3 §10]` classifica como "validar depois" |
| Copiloto durante a call, resumo pós-call | Território de Gong/Fireflies/Avoma e do não-escopo do V3 |

### O corte que eu defendo, e o que ele custa

**Recomendo MVP com calendário como única integração.** O custo honesto: o passo 3 do fluxo do V3 ("Contexto interno: busca oportunidade, histórico e notas") fica **parcialmente atendido** — só com o que o calendário carrega, não com CRM.

Isso não é acidente de escopo, é escolha estratégica. A ENTREGA 5 mostra que **os quatro concorrentes de meeting prep lidos declaram, cada um na própria página, que o brief é montado sobre artefato prévio**: AmpUp sobre gravação de call (Gong/Chorus), EchoIQ sobre histórico de deal, SiftHub sobre CRM + call data, Parsley sobre chat prévio do prospect. **Um MVP que depende de CRM entra no terreno onde eles já ganharam.** Um MVP que funciona só com calendário demonstra exatamente o caso que nenhum deles cobre: a primeira conversa, sem histórico.

**Na banca, isso vira frase, não desculpa:** *"os concorrentes precisam de um artefato que a PME ainda não tem. Nós precisamos de um convite de calendário."*

---

## 4 · Pontos de decisão em aberto

### 4.1 · Canal de entrega do brief

| Opção | Prós | Contras |
|---|---|---|
| **E-mail** | Zero atrito de instalação · já é onde vive o convite de calendário · funciona em qualquer dispositivo · formatação rica · barato de construir | Caixa cheia, pode não ser lido · concorre com todo o resto |
| **WhatsApp** | Onde o comercial brasileiro efetivamente vive · o V3 lista WhatsApp como parte do contexto fragmentado `[V3 §5, §7A, §7B]` · leitura quase garantida | API oficial exige número, verificação de negócio e template aprovado · inviável em 10h · intrusivo se errar a triagem |
| **Slack / Teams** | Bom para times que já vivem lá | **PME de 3–15 vendedores frequentemente não tem Slack.** Não tenho dado sobre penetração de Slack/Teams nesse recorte — não vou fingir que tenho |
| **App/web** | Superfície própria, controle total | Fere a autonomia do V3: exige que o usuário vá até o produto `[V3 §1]` |
| **Notificação no evento do calendário** | Chega exatamente no contexto certo | Espaço limitadíssimo; não cabe brief de 8 blocos |

**Recomendação: e-mail como canal primário do MVP, com link para uma página web read-only por brief.** Motivo: é o único canal que atende às três restrições simultaneamente — cabe nas 10h, não exige que o usuário procure o produto (preserva a autonomia do `[V3 §1]`) e suporta os 8 blocos com fonte por fato. A página web existe só para o brief ser abrível no celular sem depender do cliente de e-mail.

**WhatsApp fica na visão, e deve ser dito assim no pitch** — "o canal certo para o comercial brasileiro é o WhatsApp; o MVP entrega por e-mail porque a API oficial não cabe em 10 horas" é uma resposta que mostra domínio do problema, não limitação.

---

### 4.2 · Quem faz o onboarding

| Opção | Prós | Contras |
|---|---|---|
| **Vendedor individual (self-serve)** | Adoção bottom-up, atrito baixo | Contradiz `[V3 §11]`: "Não depender de compra individual do closer" · sem o gestor, ninguém mede |
| **Gestor ativa para o time** | Alinha com `[V3 §11]` "Priorizar dono, Diretor Comercial ou Head de Vendas" · gestor tem o contexto da empresa · gestor é quem sente inconsistência `[V3 §6]` | Gestor **não pode** conceder o calendário do vendedor — cada vendedor precisa autorizar o próprio |
| **Híbrido** | Combina os dois acima | Duas telas em vez de uma |

**Recomendação: híbrido — o gestor contrata e configura o contexto da empresa; cada vendedor concede o próprio calendário via OAuth individual.**

Por quê: o V3 é explícito que a compra não é individual `[V3 §11]`, mas permissão de calendário é pessoal por construção — nenhum provedor permite que um gestor delegue o calendário alheio sem privilégio administrativo de workspace. Fingir que o gestor "liga para o time" seria inventar um mecanismo que não existe.

**Consequência que precisa estar no radar:** isso cria o gap clássico entre compra e adoção. **A métrica de onboarding mais importante não é "quantos assinaram", é "quantos vendedores conectaram o calendário nos primeiros 7 dias".**

---

### 4.3 · Integrações mínimas do MVP

| Opção | Prós | Contras |
|---|---|---|
| **Só calendário** | Cabe em 10h · demonstra a fronteira defensável (primeira conversa) · um único consentimento · exposição LGPD menor | Atende o passo 3 do V3 só parcialmente · brief mais raso quando existe histórico rico no CRM |
| **Calendário + e-mail** | Contexto interno real: a thread com o prospect · é onde a PME brasileira de fato guarda histórico | Escopo de leitura de caixa é o pedido mais invasivo da jornada · dispara o guardião não mapeado · risco LGPD alto |
| **Calendário + e-mail + CRM** | Brief mais completo · paridade com a categoria | Não cabe em 10h · e é justamente o terreno de AmpUp/SiftHub/EchoIQ |

**Recomendação: só calendário no MVP.** Três razões, nesta ordem:

1. **Estratégica** — é o corte que demonstra o que a ENTREGA 5 mostrou ser único: funcionar sem artefato prévio.
2. **De risco** — cada integração adicional multiplica a superfície de LGPD e ativa o guardião que o `README.md:66` declara não mapeado. Ativar um bloqueador que você ainda não conhece, no meio de um hackathon, é escolha ruim.
3. **De escopo** — 10 horas.

**O que se perde e como responder na banca:** "o brief fica mais raso quando já existe histórico". Resposta honesta: *"sim — e é por isso que a primeira conversa é o caso em que somos mais fortes que os concorrentes, não mais fracos."*

---

### 4.4 · O que fazer quando não há contexto interno (a primeira conversa)

Este é **o ponto de decisão mais importante deste documento**, porque é a fronteira competitiva.

| Opção | Prós | Contras |
|---|---|---|
| **Declarar DESCONHECIDO e converter em pergunta de discovery** | É literalmente o que o V3 já manda: "Desconhecidos viram perguntas de discovery" `[V3 §8 Regra de confiança]` · honesto · o bloco "O que falta" ganha protagonismo | Brief visualmente mais "vazio" — pode ser lido como produto fraco por quem não entende a regra |
| **Pedir input ao vendedor quando faltar contexto** | Brief mais completo | Fere a autonomia `[V3 §1]` e converte o produto no chatbot que o V3 exclui |
| **Inferir por analogia com empresas parecidas** | Brief cheio | **Viola a regra de confiança do V3 e materializa o risco crítico "fatos errados ou alucinação"** `[V3 §12]`. Inaceitável |

**Recomendação: opção 1, com um ajuste de forma `[E5]` — o brief de primeira conversa muda de peso, não de estrutura.** Mantém os 8 blocos do V3, mas "O que sabemos" fica curto e explicitamente marcado, enquanto "O que falta", "Perguntas críticas" e "Resultado esperado" carregam o valor.

**Por quê:** o brief de primeira conversa **não deve tentar parecer um brief de conta conhecida**. Ele é um instrumento diferente — é um plano de discovery derivado de dados públicos, com as lacunas nomeadas. Isso é defensável contra AmpUp, Parsley, EchoIQ e SiftHub porque nenhum dos quatro consegue produzi-lo: **todos precisam do artefato prévio que, na primeira conversa, não existe.**

**Cuidado de pitch:** essa vantagem só é real se o brief de primeira conversa for **visivelmente útil**. Se ele sair como "não sabemos, não sabemos, não sabemos", a fronteira defensável vira desculpa. **Este é o item nº 1 a testar na demo.**

---

### 4.5 · Quanto o usuário pode editar ou corrigir o brief

| Opção | Prós | Contras |
|---|---|---|
| **Read-only** | Mais simples · brief é registro auditável | Fato errado fica errado e mata a confiança |
| **Correção estruturada** ("este fato está errado" + campo livre) | Mitiga o risco crítico de alucinação `[V3 §12]` · gera dado de qualidade · atrito baixo | Precisa de identidade por fato dentro do brief |
| **Edição livre** | Vendedor faz do jeito dele | Vira editor de documento · destrói a auditabilidade da regra de confiança · escopo fora |

**Recomendação: read-only no MVP + um clique de "não bate" por brief; correção por fato entra logo depois.**

Por quê: o valor do brief está em ser **auditável** — a regra de confiança do V3 só funciona se fonte e tag não puderem ser sobrescritas silenciosamente. Correção deve ser **anotação sobre o fato**, nunca substituição do fato. Em 10 horas, um clique de "não bate" no brief inteiro já entrega o sinal de qualidade sem exigir identidade por fato.

---

### 4.6 · Feedback pós-reunião: o que capturar e com quanto atrito

| Opção | Prós | Contras |
|---|---|---|
| **Nada** | Zero atrito | Sem "% de briefings considerados úteis", o V3 perde uma métrica que ele mesmo classifica como "mensurável rapidamente" `[V3 §10]` |
| **1 pergunta, 1 clique, no e-mail** ("o brief ajudou? sim / não / não li") | Atrito quase zero · sem login · responde direto do celular | Sinal grosso, sem diagnóstico |
| **Formulário com avanço da reunião, qualidade por bloco, o que faltou** | Dado rico · instrumentaria reunião → próxima etapa | Atrito alto · vendedor não preenche formulário depois de reunião · e o V3 classifica avanço de pipeline como "validar depois" `[V3 §10]` |

**Recomendação: opção 2 no MVP.** A terceira opção captura o que o V3 explicitamente adiou. **A opção "não li" é a mais valiosa das três respostas** — separa "brief ruim" de "canal errado", que são problemas completamente diferentes e têm correções opostas.

---

### 4.7 · Política de dados e privacidade (LGPD)

**Aviso de escopo:** não sou parecer jurídico. O que segue é desenho de produto com consciência de risco, e precisa de revisão jurídica antes de qualquer cliente pagante.

| Opção | Prós | Contras |
|---|---|---|
| **Mínimo viável: só calendário + dados profissionais públicos** | Menor superfície de risco · consentimento claro do titular (o próprio vendedor) · dados dos participantes externos são profissionais e públicos | Contexto mais pobre |
| **Calendário + leitura de e-mail** | Contexto muito mais rico | Trata **e-mail de terceiros que nunca consentiram** · pedido que mais provavelmente aciona o guardião · exige DPA robusto |
| **Enriquecimento de pessoa por base de dados de contatos** | Padrão da categoria | Dado pessoal de terceiro sem relação prévia · risco alto no Brasil |

**Recomendação: opção 1 no MVP**, com quatro regras de produto `[E5]`:

1. **Fonte obrigatória por fato** — a regra de confiança do V3 `[V3 §8]` já produz, de graça, uma **trilha de auditoria**: para todo dado pessoal exibido, existe a origem registrada. Isso deixa de ser só antialucinação e vira ativo de conformidade.
2. **Só contexto profissional** — cargo, empresa, papel provável na decisão, manifestações públicas em contexto de trabalho. Nada de vida pessoal, mesmo que público.
3. **Direito de exclusão operável** — participante que solicitar deixa de ser perfilado; precisa existir um canal para isso.
4. **Retenção curta e declarada** — brief tem prazo de descarte definido. Não tenho base para recomendar o prazo exato sem input jurídico.

**O que seria preciso saber e ainda não sei:** quem é controlador e quem é operador na relação Antessala–cliente; se a base legal para pesquisar o participante externo é legítimo interesse; se o cliente PME tem DPO ou política de privacidade que cubra isso. **Este é o segundo maior buraco da jornada, depois do guardião — e provavelmente é a mesma pessoa.**

---

## 5 · Perguntas para validar nas entrevistas

Todas seguem a regra do roteiro existente: **perguntar sobre o passado, nunca sobre o futuro.** Nenhuma menciona o Antessala.

### Trilha A · Usuário (AE/vendedor) — acrescentar ao roteiro existente

| Item da jornada a testar | Pergunta exata | O que fecha |
|---|---|---|
| **Canal (4.1)** | *"Nas duas horas antes da sua última reunião importante, onde você estava olhando informação — e-mail, WhatsApp, CRM, celular, papel?"* | Onde o brief tem chance de ser lido — sem perguntar preferência |
| **Momento de entrega (Etapa 5)** | *"Quando exatamente você preparou aquela reunião? Na véspera, na manhã, no deslocamento, nos 5 minutos antes?"* | A antecedência real, não a ideal |
| **Triagem (Etapa 4)** | *"Das reuniões da sua semana passada, quantas você chamaria de importantes? O que faz uma ser importante?"* | O critério nativo de "reunião de receita" — o que a máquina precisa replicar |
| **Permissão (Etapa 2)** | *"Qual foi a última ferramenta que te pediu para conectar seu Google ou Outlook? Você conectou? O que passou pela sua cabeça?"* | Atrito real do OAuth, com comportamento passado |
| **Primeira conversa (4.4)** | *"Me conta a última primeira reunião com uma empresa que você não conhecia. O que você conseguiu descobrir antes, e o que só descobriu na conversa?"* | **A pergunta mais importante da Trilha A para este documento.** Testa se a fronteira defensável tem valor percebido |
| **Correção (4.5)** | *"Alguma ferramenta já te entregou informação errada sobre um cliente? O que você fez depois disso?"* | Custo de um fato errado — risco crítico do `[V3 §12]` |
| **Pós-reunião (4.6)** | *"Depois de uma reunião, o que você registra e onde? Quanto tempo depois?"* | Atrito realista do feedback |
| **Privacidade (4.7)** | Já coberto pela **pergunta 8** do roteiro: *"qual seria sua primeira preocupação?"* — **não induzir privacidade**; anotar se ela surge espontaneamente | Se privacidade é objeção nativa ou preocupação inventada |

### Trilha B · Comprador econômico — acrescentar ao roteiro existente

| Item da jornada a testar | Pergunta exata | O que fecha |
|---|---|---|
| **Guardião (Atores)** | **Já existe — pergunta 9:** *"Se uma ferramenta precisasse de acesso ao calendário, ao e-mail e ao CRM — quem decidiria isso aí dentro?"* **Follow-up novo:** *"E se fosse só o calendário, mudaria alguma coisa?"* | Testa diretamente a recomendação 4.3: se "só calendário" reduz o atrito de aprovação, o corte de escopo ganha um segundo motivo |
| **Onboarding (4.2)** | *"Quando vocês adotaram a última ferramenta do comercial, como foi a ativação do time? Quantos estavam usando de fato 30 dias depois?"* | O gap compra→adoção, com número real |
| **Compra por time (4.2)** | *"Já aconteceu de um vendedor contratar uma ferramenta por conta própria? O que você fez?"* | Testa `[V3 §11]` "não depender de compra individual do closer" com comportamento |
| **Relatório do gestor (Etapa 6)** | *"Da última ferramenta que você aprovou, como você decidiu que estava valendo? Que número você olhou?"* | O conteúdo do relatório mensal — na linguagem dele |
| **Privacidade (4.7)** | *"Alguma ferramenta já pediu acesso ao e-mail do time? O que aconteceu?"* | Se a leitura de e-mail é bloqueador real |
| **Churn (Etapa 7)** | **Já existe — pergunta 8:** *"Me conta a última ferramenta comercial que vocês cancelaram. Por quê?"* | Previsor de churn |

> **Nota de método, alinhada ao README.** A ENTREGA 5 registra que **verbatim PT-BR do ICP está em 0% e é estruturalmente indisponível** por busca pública. Isso significa que **nenhum item desta jornada tem validação externa** — as entrevistas são a única fonte possível. Cinco conversas não validam estatisticamente nada; produzem evidência comportamental. Apresentar exatamente nesse limite.

---

## 6 · Riscos da jornada que derrubam a tese

Cada risco abaixo está ancorado em uma linha do `[V3 §12 "O que ainda pode derrubar a tese"]`.

| # | Risco da jornada | Risco-mãe no V3 | Como se manifesta | Mitigação na jornada | Gravidade |
|---|---|---|---|---|---|
| 1 | **O vendedor nunca conecta o calendário** | "PME não perceber urgência" (crítico) | Gestor assina, 2 de 8 conectam, produto morre em 30 dias | Onboarding híbrido (4.2) · métrica de ativação em 7 dias · brief-amostra antes da compra | **Crítico** |
| 2 | **O brief chega e não é lido** | "Briefing virar commodity" (alto) | Mais um e-mail. Utilidade não medida, renovação sem argumento | Canal + momento validados na Trilha A · versão curta 30 min antes · a resposta "não li" (4.6) separa canal de conteúdo | **Crítico** |
| 3 | **Um fato errado no primeiro brief** | "Fatos errados ou alucinação" (crítico) | Vendedor cita dado errado na reunião. Confiança não volta | Fonte obrigatória por fato · DESCONHECIDO em vez de inferência · "não bate" em um clique (4.5) | **Crítico** |
| 4 | **Ruído por triagem ruim** | "PME não perceber urgência" (crítico) | Brief para reunião interna, para o dentista, para o 1:1. Vira spam | Triagem por domínio externo + duração · "não é reunião de receita" em 1 clique (Etapa 4) | **Alto** |
| 5 | **"Eu faço isso no ChatGPT em 5 minutos"** | "CRM + ChatGPT ser bom o bastante" (alto) | Se a jornada exige input, o usuário conclui que faz sozinho | A jornada **não pode pedir nada** depois da conexão. É a materialização do `[V3 §1]` autonomia — e é o argumento: o valor está em acontecer **sozinho, no momento certo, sem ninguém lembrar** | **Alto** |
| 6 | **O guardião trava depois do "sim" comercial** | Não previsto no §12 — **lacuna do V3**, registrada em `README.md:66` | Comprador aprova, TI/dono barra o acesso, venda morre no meio | Pedir só calendário (4.3) · mapear o guardião na pergunta 9 da Trilha B antes de qualquer proposta | **Crítico e não mapeado** |
| 7 | **O brief de primeira conversa sai vazio** | "Briefing virar commodity" (alto) | A fronteira defensável (4.4) vira "não sabemos" repetido três vezes | Reequilibrar peso dos blocos: "O que falta" e "Perguntas críticas" carregam · **testar na demo antes do pitch** | **Alto** |
| 8 | **"Mais um point solution fora do workflow"** | Adjacente a "briefing virar commodity" — reforçado pela ENTREGA 5 (Momentum: 88% dizem usar IA, 24% têm IA dentro do workflow de receita) | Comprador já ouviu esse pitch e já se decepcionou | Preparar resposta explícita. Cuidado: o relatório é de fornecedor da categoria (Momentum, hoje da Salesforce) — citar como "relatório da Momentum", nunca como dado neutro | **Alto** |
| 9 | **Sem medição, o cliente não vê ganho** | "Empresa ser imatura demais para medir" (alto) | Cliente usa, gosta, não consegue justificar renovação | Relatório mensal com as métricas do `[V3 §10]` · maturidade mínima já é condição de ICP `[V3 §5]` | **Médio** |
| 10 | **LGPD vira objeção de compra** | Não previsto no §12 — **lacuna do V3** | Pedido de acesso a e-mail aciona receio jurídico; venda trava | Escopo mínimo (4.7) · trilha de auditoria via fonte por fato · revisão jurídica antes de cliente pagante | **Alto, não mapeado** |

### As duas lacunas que o V3 não previu

Os riscos **6 (guardião)** e **10 (LGPD)** não estão na tabela de riscos do V3. Ambos nascem exatamente do que este documento acrescentou — a jornada. **Recomendo que os dois entrem no §12 do V3 na próxima revisão**, com a ressalva de que o guardião permanece não mapeado até a Trilha B rodar.

---

## 7 · Recomendações consolidadas

| # | Decisão | Recomendação | Origem |
|---|---|---|---|
| 1 | Canal | E-mail + link web read-only. WhatsApp na visão | `[E5]` |
| 2 | Onboarding | Híbrido: gestor contrata e configura, vendedor concede o próprio calendário | `[E5]`, ancorado em `[V3 §11]` |
| 3 | Integrações MVP | Só calendário | `[E5]`, ancorado em `[V3 §8]` + ENTREGA 5 |
| 4 | Sem contexto interno | DESCONHECIDO vira pergunta de discovery; brief muda de peso, não de estrutura | `[V3 §8 Regra de confiança]` + `[E5]` a forma |
| 5 | Edição | Read-only + "não bate" em 1 clique | `[E5]` |
| 6 | Feedback | 1 pergunta, 3 respostas, sem login, ~1h após a reunião | `[E5]`, alimenta `[V3 §10]` |
| 7 | Privacidade | Escopo mínimo + fonte por fato como trilha de auditoria. **Precisa de revisão jurídica** | `[E5]` |

### Onde eu não tenho base

1. **Quem é o guardião de acesso.** `README.md:66` declara não mapeado. Preciso da pergunta 9 da Trilha B.
2. **Penetração de Slack/Teams em PME brasileira de 3–15 vendedores.** Não há dado nas fontes deste kit.
3. **Prazo de retenção de dados adequado.** Precisa de input jurídico.
4. **Se o vendedor abre e-mail antes de reunião.** É a premissa que sustenta a recomendação 1 e ela é **hipótese**. A pergunta da Trilha A sobre "as duas horas antes" existe exatamente para testá-la — e se a resposta for WhatsApp, **a recomendação 1 cai**.
5. **Quanto tempo cada integração levaria de fato.** Estimativas de esforço são do @architect, não minhas.

---

## 8 · O que fazer agora

| Ordem | Ação | Por quê |
|---|---|---|
| 1 | Levar as decisões 4.1 a 4.7 para aprovação item a item da fundadora | Nada aqui é decisão do projeto até ser aprovado. É tudo `[E5]` |
| 2 | Acrescentar as 8 perguntas da Trilha A e as 6 da Trilha B ao roteiro | As entrevistas já vão acontecer; o custo marginal é zero |
| 3 | Testar o brief de primeira conversa (4.4) **antes** de fechar o pitch | Se ele sair vazio, a fronteira defensável não existe — e isso muda o pitch inteiro |
| 4 | Depois de aprovado, promover as decisões para uma seção nova do V3 | O V3 é o cânone. Este documento não é |

---

**Documento de proposta · @pm (Morgan) · 29 ago 2026**
**Fontes lidas:** `contexto-antessala.md` · `README.md` · `fontes/antessala-documento-consolidado-v3.html` (inteiro) · `achados-pesquisa-publica.md` (ENTREGA 2 e ENTREGA 5) · `roteiro-entrevistas-primarias.md`
**Nada foi gravado dentro de `estudos/`.**
