pao_qtd = int(input('digite a quantidade de paes: '))
pao_valor = pao_qtd * 1.10
broa_qtd = int(input("digite a qtd de paes: "))
broa_valor = broa_qtd * 2.50

valor_arre = pao_valor + broa_valor
valor_porc = (valor_arre * 0.1) 

print("valor arrecadado: ", valor_arre)
print("valor na poupanca: ",valor_porc)