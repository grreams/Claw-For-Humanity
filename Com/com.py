
import serial
import struct
import serial.tools.list_ports


# Packing part

def packer(lengthData, sendData):
    lengthPacked = struct.pack(">i", lengthData)
    dataPacked = struct.pack(f">{lengthData}i", *sendData)
    return lengthPacked, dataPacked



# Port part
# global variables for port
serialComPort = None
serialInst = None 


def showPort():
    ports = serial.tools.list_ports.comports()
    for port, desc, c in sorted(ports):
        print(f"port list: {port} // {desc}\n")
        


def __startPort__():
    print('entered startport')
    global serialComPort
    global serialInst

    serialInst = serial.Serial()
    serialComPort = str(input("input port number: COM"))
    serialInst.port = "COM" + serialComPort
    serialInst.open()
    if not serialInst.is_open:
        raise Exception(f'No such port found // selected port was {serialComPort} ')
    else:
        print(f'opened port, port state is {serialInst.is_open}')


def sender(data):
    global serialInst
    lengthData = len(data)
    packed = packer(lengthData, data)
    serialInst.write(packed)

    

# initializer
def __initialize__():

    # data to be sent
    data = (1,2,3,4)

    # connect to port
    showPort()
    __startPort__()

    # send data
    sender(data)

__initialize__()
