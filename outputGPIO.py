import OPi.GPIO as GPIO
import time
# Define o número do pino que você deseja controlar
pin_number = 26  # Substitua pelo número do pino que você deseja usar
# Configuração inicial dos pinos
GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)  # Define o modo de numeração dos pinos
# Define o pino como saída
GPIO.setup(pin_number, GPIO.OUT)
	
while True:	
		# Faça alguma ação aqui enquanto o pino está ligado
		GPIO.output(pin_number, GPIO.HIGH)
		print("Pino ligado")
		time.sleep(1)
		GPIO.output(pin_number, GPIO.LOW)
		print("Pino desligado")
		time.sleep(1)
 
print("Programa encerrado")
