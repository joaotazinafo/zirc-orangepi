import OPi.GPIO as GPIO
from time import sleep

pwm_pin = 26 

GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pwm_pin, GPIO.OUT)

servo = GPIO.PWM(pwm_pin, 50)
servo.start(0)

try:
	while True:
		for dc in range (0, 101, 1):
			servo.ChangeDutyCycle(dc)
			sleep(0.1)
			print(dc)
		for dc in range (100, -1, -1):
			servo.ChangeDutyCycle(dc)
			sleep(0.1)
			print(dc)

except KeyboardInterrupt:
	print("Interrompido")
	pass
	
print("Acabou")
servo.stop()
GPIO.output(pwm_pin, 0)
GPIO.cleanup()
