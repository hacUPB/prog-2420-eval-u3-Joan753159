# Inventario Jedi
productos = [
    {"nombre": "Sable de luz", "precio": 2000, "inventario": 100},
    {"nombre": "Pistola laser", "precio": 1500, "inventario": 80},
    {"nombre": "Pasaje a Naboo", "precio": 3000, "inventario": 1000},
    {"nombre": "Aerodeslizador", "precio": 2500, "inventario": 50},
    {"nombre": "X-wing", "precio": 6500, "inventario": 150}
]

total_compra = 0
productos_comprados = []

print("-Bienvenido a starstore.com")
print("-Productos: Sable de luz, Pistola laser, Pasaje a Naboo, Aerodeslizador, X-wing")
print("-Escribir también puedes 'terminar' si la búsqueda finalizar quieres o 'inventario' para consultar el inventario disponible.")

while True:
    nombre_producto = input("Ingrese el nombre del producto para consultar su precio o comprar: ")

    
    if nombre_producto.lower() == "terminar":
        print(f"\nGracias por utilizar nuestro servicio.")
        print(f"Valor total de la compra: ${total_compra}.")

        if productos_comprados:
            print("Has comprado:")
            for item in productos_comprados:
                print(f"- {item['cantidad']} {item['nombre']}(s) por ${item['subtotal']}")
        else:
            print("No has comprado nada.")
        
        print("Que la fuerza te acompañe.")
        break

    
    if nombre_producto.lower() == "inventario":
        print("\nInventario disponible:")
        for producto in productos:
            print(f"- {producto['nombre']}: {producto['inventario']} unidades")
        print()  
        continue

    producto_encontrado = False

    for producto in productos:
        if producto["nombre"].lower() == nombre_producto.lower():
            print(f"El precio de {nombre_producto} es: ${producto['precio']}. Inventario disponible: {producto['inventario']}")
            producto_encontrado = True

          
            cantidad = int(input(f"¿Cuántos {nombre_producto} deseas comprar?: "))

            if cantidad > producto["inventario"]:
                print(f"Lo sentimos,{producto['inventario']} unidades disponibles solo tenemos.")
            else:
                
                producto["inventario"] -= cantidad
                
                total_producto = cantidad * producto["precio"]
               
                total_compra += total_producto
             
                productos_comprados.append({
                    "nombre": producto["nombre"],
                    "cantidad": cantidad,
                    "subtotal": total_producto
                })
                print(f"{cantidad} {nombre_producto}(s) por ${total_producto} Has comprado . Inventario restante: {producto['inventario']}")
            break

   
    if not producto_encontrado:
        print("Lo sentimos, no vendemos o no encontramos lo que busca, verifique y digite de nuevo.")