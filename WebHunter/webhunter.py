import requests
from colorama import Fore
import pyfiglet
from platform import python_version

python_version = python_version().split(".")[0]

url_list = []


def find_hidden_files_folder(security, url, wordlist):
    try:
        def request(url):
            try:
                return requests.get(security + url)
            except requests.exceptions.ConnectionError:
                pass

        target_url = url
        with open(wordlist, "r") as wordlist_file:
            array_of_urls = []
            for line in wordlist_file:
                word = line.strip()
                test_url = target_url + "/" + word
                response = request(test_url)
                if response:
                    print(Fore.GREEN + "[+] Discovered URL --> " + test_url)
                    array_of_urls.append(test_url)

    except KeyboardInterrupt:
        print("\n[+] Quitting the program...")


def find_subdomain(security, url, wordlist):

    try:
        def request(url):
            try:
                return requests.get(security + url)
            except requests.exceptions.ConnectionError:
                pass

        target_url = url
        with open(wordlist, "r") as wordlist_file:
            for line in wordlist_file:
                word = line.strip()
                test_url = word + "." + target_url
                response = request(test_url)
                if response:
                    print(Fore.GREEN + "[+] Discovered Sub-Domain --> " + test_url)

    except KeyboardInterrupt:
        print("\n[+] Quitting...\n\n")


try:
    print(pyfiglet.figlet_format("WebHunter", font="slant"))

    print(Fore.RED + "[!!!] For legal use, please don't use for illegal purposes" + Fore.RESET)
    print(Fore.BLUE + "[***]Report problems and bugs here: https://github.com/jyotisko/WebHunter/issues")

    print(Fore.CYAN + "\nWhat do you want to do (type option number to perform the specific task) ?" + Fore.RESET)
    print(Fore.BLUE + "\t[1] Get possible subdomains for a website")
    print(Fore.BLUE + "\t[2] Get possible hidden paths and directories in a website" + Fore.RESET)
    print(Fore.BLUE + "\t[3] Exit the program" + Fore.RESET)
    user_choice = input(Fore.CYAN + "Your choice>> " + Fore.RESET)

    if user_choice == 1 or user_choice == "1":
        if str(python_version) == "2":
            user_url = raw_input(Fore.CYAN + "Enter complete url of the website to target: " + Fore.RESET)
            user_wordlist = raw_input(Fore.CYAN + "Enter wordlist path: " + Fore.RESET)
        else:
            user_url = input(Fore.CYAN + "Enter complete url of the website to target: " + Fore.RESET)
            user_wordlist = input(Fore.CYAN + "Enter wordlist path: " + Fore.RESET)
        if "www." in user_url:
            user_url = user_url.replace("www.", "")
        if "http://" in user_url:
            user_url = user_url.replace("http://", "")
            security = "http://"
        elif "https://" in user_url:
            user_url = user_url.replace("https://", "")
            security = "https://"
        else:
            security = "http://"
        find_subdomain(security, user_url, user_wordlist)

    elif user_choice == 2 or user_choice == "2":
        if str(python_version) == "2":
            user_url = raw_input(Fore.CYAN + "Enter complete url of the website to target: " + Fore.RESET)
            user_wordlist = raw_input(Fore.CYAN + "Enter wordlist path: " + Fore.RESET)
        else:
            user_url = input(Fore.CYAN + "Enter complete url of the website to target: " + Fore.RESET)
            user_wordlist = input(Fore.CYAN + "Enter wordlist path: " + Fore.RESET)
        if "www." in user_url:
            user_url = user_url.replace("www.", "")
        if "http://" in user_url:
            user_url = user_url.replace("http://", "")
            security = "http://"
        elif "https://" in user_url:
            user_url = user_url.replace("https://", "")
            security = "https://"
        else:
            security = "http://"
        print("\n")
        find_hidden_files_folder(security, user_url, user_wordlist)

    elif user_choice == 3 or user_choice == "3":
        print(Fore.CYAN + "Quitting... Thanks for using!")
        exit()

    else:
        print(Fore.RED + "Not a valid option")

except KeyboardInterrupt:
    print(Fore.RED + "Quitting The Program")
