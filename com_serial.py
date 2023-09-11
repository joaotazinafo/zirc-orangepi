import serial
import serial.tools.list_ports
 
# Função para encontrar a porta serial do Arduino automaticamente
def encontrar_porta_arduino():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        print (port)
        if "USB Serial" in port.description:
            return port.device
    return None
 
# Encontra a porta serial do Arduino
porta_arduino = encontrar_porta_arduino()
 
if porta_arduino:
    try:
        # Abre a porta serial
        serial_port = serial.Serial(porta_arduino, 9600, timeout=1)
 
        while True:
            comando = input()
            if serial_port.isOpen():
                message = comando + "\n"
                serial_port.write(message.encode())
                
            else:
                print ("cannot open serial port ")
 
            
    except KeyboardInterrupt:
        print("\nPrograma encerrado.")
        serial_port.close()
else:
    print("Arduino não encontrado. Verifique a conexão e reinicie o programa.")
