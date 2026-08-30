# -*- coding: utf-8 -*-
"""Gera o readiness brief (card 1 página) da Fórmula Distribuidora — montado à mão (Pessoa A + @analyst)."""
import html, os, subprocess, sys, datetime

C, H, D = "CONFIRMADO", "HIPÓTESE", "DESCONHECIDO"
BRASILAPI = "https://brasilapi.com.br/api/cnpj/v1/01581193000184"
BRASILAPI_F = "https://brasilapi.com.br/api/cnpj/v1/01581193000427"
SITE = "https://www.formuladistribuidora.com.br/"
SOBRE = "https://formuladistribuidora.com.br/sobre/"
LI_CO = "https://www.linkedin.com/company/formula-distribuidora-automotiva/about/"
LI_PB = "https://www.linkedin.com/in/paulobrenha/"
P_RECORDE = "https://www.linkedin.com/feed/update/urn:li:activity:7499050708210544480/"
P_ROTA = "https://www.linkedin.com/feed/update/urn:li:activity:7498325914192216064/"
P_141 = "https://www.linkedin.com/feed/update/urn:li:activity:7497963549617623042/"
NL_0906 = "https://pt.linkedin.com/pulse/como-alinhar-o-time-e-evitar-desespero-da-%C3%BAltima-semana-paulo-brenha-brnwc"
NL_0607 = "https://pt.linkedin.com/pulse/o-balan%C3%A7o-do-semestre-e-como-entrar-q3-sem-ressaca-paulo-brenha-fms3e"
PULSE_2408 = "https://www.linkedin.com/pulse/voltei-como-gerente-para-empresa-onde-fui-vendedor-de-paulo-brenha-idome/"

# (tag, texto, [(rótulo, url), ...])
ND = "https://ndmais.com.br/educacao/paulo-brenha-sobre-o-varejo-formulas-prontas-ja-nao-respondem-a-complexidade-do-mercado/"
CNDL = "https://cndl.org.br/varejosa/5-livros-para-pensar-vendas-lideranca-carreira-e-patrimonio-nos-negocios/"
TRIB = "https://www.tribunadosertao.com.br/variedades/2026/04/28/893328-proposito-margem-e-execucao-os-pilares-do-varejo-em-transformacao"
RELEASE = "https://www.issoesaopaulo.com.br/2026/06/paulo-brenha-ganha-espaco-como-voz-da.html"
INDEED_JOBS = "https://br.indeed.com/cmp/Formula-Produtos-Automotivos/jobs"
INDEED_REV = "https://br.indeed.com/cmp/Formula-Produtos-Automotivos/reviews"
JOOBLE = "https://br.jooble.org/vagas-de-emprego-formula-distribuidora"
LOGIN = "https://formuladistribuidora.com.br/login/"
GOIASLUB = "https://goiaslubrificantes.com.br/"
TIR_QS = "https://www.tirreno.com.br/quem-somos/"
TIR_AUTO = "https://www.tirreno.com.br/categoria/linha-automotiva/"
F_SHELL = "https://www.formuladistribuidora.com.br/produtos-shell/"
SHELL_COOL = "https://raizenlubrificantes.shell.com.br/para-empresas/linha-de-produto/shell-coolant"
TECLUB = "https://www.teclub.com.br/post/filtros-automotivos-atacado-goiania"

BLOCKS = []
def block(title, subtitle, items): BLOCKS.append((title, subtitle, items))

block("Why now", "OPORTUNIDADE · por que esta reunião existe (para a X)", [
 (H, "A Fórmula opera <b>portfólio multimarca</b> (Shell + Michelin + BFGoodrich + Tirreno, 1.500+ produtos, 13 mil PDVs), mas <b>aditivos quase não aparecem</b>: a Tirreno é citada uma vez no site e não tem página; não há catálogo próprio. Ou o mix de químicos é pequeno, ou não é prioridade, ou vive só no portal B2B — <b>qualquer das três é abertura para a X</b>. O post de 26/08 (<i>“141% da meta de lançamentos”</i>) mostra que a Fórmula lança produto e mede lançamento.", [("sobre", SOBRE), ("produtos Shell", F_SHELL), ("post 26/08", P_141)]),
 (C, "Ele mesmo publicou como quer ser vendido: <i>“O que destrava não é entusiasmo. É a conta que mostra ao comprador o que ele ganha, não o que a sua empresa ganha.”</i>", [("post 26/08", P_141)]),
 (D, "Quem pediu a reunião; se existe janela formal de revisão de mix ou processo de cadastro de fornecedor. → pergunta de abertura.", []),
])
block("O que sabemos", "CONTEXTO · empresa e interlocutor", [
 (C, "<b>FORMULA PRODUTOS AUTOMOTIVOS LTDA</b> · CNPJ 01.581.193/0001-84 · ATIVA · início de atividade 10/12/1996 · capital social R$ 11.560.886 · porte “DEMAIS” · Lucro Real 2016–2024 · CNAE 4681-8/05 <i>comércio atacadista de lubrificantes</i> + 9 CNAEs secundários (peças, pneus, varejo de lubrificantes, saneantes, transporte de carga).", [("BrasilAPI", BRASILAPI)]),
 (C, "Matriz: Rua T-55, 740, Setor Bueno, Goiânia/GO. Filial logística: Av. Jataí, Parque Industrial Vice-Pres. José Alencar, Aparecida de Goiânia/GO (desde 2013; CNAE de organização logística) — <b>é para lá que a X entregaria</b>.", [("BrasilAPI matriz", BRASILAPI), ("BrasilAPI filial", BRASILAPI_F)]),
 (C, "Empresa familiar com holding: Fernando Lima Sousa (administrador desde 1998) e Fernando Lima Sousa Filho (desde 2005); três holdings sócias desde 2017 (EFFE, FFPAR, FLPAR Participações).", [("BrasilAPI", BRASILAPI)]),
 (C, "Clientes: <i>“postos de combustível (Shell e multimarcas), centros automotivos, concessionárias, indústrias”</i> · <b>13 mil+ clientes · 200+ colaboradores · 1.500+ produtos</b> · atende GO, DF, TO, MS, MT. Site sem catálogo próprio: menu “Produtos Shell” (Helix, Advance, Rimula, “Outros”) redireciona para a Raízen; portal B2B com login; ERP <b>Protheus/TOTVS</b> citado em 2013.", [("site", SITE), ("sobre", SOBRE), ("produtos Shell", F_SHELL), ("login", LOGIN), ("Indeed avaliações", INDEED_REV)]),
 (H, "Dados que não fecham: fundação <b>1989</b> (site, como “Goiás Lubrificantes”) × <b>1996</b> (LinkedIn) × <b>12/1996</b> (Receita); cobertura <b>5</b> × <b>7 estados</b> (home × “sobre”). Não repetir “35 anos” nem “7 estados” como se fosse dado.", [("sobre", SOBRE), ("site", SITE), ("BrasilAPI", BRASILAPI)]),
 (D, "Histórico da X com a Fórmula: nenhum (1ª conversa). Faturamento, nº de RCAs, giro por PDV, margem praticada por categoria. → discovery.", []),
])
block("O que mudou", "SINAIS · o que aconteceu recentemente", [
 (C, "<b>Nenhuma notícia institucional da Fórmula em 2025–26</b> em fonte aberta e <b>nenhuma vaga aberta</b> (Indeed: <i>“No momento, não há vagas abertas na empresa”</i>; Jooble: nenhuma). Sem sinal público de expansão ou contratação comercial.", [("Indeed vagas", INDEED_JOBS), ("Jooble", JOOBLE)]),
 (C, "Quem mudou foi o interlocutor: <b>ciclo de visibilidade em 2026</b> — livro <i>“Varejo com propósito e resultado”</i> (CNDL, 17/06), entrevista ND Mais (07/06): <i>“Fórmulas prontas já não respondem à complexidade do mercado”</i>, release de assessoria republicado em 3 portais (jun/26).", [("CNDL", CNDL), ("ND Mais", ND), ("release", RELEASE)]),
 (H, "<i>“141% da meta de lançamentos”</i> (post 26/08): a Fórmula acabou de rodar um ciclo de lançamentos acima da meta — o comprador está com <b>apetite e métrica de lançamento frescos</b>. Não se sabe de que produto/marca.", [("post 26/08", P_141)]),
 (H, "<i>“A maior operação Shell da América Latina”</i> aparece só em texto dele e em releases derivados; sem fonte Shell/Raízen. Usar como elogio-pergunta, não como fato.", [("post 27/08", P_ROTA), ("Tribuna", TRIB)]),
])
block("Quem está na mesa", "INTERLOCUTOR · papel provável na decisão", [
 (C, "<b>Paulo Brenha</b> — Diretor Comercial (<b>comprador</b>). Vendedor de rota em 2007; passagens por J&amp;J, Mondelez, Philip Morris, Bimbo, Shell Select e Oxxo; 29.191 seguidores, publica a cada 1–4 dias. <b>Vem de indústria de bens de consumo</b>: fala a língua de fabricante — giro, margem, positivação, lançamento.", [("perfil", LI_PB), ("Tribuna", TRIB), ("Pulse 24/08", PULSE_2408)]),
 (H, "Papel: decide o comercial, mas <b>entrada de marca nova no mix</b> pode passar pelo dono (Fernando Lima Sousa Filho), por compras e pela relação com a Shell. → confirmar quem aprova fornecedor.", [("BrasilAPI", BRASILAPI)]),
 (C, "Como ele pensa: <i>“Você só pode gerenciar as atividades que levam à receita.”</i> · <i>“qual é o evento na agenda do cliente que obriga ele a assinar”</i> · <i>“Recorde é diagnóstico, não troféu.”</i> · <i>“A execução é o real. A estratégia é a hipótese.”</i>", [("newsletter 09/06", NL_0906), ("post 29/08", P_RECORDE), ("post 27/08", P_ROTA)]),
 (D, "Se haverá comprador/categoria, gerente de compras ou o dono na reunião. → perguntar ao confirmar a agenda.", []),
])
block("O que falta", "gaps de qualificação (para a X)", [
 (D, "Se há <b>restrição contratual com a Shell</b> para químicos/aditivos de terceiros no mix da Fórmula.", []),
 (D, "Quantos SKUs <b>Tirreno</b> a Fórmula realmente estoca e giram (linha completa ou meia dúzia?) e se carrega <b>Shell Coolant</b> — define se a conversa é “substituir” ou “preencher lacuna”.", []),
 (D, "Processo de entrada de fornecedor: cadastro, margem mínima, verba de lançamento, treinamento de RCA, prazo de pagamento, logística (entrega em Aparecida).", []),
 (D, "Giro mínimo por PDV para um item ficar no mix e como a Fórmula mede um lançamento nos primeiros 90 dias.", []),
])
block("Riscos", "o que pode travar a X", [
 (C, "<b>Concorrente direto já dentro da casa:</b> Tirreno é marca da <b>Moove (grupo Cosan)</b>, com P&amp;D próprio — aditivos de radiador (E-Coolant, Aditech), fluidos de freio (DOT 3/4/5.1), descarbonizantes (aditivo gasolina/flex/diesel, DPF Cleaner), limpa-A/C, multiuso. A X entra como segunda marca e precisa de argumento de margem/giro, não de “produto melhor”.", [("Tirreno quem somos", TIR_QS), ("linha automotiva", TIR_AUTO), ("sobre", SOBRE)]),
 (H, "<b>Sobreposição Shell em arrefecimento</b>: a Raízen tem linha <b>Shell Coolant</b> (4 SKUs) na seção para onde o link “Outros Produtos” da Fórmula aponta. Restrição contratual para químicos de terceiros: não verificada.", [("Shell Coolant", SHELL_COOL), ("produtos Shell", F_SHELL)]),
 (H, "<b>Escala</b>: 13 mil PDVs em 5–7 estados. A X (PME) precisa provar capacidade de abastecer sem ruptura — a pergunta dele será <i>“quem faz isso acontecer numa terça-feira comum, com a equipe incompleta?”</i>", [("sobre", SOBRE), ("post 27/08", P_ROTA)]),
 (C, "Ele desqualifica entusiasmo, número de pico e solução pronta: <i>“Enquanto o argumento for que o produto é incrível, você está pedindo um favor.”</i> · <i>“Recorde é diagnóstico, não troféu.”</i> · <i>“Fórmulas prontas já não respondem…”</i>", [("post 26/08", P_141), ("post 29/08", P_RECORDE), ("ND Mais", ND)]),
 (C, "Plano B da X em Goiás: <b>Goiás Lubrificantes</b> é multimarca em óleo (Motul, Shell, Mobil, Petronas, YPF, Lubrax) mas <b>sem aditivos</b> nas páginas lidas; quem declara distribuir aditivos em Goiânia é a <b>Teclub</b> (marcas não nomeadas). Sem plano B forte, a X tem menos alavanca — não blefar.", [("goiaslubrificantes", GOIASLUB), ("Teclub", TECLUB)]),
 (H, "Decisor ausente: empresa familiar com holding — reunião boa com o diretor pode não avançar sem o dono.", [("BrasilAPI", BRASILAPI)]),
])
block("Perguntas críticas", "ABORDAGEM · derivadas dos gaps reais", [
 (D, "“Como a Fórmula decide colocar uma marca nova no mix — quem decide, que números olha, e o que fez o último lançamento bater 141%?”", [("post 26/08", P_141)]),
 (D, "“Tirreno hoje é linha completa ou alguns SKUs? Vocês carregam Shell Coolant? Existe restrição com a Shell para químicos de terceiros?”", [("Tirreno", TIR_AUTO), ("Shell Coolant", SHELL_COOL)]),
 (D, "“Que giro por PDV um item precisa ter para ficar, e como vocês medem um lançamento nos primeiros 90 dias?”", []),
 (D, "“O que vocês esperam do fornecedor no lançamento — treinamento de RCA, material de PDV, bonificação, prazo?”", []),
 (D, "“Quem além de você aprova um fornecedor novo — o Fernando, compras, a Shell?”", []),
])
block("Resultado esperado", "ABORDAGEM · o que já dá para propor", [
 (H, "Não é fechar pedido. É sair com <b>(1)</b> o processo e o critério de entrada de marca, <b>(2)</b> resposta sobre restrição Shell e sobre o espaço da Tirreno, <b>(3)</b> nome de quem aprova, e <b>(4)</b> um teste proposto: <b>1 região (ex.: DF) · N PDVs · 90 dias · meta de giro combinada</b> — com data no calendário dele para a revisão.", [("newsletter 09/06", NL_0906)]),
 (C, "Argumento no vocabulário dele: levar <i>“a conta que mostra ao comprador o que ele ganha”</i> — margem por PDV e giro projetado, não “produto incrível” — e mostrar <i>quem executa numa terça-feira comum</i>: plano de abastecimento e de positivação da X.", [("post 26/08", P_141), ("post 27/08", P_ROTA)]),
])

def render():
    tagcls = {C:"c", H:"h", D:"d"}
    out = []
    for title, sub, items in BLOCKS:
        lis = []
        for tag, text, links in items:
            l = " ".join(f'<a href="{html.escape(u)}">{html.escape(lbl)}</a>' for lbl, u in links)
            lis.append(f'<li><span class="tag {tagcls[tag]}">{tag}</span><span class="t">{text}</span>{(" <span class=src>[" + l + "]</span>") if l else ""}</li>')
        out.append(f'<section><h2>{html.escape(title)} <small>{html.escape(sub)}</small></h2><ul>{"".join(lis)}</ul></section>')
    n_src = len({u for _,_,items in BLOCKS for _,_,links in items for _,u in links})
    counts = {t: sum(1 for _,_,items in BLOCKS for tg,_,_ in items if tg==t) for t in (C,H,D)}
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    css = """
    @page{size:A4;margin:6mm}
    body{font-family:-apple-system,Helvetica,Arial,sans-serif;color:#111;margin:0;font-size:7.4pt;line-height:1.2}
    header{border-bottom:2px solid #111;padding-bottom:4px;margin-bottom:6px;display:flex;justify-content:space-between;align-items:flex-end}
    header h1{font-size:14pt;margin:0}header .meta{font-size:8pt;color:#444;text-align:right}
    .legend{font-size:7.5pt;color:#333;margin:0 0 6px}
    .grid{columns:2;column-gap:10px}
    section{break-inside:avoid;margin-bottom:5px}
    h2{font-size:9.5pt;margin:4px 0 2px;border-bottom:1px solid #999;padding-bottom:1px}
    h2 small{font-weight:normal;color:#666;font-size:7.5pt}
    ul{margin:0;padding:0;list-style:none}li{margin:0 0 2px;padding-left:0}
    .tag{display:inline-block;font-size:6.6pt;font-weight:700;padding:0 4px;border-radius:3px;margin-right:4px;vertical-align:middle;letter-spacing:.2px}
    .tag.c{background:#d8f0dc;color:#125c26}.tag.h{background:#fff0c2;color:#6b4d00}.tag.d{background:#e8e8e8;color:#444}
    .src{font-size:7pt;color:#1a56b0}.src a{color:#1a56b0;text-decoration:none}.src a+a:before{content:" · ";color:#888}
    footer{margin-top:6px;border-top:1px solid #999;padding-top:3px;font-size:7pt;color:#555;display:flex;justify-content:space-between}
    """
    page = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Readiness Brief · Fórmula Distribuidora · Paulo Brenha</title><style>{css}</style></head><body>
<header><div><h1>Readiness Brief · Empresa X → Fórmula Distribuidora Automotiva</h1>
<div class="legend">Preparado para o <b>vendedor da X</b> · <b>Etapa 0 (X, fictícia):</b> PME fabricante de aditivos/químicos automotivos, 8 vendedores, vende para distribuidoras; objetivo: entrar no mix da Fórmula (13 mil PDVs) · 1ª conversa · comprador: <b>Paulo Brenha, Diretor Comercial</b> · Goiânia/GO &nbsp;|&nbsp; <span class="tag c">CONFIRMADO</span>tem fonte, com link &nbsp;<span class="tag h">HIPÓTESE</span>inferido, com o porquê &nbsp;<span class="tag d">DESCONHECIDO</span>vira pergunta de discovery</div></div>
<div class="meta">Antessala · Meeting Readiness Agent<br>montado à mão (Pessoa A + @analyst) · {now}<br>{n_src} fontes abertas · {counts[C]} confirmados · {counts[H]} hipóteses · {counts[D]} desconhecidos</div></header>
<div class="grid">{"".join(out)}</div>
<footer><span>Regra: sem fonte aberta não vira fato. Só informação profissional pública; nenhuma rede social pessoal. Fonte de cada linha entre colchetes.</span><span>Antessala · hackathon ATON · 30/08/2026</span></footer>
</body></html>"""
    return page

if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv) > 1 else "."
    p = os.path.join(outdir, "Readiness-Brief-Formula-Distribuidora.html")
    open(p, "w", encoding="utf-8").write(render())
    pdf = p.replace(".html", ".pdf")
    r = subprocess.run(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome","--headless=new","--disable-gpu","--no-pdf-header-footer",f"--print-to-pdf={pdf}","file://"+os.path.abspath(p)],capture_output=True,text=True,timeout=60)
    print("html:", p); print("pdf:", pdf if os.path.exists(pdf) else "FALHOU "+r.stderr[-300:])
