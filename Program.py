print("CONVERSOR DE POLEGADAS PARA PIXEL E VICE-VERSA")

esc = 0

while esc != 3:

	print("Digite qual operação deseja fazer:")
	print("1 - Converter polegada para pixel")
	print("2 - Converter pixel para polegada")
	print("3 - Para sair")
	print("")
	esc = int(input("Digite aqui: "))

	if esc == 1:
		
		v1 = float(input("Digite aqui o valor das polegadas: "))

		convert = round(v1 * 96, 1)

		print("\nO valor de " + str(v1) + " polegadas em pixels é: " + str(convert))
		print("")
	elif esc == 2:

		v1 = float(input("Digite aqui o valor dos pixels: "))

		convert = round(v1 / 96, 1)

		print("\nO valor de " + str(v1) + " pixels em polegadas é: " + str(convert))
		print("")

input("Press enter to exit...")