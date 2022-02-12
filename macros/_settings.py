# MACROPAD Hotkeys example: Universal Numpad

import time
import random
from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

def color_from_time():
    epoch_time = int(time.clock_gettime_ns())
    return epoch_time % 0xffffff

def rand_color(brightness = 1.0):
    rand = random.randrange(0xffffff)
    ret = (int(float(rand) * brightness))
    print(f"random: {rand:02X}\ndimmed: {ret:02X}")
    return ret

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'settings', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (rand_color, 'F', ['F']),
        (rand_color, 'F', ['F']),
        (rand_color, 'F', ['F']),
        # 2nd row ----------
        (rand_color, 'F', ['F']),
        (rand_color, 'F', ['F']),
        (rand_color, 'F', ['F']),
        # 3rd row ----------
        (rand_color, 'f', ['f']),
        (rand_color, 'f', ['f']),
        (rand_color, 'f', ['f']),
        # 4th row ----------
        (rand_color, 'f', ['f']),
        (rand_color, 'f', ['f']),
        (rand_color, 'f', ['f']),
        # Encoder button ---
        (0x000000, '', ["f"])
    ]
}
