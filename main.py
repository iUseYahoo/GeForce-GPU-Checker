from bs4 import BeautifulSoup
import requests
from time import sleep

checkTime = 8

gpu3090store = "https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3090" # url of the store, no touchy
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
GPU3090name = "GeForce RTX 3090"

gpu3080store = "https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3080" # url of the store, no touchy
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
GPU3080name = "GeForce RTX 3080"

gpu3070store = "https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3070" # url of the store, no touchy
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
GPU3070name = "GeForce RTX 3070"

class CheckGPUs:
    def gpu3090():
        site = requests.get(gpu3090store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice = soup.find(id='ctl00_LFrame_prdList_rlvProdList_ctrl0_ctrl1_spanFinalPrice').get_text()
        print(f"[*] {GPU3090name} Current Price: {getGPUPrice}")

        if (getGPUPrice != "$1739.99"):
            print(f"[+] GeForce RTX 3090 Price: $1739.99 : {getGPUPrice} | https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3090")
        sleep(checkTime)

    def gpu3080():
        site = requests.get(gpu3080store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice = soup.find(id='ctl00_LFrame_prdList_rlvProdList_ctrl0_ctrl1_spanFinalPrice').get_text()
        print(f"[*] {GPU3080name} Current Price: {getGPUPrice}")

        if (getGPUPrice != "$899.99"):
            print(f"[+] GeForce RTX 3080 Price: $899.99 : {getGPUPrice} | {gpu3080store}")
        sleep(checkTime)

    def gpu3070():
        site = requests.get(gpu3070store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice = soup.find(id='ctl00_LFrame_prdList_rlvProdList_ctrl0_ctrl1_spanFinalPrice').get_text()
        print(f"[*] {GPU3070name} Current Price: {getGPUPrice}")

        if (getGPUPrice != "$709.99"):
            print(f"[+] GeForce RTX 3070 Price: $709.99 : {getGPUPrice} | {gpu3070store}")
        sleep(checkTime)


def PickGPUChecker():
    print("1 - 3090 (EVGA) | 2 - 3080 (EVGA) | 3 - 3070 (EVGA)")
    pickGPU = input("Pick GPU: ")

    if (pickGPU == "1"):
        Check3090Evga()
    elif (pickGPU == "2"):
        Check3080Evga()
    elif (pickGPU == "3"):
        Check3070Evga()
    else:
        quit()

def Check3090Evga():
    print("\n")
    while True:
        CheckGPUs.gpu3090()

def Check3080Evga():
    print("\n")
    while True:
        CheckGPUs.gpu3080()
        
def Check3070Evga():
    print("\n")
    while True:
        CheckGPUs.gpu3070()

PickGPUChecker()
