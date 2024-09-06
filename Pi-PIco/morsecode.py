import board
import busio
from adafruit_character_lcd import character_lcd_i2c as character_lcd
import digitalio

# Morse code dictionary
morse_code = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', 
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', 
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', 
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', 
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', 
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
}

# Initialize I2C and LCD
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.GP0, board.GP1)
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)

# Define buttons
b1 = digitalio.DigitalInOut(board.GP5)  # Dash (-)
b2 = digitalio.DigitalInOut(board.GP6)  # Dot (.)
b3 = digitalio.DigitalInOut(board.GP7)  # Enter
b4 = digitalio.DigitalInOut(board.GP11)  # Clear

# Set button directions
b1.direction = digitalio.Direction.INPUT
b2.direction = digitalio.Direction.INPUT
b3.direction = digitalio.Direction.INPUT
b4.direction = digitalio.Direction.INPUT

# Variables to hold the current morse code and the stacked letters
current_morse = ""
decoded_message = ""

# Function to handle button presses
def switch(btn):
    global current_morse, decoded_message
    if btn == b1:
        current_morse += "-"  # Add dash
    elif btn == b2:
        current_morse += "."  # Add dot
    elif btn == b3:  # Enter button
        if current_morse in morse_code:
            decoded_message += morse_code[current_morse]  # Convert Morse code to letter
            lcd.clear()
            lcd.message = decoded_message  # Display the decoded message on the top row
            lcd.cursor_position(0, 1)  # Move cursor to the bottom row
            lcd.message = current_morse  # Display the current Morse code
        current_morse = ""  # Reset Morse code after conversion
    elif btn == b4:  # Clear button
        current_morse = ""
        decoded_message = ""
        lcd.clear()  # Clear the LCD screen

# Main loop
while True:
    if b1.value:  # If dash button is pressed
        switch(b1)
    if b2.value:  # If dot button is pressed
        switch(b2)
    if b3.value:  # If enter button is pressed
        switch(b3)
    if b4.value:  # If clear button is pressed
        switch(b4)
