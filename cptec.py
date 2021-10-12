import urllib.request
import xml.etree.ElementTree as ET
import html
from cptec_siglas import siglas_tempo
from cptec_siglas import estacoes
from collections import namedtuple

class cptec:
    
    BASE_URL = "http://servicos.cptec.inpe.br/XML/"
    
    @classmethod
    def previsao(self, id):
        '''Retorna a previsao de tempo para 4 dias

        Informar ID da cidade, utilizar busca_id_cidade() para encontrar o ID

        Retorna uma lista de namedtuple Previsao(min,max,tempo,dia)
            min: Temperatura mínima
            max: Temperatura máxima
            tempo: Descrição textual de como estará o tempo
            dia: Dia no formato AAAA-MM-DD
        '''        
        url = f'{self.BASE_URL}cidade/{id}/previsao.xml'
        xml = urllib.request.urlopen(url).read().decode('iso-8859-1')
        root = ET.fromstring(xml)
        
        Previsao = namedtuple('Previsao', 'min,max,tempo,dia')
        
        return [Previsao(p.find('minima').text, p.find('maxima').text, siglas_tempo[p.find('tempo').text], p.find('dia').text)
                        for p in root.iter('previsao')]
   
    @classmethod
    def busca_id_cidade(self, cidade, estado):
        '''Retorna o id para uma determinada cidade e estado ou None caso nada seja encontrado
        
        Informar os parâmetros cidade e estado, ex.: (cidade='porto alegre', estado='rs')
        '''
        for el in self.lista_cidades(cidade):
            if el[1].lower() == estado.lower():
                return el[2]
        return None
    
    @classmethod
    def lista_cidades(self, cidade):
        '''Retorna uma lista de tuplas no formato (cidade,UF,id)

        Informar o nome da cidade sem acentos.
        '''
        
        cidade = urllib.parse.quote(cidade)
        url = self.BASE_URL + f'listaCidades?city={cidade}'
        resposta = urllib.request.urlopen(url).read().decode('iso-8859-1')
        root = ET.fromstring(resposta)
        return [(el.find('nome').text, el.find('uf').text, el.find('id').text) for el in root]
    
    @classmethod
    def condicoes_atuais(self, estacao):
        '''Retorna a situação atual do tempo
        
        Informar o nome da estação a qual se deseja obter a informação. A lista de estações pode ser 
        encontrada em cptec_siglas.estacoes.

        Retorna namedtuple Tempo(pressao,temperatura,tempo,data_hora)
        '''
        url = self.BASE_URL + f'estacao/{estacao}/condicoesAtuais.xml'
        resposta = urllib.request.urlopen(url).read().decode('iso-8859-1')
        root = ET.fromstring(resposta)
        Tempo = namedtuple('Tempo', 'pressao,temperatura,tempo,data_hora')
        return Tempo(root.find('pressao').text, root.find('temperatura').text, siglas_tempo[root.find('tempo').text], root.find('atualizacao').text)