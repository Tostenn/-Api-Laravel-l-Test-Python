
from requests import get, post, delete
from os import get_terminal_size
from random import choice


base = 'http://127.0.0.1:8000/api/tag/'

URL = {
    'anyVew' :base,
    'attr' :base +'attr',
    'detaille' :base +'attr?detail=1',
    'create' :base +'create',
    'show' : lambda _ : base +f'{_}/show',
    'update' : lambda _ : base +f'{_}/update',
    'delete' : lambda _ : base +f'{_}/delete',
}


def pull(url:str) -> object|bool:
    '''
    # PULL
    ## recuper les données
    `url` url Api
    '''
    try: return get(url).json()
    except: return False

def remove(url:str) -> object|bool:
    '''
    # REMOVE
    ## supprime une occurence dans la table
    `url` url Api
    '''
    try: return delete(url).json()
    except: return False

def push(url:str, data:object) -> object|bool:
    '''
    # PUSH
    ## save data
    `url` url Api | `data` data Model
    '''
    try: return post(url, data=data).json()
    except :  return False

def parse_date(
    data:list[object],
    liste:bool = False,
    objets:bool = False,
    error:bool = False
    ) -> None:
    '''
    # PARSE DATA
    ## formate les données
    `data` données
    '''
    if liste: 
        for i in data:
            print(f"{'-':-^50s}")
            print(f'{rouge if error else vert} {i}')
    elif objets:
        for k,v in data.items():
            v = v if type(v) != type([]) else v[0]
            print(f'{gris}{k}:{rouge if error else vert} {v}')
    else :
        for i in data:
            print(f"{'-':-^50s}")
            for k,v in i.items():
                print(f'{gris}{k}:{rouge if error else vert} {v}')
    
    print(blanc)

# couleur de style poour rendre l'exercution plus fluide
vert = '\x1b[32m'
blanc = '\x1b[37m'
jaune = '\x1b[33m'
rouge = '\x1b[31m'
gris = f'\x1b[38;5;{240}m'
bleu_clair = f'\x1b[38;5;{123}m'


barre = lambda c,_: f'{blanc}{'T_xOx_T':-^50s}\n{c}{_}{blanc}'

error = barre(rouge,'valeur incorrect')

logos = [
r'''
░█▀█░█▀█░▀█▀░░░█░░░█▀█░█▀▄░█▀█░█░█░█▀▀░█░░░░░░█░░░░▀█▀░█▀▀░█▀▀░▀█▀░░░█▀█░█░█░▀█▀░█░█░█▀█░█▀█
░█▀█░█▀▀░░█░░░░█░░░█▀█░█▀▄░█▀█░▀▄▀░█▀▀░█░░░░░░█░░░░░█░░█▀▀░▀▀█░░█░░░░█▀▀░░█░░░█░░█▀█░█░█░█░█
░▀░▀░▀░░░▀▀▀░░░▀▀▀░▀░▀░▀░▀░▀░▀░░▀░░▀▀▀░▀▀▀░░░░▀░░░░░▀░░▀▀▀░▀▀▀░░▀░░░░▀░░░░▀░░░▀░░▀░▀░▀▀▀░▀░▀''',r'''
    _        _   _                          _   _   _____       _     ___      _   _             
   /_\  _ __(_) | |   __ _ _ _ __ ___ _____| | | | |_   _|__ __| |_  | _ \_  _| |_| |_  ___ _ _  
  / _ \| '_ \ | | |__/ _` | '_/ _` \ V / -_) | | |   | |/ -_|_-<  _| |  _/ || |  _| ' \/ _ \ ' \ 
 /_/ \_\ .__/_| |____\__,_|_| \__,_|\_/\___|_| | |   |_|\___/__/\__| |_|  \_, |\__|_||_\___/_||_|
       |_|                                     |_|                        |__/                   ''',r"""
 _     ||         |  ____     _      
//\pi  L_]aravel  |   L|est  ||)ython
                  |          L|      """
]

cols = get_terminal_size().columns

def logo(logo:list):
    if cols >= 97:
        return choice(logos)
    else : return logo[2]

logo_ = logo(logos)
connect = True
header = lambda _='',connect= True : f'{vert}{logo_} \n {f"projet Vente | table Tags{_}{blanc} | serveur: {f'{vert}connecter' if connect else f' {rouge}deconnecter'}":^{len(logo_.split('\n')[2])}}'
def ma_fonction(param):
    """Calcule la valeur du paramètre.

    Args:
        param (int): Un paramètre entier.

    Returns:
        int: Le double de param.
    """
    return param * 2


'''
rendre ce script en une framework

- creer un modele de url
    - /table: renvoir toute les tables de la bd
    - /model: revoir une pagination
    - /model/relation: renvoir toute les relations (nom des table en relation)
    - /model/attr: revoir les attribut de la table
    - /model/attr/details: revoir les details des attribut de la table
    - /model/attr/fillable: revoir les attribut fillable de la table
    - /model/create: crée une nouvelle instance du model
    - /model/{model}/show: afficher une instance du model
    - /model/{model}/update: mettre à jours une instance du model
    - /model/{model}/delete:supprimé une instance du model

- fonction
    - recupérer automatiquement les données des relation lors de l'affiche
        ex: affiche post et lors de l'affiche on voir un _id on verifi si le nom qui précede est dans /table
            si oui on récupere la données et on affiche un seul attre comme nom, name, titre ou title
    - coder avec les bonne pratique
    - faire de la programation orienté objet 
    - qu'il soit modulable

- librairy
    - rich: pour l'affichage style du terminal
    - trio: pour l'asynchrone
    - Progressbar: pour affiche les bar de progression
    - flake8: pour le respect de la comvention pep
    
'''