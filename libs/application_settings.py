#libs/application_settings.py

from rich.console import Console
from rich.prompt import Prompt
import os

class ApplicationSettings:
    def __init__(self):
        self.console = Console()
    
    def display_menu(self):
        self.console.print("""
------------------------------
><   [bold magenta]Application Settings[/bold magenta]   ><
------------------------------
        """)
        self.console.print("""
[bold yellow]Please select an option by typing the corresponding number:[/bold yellow]
[bold cyan]1.[/bold cyan] [bold red]Project Management[/bold red]
[bold cyan]2.[/bold cyan] [bold red]Login Manager[/bold red]
[bold cyan]3.[/bold cyan] [bold red]Security Type Specification[/bold red]
[bold cyan]4.[/bold cyan] [bold red]Timeout Setting[/bold red]
[bold cyan]5.[/bold cyan] [bold red]Deep Crawling Levels[/bold red]
[bold cyan]6.[/bold cyan] [bold red]Custom Header Settings[/bold red]
[bold cyan]7.[/bold cyan] [bold red]Reading Logs[/bold red]
[bold cyan]0.[/bold cyan] [bold red]Main Menu[/bold red]
""")

    def handle_option(self, option):
        if option == "1":
            self.console.print("[bold cyan]You selected: Project Management[/bold cyan]")
        elif option == "2":
            self.console.print("[bold cyan]You selected: Login Manager[/bold cyan]")
        elif option == "3":
            self.console.print("[bold cyan]You selected: Security Type Specification[/bold cyan]")
        elif option == "4":
            self.console.print("[bold cyan]You selected: Timeout Setting[/bold cyan]")
        elif option == "5":
            self.console.print("[bold cyan]You selected: Deep Crawling Levels[/bold cyan]")
        elif option == "6":
            self.console.print("[bold cyan]You selected: Custom Header Settings[/bold cyan]")
        elif option == "7":
            self.console.print("[bold cyan]You selected: Reading Logs[/bold cyan]")
        elif option == "0":
            return False
        else:
            self.console.print("[bold red]Invalid option. Please try again.[/bold red]")
        return True

    def run(self):
        valid_options = {str(i) for i in range(8)}
        running = True
        while running:
            self.display_menu()
            choice = Prompt.ask("[bold yellow]Enter your choice[/bold yellow] [bold cyan](0-7)[/bold cyan]")
            if choice not in valid_options:
                self.console.print("[bold red]Invalid input! Please enter a number from 0 to 7.[/bold red]")
                continue
            running = self.handle_option(choice)
