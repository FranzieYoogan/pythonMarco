horas_trab = int(input("Entre o valor de horas trabalhadas: "))

horas_extras = int(input("Entre p valor de horas extras: "))
horas_trab_bruto = horas_trab * 10 + (horas_extras * 22)
valor_liq = (horas_trab_bruto - horas_trab_bruto * 0.18)  

print("o salario bruto descontando 18porcento e: ",valor_liq)