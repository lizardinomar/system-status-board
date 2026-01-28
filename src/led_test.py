import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO pin assignments (BCM numbering)
LED_SYSTEM  = 17   # Physical pin 11
LED_STOCK   = 22   # Physical pin 15
LED_WEATHER = 27   # Physical pin 13

# Setup GPIO pins as outputs
GPIO.setup(LED_SYSTEM, GPIO.OUT)
GPIO.setup(LED_STOCK, GPIO.OUT)
GPIO.setup(LED_WEATHER, GPIO.OUT)

def test_led(pin, delay=1):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)

try:
    while True:
        test_led(LED_SYSTEM)
        test_led(LED_STOCK)
        test_led(LED_WEATHER)

except KeyboardInterrupt:
    GPIO.cleanup()
