import time
import threading

def segundos():
    s = 0
    while True:
        print(f"segundo {s}", end="\r")
        time.sleep(1)
        s += 1  

threading.Thread(target=segundos).start()
