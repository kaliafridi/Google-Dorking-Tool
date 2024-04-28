from googlesearch import search
import colorama
from colorama import Fore, Style
import sys

colorama.init(autoreset=True)

def print_skull():
    print(Fore.YELLOW + r"""
┌──────────────────────────────────┐
│                                  │
│ ╔═╗┌─┐┌─┐┌─┐┬  ┌─┐  ╔╦╗┌─┐┬─┐┬┌─ │
│ ║ ╦│ ││ ││ ┬│  ├┤    ║║│ │├┬┘├┴┐ │
│ ╚═╝└─┘└─┘└─┘┴─┘└─┘  ═╩╝└─┘┴└─┴ ┴ │
│                                  │
└──────────────────────────────────┘
┌──────────────────────────────────────┐
│                                      │
│   _   _      _   _   _   _   _   _   │
│  / \ / \    / \ / \ / \ / \ / \ / \  │
│ ( B | y )  ( R | a | y | y | a | n ) │
│  \_/ \_/    \_/ \_/ \_/ \_/ \_/ \_/  │
│                                      │
└──────────────────────────────────────┘
              """)


def google_dork(query, num_results=10):
    print(Fore.CYAN + "Performing Google Dork search with payload: " + query)
    results = []
    try:
        for result in search(query, num_results=num_results):
            results.append(result)
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
    if not results:
        print(Fore.RED + "No such results.")
    return results

def display_results(results):
    if results:
        print(Fore.GREEN + "Results found:")
        for result in results:
            print(Fore.WHITE + result)
    else:
        print(Fore.RED + "No results found.")

def select_website_dork(target):
    categories = {
        "Configuration Files": "site:{target} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:env | ext:ini",
        "Database Files": "site:{target} ext:sql | ext:db | ext:dbf | ext:mdb",
        "Backup Files": "site:{target} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",
        "Source Code Repositories": "inurl:\"/.git\" {target} -site:github.com",
        "Document Files": "site:{target} ext:doc | ext:docx | ext:odt | ext:pdf",
        "Error Messages": "site:{target} intext:\"error log\"",
        "Common Web Files": "site:{target} \"Index of /admin\"",
        "Cloud Services": "site:\"blob.core.windows.net\" {target}",
        "Git Providers": "site:github.com {target} | site:gitlab.com {target}",
        "Login Pages": "site:{target} inurl:login"
    }

    print(Fore.GREEN + "Available Website Categories:\n")
    for key in categories:
        print(Fore.CYAN + Style.BRIGHT + key)

    category_choice = input(Fore.BLUE + "Enter the category name exactly as shown: ")
    if category_choice in categories:
        query = categories[category_choice].format(target=target)
        results = google_dork(query)
        display_results(results)
    else:
        print(Fore.RED + "Invalid category choice. Please try again.")

def individual_dorking():
    query = input(Fore.MAGENTA + "Enter your specific query: ").strip()
    results = google_dork(query, num_results=20)
    display_results(results)

def camera_dorking():
    camera_dorks = [
        "inurl:”CgiStart?page=”",
        "inurl:/view.shtml",
        "intitle:”Live View/ — AXIS”",
        "intitle:”live view” intitle:axis",
        "intitleiaxis intitle:”video server",
        "intitle:”Live View/ — AXIS 206M”",
        "intitle:”sony network camera snc-pl ?",
        "site:.viewnetcam.com -www.viewnetcam.com",
        "intitle:”i-Catcher Console — Web Monitor”",   
    ]

    print(Fore.GREEN + "Available Camera Dorks:\n")
    for dork in camera_dorks:
        print(Fore.CYAN + Style.BRIGHT + dork)

def main():
    print_skull()
    print(Fore.YELLOW + "1. Website Dorking")
    print(Fore.YELLOW + "2. Individual Dorking")
    print(Fore.YELLOW + "3. Camera Dorking")
    choice = int(input(Fore.BLUE + "Select an option (1, 2, or 3): "))
    
    if choice == 1:
        target = input(Fore.MAGENTA + "Enter the target domain: ").strip()
        select_website_dork(target)
    elif choice == 2:
        individual_dorking()
    elif choice == 3:
        camera_dorking()
    else:
        print(Fore.RED + "Invalid selection. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
