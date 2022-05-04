import struct
# from tkinter import Y
import serial
portx = "COM3"
bps = 115200
ser = serial.Serial(portx, bps) 
packet = bytearray() #創一個空的陣列 類型是bytearray
X=0
Y=0
Z=0
X2=X//256
X1=X%256

Y2=Y//256
Y1=Y%256

Z2=Z//256
Z1=Z%256

if(X2<0):
    X2=X2+256

if(Y2<0):
    Y2=Y2+256

if(Z2<0):
    Z2=Z2+256  

print(X2,X1,Y2,Y1,Z2,Z1)  
XOR_END=0x7B^0xAA^0xAA^X2^X1^Y2^Y1^Z2^Z1
# XOR_END=0x7B^0xFF^0xFF
packet.append(0x7B)  
packet.append(0xAA)  
packet.append(0xAA)  
packet.append(X2)  
packet.append(X1)  
packet.append(Y2)  
packet.append(Y1)
packet.append(Z2)
packet.append(Z1)  
packet.append(XOR_END)  
packet.append(0x7D)  
print(packet)
ser.write(packet)  