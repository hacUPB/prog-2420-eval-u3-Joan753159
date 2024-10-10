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

    
    productos = [
        {nombre: "Sable de luz", precio: 2000, inventario: 100},
        {nombre: "Pistola laser", precio: 1500, inventario: 80},
        {nombre: "Pasaje a Naboo", precio: 3000, inventario: 1000},
        {nombre: "Aerodeslizador", precio: 2500, inventario: 50},
        {nombre: "X-wing", precio: 6500, inventario: 150}
    ]

    
    total_compra = 0
    productos_comprados = []

    
    IMPRIMIR "Bienvenido a starstore.com"
    IMPRIMIR "Productos: Sable de luz, Pistola laser, Pasaje a Naboo, Aerodeslizador, X-wing"
    IMPRIMIR "Escribir 'terminar' para finalizar o 'inventario' para consultar inventario."

    
    MIENTRAS VERDADERO HACER

        
        LEER nombre_producto

        
        SI nombre_producto ES "terminar" ENTONCES
            IMPRIMIR "Gracias por utilizar nuestro servicio"
            IMPRIMIR "Valor total de la compra: $" + total_compra

            SI productos_comprados NO ESTÁ VACÍO ENTONCES
                IMPRIMIR "Has comprado:"
                PARA CADA producto_en_lista EN productos_comprados HACER
                    IMPRIMIR "- " + producto_en_lista['cantidad'] + " " + producto_en_lista['nombre'] + "(s) por $" + producto_en_lista['subtotal']
                FIN PARA
            SINO
                IMPRIMIR "No has comprado nada."
            FIN SI

            IMPRIMIR "Que la fuerza te acompañe."
            SALIR DEL BUCLE
        FIN SI

        
        SI nombre_producto ES "inventario" ENTONCES
            IMPRIMIR "Inventario disponible:"
            PARA CADA producto EN productos HACER
                IMPRIMIR "- " + producto['nombre'] + ": " + producto['inventario'] + " unidades"
            FIN PARA
            CONTINUAR
        FIN SI

        
        producto_encontrado = FALSO

        PARA CADA producto EN productos HACER
            SI producto["nombre"] ES IGUAL A nombre_producto ENTONCES
                IMPRIMIR "El precio de " + nombre_producto + " es: $" + producto['precio'] + ". Inventario disponible: " + producto['inventario']
                producto_encontrado = VERDADERO

                
                LEER cantidad

                
                SI cantidad > producto["inventario"] ENTONCES
                    IMPRIMIR "Lo sentimos, solo tenemos " + producto["inventario"] + " unidades disponibles."
                SINO
                    
                    producto["inventario"] = producto["inventario"] - cantidad

                    
                    total_producto = cantidad * producto["precio"]

                    
                    total_compra = total_compra + total_producto

                    
                    AÑADIR A productos_comprados {nombre: producto["nombre"], cantidad: cantidad, subtotal: total_producto}

                    IMPRIMIR "Has comprado " + cantidad + " " + nombre_producto + "(s) por $" + total_producto + ". Inventario restante: " + producto["inventario"]
                FIN SI
                ROMPER
            FIN SI
        FIN PARA

        
        SI NO producto_encontrado ENTONCES
            IMPRIMIR "Lo sentimos, no encontramos el producto solicitado."
        FIN SI

    FIN MIENTRAS

FIN

```
## Documentación del proyecto
Nombre:  Joan David García Sánchez
ID:  000539535
---
