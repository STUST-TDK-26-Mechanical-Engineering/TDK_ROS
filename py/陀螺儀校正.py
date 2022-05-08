from JY61 import JY61
from pid import pid_rum
import serial
import time

if __name__=='__main__': 
    port="COM10"
    baud=9600
    ser = serial.Serial(port, baud, timeout=0.5)  # ser = serial.Serial('com7',115200, timeout=0.5) 
    print(ser.is_open)
    Jy61=JY61()
    pid=pid_rum(P=1)
    pid.SetPoint = 100
    while(1):
        datahex = ser.read(33)
        Jy61.DueData(datahex) 
        z=Jy61.Angle[2]+pid.SetPoint
            # map()
        pid.update(z)    
        print(pid.output,"\t\t",z)  
            
