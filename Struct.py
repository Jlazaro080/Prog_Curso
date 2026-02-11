import struct


def empaquetar_persona(edad: int, altura_cm: float, inicial: str) -> bytes:
	# Formato: entero (I), flotante (f), caracter (c)
	return struct.pack("Ifc", edad, altura_cm, inicial.encode("ascii"))


def desempaquetar_persona(datos: bytes) -> tuple[int, float, str]:
	edad, altura_cm, inicial_bytes = struct.unpack("Ifc", datos)
	return edad, altura_cm, inicial_bytes.decode("ascii")


def main() -> None:
	edad = 25
	altura_cm = 172.5
	inicial = "L"

	datos = empaquetar_persona(edad, altura_cm, inicial)
	print(f"Datos empaquetados: {datos}")

	edad_out, altura_out, inicial_out = desempaquetar_persona(datos)
	print("Datos desempaquetados:")
	print(f"Edad: {edad_out}")
	print(f"Altura: {altura_out}")
	print(f"Inicial: {inicial_out}")


if __name__ == "__main__":
	main()
