#libs/firewall_invasion.py

from rich.console import Console
from rich.prompt import Prompt

class FirewallInvasion:
    def __init__(self):
        self.console = Console()
    
    def display_menu(self):
        self.console.print("""
---------------------------
><   [bold magenta]Firewall Invasion[/bold magenta]   ><
---------------------------
        """)
        self.console.print("""
[bold yellow]Please select an option by typing the corresponding number:[/bold yellow]
[bold cyan]1.[/bold cyan] [bold red]Firewall Detection[/bold red]
[bold cyan]2.[/bold cyan] [bold red]Port Scanning with Evasion[/bold red]
[bold cyan]3.[/bold cyan] [bold red]Fragmented Packet Attacks[/bold red]
[bold cyan]4.[/bold cyan] [bold red]IP Spoofing and Address Manipulation[/bold red]
[bold cyan]5.[/bold cyan] [bold red]Protocol Tunneling and Encapsulation[/bold red]
[bold cyan]6.[/bold cyan] [bold red]Proxy or VPN Relay Usage[/bold red]
[bold cyan]7.[/bold cyan] [bold red]Firewall Rule Blindness Testing[/bold red]
[bold cyan]8.[/bold cyan] [bold red]Exploit Known Firewall Vulnerabilities[/bold red]
[bold cyan]9.[/bold cyan] [bold red]Application Layer Attacks / WAF Evasion[/bold red]
[bold cyan]10.[/bold cyan] [bold red]Rate Limiting and DoS Evasion[/bold red]
[bold cyan]11.[/bold cyan] [bold red]Source Routing Attacks[/bold red]
[bold cyan]12.[/bold cyan] [bold red]TTL Expiry and Timing Attacks[/bold red]
[bold cyan]13.[/bold cyan] [bold red]ICMP Tunneling[/bold red]
[bold cyan]14.[/bold cyan] [bold red]UDP Hole Punching[/bold red]
[bold cyan]15.[/bold cyan] [bold red]SSH Tunneling and Port Forwarding[/bold red]
[bold cyan]16.[/bold cyan] [bold red]Encrypted Traffic Evasion[/bold red]
[bold cyan]17.[/bold cyan] [bold red]Firewall Policy Poisoning[/bold red]
[bold cyan]18.[/bold cyan] [bold red]Using Legitimate Services to Pivot[/bold red]
[bold cyan]19.[/bold cyan] [bold red]Spoofed TCP Flags and Sequence Numbers[/bold red]
[bold cyan]20.[/bold cyan] [bold red]Fast Flux Techniques[/bold red]
[bold cyan]21.[/bold cyan] [bold red]HTTP Parameter Pollution[/bold red]
[bold cyan]22.[/bold cyan] [bold red]Cross-Protocol & CSRF Attacks[/bold red]
[bold cyan]23.[/bold cyan] [bold red]DNS Rebinding Attacks[/bold red]
[bold cyan]24.[/bold cyan] [bold red]Null, Xmas, and FIN Scan Techniques[/bold red]
[bold cyan]25.[/bold cyan] [bold red]SYN Flood with Spoofed IPs[/bold red]
[bold cyan]26.[/bold cyan] [bold red]Firewall Bypass via WebSockets / HTTP2[/bold red]
[bold cyan]27.[/bold cyan] [bold red]FTP Bounce Attacks[/bold red]
[bold cyan]28.[/bold cyan] [bold red]VPN Split Tunneling Abuse[/bold red]
[bold cyan]29.[/bold cyan] [bold red]Stateful Packet Inspection (SPI) Evasion[/bold red]
[bold cyan]30.[/bold cyan] [bold red]IPv6/IPv4 Dual Stack Bypass[/bold red]
[bold cyan]0.[/bold cyan] [bold red]Main Menu[/bold red]
""")
    
    def handle_option(self, option):
        if option == "1":
            self.console.print("[bold cyan]You selected: Firewall Detection[/bold cyan]")
        elif option == "2":
            self.console.print("[bold cyan]You selected: Port Scanning with Evasion[/bold cyan]")
        elif option == "3":
            self.console.print("[bold cyan]You selected: Fragmented Packet Attacks[/bold cyan]")
        elif option == "4":
            self.console.print("[bold cyan]You selected: IP Spoofing and Address Manipulation[/bold cyan]")
        elif option == "5":
            self.console.print("[bold cyan]You selected: Protocol Tunneling and Encapsulation[/bold cyan]")
        elif option == "6":
            self.console.print("[bold cyan]You selected: Proxy or VPN Relay Usage[/bold cyan]")
        elif option == "7":
            self.console.print("[bold cyan]You selected: Firewall Rule Blindness Testing[/bold cyan]")
        elif option == "8":
            self.console.print("[bold cyan]You selected: Exploit Known Firewall Vulnerabilities[/bold cyan]")
        elif option == "9":
            self.console.print("[bold cyan]You selected: Application Layer Attacks / WAF Evasion[/bold cyan]")
        elif option == "10":
            self.console.print("[bold cyan]You selected: Rate Limiting and DoS Evasion[/bold cyan]")
        elif option == "11":
            self.console.print("[bold cyan]You selected: Source Routing Attacks[/bold cyan]")
        elif option == "12":
            self.console.print("[bold cyan]You selected: TTL Expiry and Timing Attacks[/bold cyan]")
        elif option == "13":
            self.console.print("[bold cyan]You selected: ICMP Tunneling[/bold cyan]")
        elif option == "14":
            self.console.print("[bold cyan]You selected: UDP Hole Punching[/bold cyan]")
        elif option == "15":
            self.console.print("[bold cyan]You selected: SSH Tunneling and Port Forwarding[/bold cyan]")
        elif option == "16":
            self.console.print("[bold cyan]You selected: Encrypted Traffic Evasion[/bold cyan]")
        elif option == "17":
            self.console.print("[bold cyan]You selected: Firewall Policy Poisoning[/bold cyan]")
        elif option == "18":
            self.console.print("[bold cyan]You selected: Using Legitimate Services to Pivot[/bold cyan]")
        elif option == "19":
            self.console.print("[bold cyan]You selected: Spoofed TCP Flags and Sequence Numbers[/bold cyan]")
        elif option == "20":
            self.console.print("[bold cyan]You selected: Fast Flux Techniques[/bold cyan]")
        elif option == "21":
            self.console.print("[bold cyan]You selected: HTTP Parameter Pollution[/bold cyan]")
        elif option == "22":
            self.console.print("[bold cyan]You selected: Cross-Protocol & CSRF Attacks[/bold cyan]")
        elif option == "23":
            self.console.print("[bold cyan]You selected: DNS Rebinding Attacks[/bold cyan]")
        elif option == "24":
            self.console.print("[bold cyan]You selected: Null, Xmas, and FIN Scan Techniques[/bold cyan]")
        elif option == "25":
            self.console.print("[bold cyan]You selected: SYN Flood with Spoofed IPs[/bold cyan]")
        elif option == "26":
            self.console.print("[bold cyan]You selected: Firewall Bypass via WebSockets / HTTP2[/bold cyan]")
        elif option == "27":
            self.console.print("[bold cyan]You selected: FTP Bounce Attacks[/bold cyan]")
        elif option == "28":
            self.console.print("[bold cyan]You selected: VPN Split Tunneling Abuse[/bold cyan]")
        elif option == "29":
            self.console.print("[bold cyan]You selected: Stateful Packet Inspection (SPI) Evasion[/bold cyan]")
        elif option == "30":
            self.console.print("[bold cyan]You selected: IPv6/IPv4 Dual Stack Bypass[/bold cyan]")
        elif option == "0":
            return False
        else:
            self.console.print("[bold red]Invalid option. Please try again.[/bold red]")
        return True
    
    def run(self):
        valid_options = {str(i) for i in range(31)} | {"0"}
        running = True
        while running:
            self.display_menu()
            choice = Prompt.ask("[bold yellow]Enter your choice[/bold yellow] [bold cyan](0-30)[/bold cyan]")
            if choice not in valid_options:
                self.console.print("[bold red]Invalid input! Please enter a number from 0 to 30.[/bold red]")
                continue
            running = self.handle_option(choice)
