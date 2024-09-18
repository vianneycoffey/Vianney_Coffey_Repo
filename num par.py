print("DETERMINAR SI UN NUMERO ES PAR O IMPAR\n")
def par_impar():
    num = int(input("Introduce un numero: "))

    if num % 2 == 0:
        print(f"El numero {num} es par.\n")
    else:
        print(f"El numero {num} es impar.\n")


while True:
    par_impar()
    
    repetir = input("¿Quiere verificar otro numero? (Si/No): ").lower()
    
    if repetir != "si" and repetir != "si":
        print("Fin del programa.")
        break
