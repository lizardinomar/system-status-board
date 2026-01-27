# real-time-stock-alert-system
## Overview
This project is a Raspberry Pie-based system status hub that uses LEDs to indicate the functioning of different services running on the Pi.
Each LED represents a subsystem amd turns off if it detects a malfunction in that service. The LEDs all blink in a specific sequence.

## LED Status Mapping
| GPIO Pin | LED Color | System Monitored | Behavior |
|--------|----------|------------------|----------|
| GPIO17 (Pin 11) | Purple | Core System | ON = Pi running, OFF = Pi down |
| GPIO22 (Pin 15) | Yellow | Stock Monitor | ON = service running, OFF = service down |
| GPIO27 (Pin 13) | Orange | Weather Service | ON = service running, OFF = service down |

## Hardware
- Raspberry Pi Zero 2 W
- Breadboard
- 3x LEDs (Purple, Orange, Yellow)
- 3x 470Ω resistors
- Jumper Wires
- 5v power supply
- GPIO pins are set HIGH when their corresponding system is running  
- GPIO pins are set LOW when a system or service is down  
- LEDs provide immediate visual feedback for system health  

## Wiring
- Each LED anode (+) connects to its GPIO pin through a 470Ω resistor.
- All LED cathodes (-) share a common GND rail connected to Pi GND.
- Pi 5V (Pin 4) connected to red power rail.
- Pi GND (Pin 6) connected to blue ground rail.

![Breadboard Wiring](wiring/led_diagram.png)

---

## Software Logic
- GPIO pins are set HIGH when their corresponding system is running.  
- GPIO pins are set LOW when a system or service is down.
- LEDs provide immediate visual feedback for system health. 
