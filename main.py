import requests
from bs4 import BeautifulSoup
from time import sleep

gpu3090store = "https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3090" # url of the store, no touchy
gpu3080store = "https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3080"
checkTime = 8 # this is the refresh time, pretty much how long for the next check message status
# You can change the header to a user agent that you want
# or you can keep it default, it doesnt really matter
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
GPU3090name = "GeForce RTX 3090"
GPU3080name = "GeForce RTX 3080"

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
            print(f"[+] GeForce RTX 3080 Price: $899.99 : {getGPUPrice} | https://www.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3080")
        sleep(checkTime)


def PickGPUChecker():
    print("1 - 3090 (EVGA) | 2 - 3080 (EVGA)")
    pickGPU = input("Pick GPU: ")

    if (pickGPU == "1"):
        Check3090Evga()
    elif (pickGPU == "2"):
        Check3080Evga()
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

PickGPUChecker()
