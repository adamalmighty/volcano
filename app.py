#!/usr/bin/env python3
# app.py
import os
import time
import logging
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

from libs.system_settings import SystemSettings
from libs.application_settings import ApplicationSettings
from libs.firewall_invasion import FirewallInvasion
from libs.web_application import WebApplication
from libs.network_interception import NetworkInterception
from libs.wireless_router import WirelessRouter
from libs.parallel_devices import ParallelDevices
from libs.application_debugging import ApplicationDebugging
from libs.file_hacking import FileHacking


class VolcanoApp:
    """
    Main application class for Volcano penetration testing terminal.
    Handles UI rendering, input parsing, and launching modular components.
    """

    def __init__(self):
        self.console = Console()
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logger = logging.getLogger("VolcanoApp")
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler("volcano.log", encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    def _clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def _exit_sequence(self):
        self.console.print("[bold red]Exiting Volcano. Goodbye![/bold red]")
        self.logger.info("Application exited by user")
        time.sleep(3)
        self._clear_screen()

    def display_welcome(self):
        """
        Display welcome banner and author info with styling.
        """
        self._clear_screen()
        banner = Text.from_markup("""
[bold bright_red] **      **   *******   **         ******      **     ****     **   *******  [/bold bright_red]
[bold bright_red]/**     /**  **/////** /**        **////**    ****   /**/**   /**  **/////** [/bold bright_red]
[bold bright_blue]/**     /** **     //**/**       **    //    **//**  /**//**  /** **     //**[/bold bright_blue]
[bold bright_blue]//**    ** /**      /**/**      /**         **  //** /** //** /**/**      /**[/bold bright_blue]
[bold bright_yellow] //**  **  /**      /**/**      /**        **********/**  //**/**/**      /**[/bold bright_yellow]
[bold bright_yellow]  //****   //**     ** /**      //**    **/**//////**/**   //****//**     ** [/bold bright_yellow]
[bold bright_green]   //**     //*******  /******** //****** /**     /**/**    //*** //*******  [/bold bright_green]
[bold bright_green]    //       ///////   ////////   //////  //      // //      ///   ///////   [/bold bright_green]
""")
        author = Text.from_markup(
            "\n+---------------------------------+\n"
            "><     [bold yellow]AUTHOR:[/bold yellow] [bold cyan]Adam Almighty[/bold cyan]     ><\n"
            "+---------------------------------+",
            justify="center"
        )
        welcome_message = Text.from_markup(
            "\n[bold bright_red]Welcome to Volcano – Your Customized Penetration Testing Terminal[/bold bright_red]\n"
            "[bold yellow]A robust, modular platform designed for security professionals and penetration testers, with cross-platform support.[/bold yellow]",
            justify="center"
        )
        panel_content = Text(justify="center")
        panel_content.append(banner)
        panel_content.append("\n")
        panel_content.append(author)
        panel_content.append("\n\n")
        panel_content.append(welcome_message)
        self.console.print(Panel(panel_content, border_style="bright_red", padding=(1, 4)))
        self.logger.info("Displayed welcome banner")

    def display_menu(self):
        menu_text = """
[bold yellow]Please select an option by typing the corresponding number (or 'h' for help):[/bold yellow]
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

    def display_help(self):
        self._clear_screen()
        help_text = """
[bold green]Volcano Help:[/bold green]

- Input the number corresponding to the menu option to enter that module.
- You can exit the application anytime by selecting [bold red]0[/bold red].
- Press [bold green]'h'[/bold green] or [bold green]'H'[/bold green] anytime to view this help message.
- Modules provide specialized penetration testing functionalities:
    • System Settings: Adjust tool/system configs.
    • Application Settings: Configure app behavior.
    • Firewall Invasion: Techniques to bypass/detect firewalls.
    • Web App Pentest: Test web apps for vulnerabilities.
    • Network Intercepting: Capture and analyze network traffic.
    • Wireless Router Hacking: Wi-Fi pentesting tools.
    • Parallel Device Hacking: Attack devices on same network.
    • Application Debugging: Debug various app types.
    • File Hacking: Analyze and manipulate files securely.
"""
        self.console.print(Panel(help_text, border_style="green"))

    def handle_option(self, option):
        try:
            if option == "1":
                self._clear_screen_and_run(SystemSettings)
            elif option == "2":
                self._clear_screen_and_run(ApplicationSettings)
            elif option == "3":
                self._clear_screen_and_run(FirewallInvasion)
            elif option == "4":
                self._clear_screen_and_run(WebApplication)
            elif option == "5":
                self._clear_screen_and_run(NetworkInterception)
            elif option == "6":
                self._clear_screen_and_run(WirelessRouter)
            elif option == "7":
                self._clear_screen_and_run(ParallelDevices)
            elif option == "8":
                self._clear_screen_and_run(ApplicationDebugging)
            elif option == "9":
                self._clear_screen_and_run(FileHacking)
            elif option == "0":
                self._exit_sequence()
                return False
            elif option.lower() == "h":
                self.display_help()
            else:
                self._clear_screen()
                self.console.print("[bold red]Invalid option. Please try again.[/bold red]")
        except Exception as e:
            self.console.print(f"[bold red]Error running module: {e}[/bold red]")
            self.logger.error(f"Error in handle_option({option}): {e}", exc_info=True)
        return True

    def _clear_screen_and_run(self, ModuleClass):
        self._clear_screen()
        self.logger.info(f"Launching module: {ModuleClass.__name__}")
        module_instance = ModuleClass()
        module_instance.run()

    def run(self):
        self.display_welcome()
        valid_options = {str(i) for i in range(10)} | {"h", "H"}
        running = True
        try:
            while running:
                self.display_menu()
                choice = Prompt.ask("[bold yellow]Enter your choice[/bold yellow] [bold cyan](0-9, h)[/bold cyan]")
                if choice not in valid_options:
                    self._clear_screen()
                    self.console.print("[bold red]Invalid input! Please enter a number from 0 to 9 or 'h' for help.[/bold red]")
                    continue
                running = self.handle_option(choice)
        except KeyboardInterrupt:
            self._exit_sequence()


if __name__ == "__main__":
    app = VolcanoApp()
    app.run()
