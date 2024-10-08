[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
# Evaluación unidad 3
## Sistema de inventario para una tienda.

#### El programa deberá guardar una lista de productos y asignarle a cada uno un precio, en caso de que uno pregunte por el precio del producto por código, indicar su precio.

Utilidad: Un inventario o catáogo de costos en una tienda es una herramienta fundamental para la gestión de ventas. Su principal utilidad es proporcionar una referencia clara y organizada de los costos asociados con los productos ofrecidos, ya sea e ciente o el vendedor quien use este programa.

### Pseudocódigo:
```
INICIO

    productos = [        ("Manzana", 2000),        ("Pera", 1500),        ("Leche", 3000),        ("Arepas", 2500),        ("Jugo", 6500)    ]

    IMPRIMIR "Ingrese el nombre del producto para consultar su precio: "
    LEER nombre_producto

    producto_encontrado = FALSO
    PARA CADA producto EN productos HACER
        SI producto[0] == nombre_producto ENTONCES
            IMPRIMIR "El precio de " + nombre_producto + " es: $" + producto[1]
            producto_encontrado = VERDADERO
            DETENER BÚSQUEDA
        FIN SI
    FIN PARA

    SI producto_encontrado == FALSO ENTONCES
        IMPRIMIR "Producto no encontrado."
    FIN SI

FIN
```
## Documentación del proyecto
Nombre:  Joan David García Sánchez
ID:  000539535
---
