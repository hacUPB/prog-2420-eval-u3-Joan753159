productos = [
    ("Manzana", 2000),
    ("Pera", 1500),
    ("Leche", 3000),
    ("Arepas", 2500),
    ("Jugo", 6500)
]
print ("Productos: Manzana, Pera, Leche, Arepas, Jugo")

nombre_producto = input("Ingrese el nombre del producto para consultar su precio: ")

producto_encontrado = False

for producto in productos:
    if producto[0].lower() == nombre_producto.lower():
        print(f"El precio de {nombre_producto} es: ${producto[1]}")
        producto_encontrado = True
        break

if not producto_encontrado:
    print("Lo sentimos, no vendemos o no encontramos lo que busca, verifique y digite denuevo.")
nombre_producto = input("Ingrese el nombre del producto para consultar su precio: ")

producto_encontrado = False

for producto in productos:
    if producto[0].lower() == nombre_producto.lower():
        print(f"El precio de {nombre_producto} es: ${producto[1]}")
        producto_encontrado = True
        break

if not producto_encontrado:
    print("Lo sentimos, no vendemos o no encontramos lo que busca, verifique y digite denuevo.")