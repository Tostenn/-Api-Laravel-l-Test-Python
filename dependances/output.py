from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from rich import box
from keyboard import read_event

class Output:
    """
    # Outsite
    gestion des print 
    """
    pass

    def __init__(self) -> None:
        self.console = Console()
        pass

    def menu():
        pass

    def url_code(self,data):
        panel_1 = Panel(f"method: [bold cyan]{data[0].upper()}[/]", style="green")
        panel_2 = Panel(f"url: [bold cyan]{data[1]}[/]", style="green")
        panel_3 = Panel(f"code: [bold cyan]{data[2]}[/]", style="green")
        self.console.print(Columns([panel_1, panel_2,panel_3]),justify='center')

    def read_event_touch(self):
        
        print("\nAppuyez sur n'importe quelle touche pour fermer...")

        # Attendre qu'une touche soit pressée
        read_event()  # Lecture d'un événement de touche

    def model(self,model, id, data):
        # ajouter les type des donné
        # url et code 
        self.url_code(data[0])
       
        half_width = self.console.size.width // 2
        table = Table(box=box.ROUNDED, style="purple",expand=False, width=half_width)
        table.add_column(f"[bold cyan]{model.capitalize()} - {id}[/]", justify="center", style="cyan", no_wrap=True)
        
        for k,v in data[1]['data'][0].items():
            panel_1 = Panel(k, style="white")
            panel_2 = Panel(f"[bold cyan]{str(v)}[/]", style="green")
            row = Columns([panel_1, panel_2])
            table.add_row(row)
        

        self.console.print(table,justify='center',)

        self.read_event_touch()
        # Effacer l'affichage en nettoyant la console
        self.console.clear()

    def prompt_for_pagination(self,next, prev):
        choices = [str(i+1) for i in range(4)]
        if not next: choices.remove('1')
        if not prev: choices.remove('2')
        # Demander à l'utilisateur de choisir une option
        return Prompt.ask("\n[bold green]Choisissez une option[/]", console=self.console, choices=choices)
        
    def menu_pagination(self,model, current, last):
        # Création du tableau de menu
        table = Table( box=box.ROUNDED, style="purple")

        table.add_column(f"Pagination {model} | page [bold cyan]{current}[/bold cyan] / {last}", style="bold cyan")
        # table.add_column("Description", style="yellow")
        end = '[bold red] \[not] [/bold red]'
        # Ajout des options de menu
        table.add_row(f"1 - suivant {end if current == last else ''}")
        table.add_row(f"2 - precedent {end if current == 1 else ''}")
        table.add_row("3 - show id")
        table.add_row("4 - menu")

        # Affichage du menu

        self.console.print(table,justify='left')

    def show_table_for_pagination(self,model:str, data):
        self.url_code(data[0])
        data = data[1]
        model = model.capitalize()
        
        print('\n')
        self.tables(model,data['data'])
        print('')
        self.menu_pagination(model, data['meta']['current_page'], data['meta']['last_page'])
    
    def show_table(self,model:str, data):
        self.url_code(data[0])
        data = data[1]
        model = model.capitalize()
        
        print('\n')
        self.tables(model,data['data'])
        self.read_event_touch()
    
    def show_attr(self, model:str, url:str, method:str, data,column='columns',specify=False):
        self.url_code((method, url, 200))
        model = model.capitalize()
        
        print('\n')
        if specify:
            self.tables(model,data,column='specify' + column)
        else:
            self.tables(model,data,True,column)
        self.read_event_touch()
        

    def tables(self, model,data,array:bool=False,column=""):
        # Création de la table avec Rich
        table = Table(title=model ,box=box.ROUNDED, style="purple",show_lines=True)

        # Définition des colonnes de la table
        if not array:
            for k in data[0]:
                table.add_column(k.upper(), justify="center", style="cyan", no_wrap=True)

            # Ajout des données dans la table
            for item in data:
                row = [str(v) for k,v in item.items() ]
                table.add_row(*row)
            
        else:
            table.add_column(column, justify="center", style="cyan", no_wrap=True)
            for i in data:
                table.add_row(i)

        # Affichage de la table
        self.console.print(table,justify='center')


