def saludar(nombre: str) -> None:
	print(f"Hola, {nombre}.")


def sumar(a: int, b: int) -> int:
	return a + b


def main() -> None:
	print("Programa base con funciones y main")
	saludar("Luis")

	resultado = sumar(3, 5)
	print(f"Resultado de la suma: {resultado}")


if __name__ == "__main__":
	main()
