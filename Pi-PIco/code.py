import board
import busio
from time import sleep
import displayio
from adafruit_st7735r import ST7735R
'''
import sdos
from sim800l import SIM800L
'''
displayio.release_displays()
'''
tx = board.GP3
rx = board.GP4
'''
tft_SCL = board.GP10
tft_SDA = board.GP11
tft_RES = board.GP13
tft_DC = board.GP14
tft_CS = board.GP15

tft_width = 160
tft_height = 80

tft_spi = busio.SPI(clock=tft_SCL, MOSI=tft_SDA)
display_bus = displayio.FourWire(tft_spi, command=tft_DC, chip_select=tft_CS, reset=tft_RES)
display = ST7735R(display_bus,
                  width=tft_width, height=tft_height,
                  rotation=270,
                  colstart=26, rowstart=1,
                  invert=True)

bitmap_list = [displayio.OnDiskBitmap(f'/{i}.bmp') for i in range(8)]

group = displayio.Group()
display.show(group)
'''
recipient_number = "+**********"
sms_message = "Hello from Raspberry Pi Pico!"
response = SIM800L(tx, rx).send_sms(recipient_number, sms_message)
print("SIM800L Response (SMS):", response)
sdos.list_sd_contents()
'''
while True:
    for bitmap in bitmap_list:
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
        group.append(tile_grid)
        sleep(0.05)
        group.pop()
