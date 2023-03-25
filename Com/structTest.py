# written by Eric Kang

import struct

sendData = (1, 2, 3, 4)
lengthData = len(sendData)

# the number of data in tuple alpha will have to be set.
# or the other way is sending 2 different datas at the same time
# 1st length of tuple len(tuple) -- which will be one integer
# 2nd depending on the length of integer, the array will be unpacked differently

def packer(lengthData, sendData):

    lengthPacked = struct.pack(">i", lengthData)

    dataPacked = struct.pack(f">{lengthData}i", *sendData)

    return lengthPacked, dataPacked

def unpacker(received):
    length, receivedBytes = received
    length = struct.unpack(">i",length) [0]
    unpackedData = struct.unpack(f">{length}i", receivedBytes)

    return unpackedData


packed = packer(lengthData, sendData)

print(f'packed data is {packed}')

print(f'unpacked data is {unpacker(packed)}')