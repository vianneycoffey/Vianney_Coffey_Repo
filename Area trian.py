print("\nCALCULAR EL AREA DE UN TRIANGULO\n")
def calc_area():
    base = float(input("Introduce la base del triangulo: "))
    altura = float(input("Introduce la altura del triangulo: "))


    area = (base * altura) / 2


    print(f"El área del triangulo es: {area:.2f}\n")

while True:
    calc_area()
    
    repetir = input("¿Deseas calcular otro triángulo? (sí/no): ").lower()
     
    if repetir != "sí" and repetir != "si":
        print("Fin del programa.")
        break