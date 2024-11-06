
from dependances.table import Table

class Model:
    """
    # model
    represente une table
    """

    def __init__(self,model:str, table:Table) -> None:
        self.model = model
        self.table = table

        # recuperer tout les attribut
        self.attr = self.table.url.fetch(self.table.url.WORL['attr'], model=self.model)[1]
        self.specify = self.table.url.fetch(self.table.url.WORL['specify'], model=self.model)[1]
        self.fillable = self.table.url.fetch(self.table.url.WORL['fillable'], model=self.model)[1]
    
    def create(self):
        self.table.create(model=self.model, fillable=self.fillable)
            
    def show_attr(self, specify=False):
        self.table.show_attr(
            model=self.model,
            data=self.specify if specify else self.attr,
            specify=specify
        )

    def any_view(self):
        self.table.any_view(model=self.model)
    
    def show(self, id):
        self.table.show(
            model=self.model,
            id=id
        )

    def update(self, id):
        self.table.update(
            model=self.model,
            id=id,
            fillable=self.fillable
        )

    def delete(self, id):
        self.table.delete(
            model=self.model,
            id=id
        )

