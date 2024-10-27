
from dependances.model import Model
from dependances.url import Url
from dependances.output import Output
from repertoire import cls
from rich import print
cls()


# url -----------
url = Url('url.json')
# print(url.parse_url(url.WORL['attr'],output_url=True))
# url -----------
output = Output()

# model -------
model = Model(model='tag',url=url,output=output)

model.show_attr()
