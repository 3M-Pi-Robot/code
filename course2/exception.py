import time


try:
    while(True):
        print("test")
        time.sleep(1)        
except KeyboardInterrupt:
    print("End")
finally:
    print("END")
