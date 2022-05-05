import struct
import time
# from tkinter import Y
import serial
from multiprocessing import Process
class control:
    def __init__(self,portx,bps) -> None:
        # self.portx = portx
        # self.bps = bps
        self.ser = serial.Serial(portx, bps) 
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
        return packet
    def play(self,X=0,Y=0,Z=0,s=500):    
        packet=self.coding(X,Y,Z)
        self.ser.write(packet)  
        time.sleep(s)
        packet=self.coding(0,0,0)
        self.ser.write(packet)
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
        f = open('test.txt','w') 
        while self.ser.isOpen():
            num = self.ser.inWaiting()   #查询串口接收字节数据，非阻塞
            if num:
                line = self.ser.read(num)
                content = self.bytes2Hex(line)
                f.write(content)
                print(content)    

if __name__ == '__main__':
    bot=control("COM3",115200)      
    # bot.play(X=1000,s=5)  
    # # bot.play(X=-500,s=10) 
    # bot.play(Y=-1000,s=2) 
    # bot.res() 
    p=Process(target=bot.res)
    p.start()
    p.join()