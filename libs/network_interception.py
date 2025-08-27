#libs/network_interception.py

from rich.console import Console
from rich.prompt import Prompt
import os

class NetworkInterception:
    def __init__(self):
        self.console = Console()

    def _clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_menu(self):
        self.console.print("""
------------------------------
><   [bold magenta]Network Interception[/bold magenta]   ><
------------------------------
        """)
        self.console.print("""
[bold yellow]Please select an option by typing the corresponding number:[/bold yellow]
[bold cyan]1.[/bold cyan] [bold red]ARP Spoofing / Poisoning[/bold red]
[bold cyan]2.[/bold cyan] [bold red]DNS Spoofing / Cache Poisoning[/bold red]
[bold cyan]3.[/bold cyan] [bold red]Man-in-the-Middle (MITM) Setup[/bold red]
[bold cyan]4.[/bold cyan] [bold red]SSL Stripping Attacks[/bold red]
[bold cyan]5.[/bold cyan] [bold red]Packet Sniffing / Traffic Capture[/bold red]
[bold cyan]6.[/bold cyan] [bold red]Session Hijacking[/bold red]
[bold cyan]7.[/bold cyan] [bold red]TCP/IP Hijacking[/bold red]
[bold cyan]8.[/bold cyan] [bold red]ICMP Redirect Attacks[/bold red]
[bold cyan]9.[/bold cyan] [bold red]WiFi Deauthentication Attacks[/bold red]
[bold cyan]10.[/bold cyan] [bold red]Network Traffic Analysis[/bold red]
[bold cyan]11.[/bold cyan] [bold red]Port Mirroring / SPAN Setup[/bold red]
[bold cyan]12.[/bold cyan] [bold red]DNS Tunneling[/bold red]
[bold cyan]13.[/bold cyan] [bold red]Proxy and VPN Traffic Interception[/bold red]
[bold cyan]14.[/bold cyan] [bold red]MAC Spoofing[/bold red]
[bold cyan]15.[/bold cyan] [bold red]Passive Reconnaissance[/bold red]
[bold cyan]16.[/bold cyan] [bold red]Active Reconnaissance[/bold red]
[bold cyan]17.[/bold cyan] [bold red]Network Port Scanning[/bold red]
[bold cyan]18.[/bold cyan] [bold red]Man-in-the-Browser Attacks[/bold red]
[bold cyan]19.[/bold cyan] [bold red]Wireshark Integration[/bold red]
[bold cyan]20.[/bold cyan] [bold red]Traffic Injection[/bold red]
[bold cyan]21.[/bold cyan] [bold red]Message Replay Attacks[/bold red]
[bold cyan]22.[/bold cyan] [bold red]DHCP Spoofing[/bold red]
[bold cyan]23.[/bold cyan] [bold red]Network Segmentation Bypass[/bold red]
[bold cyan]24.[/bold cyan] [bold red]VPN Kill Switch Bypass[/bold red]
[bold cyan]25.[/bold cyan] [bold red]Firewall Traffic Analysis[/bold red]
[bold cyan]26.[/bold cyan] [bold red]TCP Reset Attacks[/bold red]
[bold cyan]27.[/bold cyan] [bold red]SSL/TLS Interception Proxy[/bold red]
[bold cyan]28.[/bold cyan] [bold red]Network Protocol Fuzzing[/bold red]
[bold cyan]29.[/bold cyan] [bold red]IPv6 Network Attacks[/bold red]
[bold cyan]30.[/bold cyan] [bold red]Zero-Day Network Exploits Testing[/bold red]
[bold cyan]0.[/bold cyan] [bold red]Main Menu[/bold red]
""")

    def handle_option(self, option):
        if option == "1":
            self.console.print("[bold cyan]You selected: ARP Spoofing / Poisoning[/bold cyan]")
        elif option == "2":
            self.console.print("[bold cyan]You selected: DNS Spoofing / Cache Poisoning[/bold cyan]")
        elif option == "3":
            self.console.print("[bold cyan]You selected: Man-in-the-Middle (MITM) Setup[/bold cyan]")
        elif option == "4":
            self.console.print("[bold cyan]You selected: SSL Stripping Attacks[/bold cyan]")
        elif option == "5":
            self.console.print("[bold cyan]You selected: Packet Sniffing / Traffic Capture[/bold cyan]")
        elif option == "6":
            self.console.print("[bold cyan]You selected: Session Hijacking[/bold cyan]")
        elif option == "7":
            self.console.print("[bold cyan]You selected: TCP/IP Hijacking[/bold cyan]")
        elif option == "8":
            self.console.print("[bold cyan]You selected: ICMP Redirect Attacks[/bold cyan]")
        elif option == "9":
            self.console.print("[bold cyan]You selected: WiFi Deauthentication Attacks[/bold cyan]")
        elif option == "10":
            self.console.print("[bold cyan]You selected: Network Traffic Analysis[/bold cyan]")
        elif option == "11":
            self.console.print("[bold cyan]You selected: Port Mirroring / SPAN Setup[/bold cyan]")
        elif option == "12":
            self.console.print("[bold cyan]You selected: DNS Tunneling[/bold cyan]")
        elif option == "13":
            self.console.print("[bold cyan]You selected: Proxy and VPN Traffic Interception[/bold cyan]")
        elif option == "14":
            self.console.print("[bold cyan]You selected: MAC Spoofing[/bold cyan]")
        elif option == "15":
            self.console.print("[bold cyan]You selected: Passive Reconnaissance[/bold cyan]")
        elif option == "16":
            self.console.print("[bold cyan]You selected: Active Reconnaissance[/bold cyan]")
        elif option == "17":
            self.console.print("[bold cyan]You selected: Network Port Scanning[/bold cyan]")
        elif option == "18":
            self.console.print("[bold cyan]You selected: Man-in-the-Browser Attacks[/bold cyan]")
        elif option == "19":
            self.console.print("[bold cyan]You selected: Wireshark Integration[/bold cyan]")
        elif option == "20":
            self.console.print("[bold cyan]You selected: Traffic Injection[/bold cyan]")
        elif option == "21":
            self.console.print("[bold cyan]You selected: Message Replay Attacks[/bold cyan]")
        elif option == "22":
            self.console.print("[bold cyan]You selected: DHCP Spoofing[/bold cyan]")
        elif option == "23":
            self.console.print("[bold cyan]You selected: Network Segmentation Bypass[/bold cyan]")
        elif option == "24":
            self.console.print("[bold cyan]You selected: VPN Kill Switch Bypass[/bold cyan]")
        elif option == "25":
            self.console.print("[bold cyan]You selected: Firewall Traffic Analysis[/bold cyan]")
        elif option == "26":
            self.console.print("[bold cyan]You selected: TCP Reset Attacks[/bold cyan]")
        elif option == "27":
            self.console.print("[bold cyan]You selected: SSL/TLS Interception Proxy[/bold cyan]")
        elif option == "28":
            self.console.print("[bold cyan]You selected: Network Protocol Fuzzing[/bold cyan]")
        elif option == "29":
            self.console.print("[bold cyan]You selected: IPv6 Network Attacks[/bold cyan]")
        elif option == "30":
            self.console.print("[bold cyan]You selected: Zero-Day Network Exploits Testing[/bold cyan]")
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
