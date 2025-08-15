#!/usr/bin/env python3
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
import os

class VolcanoApp:
    def __init__(self):
        self.console = Console()

    def display_welcome(self):
        os.system("clear")
        banner = Text.from_markup("""
[bold bright_red]*@@@@*   *@@@*  mm@**@@m  *@@@@*      mm@***@m@      @@      *@@@m   *@@@*  mm@**@@m  [/bold bright_red]
[bold bright_red]  *@@     m@  m@@*    *@@m  @@      m@@*     *@     m@@m       @@@m    @  m@@*    *@@m[/bold bright_red]
[bold bright_red]   @@m   m@   @@*      *@@  @@      @@*       *    m@*@@!      @ @@@   @  @@*      *@@[/bold bright_red]
[bold bright_green]    @@m  @*   @@        @@  @@      @@            m@  *@@      @  *@@m @  @@        @@[/bold bright_green]
[bold bright_green]    *!@ !*    @@        @@  @!     m@!m           @@@!@!@@     @   *@@m!  @@        @@[/bold bright_green]
[bold bright_green]     !@@m     *@@      @@*  @!    :@*!@m     m*  !*      @@    !     !@!  *@@      @@*[/bold bright_green]
[bold bright_blue]     !! !*    !@@      !@!  !!     !!!!           !!!!@!!@     !   *!!!!  !@@      !@![/bold bright_blue]
[bold bright_blue]     !!::     *@!!!    !!!  !:    !!:!!:     !*  !*      !!    !     !!!  *@!!!    !!![/bold bright_blue]
[bold bright_blue]      :         : : : :   : :: !: :   : : : :! : : :   : ::: : : :    :!!   : : : :   [/bold bright_blue]
""")
        author = Text.from_markup(
            "\n+---------------------------------+\n"
            "|      [bold yellow]Author:[/bold yellow] [bold cyan]Adam Almighty[/bold cyan]      |\n"
            "+---------------------------------+",
            justify="center"
        )
        welcome_message = Text.from_markup(
            "\n[bold bright_red]Welcome to Volcano - A customised penetration testing terminal[/bold bright_red]\n"
            "[bold yellow]A powerful, modular tool crafted for Arch Linux enthusiasts and security professionals.[/bold yellow]",
            justify="center"
        )
        panel_content = Text(justify="center")
        panel_content.append(banner)
        panel_content.append("\n")
        panel_content.append(author)
        panel_content.append("\n\n")
        panel_content.append(welcome_message)
        self.console.print(Panel(panel_content, border_style="bright_red", padding=(1, 4)))

    def display_menu(self):
        menu_text = """
[bold yellow]Please select an option by typing the corresponding number:[/bold yellow]
[bold cyan]1.[/bold cyan] [bold red]System Settings[/bold red]
[bold cyan]2.[/bold cyan] [bold red]Application Settings[/bold red]
[bold cyan]3.[/bold cyan] [bold red]Firewall Invasion[/bold red]
[bold cyan]4.[/bold cyan] [bold red]Web Application Penetration Testing[/bold red]
[bold cyan]5.[/bold cyan] [bold red]Network Intercepting[/bold red]
[bold cyan]6.[/bold cyan] [bold red]Wireless Router Hacking[/bold red]
[bold cyan]7.[/bold cyan] [bold red]Parallel Device Hacking[/bold red]
[bold cyan]8.[/bold cyan] [bold red]Application Debugging[/bold red]
[bold cyan]9.[/bold cyan] [bold red]File Hacking[/bold red]
[bold cyan]0.[/bold cyan] [bold red]Exit[/bold red]
"""
        self.console.print(menu_text)

    def handle_option(self, option):
        if option == "1":
            self.console.print("[bold cyan]You selected: System Settings[/bold cyan]")
            # Placeholder for system settings functionality
        elif option == "2":
            self.console.print("[bold cyan]You selected: Application Settings[/bold cyan]")
            # Placeholder for application settings functionality
        elif option == "3":
            self.console.print("[bold cyan]You selected: Firewall Invasion[/bold cyan]")
            # Placeholder for firewall invasion functionality
        elif option == "4":
            self.console.print("[bold cyan]You selected: Web Application Penetration Testing[/bold cyan]")
            # Placeholder for web application testing functionality
        elif option == "5":
            self.console.print("[bold cyan]You selected: Network Intercepting[/bold cyan]")
            # Placeholder for network intercepting functionality
        elif option == "6":
            self.console.print("[bold cyan]You selected: Wireless Router Hacking[/bold cyan]")
            # Placeholder for wireless hacking functionality
        elif option == "7":
            self.console.print("[bold cyan]You selected: Parallel Device Hacking[/bold cyan]")
            # Placeholder for parallel device hacking functionality
        elif option == "8":
            self.console.print("[bold cyan]You selected: Application Debugging[/bold cyan]")
            # Placeholder for debugging functionality
        elif option == "9":
            self.console.print("[bold cyan]You selected: File Hacking[/bold cyan]")
            # Placeholder for file hacking functionality
        elif option == "0":
            self.console.print("[bold red]Exiting Volcano. Goodbye![/bold red]")
            return False
        else:
            self.console.print("[bold red]Invalid option. Please try again.[/bold red]")
        return True

    def run(self):
        self.display_welcome()
        valid_options = {str(i) for i in range(10)}  # '0' through '9'
        running = True
        while running:
            self.display_menu()
            choice = Prompt.ask("[bold yellow]Enter your choice[/bold yellow] [bold cyan](0-9)[/bold cyan]")
            if choice not in valid_options:
                self.console.print("[bold red]Invalid input! Please enter a number from 0 to 9.[/bold red]")
                continue
            running = self.handle_option(choice)

if __name__ == "__main__":
    app = VolcanoApp()
    app.run()
