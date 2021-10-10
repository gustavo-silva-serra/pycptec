# pycptec
Módulo Python de integração com serviço de previsão meteorológica CPTEC/INPE ([Documentação](http://servicos.cptec.inpe.br/XML/))

Desenvolvi para uso pessoal em outro projeto, por isso a integração com todos os serviços disponibilizados pela CPTEC ainda é um trabalho em evolução.

* A previsão para os próximos 4 dias
* A listagem de cidades retorna no máximo 60 cidades
* Testado na versão 3.9.7

# Exemplo

Para buscar a previsão para São Paulo, SP

```python
from cptec import cptec
id = cptec.busca_id_cidade('sao paulo', 'SP')
for p in cptec.previsao(id):
  print(f'min={p.min} max={p.max} tempo={p.tempo} dia={p.dia}')
```

Para listar as cidades que possuem 'Porto' no nome

```python
from cptec import cptec
for cidade in cptec.lista_cidades('Porto'):
    print(cidade)
```
