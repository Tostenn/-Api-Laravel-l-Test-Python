
from dependances.url import Url
from dependances.output import Output

class Model:
    """
    # model
    represente une table laravel
    """

    def __init__(self,model:str, url:Url, output:Output) -> None:
        self.fillable = []
        self.relation = []
        self.url = url
        self.model = model
        self.output = output

        # recuperer tout les attribut
        self.attr =  self.url.fetch(self.url.WORL['attr'], model=self.model)[1]
        self.specify =  self.url.fetch(self.url.WORL['specify'], model=self.model)[1]
        
    def create():
        pass

    def show_attr(self):
        url = self.url.parse_url(self.url.WORL['attr'])
        self.output.show_attr(self.model,url[1],url[0],self.attr)
        pass

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
        data = self.url.fetch(self.url.WORL['show'], model=self.model,id=id)
        self.output.model(self.model, id, data)
        return True

    def update(id):
        pass

    def delete(id):
        pass

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