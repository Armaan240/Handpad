print("Starting Macropad")
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes


# Keys
keyboard = KMKKeyboard()

PINS = [board.D7, board.D8, board.D9, board.D10]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D0, board.D1, None), 
)

encoder_handler.map = [
    ((KC.LCTL(KC.EQUAL), KC.LCTL(KC.MINUS)),),
]

rgb = RGB(
    pixel_pin=board.D6,  
    num_pixels=6,
    val_limit=100,
    hue_default=150,
    sat_default=200,
    rgb_order=(1, 0, 2),  # GRB WS2812
    val_default=100,
    hue_step=5,
    sat_step=5,                                      
    val_step=5,
    animation_speed=2,
    breathe_center=2,  # 1.0-2.7
    knight_effect_length=3,
    animation_mode=AnimationModes.STATIC,
    reverse_animation=False,
    refresh_rate=60,)

keyboard.extensions.append(rgb)
# Keymap
keyboard.keymap = [
    [KC.A, KC.W, KC.S , KC.RGB_MODE_RAINBOW]
]

# Start everything
if __name__ == '__main__':
    print("Keyboard starting...")
    keyboard.go()
