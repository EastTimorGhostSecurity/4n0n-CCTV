#code by East Timor Ghost Security
#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests, re, colorama
from requests.structures import CaseInsensitiveDict
from colorama import Fore, Style

colorama.init()

url = "http://www.insecam.org/en/jsoncountries/"

headers = CaseInsensitiveDict()
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
headers["Host"] = "www.insecam.org"
headers["Upgrade-Insecure-Requests"] = "1"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/110.0.0.0 Safari/537.36"

resp = requests.get(url, headers=headers)

data = resp.json()
countries = data['countries']

print("""
\033[1;33m███████╗ █████╗ ███████╗████████╗    ████████╗██╗███╗   ███╗ ██████╗ ██████╗      ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗███████╗███████╗ ██████╗
\033[1;33m██╔════╝██╔══██╗██╔════╝╚══██╔══╝    ╚══██╔══╝██║████╗ ████║██╔═══██╗██╔══██╗    ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝██╔════╝
\033[1;37m█████╗  ███████║███████╗   ██║          ██║   ██║██╔████╔██║██║   ██║██████╔╝    ██║  ███╗███████║██║   ██║███████╗   ██║   ███████╗█████╗  ██║     
\033[1;37m██╔══╝  ██╔══██║╚════██║   ██║          ██║   ██║██║╚██╔╝██║██║   ██║██╔══██╗    ██║   ██║██╔══██║██║   ██║╚════██║   ██║   ╚════██║██╔══╝  ██║     
\033[1;31m███████╗██║  ██║███████║   ██║          ██║   ██║██║ ╚═╝ ██║╚██████╔╝██║  ██║    ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ███████║███████╗╚██████╗
\033[1;31m╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝          ╚═╝   ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚══════╝ ╚═════╝
                                                                CODE BY Mr.Y
\033[1;32m""")

col_widths = {
    "code": 6,
    "country": 22
}

country_list = [
    f'{Fore.CYAN}[{key}]{Style.RESET_ALL}  {Fore.LIGHTGREEN_EX}{value["country"]:<{col_widths["country"]}}{Style.RESET_ALL}'
    for key, value in countries.items()
]

for i, country in enumerate(country_list, 1):
    print(f'{country}', end='  ')
    if i % 4 == 0:
        print()

if len(country_list) % 4 != 0:
    print()

try:
    country = input(f"{Fore.CYAN}Country Code{Fore.YELLOW}[$]: {Style.RESET_ALL}")
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\(\"\?page=\", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
    
        with open(f'{country}.txt', 'w') as f:
          for ip in find_ip:
              print(f"{Fore.RED}{ip}{Style.RESET_ALL}")
              f.write(f'{ip}\n')
except:
    pass
finally:
    print(f"\n{Fore.GREEN}Save File : {Fore.YELLOW}{country}.txt{Style.RESET_ALL}")
    exit()
