# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'F', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x110000, 'F', ['F']),
        (0x110000, 'F', ['F']),
        (0x110000, 'F', ['F']),
        # 2nd row ----------
        (0x110000, 'F', ['F']),
        (0x110000, 'F', ['F']),
        (0x110000, 'F', ['F']),
        # 3rd row ----------
        (0x110000, 'f', ['f']),
        (0x110000, 'f', ['f']),
        (0x110000, 'f', ['f']),
        # 4th row ----------
        (0x110000, 'f', ['f']),
        (0x110000, 'f', ['f']),
        (0x110000, 'f', ['f']),
        # Encoder button ---
        (0x000000, '', ["f"])
    ]
}
