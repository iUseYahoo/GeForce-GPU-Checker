from bs4 import BeautifulSoup
import requests
from time import sleep

gpu3070store = "https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3070" # url of the store, no touchy
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
checkTime = 8
GPU3070name = "GeForce RTX 3070"

class CheckGPUs:
    def gpu3070():
        site = requests.get(gpu3070store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice = soup.find(id='ctl00_LFrame_prdList_rlvProdList_ctrl0_ctrl1_spanFinalPrice').get_text()
        print(f"[*] {GPU3070name} Current Price: {getGPUPrice}")

        if (getGPUPrice != "$709.99"):
            print(f"[+] GeForce RTX 3070 Price: $709.99 : {getGPUPrice} | {gpu3070store}")
        sleep(checkTime)