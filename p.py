
from dependances.model import Model
from dependances.url import Url
from dependances.output import Output
from dependances.table import Table

path = "public/data"
# url -----------
url = Url(path + '/url.json',header=path + '/header.json')

# output -----------
output = Output()
output.console.clear()

# table -----------
table = Table(path + '/idShow.json', url=url, output=output)

# model -------
model = Model(model='user',table=table)

# exit()
# model.show(1)
id= 15
model.delete(1)
# model.delete(id)
# from repertoire import enreJson
# from requests import get,delete

# url = url.parse_url('destroy',model="tag",id=50,output_url=True)
# print(url)
# h = {
#     'accept':'application/json'
# }
# # enreJson('header.json',h)
# r = delete(url,headers=h)
# print(r.status_code)
# output.console.print(r.json())