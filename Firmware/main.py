from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

# ---- XIAO RP2040 GPIO PINS ----
# 1 row, 4 columns
keyboard.col_pins = (9, 10, 11, 12)  # Columns for your 1x4 macropad
keyboard.row_pins = (13,)            # Single row, connect to ground

keyboard.diode_orientation = keyboard.DIODE_COL2ROW

# ---- KEYMAP (1x4) ----
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D]
]

if __name__ == '__main__':
    keyboard.go()
