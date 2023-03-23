peso = int(input("Entre o peso: "))
altura = float(input("Entre a altura"))

calc = peso / (altura*altura)

if(calc == 16):
    print("Magreza grau 3")

elif((calc >= 16) and (calc <= 16.9)):
    print("magreza grau 2")

elif((calc >= 17) and (calc <= 18.4)):
    print("magreza grau 1")

elif((calc >=18.5) and (calc <= 24.9)):
    print("Adequado")

elif((calc >= 25) and (calc <= 29.9)):
    print("pre obeso")

elif(calc > 30):
    print("obeso")