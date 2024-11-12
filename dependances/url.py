
from requests import get, post, put, delete, patch
from env import DATA_URL, HEADER

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
    
    def __init__(self) -> None:
        # rucupere les url
        self.DATA_URL = DATA_URL
        self.base = self.DATA_URL['base']

        # recupere les en têtê
        self.header = HEADER

    def parse_url(self,key:str, **kwargs):
        """formatage de l'url

            :param key: clé de route du fichier json
            :param kwargs: arguments suplémentaire
            
        """
        if self.DATA_URL.get(key):
            key = self.DATA_URL[key]
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
        try: return get(url, headers=self.header)
        except: return False # lever une exception personnaliser

    def push(self, url:str, data:dict, method:str="post"):
        r""" envoir les données
       
        :param url: url pour la requête
        :param data: données à envoyer
        """
        try:
            if method == 'post':
                return post(url,data=data, headers=self.header)
            elif method == 'put':
                return put(url,data=data, headers=self.header)
            elif method == 'patch':
                return patch(url,data=data, headers=self.header)
        except: return False # lever une exception personnaliser
    
    def destroy(self, url):
        r""" envoir les données
       
        :param url: url pour la requête
        :param data: données à envoyer
        """
        try:
            return delete(url, headers=self.header)
        except: return False # lever une exception personnaliser

    def fetch(self, key="", **kwargs):
        kwargs['output_str'] = False

        if not kwargs.get('url'):
            method, url = self.parse_url(key, **kwargs)
            
        else:
            url = kwargs.get('url')
            method = kwargs.get('method', 'get')
        
        method = method.lower()

        if method == 'get':
            reponse = self.pull(url) 
        
        elif method in ['put', 'patch', 'post']:
            reponse = self.push(url,kwargs.get('data'),method)
        
        elif method == 'delete':
            reponse = self.destroy(url)
            
        else: return None
        
        return (method, url, reponse.status_code), reponse.json()
        
        