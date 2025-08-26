#libs/system.settings.py

from rich.console import Console
from rich.prompt import Prompt
import os

class SystemSettings:
    def __init__(self):
        self.console = Console()
    
    def display_menu(self):
        self.console.print("""
-------------------------
><   [bold magenta]System Settings[/bold magenta]   ><
-------------------------
        """)
        self.console.print("""
[bold yellow]Please select an option by typing the corresponding number:[/bold yellow]
[bold cyan]1.[/bold cyan] [bold red]Network Information[/bold red]
[bold cyan]2.[/bold cyan] [bold red]Interface Manager[/bold red]
[bold cyan]3.[/bold cyan] [bold red]MAC Address Manager[/bold red]
[bold cyan]4.[/bold cyan] [bold red]IP Address Manager[/bold red]
[bold cyan]5.[/bold cyan] [bold red]DNS Manager[/bold red]
[bold cyan]6.[/bold cyan] [bold red]Proxy Manager[/bold red]
[bold cyan]7.[/bold cyan] [bold red]Reset All Changes[/bold red]
[bold cyan]8.[/bold cyan] [bold red]Update All Packages[/bold red]
[bold cyan]9.[/bold cyan] [bold red]Clear Cache[/bold red]
[bold cyan]0.[/bold cyan] [bold red]Main Menu[/bold red]
""")

    def handle_option(self, option):
        if option == "1":
            self.console.print("[bold cyan]You selected: Network Information[/bold cyan]")
        elif option == "2":
            self.console.print("[bold cyan]You selected: Interface Manager[/bold cyan]")
        elif option == "3":
            self.console.print("[bold cyan]You selected: MAC Address Manager[/bold cyan]")
        elif option == "4":
            self.console.print("[bold cyan]You selected: IP Address Manager[/bold cyan]")
        elif option == "5":
            self.console.print("[bold cyan]You selected: DNS Manager[/bold cyan]")
        elif option == "6":
            self.console.print("[bold cyan]You selected: Proxy Manager[/bold cyan]")
        elif option == "7":
            self.console.print("[bold cyan]You selected: Reset All Changes[/bold cyan]")
        elif option == "8":
            self.console.print("[bold cyan]You selected: Update All Packages[/bold cyan]")
        elif option == "9":
            self.console.print("[bold cyan]You selected: Clear Cache[/bold cyan]")
        elif option == "0":
            return False
        else:
            self.console.print("[bold red]Invalid option. Please try again.[/bold red]")
        return True

    def run(self):
        valid_options = {str(i) for i in range(10)}
        running = True
        while running:
            self.display_menu()
            choice = Prompt.ask("[bold yellow]Enter your choice[/bold yellow] [bold cyan](0-9)[/bold cyan]")
            if choice not in valid_options:
                self.console.print("[bold red]Invalid input! Please enter a number from 0 to 9.[/bold red]")
                continue
            running = self.handle_option(choice)
