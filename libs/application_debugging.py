#libs/application_debugging.py

from rich.console import Console
from rich.prompt import Prompt
import os

class ApplicationDebugging:
    def __init__(self):
        self.console = Console()

    def _clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
    
    def display_menu(self):
        self.console.print("""
-------------------------------
><   [bold magenta]Application Debugging[/bold magenta]   ><
-------------------------------
        """)
        self.console.print("""
[bold yellow]Please select an option by typing the corresponding number:[/bold yellow]
[bold cyan]1.[/bold cyan] [bold red]Android APK Debugging[/bold red]
[bold cyan]2.[/bold cyan] [bold red]Windows EXE Debugging[/bold red]
[bold cyan]3.[/bold cyan] [bold red]Java Application Debugging[/bold red]
[bold cyan]4.[/bold cyan] [bold red]MacOS Application Debugging[/bold red]
[bold cyan]5.[/bold cyan] [bold red]Python Script Debugging[/bold red]
[bold cyan]6.[/bold cyan] [bold red]Browser Extension Debugging[/bold red]
[bold cyan]7.[/bold cyan] [bold red]Log File Analysis[/bold red]
[bold cyan]0.[/bold cyan] [bold red]Main Menu[/bold red]
""")
    def handle_option(self, option):
        if option == "1":
            self.console.print("[bold cyan]You selected: Android APK Debugging[/bold cyan]")
        elif option == "2":
            self.console.print("[bold cyan]You selected: Windows EXE Debugging[/bold cyan]")
        elif option == "3":
            self.console.print("[bold cyan]You selected: Java Application Debugging[/bold cyan]")
        elif option == "4":
            self.console.print("[bold cyan]You selected: MacOS Application Debugging[/bold cyan]")
        elif option == "5":
            self.console.print("[bold cyan]You selected: Python Script Debugging[/bold cyan]")
        elif option == "6":
            self.console.print("[bold cyan]You selected: Browser Extension Debugging[/bold cyan]")
        elif option == "7":
            self.console.print("[bold cyan]You selected: Log File Analysis[/bold cyan]")
        elif option == "0":
            self._clear_screen()
            return False
        else:
            self._clear_screen()
            self.console.print("[bold red]Invalid option. Please try again.[/bold red]")
        return True
    
    def run(self):
        valid_options = {str(i) for i in range(8)}
        running = True
        while running:
            self.display_menu()
            choice = Prompt.ask("[bold yellow]Enter your choice[/bold yellow] [bold cyan](0-7)[/bold cyan]")
            if choice not in valid_options:
                self._clear_screen()
                self.console.print("[bold red]Invalid input! Please enter a number from 0 to 7.[/bold red]")
                continue
            running = self.handle_option(choice)
