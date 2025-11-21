import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.digital import DigitalScanner
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB
from kmk.modules.display import Display
from kmk.extensions.display.ssd1306 import SSD1306
keyboard = KMKKeyboard()

keyboard.matrix = DigitalScanner(
    pins=[board.GP4, board.GP2, board.GP1, board.GP0], 
    pull=True
)
enc = EncoderHandler()
enc.pins = [
    (board.GP26, board.GP27, None)
]
enc.map = [
    ((KC.VOLU,), (KC.VOLD,)),
]
keyboard.modules.append(enc)
rgb = RGB(
    pixel_pin=board.GP28,  
    num_pixels=6,          
    val_limit=50           
)
keyboard.modules.append(rgb)
oled = Display(
    driver=SSD1306(
        width=128,
        height=64,
        i2c=board.I2C(),  
        addr=0x3C
    )
)
keyboard.modules.append(oled)
keyboard.keymap = [
    [
        KC.A, 
        KC.W,  
        KC.S, 
        KC.D,  
    ]
]
if __name__ == '__main__':
    keyboard.go()
