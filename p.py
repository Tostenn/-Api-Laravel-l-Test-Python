
from dependances.url import Url
from dependances.output import Output
from dependances.table import Table
from dependances.model import Model

from repertoire import rlt

# url -----------
url = Url()

# output -----------
output = Output()
output.console.clear()

# table -----------           

table = Table(url=url, output=output)

# model -------
model = Model(model='objet', table=table)

model.show(20)

# programme principale ---------

# afficher les tables a séléctionné 

    # menu de navigarion
"""
1 - any View
2 - show
3 - create
4 - update
5 - delete
6 - change Table
0 - exit
"""
    # 1 - any View
        
    # 2 - show
        
    # 3 - create
        
    # 4 - update
        
    # 5 - delete
        
    # 6 - change Table
        
    # 0 - exit