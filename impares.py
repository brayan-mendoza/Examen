def numeroImpar(numero):
   cont=2
   non=1

   if numero <= 0: 
        print ("error, introdue un valor mayor a 0:")
     

   else:
       print("la posicion 1 es: " + str(non))


   while numero>1 and cont<=numero :
        non=non+2
        print ("la posicion "+ str(cont)+ " es: " + str(non))
        cont = cont+1

valor=int(input("Introduce la posicion"))
numeroImpar(valor)  