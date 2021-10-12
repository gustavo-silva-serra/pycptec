# pycptec
Módulo Python de integração com serviço de previsão meteorológica CPTEC/INPE ([Documentação](http://servicos.cptec.inpe.br/XML/))

Desenvolvi para uso pessoal em outro projeto, por isso a integração com todos os serviços disponibilizados pela CPTEC ainda é um trabalho em evolução.

* A previsão do tempo é para os próximos 4 dias
* A listagem de cidades retorna no máximo 60 cidades
* Testado em Python 3.9.7

# instalação
```
 pip install git+https://github.com/gustavo-silva-serra/pycptec
 ```

# exemplo

Para buscar a previsão para São Paulo, SP

```python
from cptec import Cptec
id = Cptec.busca_id_cidade('sao paulo', 'SP')
for p in Cptec.previsao(id):
  print(f'min={p.min} max={p.max} tempo={p.tempo} dia={p.dia}')
```

Para listar as cidades que possuem 'Porto' no nome

```python
from cptec import Cptec
for cidade in Cptec.lista_cidades('Porto'):
  print(cidade)
```

O parâmetro para a busca das condições é a sigla da estação metereológica. Favor consultar o dicionário cptec_siglas.estacoes.
```python
from cptec import Cptec
from cptec import estacoes
print(Cptec.condicoes_atuais(estacoes['RS']['Salgado Filho']))
```
