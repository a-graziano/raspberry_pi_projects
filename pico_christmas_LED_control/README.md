# Raspberry Pi Pico Christmas LED Control

This script controls a NeoPixel LED strip using a Raspberry Pi Pico and a tilt switch to create a Christmas-themed lighting effect. When tilted, the LEDs smoothly transition through Christmas colors.

## Hardware Setup

- Raspberry Pi Pico
- NeoPixel LED strip
- Tilt switch

Connect the components according to the provided GPIO pin configurations in the script.

## Script Description

The script initializes the NeoPixel LED strip and defines Christmas colors with reduced intensity for a dimmer effect. It continuously monitors the tilt switch state and transitions through Christmas colors when tilted.

### Usage

1. Load the script onto your Raspberry Pi Pico as `main.py`.
2. Connect the components as per the provided GPIO configurations.
3. Power on the Raspberry Pi Pico.
4. Tilt the switch to observe the Christmas-themed LED transition effect.

## Script Notes

- Adjust the GPIO pin configurations in the script according to your hardware setup.
- Modify color values or add more colors in the `christmas_colors` list for different effects.
- You can adjust the transition steps for smoother or quicker color transitions.
