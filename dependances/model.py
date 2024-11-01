
from dependances.url import Url
from dependances.output import Output

class Model:
    """
    # model
    represente une table
    """

    def __init__(self,model:str, url:Url, output:Output) -> None:
        self.relation = []
        self.url = url
        self.model = model
        self.output = output

        # recuperer tout les attribut
        self.attr = self.url.fetch(self.url.WORL['attr'], model=self.model)[1]
        self.specify =  self.url.fetch(self.url.WORL['specify'], model=self.model)[1]
        self.fillable = self.url.fetch(self.url.WORL['fillable'], model=self.model)[1]
    
    def create(self):
        # rempli les champs
        champs = {}
        for champ in self.fillable:
            champs[champ] = self.output.prompt_for_create(champ)

        # envoyer les données
        data_request, data = self.url.fetch(self.url.WORL['store'], model=self.model, data=champs)
        
        # afficher l'enregistrement
        if data.get('data'):
            self.output.console.clear()
            # affiche l'url, la method et le code de reponse
            self.output.url_code(data_request)

            # affichage de l'enregistrement
            model_id = data['data']['id']
            self.output.model(self.model, id=model_id, data=data)
        
        # afficher les erreur
        else:
            errors =[v[0] for k,v in data.items()]
            self.output.display_errors(errors)
            
    def show_attr(self, specify=False):
        url = self.url.parse_url(self.url.WORL['specify' if specify else 'attr'])

        self.output.show_attr(
            model=self.model,
            method=url[0],
            url=url[1],
            data=self.specify if specify else self.attr,
            specify=specify
        )

    def any_view(self):
        data = self.url.fetch(self.url.WORL['anyView'], model=self.model)
        
        if 'meta' in data[1]:
            self.output.show_table_for_pagination(self.model, data)
            self.pagination(data)
        else:
            self.output.show_table(self.model, data)

    def pagination(self,data):
        next = data[1]['links']['next']
        prev = data[1]['links']['prev']
        choix = int(self.output.prompt_for_pagination(next,prev))
        self.output.console.clear()
        while choix != 4:
            if choix == 1:
                data = self.url.fetch(url=data[1]['links']['next'], model=self.model)
                self.output.show_table_for_pagination(self.model, data)

            elif choix == 2:
                data = self.url.fetch(url=data[1]['links']['prev'], model=self.model)
                self.output.show_table_for_pagination(self.model, data)

            next = data[1]['links']['next']
            prev = data[1]['links']['prev']
            choix = int(self.output.prompt_for_pagination(next,prev))
            self.output.console.clear()

    def show(self, id):
        # verifi si l'id existe
        data_request, data = self.url.fetch(self.url.WORL['show'], model=self.model,id=id)
    
        if 404 in data_request:
            self.output.display_errors(title='id inconnu',errors=["l'id inqiqué n'exite pas"])
            return 'error' # levez une errer personnalisée

        # affiche l'url, la method et le code de reponse
        self.output.url_code(data_request)
        
        # affichage
        self.output.model(self.model, id, data)

    def update(self, id):
        # verifi si l'id existe
        data_request, data = self.url.fetch(self.url.WORL['show'], model=self.model,id=id)
        
        if 404 in data_request:
            self.output.display_errors(title='id inconnu',errors=["l'id inqiqué n'exite pas"])
            return 'error' # levez une errer personnalisée

        # rempli les champs
        champs = {}
        for champ in self.fillable:
            self.output.panel(
                message=data['data'][champ],
                color='cyan',
                show=True,
                justify="left",
                title='valeur actuelle du champ '+ champ,
            )
            champs[champ] = self.output.prompt_for_create(champ)

        # envoyer les données
        data_request, data = self.url.fetch(
            self.url.WORL['update'],
            model=self.model,
            id=id,
            data=champs
        )
        
        # afficher l'enregistrement
        if data.get('data'):
            self.output.console.clear()
            # affiche l'url, la method et le code de reponse
            self.output.url_code(data_request)

            # affichage de l'enregistrement
            model_id = data['data']['id']
            self.output.model(self.model, id=model_id, data=data)
        
        # afficher les erreur
        else:
            errors =[v[0] for k,v in data.items()]
            self.output.display_errors(errors)

    def delete(self, id):
        # verifi si l'id existe
        data_request, data = self.url.fetch(self.url.WORL['show'], model=self.model,id=id)
        
        if 404 in data_request:
            self.output.display_errors(title='id inconnu',errors=["l'id inqiqué n'exite pas"])
            return 'error' # levez une errer personnalisée
        
        data_request, data = self.url.fetch(self.url.WORL['destroy'], model=self.model,id=id)
        
        self.output.panel(
                message= str(data['data']),
                color='green',
                show=True,
                justify="left",
                title=f'destroy {self.model} {id}',
            )

    def belongsTo():
        '''
        relation de 1, n
        sert a déterminer le parent
        pour faire un select lors de la creation
        '''
        pass

    def hasMany():
        '''
        relation de 1, n
        sert a déterminer les enfants
        '''
        pass

    def belongsToMany():
        '''
        relation de 1, n
        sert a déterminer le parrent
        '''
        pass




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

'''