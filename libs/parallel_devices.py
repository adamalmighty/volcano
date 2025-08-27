#libs/parallel_devices.py

from rich.console import Console
from rich.prompt import Prompt

class ParallelDevices:
    def __init__(self):
        self.console = Console()
    
    def display_menu(self):
        self.console.print("""
----------------------------------
><   [bold magenta]Parallel Devices Hacking[/bold magenta]   ><
----------------------------------
        """)
        self.console.print("""
[bold yellow]Please select an option by typing the corresponding number:[/bold yellow]
[bold cyan]1.[/bold cyan] [bold red]Network Device Discovery[/bold red]
[bold cyan]2.[/bold cyan] [bold red]OS Detection & Fingerprinting[/bold red]
[bold cyan]3.[/bold cyan] [bold red]Port and Service Scanning[/bold red]
[bold cyan]4.[/bold cyan] [bold red]Enumerate Shared Resources (SMB/NFS/AirDrop)[/bold red]
[bold cyan]5.[/bold cyan] [bold red]Windows Exploits (EternalBlue, MS17-010, etc.)[/bold red]
[bold cyan]6.[/bold cyan] [bold red]Linux Exploits (DirtyCow, Sudo, SSH, etc.)[/bold red]
[bold cyan]7.[/bold cyan] [bold red]MacOS Exploits & Enumeration[/bold red]
[bold cyan]8.[/bold cyan] [bold red]Android Device Attacks[/bold red]
[bold cyan]9.[/bold cyan] [bold red]IoT & Android TV Device Detection & Exploitation[/bold red]
[bold cyan]10.[/bold cyan] [bold red]Man-in-the-Middle (MITM) Attacks[/bold red]
[bold cyan]11.[/bold cyan] [bold red]Credential Harvesting[/bold red]
[bold cyan]12.[/bold cyan] [bold red]ARP/DNS/LLMNR Poisoning[/bold red]
[bold cyan]13.[/bold cyan] [bold red]Session Hijacking & SMB Relay[/bold red]
[bold cyan]14.[/bold cyan] [bold red]Remote Command Execution[/bold red]
[bold cyan]15.[/bold cyan] [bold red]Privilege Escalation Checks (Win/Linux)[/bold red]
[bold cyan]16.[/bold cyan] [bold red]Pass-the-Hash/Pass-the-Ticket[/bold red]
[bold cyan]17.[/bold cyan] [bold red]ADB (Android Debug Bridge) Exploitation[/bold red]
[bold cyan]18.[/bold cyan] [bold red]Apple AirDrop/Bonjour Attacks[/bold red]
[bold cyan]19.[/bold cyan] [bold red]WiFi Direct/NFC/Bluetooth Attacks[/bold red]
[bold cyan]20.[/bold cyan] [bold red]Persistence Techniques (PC/Mobile)[/bold red]
[bold cyan]21.[/bold cyan] [bold red]Screen/Remote Desktop Hijacking (RDP/VNC)[/bold red]
[bold cyan]22.[/bold cyan] [bold red]Network Print & Scan Device Attacks[/bold red]
[bold cyan]23.[/bold cyan] [bold red]Webcam/Microphone Hijacking[/bold red]
[bold cyan]24.[/bold cyan] [bold red]Data Exfiltration (via Network Services)[/bold red]
[bold cyan]25.[/bold cyan] [bold red]Inter-Device Messaging Snooping[/bold red]
[bold cyan]26.[/bold cyan] [bold red]Rogue DHCP/Network Services[/bold red]
[bold cyan]27.[/bold cyan] [bold red]Worm/Propagation Simulation[/bold red]
[bold cyan]28.[/bold cyan] [bold red]Enumerate & Exploit Smart Home Devices[/bold red]
[bold cyan]29.[/bold cyan] [bold red]Zero-Day Exploit Testing[/bold red]
[bold cyan]30.[/bold cyan] [bold red]Clear Tracks/Logs on Devices[/bold red]
[bold cyan]0.[/bold cyan] [bold red]Main Menu[/bold red]
""")
    
    def handle_option(self, option):
        if option == "1":
            self.console.print("[bold cyan]You selected: Network Device Discovery[/bold cyan]")
        elif option == "2":
            self.console.print("[bold cyan]You selected: OS Detection & Fingerprinting[/bold cyan]")
        elif option == "3":
            self.console.print("[bold cyan]You selected: Port and Service Scanning[/bold cyan]")
        elif option == "4":
            self.console.print("[bold cyan]You selected: Enumerate Shared Resources (SMB/NFS/AirDrop)[/bold cyan]")
        elif option == "5":
            self.console.print("[bold cyan]You selected: Windows Exploits (EternalBlue, MS17-010, etc.)[/bold cyan]")
        elif option == "6":
            self.console.print("[bold cyan]You selected: Linux Exploits (DirtyCow, Sudo, SSH, etc.)[/bold cyan]")
        elif option == "7":
            self.console.print("[bold cyan]You selected: MacOS Exploits & Enumeration[/bold cyan]")
        elif option == "8":
            self.console.print("[bold cyan]You selected: Android Device Attacks[/bold cyan]")
        elif option == "9":
            self.console.print("[bold cyan]You selected: IoT & Android TV Device Detection & Exploitation[/bold cyan]")
        elif option == "10":
            self.console.print("[bold cyan]You selected: Man-in-the-Middle (MITM) Attacks[/bold cyan]")
        elif option == "11":
            self.console.print("[bold cyan]You selected: Credential Harvesting[/bold cyan]")
        elif option == "12":
            self.console.print("[bold cyan]You selected: ARP/DNS/LLMNR Poisoning[/bold cyan]")
        elif option == "13":
            self.console.print("[bold cyan]You selected: Session Hijacking & SMB Relay[/bold cyan]")
        elif option == "14":
            self.console.print("[bold cyan]You selected: Remote Command Execution[/bold cyan]")
        elif option == "15":
            self.console.print("[bold cyan]You selected: Privilege Escalation Checks (Win/Linux)[/bold cyan]")
        elif option == "16":
            self.console.print("[bold cyan]You selected: Pass-the-Hash/Pass-the-Ticket[/bold cyan]")
        elif option == "17":
            self.console.print("[bold cyan]You selected: ADB (Android Debug Bridge) Exploitation[/bold cyan]")
        elif option == "18":
            self.console.print("[bold cyan]You selected: Apple AirDrop/Bonjour Attacks[/bold cyan]")
        elif option == "19":
            self.console.print("[bold cyan]You selected: WiFi Direct/NFC/Bluetooth Attacks[/bold cyan]")
        elif option == "20":
            self.console.print("[bold cyan]You selected: Persistence Techniques (PC/Mobile)[/bold cyan]")
        elif option == "21":
            self.console.print("[bold cyan]You selected: Screen/Remote Desktop Hijacking (RDP/VNC)[/bold cyan]")
        elif option == "22":
            self.console.print("[bold cyan]You selected: Network Print & Scan Device Attacks[/bold cyan]")
        elif option == "23":
            self.console.print("[bold cyan]You selected: Webcam/Microphone Hijacking[/bold cyan]")
        elif option == "24":
            self.console.print("[bold cyan]You selected: Data Exfiltration (via Network Services)[/bold cyan]")
        elif option == "25":
            self.console.print("[bold cyan]You selected: Inter-Device Messaging Snooping[/bold cyan]")
        elif option == "26":
            self.console.print("[bold cyan]You selected: Rogue DHCP/Network Services[/bold cyan]")
        elif option == "27":
            self.console.print("[bold cyan]You selected: Worm/Propagation Simulation[/bold cyan]")
        elif option == "28":
            self.console.print("[bold cyan]You selected: Enumerate & Exploit Smart Home Devices[/bold cyan]")
        elif option == "29":
            self.console.print("[bold cyan]You selected: Zero-Day Exploit Testing[/bold cyan]")
        elif option == "30":
            self.console.print("[bold cyan]You selected: Clear Tracks/Logs on Devices[/bold cyan]")
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