import socket
import colorama
from colorama import Fore, Style
import sys
import requests
from googlesearch import search

colorama.init(autoreset=True)

def input_target(prompt_text):
    print(Fore.MAGENTA + prompt_text, end="")
    target = input().strip()
    if not target:
        print(Fore.RED + "Input cannot be empty. Please try again.")
        return None
    return target

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
                [ Version 4.0.0 ]
         [ Special Thanks to @Vortex4242 ]
    """)

def google_dork(query, num_results=10, proxy=None):
    print(Fore.CYAN + "Performing Google Dork search with payload: " + query)
    results = []
    try:
        response = requests.get(f"https://www.google.com/search?q={query}", timeout=10, proxies={'http': proxy, 'https': proxy} if proxy else None)
        if response.status_code == 200:
            for result in search(query, num_results=num_results):
                results.append(result)
        else:
            print(Fore.RED + f"Error {response.status_code} occurred.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
    if not results:
        print(Fore.RED + "No results found.")
    return results

def display_results(results):
    if results:
        print(Fore.GREEN + "Results found:")
        for result in results:
            print(Fore.WHITE + result)
    else:
        print(Fore.RED + "No results found.")

def menu_select(options):
    for key, value in options.items():
        print(Fore.CYAN + f"{key}: {value}")
    choice = input(Fore.BLUE + "Select an option by number: ")
    return choice

def select_dorking_category(proxy):
    categories = {
        "1": "Website Dorking",
        "2": "Educational Files",
        "3": "Government Files",
        "4": "Social Media Dorking",
        "5": "Camera Dorking",
        "6": "Individual Dorking"
    }

    print(Fore.GREEN + "Available Dorking Categories:\n")
    choice = menu_select(categories)
    if choice == "1":
        select_website_dork(proxy)
    elif choice in ["2", "3", "4"]:
        target_query = "Enter your search query: " if choice == "4" else "Enter the target domain: "
        query = input_target(target_query)
        if not query:
            return
        perform_category_dork(choice, query, proxy)
    elif choice == "5":
        perform_camera_dorking(proxy)
    elif choice == "6":
        query = input_target("Enter your specific query: ")
        results = google_dork(query, proxy=proxy)
        display_results(results)
    else:
        print(Fore.RED + "Invalid selection. Please try again.")

def perform_category_dork(choice, query, proxy):
    payloads = {
        "2": f"site:{query} ext:pdf OR ext:doc OR ext:docx OR ext:ppt OR ext:pptx intitle:\"lectures\" OR \"assignments\" OR \"examinations\" OR \"syllabus\" OR \"academic\" OR \"course\"",
        "3": f"site:{query} ext:gov",
        "4": f"\"{query}\" site:facebook.com OR site:twitter.com OR site:instagram.com OR site:linkedin.com OR site:tumblr.com OR site:pinterest.com"
    }
    results = google_dork(payloads[choice], proxy=proxy)
    display_results(results)

def select_website_dork(proxy):
    website_categories = {
        "1": "Configuration Files",
        "2": "Database Files",
        "3": "Backup Files",
        "4": "Source Code Repositories",
        "5": "Document Files",
        "6": "Error Messages",
        "7": "Common Web Files",
        "8": "Cloud Services",
        "9": "Git Providers",
        "10": "Login Pages"
    }

    print(Fore.GREEN + "Available Website Dork Categories:\n")
    category_choice = menu_select(website_categories)
    if category_choice in website_categories:
        target = input_target("Enter the target domain: ")
        if not target:
            return
        query = generate_website_query(category_choice, target)
        results = google_dork(query, proxy=proxy)
        display_results(results)
    else:
        print(Fore.RED + "Invalid category choice. Please try again.")

def generate_website_query(choice, target):
    queries = {
        "1": f"site:{target} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:env | ext:ini",
        "2": f"site:{target} ext:sql | ext:db | ext:dbf | ext:mdb",
        "3": f"site:{target} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",
        "4": f"inurl:\"/.git\" {target} -site:github.com",
        "5": f"site:{target} ext:doc | ext:docx | ext:odt | ext:pdf",
        "6": f"site:{target} intext:\"error log\"",
        "7": f"site:{target} \"Index of /admin\"",
        "8": f"site:\"blob.core.windows.net\" {target}",
        "9": f"site:github.com {target} | site:gitlab.com {target}",
        "10": f"site:{target} inurl:login"
    }
    return queries[choice]

def perform_camera_dorking(proxy):
    camera_dorks = {
        "1": "inurl:\"CgiStart?page=\"",
        "2": "inurl:/view.shtml",
        "3": "intitle:\"Live View / - AXIS\"",
        # Add more camera dorks as needed
    }

    print(Fore.GREEN + "Available Camera Dorks:\n")
    dork_choice = menu_select(camera_dorks)
    if dork_choice in camera_dorks:
        results = google_dork(camera_dorks[dork_choice], num_results=20, proxy=proxy)
        display_results(results)
    else:
        print(Fore.RED + "Invalid camera dork selection. Please try again.")

def main():
    print_skull()
    proxy = input(Fore.BLUE + "Enter proxy (if any): ")
    select_dorking_category(proxy)

if __name__ == "__main__":
    main()
