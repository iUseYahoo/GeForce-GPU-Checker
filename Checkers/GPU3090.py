from bs4 import BeautifulSoup
import requests
from time import sleep

gpu3090store = "https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3090" # url of the store, no touchy
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
checkTime = 8
GPU3090name = "GeForce RTX 3090"

class CheckGPUs:
    def gpu3090():
        site = requests.get(gpu3090store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice = soup.find(id='ctl00_LFrame_prdList_rlvProdList_ctrl0_ctrl1_spanFinalPrice').get_text()
        print(f"[*] {GPU3090name} Current Price: {getGPUPrice}")

        if (getGPUPrice != "$1739.99"):
            print(f"[+] GeForce RTX 3090 Price: $1739.99 : {getGPUPrice} | https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3090")
        sleep(checkTime)