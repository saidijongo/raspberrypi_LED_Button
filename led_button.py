from gpiozero import LED, Button
from signal import pause

led1 = LED(19)
led2 = LED(26)
button1 = Button(4)
button2 = Button(3)

def jongo_blink():
    while True:
        led1.on()
        sleep(1)
        led1.off()
        led2.on()
        sleep(1)
        led2.off()

def butt_stop():
    led1.off()
    led2.off()

def restart_blink():
    led1.off()
    led2.off()
    jongo_blink()

try:
    name = "Jongo"
    print(f"There you go {name}, started blinking")
    jongo_blink()

    button1.when_pressed = butt_stop
    button2.when_pressed = jongo_blink

    

except KeyboardInterrupt:
    led1.off()
    led2.off()
