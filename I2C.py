import smbus2
import time
# for RPI version 1, use “bus = smbus.SMBus(0)”
bus = smbus2.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
   value= int(value)
   bus.write_byte(address, value)
   bus.write_byte(address, value*2)
   #bus.write_byte_data(address, 0, value)
   return -1

def readNumber():
   number = bus.read_byte(address)
   #number = bus.read_byte_data(address, 1)
   return number

while True:
   var = input("Enter 1 – 9: ")
   if not var:
      continue

   writeNumber(var)
   print ("Envio: ", var)
   # sleep one second
   time.sleep(1)

   number = readNumber()
   print ("Arduino: ", number)
   print
