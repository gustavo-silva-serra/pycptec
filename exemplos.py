from cptec import cptec
from cptec_siglas import estacoes

id = cptec.busca_id_cidade("porto alegre", "rs")
previsoes = cptec.previsao(id)
for p in previsoes:
    print(f'min={p.min} max={p.max} tempo={p.tempo} tempo={p.dia}')
