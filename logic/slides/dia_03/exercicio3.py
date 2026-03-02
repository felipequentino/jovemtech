import math

celsius = float(input("Temperatura em Celsius"))

# cast to Fº bc the client asked  
fahrenheit = (celsius * 1.8) + 32

kelvin = celsius + 297

print(f"{celsius}ºC -> {kelvin}ºK")

# aqui eu criei uma variavel pro cara que tem 25 anos 
idade = 25


a = 25
h = 1.65
i = a / (h ** 2)
print(f"i {i}")

idade = 25
altura = 1.65
imc_br = idade / (altura ** 2)
print(f"imc br {imc_br}")

age = 25
height = 1.65
imc = age / (height ** 2)
print(f"imc {imc}")
