# Import necessary libraries
import neopixel
from machine import Pin
import time

# Define GPIO pins for tilt switch and NeoPixel
tilt_pin = Pin(26, Pin.IN)
pixel_pin = 28
num_pixels = 15


# Initialize NeoPixel strip
pixels = neopixel.NeoPixel(Pin(pixel_pin), num_pixels, bpp=3)

# Define Christmas colors with reduced intensity for dimmer effect
color_red = (50, 0, 0)         # Red with reduced intensity
color_green = (0, 20, 0)       # Dark Green with reduced intensity
color_gold = (50, 43, 0)       # Gold/Yellow with reduced intensity

# Create a list of Christmas colors
christmas_colors = [color_red, color_green, color_gold]


# Define sleep time for inactivity
sleep_time = 60 * 2  # 2 minutes

last_activity_time = time.time()

# Function to smoothly transition between colors
def transition_color(current_color, target_color, steps):
    step_r = target_color[0] - current_color[0] / steps
    step_g = target_color[1] - current_color[1] / steps
    step_b = target_color[2] - current_color[2] / steps
    
    transitioned_colors = []
    for step in range(steps):
        transitioned_colors.append((
            int(current_color[0] + step_r * step),
            int(current_color[1] + step_g * step),
            int(current_color[2] + step_b * step)
        ))
    return transitioned_colors

try:
    current_color = (0, 0, 0)  # Initial color
    while True:
        # Read tilt switch state
        tilt_state = tilt_pin.value()
        
       # Define the color to transition to based on tilt switch state
        if tilt_state == 1:
            target_colors = christmas_colors
        else:
            target_colors = reversed(christmas_colors)

        # Check if the tilt state has changed
        if tilt_state == 1:  # Tilted
            print("Tilt switch activated!") # Print a message when tilted
        else:
            print("Tilt switch not active.")  # Print a message when not tilted
            for color in christmas_colors:
                transitioned_colors = transition_color(current_color, color, 50)  # Adjust steps for transition
                for new_color in transitioned_colors:
                    pixels.fill(new_color)
                    pixels.write()
                    time.sleep(0.1)  # Adjust the delay between steps for smoother transitions
                current_color = color  # Update current color after transition
               
        # Check for inactivity and activate sleep mode
        current_time = time.time()
        if current_time - last_activity_time > sleep_time:
            pixels.fill((0, 0, 0))  # Turn off the LEDs
            pixels.write()
            last_activity_time = current_time
            
        time.sleep(0.05)  # Adjust the sleep time for responsiveness
    
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))  # Turn off the LEDs before exiting
    pixels.write()
