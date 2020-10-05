import serial

port ="COM6"

conn = serial.Serial(port, 115200)

msg = input("Tapez pour envoyer au MicroBit ")

conn.write(msg.encode())
