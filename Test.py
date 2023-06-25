import configparser

from tabulate import tabulate

config = configparser.ConfigParser()
config.read_file(open(r'Config.txt'))
path1 = config.get('My Section', 'path1')
path2 = config.get('My Section', 'path2')
path3 = config.get('My Section', 'path3')

print(path1,path2,path3)



from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("T1", style="dim", width=12)
table.add_column("T1", style="dim", width=12)
table.add_column("T1", style="dim", width=12)
table.add_column("T1", style="dim", width=12)
table.add_row("T1", "T1", "T1", "T1")
table.add_row("T1", "T1", "T1", "T1")
table.add_row("T1", "T1", "T1", "T1")
console.print(table)