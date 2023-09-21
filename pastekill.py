import threading
from time import sleep
from os import remove
from sys import argv

#Config necesary for interacting with pastebin
import requests as req

req.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"

API_DEV_KEY = "YOUR API_DEV_KEY HERE"
API_USER_KEY = "YOUR API_USER_KEY HEY"
PASTE_KEY = "KEY TO THE PASTE WHERE KILL CODE WILL BE"
kill_code = "THE CODE THAT WILL KILL THE PROGRAM"

def hacking():
    # Dummy function to simulate some task
    while True:
        print("doing cool hacking stuff")
        sleep(1)
   

def killer():
    # Function that reads paste for kill code and if found runs the kill function
    while True:
        switch_code = check_switch()
        signal = bool(switch_code == kill_code)
        print(f"signal: {signal}")
        print(f"switch code: {switch_code}")
        if(signal):
            run_kill()
        sleep(5)

def run_kill():
    # run cleanup tasks and exit
    # exit code is for debugging

    # example cleanup that deletes the file running this code
    #remove(argv[0])

    print("killing and exiting")
    exit(45)

def check_switch():
    # Pretty self explanitory
    url = "https://pastebin.com/api/api_raw.php"
    
    data_obj = {
    	    "api_dev_key": API_DEV_KEY,
    	    "api_user_key": API_USER_KEY,
    	    "api_option": "show_paste",
    	    "api_paste_key": PASTE_KEY
    	}
    	
    switch_code = req.post(url, data=data_obj)
    	
    return switch_code.text
    


# example usage:
# hacking_thread = threading.Thread(target=hacking, daemon=True)
# killer_thread = threading.Thread(target=killer)

# hacking_thread.start()
# killer_thread.start()

