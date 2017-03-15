from gpiozero import LED, Button
from time import sleep
from random import uniform
from time import time
import numbers
import decimal

led = LED(3)
right_button = Button(15)
left_button = Button(14)



def blink(timer):
    if (isinstance(timer,numbers.Number) == 0):
        print('wrong arg, blink is waiting for a number, '+timer+' given')
        return

    timeStamp = timeNow = time()
    while(timeNow - timeStamp < timer):
        print('Blink ' + str(timeNow - timeStamp))
        timeNow = time()
        led.on()
        sleep(0.25)
        led.off()
        sleep(0.25)


def pressed(button):
    print(str(button.pin.number) + ' won the game')
    sleep(2)
    blink(uniform(4, 6))

print('Initializing components')
blink(4)
right_button.when_pressed = pressed
left_button.when_pressed = pressed
