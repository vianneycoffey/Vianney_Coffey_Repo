print("DETERMINAR SI PUEDES CONDUCIR\n")
def puede_conducir():
    edad = int(input("Introduce su edad: "))
    
    if edad >= 18:
        tiene_licencia = input("¿Tiene licencia de conducir? (sí/no): ").lower()

        if tiene_licencia == "sí" or tiene_licencia == "si":
            print("Puede conducir.\n")
        else:
            print("No puede conducir porque no tiene licencia.\n")
    else:
        print("No puede conducir porque es menor de 18 años.\n")
while True:
    puede_conducir()
    repetir = input("¿Deseas verificar otra persona? (Si/No): ").lower()
    
    if repetir != "si" and repetir != "si":
        print("Fin del programa.")
        break