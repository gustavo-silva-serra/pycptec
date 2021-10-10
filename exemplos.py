from cptec import cptec
from cptec_siglas import estacoes

# Busca a previsão para Porto Alegre
id = cptec.busca_id_cidade("porto alegre", "rs")
previsoes = cptec.previsao(id)
for p in previsoes:
    print(f'min={p.min} max={p.max} tempo={p.tempo} dia={p.dia}')

# Listar cidades 
for cidade in cptec.lista_cidades('Rio de'):
    print(cidade)