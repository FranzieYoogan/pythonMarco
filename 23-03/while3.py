soma = 0
x=0
while x<= 5:
    y = int(input("valor: "))
    if(y%2 ==0):
        print(y,"par")
        
        x+=1
      
    else:
        print(y,"impar")
        soma = soma + y

        x+=1
print(soma)