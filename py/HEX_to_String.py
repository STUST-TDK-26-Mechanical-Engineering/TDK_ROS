from re import S
import struct
import time
# from typing_extensions import Self
# from tkinter import Y
import serial
from multiprocessing import Process
import threading

class control():
    def __init__(self,portx,bps) -> None:
        self.portx = portx
        self.bps = bps
        self.packet = bytearray()
    def coding(self,X=0,Y=0,Z=0):
        packet = bytearray() #創一個空的陣列 類型是bytearray
        # X=0
        # Y=0
        # Z=0
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
        self.packet=packet
        return packet
    def play(self,X=0,Y=0,Z=0,s=1):    
        packet=self.coding(X,Y,Z)
        time.sleep(s)
        packet=self.coding(0,0,0)
    def online(self):
        self.ser.write(self.packet)     
    def bytes2Hex(self,argv):        #十六进制显示 方法1
        try:
            result = ''  
            hLen = len(argv)  
            for i in range(hLen):  
                hvol = argv[i]
                if hvol == 0xfe:    #遇到0xfe换行
                    result += '\r\n'
                hhex = '0x%02x,'%hvol #转为0xff,
                result += hhex
        except:
            pass
        return result
    
    def res(self):
        if __name__ == "__main__":
           
            f = open('test.txt','w') 
            while self.ser.isOpen():
                num = self.ser.inWaiting()   #查询串口接收字节数据，非阻塞
                if num:
                    line = self.ser.read(num)  
                    data=hex(line[18])[2:]+hex(line[19])[2:] 
                    data=int(data,16)
                    if(data>32767):
                        data=data-(65536)
                    print(data*(10**-3))
                    # content = self.bytes2Hex(line)
                    # f.write(content)
                    # print(content) 
                    self.online() 
                    # time.sleep(1)  
    def rum(self):
        self.ser = serial.Serial(self.portx, self.bps) 
        t = threading.Thread(target = self.res)
        t.start()
        # self.play(X=1000,s=3)
        # self.play(X=-1000,s=3)
        # self.play(Y=1000,s=3)
        # self.play(Y=-1000,s=3)
        # self.play(Z=1000,s=3)
        # self.play(Z=-1000,s=3)
             
control("COM3",115200).rum()