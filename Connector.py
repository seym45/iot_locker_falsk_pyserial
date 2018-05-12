import serial

import time
current_milli_time = lambda: int(round(time.time() * 1000))

class Connector:
    connected = False
    port = ""
    baudrate = ""
    timeout = 1000 # milisec
    ser = serial.Serial()
    
    def __init__(self, port, baudrate=9600, timeout=1000):
        self.port=port
        self.baudrate=baudrate
        self.timeout = timeout
    
    def connect(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate)
            self.connected = True
        except:
            print ("Failed to connect on ",self.port)
    
    def sendandread(self, data):
        
        if not self.connected:
            self.connect()
        try:
            self.ser.write(data.encode())
            outdata = ""

            past = current_milli_time()
            while True:
                if self.ser.inWaiting():
                    x = self.ser.readline()
                    outdata += x.decode()
                if (past - current_milli_time) > self.timeout:
                    break
            return outdata
        except:
            self.connected = False

        