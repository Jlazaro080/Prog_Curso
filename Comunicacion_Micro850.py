from pymodbus.client import ModbusTcpClient

PLC_IP = "192.168.0.1"
client = ModbusTcpClient(PLC_IP, port=502)

if client.connect():
    r = client.read_coils(address=0, count=1)  # 000001 -> offset 0
    if r.isError():
        print("Error lectura:", r)
    else:
        print("ESTACION_OK =", r.bits[0])
    client.close()
else:
    print("No conecta")
