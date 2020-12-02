import serial
import time
import matplotlib.pyplot as plt

# print("Ingresa el numero de puerto COM")
# while True:
#     numPort = input()
#     if numPort.isdigit() == True: 
#         devPort = "COM"+numPort
#         print("El puerto seleccionado es: "+devPort)
#         break
#     else:
#         print("Ingresa un numero no letra")
# print("Ingresa el baudrate")
# while True:
#     rate = input()
#     if rate.isdigit() == True: 
#         print("El baudrate seleccionado es: "+rate)
#         break
#     else:
#         print("Ingresa un numero no letra")
# device = serial.Serial(port=devPort,baudrate=rate)
# print("Connected to: "+device.portstr)

# while True:
#     data = str(device.readline())
#     print(data)
#     if "@" in data:
#         print("Termina sesión")
#         time.sleep(5)
#         device.close()
#         break

starTime = time.time()
print("Start time: "+ str(starTime))
while True:
    if time.time() > starTime+10:
        print("End script: "+ str(time.time()))
        break
