# Convertir dolares a pesos mexicanos.
dolares = input("¿Cuantos dolares tienes? ")
dolares = float(dolares)
valor_dolar = 22.72
pesos = dolares * valor_dolar
pesos = str(pesos)

print("Tienes $ " + pesos + " pesos")


# Convertir pesos mexicanos a dolares
pesos = input("¿Cuantos pesos mexicanos tienes? ")
pesos = float(pesos)
valor_dolar = 22.72
valor_peso= 1/valor_dolar
dolares = pesos * valor_peso
dolares = str(dolares)

print("Tienes $ " + dolares + " dolares")