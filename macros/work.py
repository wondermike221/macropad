# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
# import http
# import tkinter

PASTE = [Keycode.CONTROL, 'v', -Keycode.CONTROL]
BACKSPACE = [Keycode.BACKSPACE, -Keycode.BACKSPACE]
HUB_PROFILE_URL = 'https://hub.corp.ebay.com/profile/'
HUB_PROFILE_JSON = 'https://hub.corp.ebay.com/searchsvc/profile/'
FEDEX_TRACKING = 'https://www.fedex.com/fedextrack/?trknbr='

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Work', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '7', ['7']),
        (0x000000, '8', ['8']),
        (0x000000, '9', ['9']),
        # 2nd row ----------
        (0x000000, '4', ['4']),
        (0x000000, '5', ['5']),
        (0x000000, '6', ['6']),
        # 3rd row ----------
        (0x000011, 'cc', [Keycode.CONTROL, 'n', HUB_PROFILE_JSON]
            + PASTE + BACKSPACE + BACKSPACE + BACKSPACE + BACKSPACE + BACKSPACE
            + BACKSPACE + BACKSPACE + BACKSPACE + BACKSPACE + [Keycode.ENTER, .5,
            Keycode.CONTROL, 'fcostCenterCode']),
        (0x000000, '2', ['2']),
        (0x110000, 'track', [Keycode.CONTROL, 'n', FEDEX_TRACKING] + PASTE + [Keycode.ENTER]),
        # 4th row ----------
        (0x110000, 'ship', ['Shipped, Tracking # ']+PASTE),
        (0x001100, 'clip hist', [Keycode.WINDOWS, 'v']),
        (0x000011, 'chat', ['Chat log:\n']+PASTE),
        # Encoder button ---
        (0x000000, '', [""])
    ]
}
