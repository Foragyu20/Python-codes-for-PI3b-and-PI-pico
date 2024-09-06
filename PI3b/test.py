import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
names = ["SherylynErguiza","RosalieRapisora","AifhaFernandez","DanielaNoe","MhikaellaMamaradlo","GeromeGarcia","GeraldLucena","JioloDelaCruz","DanmelSurat","ReysterFernandez"] # replace this with your list of names

reader = SimpleMFRC522()

for i, name in enumerate(names, start=1):
    print(f"Now placing tag {i} of {len(names)}...")
    reader.write(name)
    print(f"Written {name} to tag {i}.")
    time.sleep(2)
	
GPIO.cleanup()
