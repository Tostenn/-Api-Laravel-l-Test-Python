
from dependances.url import Url
from dependances.output import Output
from dependances.table import Table
from dependances.model import Model


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
