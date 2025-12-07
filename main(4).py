import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [
    board.A0,
    board.A1,
    board.A2,
    board.A3,
    board.D6,
    board.D7,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
        KC.E,
        KC.F,
    ]
]

if __name__ == "__main__":
    keyboard.go()
