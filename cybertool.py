from colorama import Fore, Style
import pyfiglet
import requests
import sys

# 🎨 Banner
banner = pyfiglet.figlet_format("CyberTool")
print(Fore.CYAN + banner + Style.RESET_ALL)
print(Fore.YELLOW + "🔍 Created by Cyber Cratic | IP Tracker Tool\n" + Style.RESET_ALL)

def track_ip(ip):
    try:
        response = requests.get(f"http://ipinfo.io/{ip}/json")
        data = response.json()

        print(Fore.GREEN + "\n📡 CyberTool IP Tracker")
        print("---------------------------")
        print(f"IP Address : {data.get('ip')}")
        print(f"City       : {data.get('city')}")
        print(f"Region     : {data.get('region')}")
        print(f"Country    : {data.get('country')}")
        print(f"Location   : {data.get('loc')}")
        print(f"Organization: {data.get('org')}")
        print(f"Timezone   : {data.get('timezone')}")
        print(f"Postal Code: {data.get('postal')}")
        print("---------------------------\n" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"⚠️ Error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "⚠️ Usage: python cybertool.py <ip_address>" + Style.RESET_ALL)
        sys.exit(1)

    ip = sys.argv[1]
    track_ip(ip)
