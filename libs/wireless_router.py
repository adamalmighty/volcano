#libs/wireless_router.py

from rich.console import Console
from rich.prompt import Prompt
import os

class WirelessRouter:
    def __init__(self):
        self.console = Console()

    def _clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_menu(self):
        self.console.print("""
---------------------------------
><   [bold magenta]Wireless Router Hacking[/bold magenta]   ><
---------------------------------
        """)
        self.console.print("""
[bold yellow]Please select an option by typing the corresponding number:[/bold yellow]
[bold cyan]1.[/bold cyan] [bold red]List Wireless Interfaces[/bold red]
[bold cyan]2.[/bold cyan] [bold red]Enable Monitor Mode[/bold red]
[bold cyan]3.[/bold cyan] [bold red]Scan for WiFi Networks[/bold red]
[bold cyan]4.[/bold cyan] [bold red]Capture Handshakes[/bold red]
[bold cyan]5.[/bold cyan] [bold red]Deauthentication Attack[/bold red]
[bold cyan]6.[/bold cyan] [bold red]Handshake Cracking (WPA/WPA2)[/bold red]
[bold cyan]7.[/bold cyan] [bold red]WPS Pin Attack[/bold red]
[bold cyan]8.[/bold cyan] [bold red]Evil Twin Attack[/bold red]
[bold cyan]9.[/bold cyan] [bold red]Fake AP with Captive Portal[/bold red]
[bold cyan]10.[/bold cyan] [bold red]PMKID Capture & Attack[/bold red]
[bold cyan]11.[/bold cyan] [bold red]Probe Request/Response Analysis[/bold red]
[bold cyan]12.[/bold cyan] [bold red]Rogue DHCP Attack[/bold red]
[bold cyan]13.[/bold cyan] [bold red]Network Sniffing (WiFi)[/bold red]
[bold cyan]14.[/bold cyan] [bold red]MAC Address Spoofing[/bold red]
[bold cyan]15.[/bold cyan] [bold red]Beacon Flood Attack[/bold red]
[bold cyan]16.[/bold cyan] [bold red]Disassociation Attack[/bold red]
[bold cyan]17.[/bold cyan] [bold red]Hidden SSID Discovery[/bold red]
[bold cyan]18.[/bold cyan] [bold red]WiFi Jamming Attack[/bold red]
[bold cyan]19.[/bold cyan] [bold red]AP/Client Isolation Bypass[/bold red]
[bold cyan]20.[/bold cyan] [bold red]5GHz Band Attack Tools[/bold red]
[bold cyan]21.[/bold cyan] [bold red]Krack/PMF/Broadcast Attacks[/bold red]
[bold cyan]22.[/bold cyan] [bold red]Bluetooth/BLE Attacks[/bold red]
[bold cyan]23.[/bold cyan] [bold red]ZigBee/WiFi Interference[/bold red]
[bold cyan]24.[/bold cyan] [bold red]Auth DoS & Association Flood[/bold red]
[bold cyan]25.[/bold cyan] [bold red]Router Web Admin Attack[/bold red]
[bold cyan]26.[/bold cyan] [bold red]WiFi Pineapple Integration[/bold red]
[bold cyan]27.[/bold cyan] [bold red]Credential Harvesting (Captive Portal)[/bold red]
[bold cyan]28.[/bold cyan] [bold red]Wireless Client Tracking[/bold red]
[bold cyan]29.[/bold cyan] [bold red]Radius/EAP Attack Tools[/bold red]
[bold cyan]30.[/bold cyan] [bold red]Reset Wireless Settings[/bold red]
[bold cyan]0.[/bold cyan] [bold red]Main Menu[/bold red]
""")

    def handle_option(self, option):
        if option == "1":
            self.console.print("[bold cyan]You selected: List Wireless Interfaces[/bold cyan]")
        elif option == "2":
            self.console.print("[bold cyan]You selected: Enable Monitor Mode[/bold cyan]")
        elif option == "3":
            self.console.print("[bold cyan]You selected: Scan for WiFi Networks[/bold cyan]")
        elif option == "4":
            self.console.print("[bold cyan]You selected: Capture Handshakes[/bold cyan]")
        elif option == "5":
            self.console.print("[bold cyan]You selected: Deauthentication Attack[/bold cyan]")
        elif option == "6":
            self.console.print("[bold cyan]You selected: Handshake Cracking (WPA/WPA2)[/bold cyan]")
        elif option == "7":
            self.console.print("[bold cyan]You selected: WPS Pin Attack[/bold cyan]")
        elif option == "8":
            self.console.print("[bold cyan]You selected: Evil Twin Attack[/bold cyan]")
        elif option == "9":
            self.console.print("[bold cyan]You selected: Fake AP with Captive Portal[/bold cyan]")
        elif option == "10":
            self.console.print("[bold cyan]You selected: PMKID Capture & Attack[/bold cyan]")
        elif option == "11":
            self.console.print("[bold cyan]You selected: Probe Request/Response Analysis[/bold cyan]")
        elif option == "12":
            self.console.print("[bold cyan]You selected: Rogue DHCP Attack[/bold cyan]")
        elif option == "13":
            self.console.print("[bold cyan]You selected: Network Sniffing (WiFi)[/bold cyan]")
        elif option == "14":
            self.console.print("[bold cyan]You selected: MAC Address Spoofing[/bold cyan]")
        elif option == "15":
            self.console.print("[bold cyan]You selected: Beacon Flood Attack[/bold cyan]")
        elif option == "16":
            self.console.print("[bold cyan]You selected: Disassociation Attack[/bold cyan]")
        elif option == "17":
            self.console.print("[bold cyan]You selected: Hidden SSID Discovery[/bold cyan]")
        elif option == "18":
            self.console.print("[bold cyan]You selected: WiFi Jamming Attack[/bold cyan]")
        elif option == "19":
            self.console.print("[bold cyan]You selected: AP/Client Isolation Bypass[/bold cyan]")
        elif option == "20":
            self.console.print("[bold cyan]You selected: 5GHz Band Attack Tools[/bold cyan]")
        elif option == "21":
            self.console.print("[bold cyan]You selected: Krack/PMF/Broadcast Attacks[/bold cyan]")
        elif option == "22":
            self.console.print("[bold cyan]You selected: Bluetooth/BLE Attacks[/bold cyan]")
        elif option == "23":
            self.console.print("[bold cyan]You selected: ZigBee/WiFi Interference[/bold cyan]")
        elif option == "24":
            self.console.print("[bold cyan]You selected: Auth DoS & Association Flood[/bold cyan]")
        elif option == "25":
            self.console.print("[bold cyan]You selected: Router Web Admin Attack[/bold cyan]")
        elif option == "26":
            self.console.print("[bold cyan]You selected: WiFi Pineapple Integration[/bold cyan]")
        elif option == "27":
            self.console.print("[bold cyan]You selected: Credential Harvesting (Captive Portal)[/bold cyan]")
        elif option == "28":
            self.console.print("[bold cyan]You selected: Wireless Client Tracking[/bold cyan]")
        elif option == "29":
            self.console.print("[bold cyan]You selected: Radius/EAP Attack Tools[/bold cyan]")
        elif option == "30":
            self.console.print("[bold cyan]You selected: Reset Wireless Settings[/bold cyan]")
        elif option == "0":
            self._clear_screen()
            return False
        else:
            self._clear_screen()
            self.console.print("[bold red]Invalid option. Please try again.[/bold red]")
        return True

    def run(self):
        valid_options = {str(i) for i in range(31)} | {"0"}
        running = True
        while running:
            self.display_menu()
            choice = Prompt.ask("[bold yellow]Enter your choice[/bold yellow] [bold cyan](0-30)[/bold cyan]")
            if choice not in valid_options:
                self._clear_screen()
                self.console.print("[bold red]Invalid input! Please enter a number from 0 to 30.[/bold red]")
                continue
            running = self.handle_option(choice)
