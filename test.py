import serial,time

def get_value(var):
    ret = ''
    try:
        ser = serial.Serial('COM8', 9600, timeout=1)
        var = 'deligram' + var + '\n'
        ser.write(var.encode())
        ret = ser.readline()
    except:
        ret = 'COM PORT ERROR'
    return  ret


if __name__== "__main__":
    ret = get_value("?")
    ret = ret.decode()
    ret = ret.strip()
    print(ret)