import Checkers.GPU3090 as check3090
import Checkers.GPU3080 as check3080
import Checkers.GPU3070 as check3070

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
        check3090

def Check3080Evga():
    print("\n")
    while True:
        check3080
        
def Check3070Evga():
    print("\n")
    while True:
        check3070

PickGPUChecker()
