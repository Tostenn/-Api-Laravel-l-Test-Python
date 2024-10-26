from repertoire import cls, verch
from setup import *

choix = None

while choix != 0:
    cls()
    info = f'''{header()}{gris}
1 - listing
2 - create
3 - show
4 - update
5 - delete
0 - quitter
-> {bleu_clair}'''

    choix = verch(info,error,deb=0,fin=5)

    # listing 
    if choix == 1:
        ch = None
        while ch != 0:
            cls()
            info = f'''{header(' | listing',connect)} {gris}
1 - data
2 - attribut
3 - attribut détallé
0 - retour
-> {bleu_clair}'''
            ch = verch(info,error,deb=0,fin=3)
            
            if ch == 0 : continue
            
            elif ch == 1:
                cls()
                data = pull(URL['anyVew'])
                if not data:
                    connect = False
                    continue
                connect = True
                print(barre(vert,f'listing Tags | page {jaune}{data['meta']['current_page']}{vert} / {data['meta']['last_page']}'))
                
                parse_date(data['data'])

                # la pagination

                ch_ = None
                while ch_ != 0:
                    info = f'''pagination
1 - suivant
2 - précedent
0 - retour
-> {bleu_clair}'''
                    ch_ = verch(info,error,deb=0,fin=2)
                    cls()
                    if ch_ == 1 :
                        if data['links']['next']:
                            data = pull(data['links']['next'])
                            print(barre(vert,f'listing Tags | page {jaune}{data['meta']['current_page']}{vert} / {data['meta']['last_page']}'))
                            parse_date(data['data'])            
                        else : print(barre(rouge,"c'est la derniére page"))
                    elif ch_ == 2:
                        if data['links']['prev']:
                            data = pull(data['links']['prev'])
                            print(barre(vert,f'listing Tags | page {jaune}{data['meta']['current_page']}{vert} / {data['meta']['last_page']}'))
                            parse_date(data['data'])            
                        else : print(barre(rouge,"il n'y a pas de page qui précede celle là"))

            elif ch == 2:
                cls()
                data = pull(URL['attr'])
                
                if not data:
                    connect = False
                    continue

                print(barre(vert,f'listing Columns Tags | Columns {jaune}{len(data)}'))
                parse_date(data,True)
                input()
            
            elif ch == 3:
                cls()
                data = pull(URL['detaille'])

                if not data:
                    connect = False
                    continue
                
                print(barre(vert,f'listing Columns Tags | Columns detalle {jaune}{len(data)}'))
                parse_date(data)
                input()

    # create
    elif choix == 2:
        name = input(f'{gris}entrer le nom du tag : {bleu_clair}')
        data = {"nom":name}
        data = push(URL['create'], data)
        cls()
        if not data:
            connect = False
            continue
        elif data.get('data'):
            print(barre(vert,f'Create new Tags | Tag id: {jaune}{data["data"]['id']}{blanc}'))
            parse_date(data=data['data'], objets=True)
        else :
            print(barre(vert,f'Create new Tags | {rouge}Error !{blanc}'))
            parse_date(data=data, objets=True, error=True)
        input()
    
    # shpw
    elif choix == 3:
        name = input(f'{gris}entrer le nom ou l\'id du tag : {bleu_clair}')
        data = pull(URL['show'](name))
        if not data:
            connect = False
            continue
        elif data.get("data"):
            print(barre(vert,f'Show Tags | Tag number: {jaune}{len(data["data"])}{blanc}'))
            cls()
            parse_date(data=data['data'])
        else : 
            print(barre(rouge,f'Show Tags | Aucune correspondance trouver{blanc}'))
        input()

    # update
    elif choix == 4: 
        tag_id = input(f'{gris}entrer l\'id du tag : {bleu_clair}')
        data = pull(URL['show'](tag_id))
        if not data:
            connect = False
            continue
        elif data.get("data"):
            print(barre(vert,f'Update Tags | Tag ID: {jaune}{tag_id}{blanc}'))
            cls()
            parse_date(data=data['data'])
       
            name = input(f'{gris}entrer le nouveau nom du tag : {bleu_clair}')
            data = {"nom":name}
            data = push(URL['update'](tag_id), data)
            cls()

            if data.get('data'):
                print(barre(vert,f'Update Tags | Tag id: {jaune}{data["data"]['id']}{blanc}'))
                parse_date(data=data['data'], objets=True)

            else :
                print(barre(vert,f'Update Tags | {rouge}Error !{blanc}'))
                parse_date(data=data, objets=True, error=True)


        else : 
            print(barre(rouge,f'Update Tags | Aucune correspondance trouver{blanc}'))
        
        input()

    # delete
    elif choix == 5:
        tag_id = input(f'{gris}entrer l\'id du tag : {bleu_clair}')
        data = pull(URL['show'](tag_id))
        if not data:
            connect = False
            continue
        elif data.get("data"):
            print(barre(vert,f'Delete Tags | Tag ID: {jaune}{tag_id}{blanc}'))
            cls()
            parse_date(data=data['data'])
       
            c = input(f'{gris}voulez vous vraiment supprimer ce tag (o/n) (defaut=o) : {bleu_clair}')
            if c.lower() == 'n': continue
            data = remove(URL['delete'](tag_id))
            cls()

            if data.get('data'):
                print(barre(vert,f'Delete Tags | Tag id: {jaune}{tag_id}{blanc}'))
                

            else :
                print(barre(vert,f'Delete Tags | {rouge}Error !{blanc}'))
                parse_date(data=data, objets=True, error=True)


        else : 
            print(barre(rouge,f'Delete Tags | Aucune correspondance trouver{blanc}'))
        
        input()
    elif choix == 5:
        print(f'{gris}end programm.{blanc}')
