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
        
        Parâmetros
        ----------
        id : str
            ID da cidade, utilizar busca_id_cidade() para encontrar o ID
            
        Retorno
        -------
        Uma lista de namedtuple Previsao(min,max,tempo,dia)
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
        
        Parâmetros
        ----------
        cidade : str
            Nome da cidade, informar sem acentos
        estado : str
            Sigla da UF
        '''
        for el in self.lista_cidades(cidade):
            if el[1].lower() == estado.lower():
                return el[2]
        return None
    
    @classmethod
    def lista_cidades(self, cidade=None):
        '''Retorna uma lista de cidades com suas respectivas UF e id 
        
        Parâmetros
        ----------
        cidade : str, opcional
            Filtro de nome da cidade, informar sem acentos (padrão None)
        
        Retorno
        -------
        list
            Lista de tuplas no formato (cidade,UF,id)
        '''
        url = self.BASE_URL + 'listaCidades'
        if cidade is not None:
            cidade = urllib.parse.quote(cidade)
            url += f'?city={cidade}'

        resposta = urllib.request.urlopen(url).read().decode('iso-8859-1')
        root = ET.fromstring(resposta)
        return [(el.find('nome').text, el.find('uf').text, el.find('id').text) for el in root]
    
    @classmethod
    def condicoes_atuais(self, estacao):
        url = self.BASE_URL + f'estacao/{estacao}/condicoesAtuais.xml'
        resposta = urllib.request.urlopen(url).read().decode('iso-8859-1')
        root = ET.fromstring(resposta)
        print(resposta)

    

# print(cptec.lista_cidades())
# ~ print("Codigo",cptec.busca_id_cidade("porto alegre", "rs"))
# ~ previsoes = cptec.previsao(237)
# ~ for p in previsoes:
    # ~ print(f'min={p.min} max={p.max} tempo={p.tempo} tempo={p.dia}')

cptec.condicoes_atuais(estacoes['RS']['Salgado Filho'])
