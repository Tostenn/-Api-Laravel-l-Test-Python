
from dependances.url import Url
from dependances.output import Output
from env import DATA_TABLE

class Table:

    def __init__(self, url:Url, output:Output) -> None:
        
        # recupere la varible data_table
        self.belongsTo = DATA_TABLE['belongsTo']
        self.secondary_id = DATA_TABLE['secondary_id']
        
        self.output = output
        self.url = url
    
    def get(self, model:str) -> list|None:
        return self.belongsTo.get(model)
    
    def create(self, model, fillable):
        # rempli les champs
        champs = {}
        for champ in fillable:
            champs[champ] = self.output.prompt_for_create(champ)

        # envoyer les données
        data_request, data = self.url.fetch(self.url.WORL['store'], model=model, data=champs)
        
        # afficher l'enregistrement
        if data.get('data'):
            data = data['data']
            self.output.console.clear()
            # affiche l'url, la method et le code de reponse
            self.output.url_code(data_request)

            # recupere les relation parent du model
            data = self.check_belongsTo(data)

            # affichage de l'enregistrement
            model_id = data['id']
            self.output.model(model, id=model_id, data=data)
        
        # afficher les erreur
        else:
            # self.output.console.print(data)
            # exit()
            errors =[v[0] for k,v in data.items()]
            self.output.display_errors(errors)
    
    def show_attr(self, model, data, specify=False):
        url = self.url.parse_url(self.url.WORL['specify' if specify else 'attr'],model=model)

        self.output.show_attr(
            model=model,
            method=url[0],
            url=url[1],
            data=data,
            specify=specify
        )

    def any_view(self, model):
        data = self.url.fetch(self.url.WORL['anyView'], model=model)
        
        if 'meta' in data[1]:
            self.output.show_table_for_pagination(model, data)
            self.pagination(model, data)
        else:
            self.output.show_table(model, data)

    def pagination(self, model,data):
        next = data[1]['links']['next']
        prev = data[1]['links']['prev']
        choix = int(self.output.prompt_for_pagination(next,prev))
        self.output.console.clear()

        while choix != 4:
            if choix == 1:
                data = self.url.fetch(url=data[1]['links']['next'], model=model)
                self.output.show_table_for_pagination(model, data)

            elif choix == 2:
                data = self.url.fetch(url=data[1]['links']['prev'], model=model)
                self.output.show_table_for_pagination(model, data)

            elif choix == 3:
                self.output.console.clear()
                choix = self.output.prompt_for_id_pagination()
                
                if choix == 0:
                    self.output.console.clear()
                    
                else:
                    self.show(model=model, id=choix)
                        
                self.output.show_table_for_pagination(model, data)

            next = data[1]['links']['next']
            prev = data[1]['links']['prev']
            choix = int(self.output.prompt_for_pagination(next,prev))
            self.output.console.clear()

    def show(self, model, id):
        # verifi si l'id existe
        data_request, data = self.url.fetch(
            self.url.WORL['show'],
            model=model,
            id=id
        )
    
        if 404 in data_request:
            self.output.display_errors(title='id inconnu',errors=["l'id inqiqué n'exite pas"])
            return False # levez une errer personnalisée

        # affiche l'url, la method et le code de reponse
        self.output.url_code(data_request)
        
        # recupere les relation parent du model
        data = self.check_belongsTo(data['data'])
        
        # affichage
        self.output.model(model, id, data)

        return True

    def check_belongsTo(self, data:dict) -> dict:
        # vérifie si le model a une clé etrangere
        for key in data:
            data_show = self.get(key.replace(self.secondary_id,''))
            if self.secondary_id in key and data_show:
                key_table = key.replace(self.secondary_id,'')
                
                # on recupere la valeur de la clé secondaire
                data_request, data_ = self.url.fetch(self.url.WORL['show'], model=key_table, id=data[key])

                if 200 in data_request:

                    # si data_show contient une clé secondaire on recupere la valeur de la clé secondaire
                    if len(data_show) == 1 and self.secondary_id in data_show[0]:
                        key_table = data_show[0].replace(self.secondary_id, '')
                        data_request, data_ = self.url.fetch(self.url.WORL['show'], model=key_table, id=data_['data'][data_show[0]])
                    
                    data[key] = ' '.join([data_['data'].get(name) for name in self.get(key_table) if data_['data'].get(name)])
        
        return data

    def update(self, model, id, fillable):
        # verifi si l'id existe
        data_request, data = self.url.fetch(
            self.url.WORL['show'],
            model=model,
            id=id
        )
        
        if 404 in data_request:
            self.output.display_errors(title='id inconnu',errors=["l'id inqiqué n'exite pas"])
            return 'error' # levez une errer personnalisée

        # rempli les champs
        champs = {}
        # self.output.console.print(data)
        # exit()
        for champ in fillable:
            try:
                self.output.panel(
                    message=data['data'][champ],
                    color='cyan',
                    show=True,
                    justify="left",
                    title='valeur actuelle du champ '+ champ,
                )
                champs[champ] = self.output.prompt_for_create(champ)
            except:pass
        # envoyer les données
        data_request, data = self.url.fetch(
            self.url.WORL['update'],
            model=model,
            id=id,
            data=champs
        )
        
        # afficher l'enregistrement
        if data.get('data'):
            data = data['data']
            self.output.console.clear()
            # affiche l'url, la method et le code de reponse
            self.output.url_code(data_request)

            # affichage de l'enregistrement
            model_id = data['id']
            self.output.model(model, id=model_id, data=data)
        
        # afficher les erreur
        else:
            errors =[v[0] for k,v in data.items()]
            self.output.display_errors(errors)

    def delete(self, model, id):
        # verifi si l'id existe
        data_request, data = self.url.fetch(self.url.WORL['show'], model=model,id=id)
        
        if 404 in data_request:
            self.output.display_errors(title='id inconnu',errors=["l'id inqiqué n'exite pas"])
            return 'error' # levez une errer personnalisée
        
        data_request, data = self.url.fetch(self.url.WORL['destroy'], model=model,id=id)
        
        self.output.panel(
                message= 'True',
                color='green',
                show=True,
                justify="left",
                title=f'destroy {model} {id}',
            )
