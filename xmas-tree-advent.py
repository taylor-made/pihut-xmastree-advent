from gpiozero import LEDBoard
from signal import pause
import datetime

pinmap = { 4:1, 5:7, 6:16, 7:22, 8:6, 9:14, 10:8, 11:21, 12:15, 13:3, 14:19, 15:2, 16:9, 17:10, 18:20, 19:18, 20:17, 21:4, 22:24, 23:23, 24:13, 25:5, 26:12, 27:11 }

leds = LEDBoard(*range(4,28), pwm=True)

def createSource(day):
 while True:
  yield day <= datetime.date.today().day

for led in leds:
 day = pinmap[led.pin.number]
 led.source = createSource(day)
 led.source_delay = 60

pause()