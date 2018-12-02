import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)

def measure():
	print("Measuring Wind Speed for 10 Seconds...")
	current_time = time.strftime("%S")

	if int(current_time) + 10 > 60:
		target = int(current_time) + 10 - 60
	else:
		target = int(current_time) + 10

	rotations = 0
	distance = 0.0004398
	hour = 0.00277777777

	while int(time.strftime("%S")) != target:
		if(GPIO.input(5) == 1):
			rotations += 1
			time.sleep(0.1)

		#print(time.strftime("%S"), target)

	rotations = rotations / 2
	distance = 43.98*rotations

	return(round(distance/10 /100, 2))
