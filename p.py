
from dependances.model import Model
from dependances.url import Url
from dependances.output import Output


# url -----------
url = Url('url.json',header='header.json')
# print(url.parse_url(url.WORL['attr'],output_url=True))
# output -----------
output = Output()

output.console.clear()

# model -------
model = Model(model='tag',url=url,output=output)

# exit()
# model.show_attr(specify=True)
id= 12
# model.update(id)
model.delete(id)
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