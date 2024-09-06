import board
import busio
import digitalio
import adafruit_sdcard
import storage

spi = busio.SPI(board.GP2, MOSI=board.GP3, MISO=board.GP4)
cs = digitalio.DigitalInOut(board.GP1)
sdcard = adafruit_sdcard.SDCard(spi, cs)

vfs = storage.VfsFat(sdcard)
storage.mount(vfs, '/')

def list_sd_contents():
    try:
        sd_contents = sdcard.listdir()
        print("Contents of SD card:")
        for item in sd_contents:
            print(item)
    except Exception as e:
        print("Error:", e)


