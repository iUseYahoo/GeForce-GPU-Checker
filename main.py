from bs4 import BeautifulSoup
import requests
from time import sleep
import sys

arg = sys.argv

checkTime = 8

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

gpu3090store = "https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3090" # url of the store, no touchy
GPU3090name = "GeForce RTX 3090"

gpu3080store = "https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3080" # url of the store, no touchy
GPU3080name = "GeForce RTX 3080"

gpu3070store = "https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3070" # url of the store, no touchy
GPU3070name = "GeForce RTX 3070"

gpu3060store = "https://www.evga.com/products/product.aspx?pn=12G-P5-3655-KR" # url of the store, no touchy
GPU3060name = "GeForce RTX 3060"

class CheckGPUs:
    def gpu3090():
        site = requests.get(gpu3090store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice = soup.find(id='ctl00_LFrame_prdList_rlvProdList_ctrl0_ctrl1_spanFinalPrice').get_text()
        print(f"[*] {GPU3090name} Current Price: {getGPUPrice}")

        if (getGPUPrice != "$1739.99"):
            print(f"[+] GeForce RTX 3090 Price: {getGPUPrice} | {gpu3090store}")
        sleep(checkTime)

    def gpu3080():
        site = requests.get(gpu3080store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice = soup.find(id='ctl00_LFrame_prdList_rlvProdList_ctrl0_ctrl1_spanFinalPrice').get_text()
        print(f"[*] {GPU3080name} Current Price: {getGPUPrice}")

        if (getGPUPrice != "$899.99"):
            print(f"[+] GeForce RTX 3080 Price: {getGPUPrice} | {gpu3080store}")
        sleep(checkTime)

    def gpu3070():
        site = requests.get(gpu3070store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice = soup.find(id='ctl00_LFrame_prdList_rlvProdList_ctrl0_ctrl1_spanFinalPrice').get_text()
        print(f"[*] {GPU3070name} Current Price: {getGPUPrice}")

        if (getGPUPrice != "$709.99"):
            print(f"[+] GeForce RTX 3070 Price: $709.99 : {getGPUPrice} | {gpu3070store}")
        sleep(checkTime)

    def gpu3060():
        site = requests.get(gpu3070store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice = soup.find(id='LFrame_spanFinalPrice').get_text()
        print(f"[*] {GPU3060name} Current Price: {getGPUPrice}")

        if (getGPUPrice != "$339.99"):
            print(f"[+] GeForce RTX 3060 Price: {getGPUPrice} | {gpu3060store}")
        sleep(checkTime)

def sysarg():
    if (arg[1] == "3090"):
        Check3090Evga()
    elif (arg[1] == "3080"):
        Check3080Evga()
    elif (arg[1] == "3070"):
        Check3070Evga()
    elif (arg[1] == "3060"):
        Check3060Evga()
    elif (arg[1] == "gpus"):
        print("\n---- GPU List ----\nGeForce RTX 3090\nGeForce RTX 3080\nGeForce RTX 3070\nGeForce RTX 3060")
        print("-" * 18)
    else:
        print("That GPU isnt added.")
        sys.exit()

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

def Check3060Evga():
    print("\n")
    while True:
        CheckGPUs.gpu3060()

sysarg()