def calcular_total_final(monto_compra, es_vip):
    if monto_compra >= 1000:
        descuento = 0.10  
    elif monto_compra >= 500:
        descuento = 0.05  
    else:
        descuento = 0.0  
    total_con_descuento = monto_compra - (monto_compra * descuento)
    if es_vip:
        total_con_descuento -= total_con_descuento * 0.05
    return total_con_descuento
monto_compra = float(input("Ingresa el total de la compra: "))
es_vip = input("¿El cliente es VIP? (s/n): ").lower() == "s"
total_final = calcular_total_final(monto_compra, es_vip)
print(f"El total final a pagar es: ${total_final:.2f}")
