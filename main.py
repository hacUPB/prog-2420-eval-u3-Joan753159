productos = [
    ("Sable de luz", 2000),
    ("pistola laser", 1500),
    ("pasaje a Naboo", 3000),
    ("Aerodeslizador", 2500),
    ("X-wing", 6500)
]
print("-Bienvenido a starstore.com")
print("-Productos: sable de luz, pistola laser, pasaje a naboo, Aerodeslizador, X-wing")
print("-escribir tambien puedes 'terminar' si la busqueda finalizar quieres")

while True:
    nombre_producto = input("Ingrese el nombre del producto para consultar su precio: ")

    if nombre_producto.lower() == "terminar":
        print("Gracias por utilizar nuestro servicio, siempre bienvenido a starstore.com, que la fuerza te acompañe.")
        break

    producto_encontrado = False

    for producto in productos:
        if producto[0].lower() == nombre_producto.lower():
            print(f"El precio de {nombre_producto} es: ${producto[1]}")
            producto_encontrado = True
            break

    if not producto_encontrado:
        print("Lo sentimos, no vendemos o no encontramos lo que busca, verifique y digite de nuevo.")