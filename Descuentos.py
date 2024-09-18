print("PROGRAMA QUE CALCULE DESCUENTOS DE COMPRA\n")

def calcular_total_final():
    monto_compra = float(input("Introduce el monto total de la compra: $"))
    
    es_vip = input("¿Es miembro VIP? (Si/No): ").lower()
     
    descuento_monto = 0.00
    descuento_vip = 0.00
    
    if monto_compra >= 1000:
        descuento_monto = monto_compra * 0.10  
    elif monto_compra >= 500:
        descuento_monto = monto_compra * 0.05  
    
    monto_con_descuento = monto_compra - descuento_monto
    

    if es_vip == "si" or es_vip == "si":
        descuento_vip = monto_con_descuento * 0.05  
        monto_final = monto_con_descuento - descuento_vip
    else:
        monto_final = monto_con_descuento
    
    print(f"\nEl total a pagar es: ${monto_final:.2f}")

    print("\nDesglose de descuentos:")
    print(f"Monto inicial: ${monto_compra:.2f}")
    
    if descuento_monto > 0:
        print(f"Descuento por monto de compra: ${descuento_monto:.2f}")
        print(f"Total después del descuento por monto: ${monto_con_descuento:.2f}")
    
    if descuento_vip > 0:
        print(f"Descuento adicional para miembros VIP: ${descuento_vip:.2f}")
    
    print(f"Total final a pagar: ${monto_final:.2f}")


while True:
    calcular_total_final()
    
    repetir = input("\n¿Desea calcular el total para otra compra? (Si/No): ").lower()
    
    if repetir != "si" and repetir != "si":
        print("Fin del programa.")
        break
