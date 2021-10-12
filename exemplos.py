from cptec import Cptec
from cptec import estacoes

# Busca a previsão para Porto Alegre
id = Cptec.busca_id_cidade("porto alegre", "rs")
previsoes = Cptec.previsao(id)
for p in previsoes:
    print(f'min={p.min} max={p.max} tempo={p.tempo} dia={p.dia}')

# Listar cidades 
for cidade in Cptec.lista_cidades('Rio de'):
    print(cidade)

# Busca as condições atuais para o aeroporto Salgado Filho
print(Cptec.condicoes_atuais(estacoes['RS']['Salgado Filho']))