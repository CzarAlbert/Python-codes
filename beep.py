import winsound 
import time

x= 10
while x >= 0 :
    print(x)
    x-=1
    time.sleep(0.5)

winsound.Beep(500, 1000)

