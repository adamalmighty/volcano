#libs/web_application.py

from rich.console import Console
from rich.prompt import Prompt

class WebApplication:
    def __init__(self):
        self.console = Console()

    def display_menu(self):
        self.console.print("""
---------------------------------------------
><   [bold magenta]Web Application Penetration Testing[/bold magenta]   ><
---------------------------------------------
        """)
        self.console.print("""
[bold yellow]Please select an option by typing the corresponding number:[/bold yellow]
[bold cyan]1.[/bold cyan] [bold red]Manual Domain Input[/bold red]
[bold cyan]2.[/bold cyan] [bold red]Subdomain Enumeration (subfinder/sublist3r)[/bold red]
[bold cyan]3.[/bold cyan] [bold red]Subdomain Verification (httpx-toolkit)[/bold red]
[bold cyan]4.[/bold cyan] [bold red]Subdomain Takeover Testing (subzy)[/bold red]
[bold cyan]5.[/bold cyan] [bold red]Webpage Crawling (URL Collection)[/bold red]
[bold cyan]6.[/bold cyan] [bold red]IP Address Enumeration[/bold red]
[bold cyan]7.[/bold cyan] [bold red]IP Verification (Detect real vs firewall IPs)[/bold red]
[bold cyan]8.[/bold cyan] [bold red]SQL Injection Testing[/bold red]
[bold cyan]9.[/bold cyan] [bold red]Cross-Site Scripting (XSS) Testing[/bold red]
[bold cyan]10.[/bold cyan] [bold red]Cross-Site Request Forgery (CSRF) Testing[/bold red]
[bold cyan]11.[/bold cyan] [bold red]Authentication Bypass Testing[/bold red]
[bold cyan]12.[/bold cyan] [bold red]Session Management Testing[/bold red]
[bold cyan]13.[/bold cyan] [bold red]File Upload Vulnerability Testing[/bold red]
[bold cyan]14.[/bold cyan] [bold red]Directory Traversal Testing[/bold red]
[bold cyan]15.[/bold cyan] [bold red]Command Injection Testing[/bold red]
[bold cyan]16.[/bold cyan] [bold red]Insecure Deserialization Testing[/bold red]
[bold cyan]17.[/bold cyan] [bold red]Security Misconfiguration Testing[/bold red]
[bold cyan]18.[/bold cyan] [bold red]Unvalidated Redirects and Forwards Testing[/bold red]
[bold cyan]19.[/bold cyan] [bold red]Sensitive Data Exposure Testing[/bold red]
[bold cyan]20.[/bold cyan] [bold red]Broken Access Control Testing[/bold red]
[bold cyan]21.[/bold cyan] [bold red]Local File Inclusion (LFI) Testing[/bold red]
[bold cyan]22.[/bold cyan] [bold red]Remote File Inclusion (RFI) Testing[/bold red]
[bold cyan]23.[/bold cyan] [bold red]XML External Entity (XXE) Testing[/bold red]
[bold cyan]24.[/bold cyan] [bold red]Broken Authentication Testing[/bold red]
[bold cyan]25.[/bold cyan] [bold red]Business Logic Testing[/bold red]
[bold cyan]26.[/bold cyan] [bold red]Clickjacking Testing[/bold red]
[bold cyan]27.[/bold cyan] [bold red]API Security Testing[/bold red]
[bold cyan]28.[/bold cyan] [bold red]Security Headers Testing[/bold red]
[bold cyan]29.[/bold cyan] [bold red]SSL/TLS Certificate Validation[/bold red]
[bold cyan]30.[/bold cyan] [bold red]SSL/TLS Configuration Testing[/bold red]
[bold cyan]31.[/bold cyan] [bold red]Security Logging and Monitoring Testing[/bold red]
[bold cyan]32.[/bold cyan] [bold red]JavaScript and HTML Injection Testing[/bold red]
[bold cyan]33.[/bold cyan] [bold red]Memory Leak and DoS Testing[/bold red]
[bold cyan]34.[/bold cyan] [bold red]Content Security Policy (CSP) Testing[/bold red]
[bold cyan]35.[/bold cyan] [bold red]OAuth and OpenID Connect Testing[/bold red]
[bold cyan]36.[/bold cyan] [bold red]Sensitive Information in URL / Query Parameters Testing[/bold red]
[bold cyan]37.[/bold cyan] [bold red]Third-Party Components and Vulnerabilities Testing[/bold red]
[bold cyan]38.[/bold cyan] [bold red]Resource Exhaustion and Rate Limiting Testing[/bold red]
[bold cyan]39.[/bold cyan] [bold red]Server-Side Template Injection (SSTI) Testing[/bold red]
[bold cyan]40.[/bold cyan] [bold red]Remote Code Execution (RCE) Testing[/bold red]
[bold cyan]41.[/bold cyan] [bold red]GraphQL Security Testing[/bold red]
[bold cyan]42.[/bold cyan] [bold red]WebSocket Security Testing[/bold red]
[bold cyan]43.[/bold cyan] [bold red]HTTP Request Smuggling & Desynchronization Attacks[/bold red]
[bold cyan]44.[/bold cyan] [bold red]JWT Security Testing[/bold red]
[bold cyan]45.[/bold cyan] [bold red]OAuth Token Manipulation[/bold red]
[bold cyan]46.[/bold cyan] [bold red]Cloud Service Misconfiguration Testing[/bold red]
[bold cyan]47.[/bold cyan] [bold red]Mobile App Backend API Testing[/bold red]
[bold cyan]48.[/bold cyan] [bold red]Client-Side Template Injection[/bold red]
[bold cyan]49.[/bold cyan] [bold red]Dependency Confusion & Supply Chain Attacks[/bold red]
[bold cyan]50.[/bold cyan] [bold red]CSV, XML, HTML, PHP Injection Testing[/bold red]
[bold cyan]0.[/bold cyan] [bold red]Main Menu[/bold red]
""")

    def handle_option(self, option):
        if option == "1":
            self.console.print("[bold cyan]You selected: Manual Domain Input[/bold cyan]")
        elif option == "2":
            self.console.print("[bold cyan]You selected: Subdomain Enumeration (subfinder/sublist3r)[/bold cyan]")
        elif option == "3":
            self.console.print("[bold cyan]You selected: Subdomain Verification (httpx-toolkit)[/bold cyan]")
        elif option == "4":
            self.console.print("[bold cyan]You selected: Subdomain Takeover Testing (subzy)[/bold cyan]")
        elif option == "5":
            self.console.print("[bold cyan]You selected: Webpage Crawling (URL Collection)[/bold cyan]")
        elif option == "6":
            self.console.print("[bold cyan]You selected: IP Address Enumeration[/bold cyan]")
        elif option == "7":
            self.console.print("[bold cyan]You selected: IP Verification (Detect real vs firewall IPs)[/bold cyan]")
        elif option == "8":
            self.console.print("[bold cyan]You selected: SQL Injection Testing[/bold cyan]")
        elif option == "9":
            self.console.print("[bold cyan]You selected: Cross-Site Scripting (XSS) Testing[/bold cyan]")
        elif option == "10":
            self.console.print("[bold cyan]You selected: Cross-Site Request Forgery (CSRF) Testing[/bold cyan]")
        elif option == "11":
            self.console.print("[bold cyan]You selected: Authentication Bypass Testing[/bold cyan]")
        elif option == "12":
            self.console.print("[bold cyan]You selected: Session Management Testing[/bold cyan]")
        elif option == "13":
            self.console.print("[bold cyan]You selected: File Upload Vulnerability Testing[/bold cyan]")
        elif option == "14":
            self.console.print("[bold cyan]You selected: Directory Traversal Testing[/bold cyan]")
        elif option == "15":
            self.console.print("[bold cyan]You selected: Command Injection Testing[/bold cyan]")
        elif option == "16":
            self.console.print("[bold cyan]You selected: Insecure Deserialization Testing[/bold cyan]")
        elif option == "17":
            self.console.print("[bold cyan]You selected: Security Misconfiguration Testing[/bold cyan]")
        elif option == "18":
            self.console.print("[bold cyan]You selected: Unvalidated Redirects and Forwards Testing[/bold cyan]")
        elif option == "19":
            self.console.print("[bold cyan]You selected: Sensitive Data Exposure Testing[/bold cyan]")
        elif option == "20":
            self.console.print("[bold cyan]You selected: Broken Access Control Testing[/bold cyan]")
        elif option == "21":
            self.console.print("[bold cyan]You selected: Local File Inclusion (LFI) Testing[/bold cyan]")
        elif option == "22":
            self.console.print("[bold cyan]You selected: Remote File Inclusion (RFI) Testing[/bold cyan]")
        elif option == "23":
            self.console.print("[bold cyan]You selected: XML External Entity (XXE) Testing[/bold cyan]")
        elif option == "24":
            self.console.print("[bold cyan]You selected: Broken Authentication Testing[/bold cyan]")
        elif option == "25":
            self.console.print("[bold cyan]You selected: Business Logic Testing[/bold cyan]")
        elif option == "26":
            self.console.print("[bold cyan]You selected: Clickjacking Testing[/bold cyan]")
        elif option == "27":
            self.console.print("[bold cyan]You selected: API Security Testing[/bold cyan]")
        elif option == "28":
            self.console.print("[bold cyan]You selected: Security Headers Testing[/bold cyan]")
        elif option == "29":
            self.console.print("[bold cyan]You selected: SSL/TLS Certificate Validation[/bold cyan]")
        elif option == "30":
            self.console.print("[bold cyan]You selected: SSL/TLS Configuration Testing[/bold cyan]")
        elif option == "31":
            self.console.print("[bold cyan]You selected: Security Logging and Monitoring Testing[/bold cyan]")
        elif option == "32":
            self.console.print("[bold cyan]You selected: JavaScript and HTML Injection Testing[/bold cyan]")
        elif option == "33":
            self.console.print("[bold cyan]You selected: Memory Leak and DoS Testing[/bold cyan]")
        elif option == "34":
            self.console.print("[bold cyan]You selected: Content Security Policy (CSP) Testing[/bold cyan]")
        elif option == "35":
            self.console.print("[bold cyan]You selected: OAuth and OpenID Connect Testing[/bold cyan]")
        elif option == "36":
            self.console.print("[bold cyan]You selected: Sensitive Information in URL / Query Parameters Testing[/bold cyan]")
        elif option == "37":
            self.console.print("[bold cyan]You selected: Third-Party Components and Vulnerabilities Testing[/bold cyan]")
        elif option == "38":
            self.console.print("[bold cyan]You selected: Resource Exhaustion and Rate Limiting Testing[/bold cyan]")
        elif option == "39":
            self.console.print("[bold cyan]You selected: Server-Side Template Injection (SSTI) Testing[/bold cyan]")
        elif option == "40":
            self.console.print("[bold cyan]You selected: Remote Code Execution (RCE) Testing[/bold cyan]")
        elif option == "41":
            self.console.print("[bold cyan]You selected: GraphQL Security Testing[/bold cyan]")
        elif option == "42":
            self.console.print("[bold cyan]You selected: WebSocket Security Testing[/bold cyan]")
        elif option == "43":
            self.console.print("[bold cyan]You selected: HTTP Request Smuggling & Desynchronization Attacks[/bold cyan]")
        elif option == "44":
            self.console.print("[bold cyan]You selected: JWT Security Testing[/bold cyan]")
        elif option == "45":
            self.console.print("[bold cyan]You selected: OAuth Token Manipulation[/bold cyan]")
        elif option == "46":
            self.console.print("[bold cyan]You selected: Cloud Service Misconfiguration Testing[/bold cyan]")
        elif option == "47":
            self.console.print("[bold cyan]You selected: Mobile App Backend API Testing[/bold cyan]")
        elif option == "48":
            self.console.print("[bold cyan]You selected: Client-Side Template Injection[/bold cyan]")
        elif option == "49":
            self.console.print("[bold cyan]You selected: Dependency Confusion & Supply Chain Attacks[/bold cyan]")
        elif option == "50":
            self.console.print("[bold cyan]You selected: CSV, XML, HTML, PHP Injection Testing[/bold cyan]")
        elif option == "0":
            return False
        else:
            self.console.print("[bold red]Invalid option. Please try again.[/bold red]")
        return True

    def run(self):
        valid_options = {str(i) for i in range(51)} | {"0"}
        running = True
        while running:
            self.display_menu()
            choice = Prompt.ask("[bold yellow]Enter your choice[/bold yellow] [bold cyan](0-50)[/bold cyan]")
            if choice not in valid_options:
                self.console.print("[bold red]Invalid input! Please enter a number from 0 to 50.[/bold red]")
                continue
            running = self.handle_option(choice)
