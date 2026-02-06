import RPi.GPIO as GPIO
import time

# -------------------------
# GPIO SETUP
# -------------------------
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

SUBSYSTEMS = {
    "Stock-Green": 16,
    "Stock-Red": 18,
    "Weather-Blue": 29,
    "Weather-Pink": 31,
}

BUZZER = 22

for pin in SUBSYSTEMS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

GPIO.setup(BUZZER, GPIO.OUT)
GPIO.output(BUZZER, GPIO.LOW)

print("System Status Hub Initialized")

# -------------------------
# HELPER FUNCTIONS
# -------------------------
def flash(pin, duration=1):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)

def heartbeat():
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(BUZZER, GPIO.LOW)

# -------------------------
# MAIN LOOP
# -------------------------
try:
    while True:
        for name, pin in SUBSYSTEMS.items():
            print(f"Subsystem active: {name}")
            flash(pin, 1)
            heartbeat()
            time.sleep(0.3)

except KeyboardInterrupt:
    print("Shutting down Status Hub")

finally:
    GPIO.cleanup()
