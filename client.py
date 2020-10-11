import socket 
import sys
so = socket.socket()

so.connect(('localhost',3000))
so.send(bytes("hola", "utf-8"))

received = str(so.recv(1024), "utf-8")

print("Sent")
print("Recibido: {}".format(received))
while True:
    if received != "":
        print(received)
        received = ""
    mensaje = input("ingrese su mensaje: ")
    so.send(bytes("hola2","utf-8"))
        