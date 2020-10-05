from microbit import *
import radio

while True :
    msg = uart.read()
    if msg :
        display.scroll(msg)
