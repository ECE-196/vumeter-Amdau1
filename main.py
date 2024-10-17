import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore 
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
    # do the rest...
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

maxval = 42000
fastorslow = 0.05
displayed_volume = 0

def get_volume():
    aval = microphone.value
    normal = aval / maxval
    volume = max(0, normal - 0.1)
    
    return volume
def update_leds(volume):
    cnt = len(leds)
    ledon= int(volume * cnt)
    for i in range(cnt):
        leds[i].value = i < ledon

# Main loop
while True:
    volume = get_volume()
    if volume > displayed_volume:
        displayed_volume = volume
    else:
        displayed_volume = max(0, displayed_volume - fastorslow)
    update_leds(displayed_volume)
    sleep(1)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
