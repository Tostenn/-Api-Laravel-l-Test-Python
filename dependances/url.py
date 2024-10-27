from repertoire import recujson
from requests import get

class Url:
    r"""
    # Url
    gestion des url  

    :param json: chemin vers le fichier json des url
    """
    WORL = {
        'anyView':'anyView',
        'show':'show',
        'table':'table',
        'update':'update',
        'destroy':'destroy',
        'store':'store',
        'fillable':'fillable',
        'specify':'specify',
        'attr':'attr',
    }
    
    def __init__(self, json:str) -> None:
        self.json = recujson(json)
        self.base = self.json['base']
        pass

    def parse_url(self,key:str, **kwargs):
        """formatage de l'url

            :param key: clé de route du fichier json
            :param kwargs: arguments suplémentaire
            
        """
        if self.json.get(key):
            key = self.json[key]
            url = '/' + key[0].format(model=kwargs.get('model',''),id=kwargs.get('id',''))
            url = self.base + url.replace('//','/')
            
            if kwargs.get('output_str'): return f'({key[1]}) {url}'
            if kwargs.get('output_url'): return url

            return key[1], url
        
        else: return 'error' # lever une exception personnaliser
        
    def pull(self, url:str):
        r""" recuper les données
       
        :param url: url pour la requête
        """
        try: return get(url)
        except: return False # lever une exception personnaliser

    def push(self, url:str, data:object, method:str):
        r""" envoir les données
       
        :param url: url pour la requête
        :param data: données à envoyer
        :param method: methode d'envoie
        """
        pass
    

    def fetch(self, key="", **kwargs):
        kwargs['output_str'] = False

        if not kwargs.get('url'):
            method, url = self.parse_url(key, **kwargs)
        else:
            url = kwargs.get('url')
            method = kwargs.get('method', 'get')

        if method.lower() == 'get':
            reponse = self.pull(url) 
            return ('get', url, reponse.status_code), reponse.json()
        
        