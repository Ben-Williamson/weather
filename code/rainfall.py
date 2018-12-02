import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)

def measure():
	print("Measuring Rainfall for 10 seconds...")
	current_time = time.strftime("%S")

	if int(current_time) + 10 > 60:
		target = int(current_time) + 10 - 60
	else:
		target = int(current_time) + 10

	tips = 0
	volume = 0.2794

	while int(time.strftime("%S")) != target:
		if(GPIO.input(6) == 0):
			tips += 1
			time.sleep(0.5)

	volPerTen = tips*volume
	volPerMin = volPerTen*6
	volPerHour = volPerMin*60

	print(volPerHour)

	return volPerHour

