from repertoire import cls,rlt

import trio

cls()

async def child1():
    print("  child1: started! sleeping now...")
    await trio.sleep(3)
    print("  child1: exiting!")


async def child2():
    print("  child2: started! sleeping now...")
    await trio.sleep(1)
    print("  child2: exiting!")


async def parent():
    print("parent: started!")
    async with trio.open_nursery() as nursery:
        print("parent: spawning child1...")
        nursery.start_soon(child1)

        print("parent: spawning child2...")
        nursery.start_soon(child2)

        print("parent: waiting for children to finish...")
        # -- we exit the nursery block here --
    print("parent: all done!")


# trio.run(parent)
# from dependances.model import Model
from repertoire import cls,rlt,__conten_fic__
from rich.console import Console

console = Console(stderr=True)

cls()
menu = f'''
1 - listing
2 - create
3 - show
4 - update
5 - delete
0 - quitter
-> '''

from rich import print
# print(":blue_heart-emoji:")
# print(":red_heart-text:")
data = {
    'name':'kouya tosten',
}
# console.print("[bold]Bold[italic] bold and italic [/bold]italic[/italic]")
# console.print("Visit my [link=https://www.willmcgugan.com]blog[/link]!")
# console.print("[bold italic yellow on red blink]This text is impossible to read")
# console.rule("[bold red]Chapter 2")
# console.print_json('[false, true, null, "foo"]')

# with console.status("[bold italic yellow on red blink]This text is impossible to read"):
#     rlt(3)
# with console.status("Monkeying around...", spinner="monkey"):
#     rlt(3)

# console.input("What is [i]your[/i] [bold red]name[/]? :smiley: ")

# from time import sleep
# from rich.console import Console

# affiche un element pendant un certaint temps
# console = Console()
# with console.screen():
#     console.print(data)
#     sleep(5)
# from time import sleep

# from rich.console import Console

# from rich.console import Console
# from rich.text import Text

# console = Console()
# text = Text("Hello, World!")
# text.stylize("bold magenta", 0, 10)
# console.print(text)

# text = Text()
# text.append("Hello", style="bold magenta")
# text.append(" World!",style="i green")
# console.print(text)
# text = Text.from_ansi("\033[1mHello, World!\033[0m")
# console.print(text.spans)

# from random import randint

# from rich import print
# from rich.highlighter import Highlighter


# class RainbowHighlighter(Highlighter):
#     def highlight(self, text):
#         for index in range(len(text)):
#             text.stylize(f"color({randint(16, 255)})", index, index + 1)


# rainbow = RainbowHighlighter()
# console.print(rainbow("[i] I must not fear. [/i] Fear is the mind-killer."))
# from rich.pretty import pprint
# pprint(locals(),max_length=2)

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

# Initialisation de la console Rich
console = Console()

def afficher_menu():
    console.print(Panel("Bienvenue dans [bold cyan]Mon Application[/] 🌟", style="green"), justify="center")

    # Création du tableau de menu
    table = Table(title="Menu Principal", box=box.ROUNDED, style="purple")

    table.add_column("Option", justify="center", style="bold cyan")
    table.add_column("Description", style="yellow")

    # Ajout des options de menu
    table.add_row("1", "Afficher les informations")
    table.add_row("2", "Modifier les paramètres")
    table.add_row("3", "Consulter les statistiques")
    table.add_row("4", "Quitter")

    # Affichage du menu
    console.print(table)

# Fonction principale
def main():
    while True:
        afficher_menu()
        
        # Demander à l'utilisateur de choisir une option
        choix = Prompt.ask("\n[bold green]Choisissez une option[/]", choices=["1", "2", "3", "4"])
        
        if choix == "1":
            console.print("[bold green]Informations[/] : Voici vos informations...")
        elif choix == "2":
            console.print("[bold green]Paramètres[/] : Modification des paramètres en cours...")
        elif choix == "3":
            console.print("[bold green]Statistiques[/] : Affichage des statistiques...")
        elif choix == "4":
            console.print("[bold red]Quitter[/] : Au revoir!")
            break

# Lancer le programme
# afficher_menu()
# from rich.prompt import Prompt
# name = Prompt.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Paul")

# from rich import print
# from rich.console import Group
# from rich.panel import Panel
# @group()
# panel_group = Group(
#     Panel("Hello", style="on blue"),
#     Panel("World", style="on red"),
# )
# print(Panel(panel_group))
# from rich import print
# from rich.console import group
# from rich.panel import Panel

# @group()
# def get_panels():
#     yield Panel("Hello", style="on blue")
#     yield Panel("World", style="on red")

# print(Panel(get_panels()))
# from rich import print
# from rich.padding import Padding
# test = Padding("Hello", (2, 4))
# print(test)

# test = Padding("Hello", (2, 4), style="on blue", expand=False)
# print(test)

# from rich import print
# from rich.panel import Panel
# print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))
# from rich.tree import Tree

# tree = Tree("Rich Tree")
# print(tree)
# tree.add("foo")
# tree.add("bar")
# baz_tree = tree.add("baz")
# baz_tree.add("[red]Red").add("[green]Green").add("[blue]Blue")
# print(tree)
# console.print(Panel(tree, style="green",title='model id'), justify="left")

# import time

# from rich.live import Live
# from rich.table import Table

# table = Table()
# table.add_column("Row ID")
# table.add_column("Description")
# table.add_column("Level")

# with Live(table, refresh_per_second=4,screen=True):  # update 4 times a second to feel fluid
#     for row in range(12):
#         time.sleep(0.4)  # arbitrary delay
#         # update the renderable internally
#         table.add_row(f"{row}", f"description {row}", "[red]ERROR")

# import random
# import time

# from rich.live import Live
# from rich.table import Table


# def generate_table() -> Table:
#     """Make a new table."""
#     table = Table()
#     table.add_column("ID")
#     table.add_column("Value")
#     table.add_column("Status")

#     for row in range(random.randint(2, 6)):
#         value = random.random() * 100
#         table.add_row(
#             f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
#         )
#     return table


# with Live(generate_table(), refresh_per_second=4,screen=True,transient=True) as live:
#     for _ in range(5):
#         time.sleep(0.4)
#         live.update(generate_table())

# from rich import print
# from rich.layout import Layout

# layout = Layout(name='lower')
# # print(layout)
# layout["lower"].split_row(
#     Layout(name="left"),
#     Layout(name="right"),
# )
# # print(layout)
# print(layout.tree)

from repertoire import recujson, enreJson
base = 'http://127.0.0.1:8000/api'

URL = {
    'secondaire_id': '_id',
    'table':{
        'category':['nom'],
        'vendeur' :['user_id'],
        'user' :['nom','prenom'],
    }
}
enreJson('idShow.json', URL)

print(URL)

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
'''

# from rich.console import Console
# from rich.panel import Panel
# from rich.text import Text

# # Créer une console rich
# console = Console()

# def validate_form(data):
#     errors = []

#     # Exemple de validation de base
#     if not data.get("nom"):
#         errors.append("Le champ [bold red]Nom[/bold red] est obligatoire.")
    
#     if not data.get("email"):
#         errors.append("Le champ [bold red]Email[/bold red] est obligatoire.")
#     elif "@" not in data["email"]:  # Validation simple de l'email
#         errors.append("Le champ [bold red]Email[/bold red] doit contenir un '@'.")

#     return errors

# def display_errors(errors):
#     if errors:
#         error_text = "\n".join(errors)
#         console.print(Panel(
#             Text(error_text, style="bold red"),
#             title="Erreurs de validation",
#             border_style="red"
#         ))
#     else:
#         console.print(Panel(
#             "[bold green]Tous les champs sont valides ![/bold green]",
#             title="Succès",
#             border_style="green"
#         ))

# # Exemple d'utilisation
# form_data = {
#     "nom": "",       # Champ vide pour tester l'erreur
#     "email": "test"  # Email invalide pour tester l'erreur
# }

# Validation des données et affichage des erreurs
# errors = validate_form(form_data)
# display_errors(errors)
