import time
import board
import busio

class SIM800L:
    def __init__(self, tx_pin, rx_pin):
        self.uart = busio.UART(tx_pin, rx_pin, baudrate=9600)

    def send_at_command(self, command):
        self.uart.write(command.encode('utf-8') + b'\r\n')
        response = self.uart.readline()
        return response

    def send_sms(self, recipient, message):
        self.send_at_command('AT+CMGF=1')  # Set SMS text mode
        self.send_at_command('AT+CMGS="{}"'.format(recipient))  # Specify recipient phone number
        self.uart.write(message.encode('utf-8') + b'\x1A\r\n')  # Send the message
        response = self.uart.read(64)
        return response

    def check_sms(self):
        self.send_at_command('AT+CNMI=2,2,0,0,0')  # Set up SMS notification
        response = self.send_at_command('AT+CMGL="REC UNREAD"')  # List unread messages

        if response:
            # Parse the response to extract SMS messages
            response_lines = response.decode('utf-8').splitlines()
            messages = []

            for line in response_lines:
                if line.startswith('+CMGL:'):
                    messages.append(response_lines.index(line) + 1)

            for msg_index in messages:
                # Read the SMS
                sms_response = self.send_at_command('AT+CMGR=' + str(msg_index))
                print("Received SMS:", sms_response)

# Create an instance of the SIM800L class
tx_pin = board.GP0  # Replace with your actual TX pin
rx_pin = board.GP1  # Replace with your actual RX pin
sim800l = SIM800L(tx_pin, rx_pin)

# Power on the SIM800L module if it's not already powered on


# Send an SMS using the send_sms method
recipient_number = "+639605554877"
sms_message = "Hello from Raspberry Pi Pico!"
response = sim800l.send_sms(recipient_number, sms_message)
print("SIM800L Response (SMS):", response)

# Power off the SIM800L module when done

