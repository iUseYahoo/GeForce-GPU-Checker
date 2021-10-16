from bs4 import BeautifulSoup
import requests
from time import sleep

gpu3080store = "https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3080" # url of the store, no touchy
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
checkTime = 8
GPU3080name = "GeForce RTX 3080"

class CheckGPUs:
    def gpu3080():
        site = requests.get(gpu3080store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice = soup.find(id='ctl00_LFrame_prdList_rlvProdList_ctrl0_ctrl1_spanFinalPrice').get_text()
        print(f"[*] {GPU3080name} Current Price: {getGPUPrice}")

        if (getGPUPrice != "$899.99"):
            print(f"[+] GeForce RTX 3080 Price: $899.99 : {getGPUPrice} | {gpu3080store}")
        sleep(checkTime)