import board
import busio
from adafruit_character_lcd import character_lcd_i2c as character_lcd
import digitalio

lcd_columns = 16
lcd_rows = 2
b1 = board.GP5
b2 = board.GP6
b3 = board.GP7
b4 = board.GP11
"-"=b1
"."=b2
"enter"=b3
"clear"=b4
i2c = busio.I2C(board.GP0, board.GP1)
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)



lcd.clear()
lcd.message = "Hello, World!"
lcd.cursor_position(0, 1) 
lcd.message = "CircuitPython!"

