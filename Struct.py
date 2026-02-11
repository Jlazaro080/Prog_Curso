import struct

# Seccion: importacion del modulo struct


# Seccion: funciones para empaquetar datos
def empaquetar_persona(edad: int, altura_cm: float, inicial: str, peso: float) -> bytes:
    # Formato: entero (I), flotante (f), caracter (c), flotante (f)
    return struct.pack("I f c f", edad, altura_cm, inicial.encode("ascii"), peso)


# Seccion: funciones para desempaquetar datos
def desempaquetar_persona(datos: bytes) -> tuple[int, float, str, float]:
    edad, altura_cm, inicial_bytes, peso = struct.unpack("I f c f", datos)
    return edad, altura_cm, inicial_bytes.decode("ascii"), peso


# Seccion: funcion principal de ejemplo
def main() -> None:
    edad = 25
    altura_cm = 172.5
    inicial = "L"
    peso = 70.5
    datos = empaquetar_persona(edad, altura_cm, inicial, peso)
    print(f"Datos empaquetados: {datos}")

    edad_out, altura_out, inicial_out, peso_out = desempaquetar_persona(datos)
    print("Datos desempaquetados:")
    print(f"Edad: {edad_out}")
    print(f"Altura: {altura_out}")
    print(f"Inicial: {inicial_out}")
    print(f"Peso: {peso_out}")


# Seccion: punto de entrada del programa
if __name__ == "__main__":
    main()
