#Programa Tienda PetMarket

def validar_codigo(codigo, productos):
    if not codigo or codigo.strip() == "":
        return False
    cod_buscar = codigo.upper().strip()
    for cod in productos.keys():
        if cod.upper() == cod_buscar:
            return False
    return True  

def validar_nombre(nombre):
    if not nombre or nombre.strip() == "":
        return False
    return True

def validar_categoria(categoria):
    if not categoria or categoria.strip() == "":
        return False
    return True

def validar_marca(marca):
    if not marca or marca.strip() == "":
        return False
    return True

def validar_peso(peso_op):
    try:
        peso = float(peso_op)
        if peso > 0:
            return True
        return False
    except ValueError:
        return False

def validar_es_importado(opcion_op):
    opc = opcion_op.lower().strip()
    return opc == 's' or opc == 'n'

def validar_es_para_cachorro(opcion_op):
    opc = opcion_op.lower().strip()
    return opc == 's' or opc == 'n'

def validar_precio(precio_op):
    try:
        precio = int(precio_op)
        if precio >= 0:
            return True
        return False
    except ValueError:
        return False

def validar_unidades(unidades_op):
    try:
        unidades = int(unidades_op)
        if unidades >= 0:
            return True
        return False
    except ValueError:
        return False

def leer_opcion():
    try:
        opcion_op = input("Ingrese la opcion que desea realizar: ")
        opcion = int(opcion_op)
        if 1 <= opcion <= 6:  
            return opcion
        return -1
    except ValueError:
        return -1

def unidades_categoria(categoria, productos, stock):
    total = 0
    cat_buscar = categoria.lower().strip()
    for cod, datos in productos.items():
        if datos[1].lower().strip() == cat_buscar:
            if cod in stock:
                total += stock[cod][1]
    print(f"El total de unidades corresponde a: {total}")

def busqueda_precios(p_min, p_max, productos, stock):
    resultados = []
    for cod, datos_stock in stock.items():
        precio = datos_stock[0]
        unidades = datos_stock[1]
        if p_min <= precio <= p_max and unidades > 0:
            if cod in productos:
                nombre = productos[cod][0]
                resultados.append(f"{nombre}-{cod}")
    if len(resultados) == 0:
        print("No existen productos entre esos rangos de precio")
    else:
        resultados.sort()
        print(f"Los productos que se han encontrado son: {resultados}")

def buscar_codigo(codigo, stock):
    cod_buscar = codigo.upper().strip()
    for cod in stock.keys():
        if cod.upper() == cod_buscar:
            return True
    return False  

def actualizar_precio(codigo, nuevo_precio, stock):
    if buscar_codigo(codigo, stock):
        cod_buscar = codigo.upper().strip()
        for cod in stock.keys():
            if cod.upper() == cod_buscar:
                stock[cod][0] = nuevo_precio  
                return True
    return False

def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades, productos, stock):
    if not validar_codigo(codigo, productos):
        return False
    cod_final = codigo.upper().strip()
    bool_importado = True if es_importado.lower().strip() == 's' else False
    bool_cachorro = True if es_para_cachorro.lower().strip() == 's' else False
    productos[cod_final] = [
        nombre.strip(),
        categoria.strip(),
        marca.strip(),
        float(peso_kg),
        bool_importado,
        bool_cachorro,
    ]
    stock[cod_final] = [
        int(precio),
        int(unidades)
    ]
    return True

def eliminar_producto(codigo, productos, stock):
    if buscar_codigo(codigo, stock):
        cod_buscar = codigo.upper().strip()
        key_to_del = None
        for cod in stock.keys():
            if cod.upper() == cod_buscar:
                key_to_del = cod
                break
        if key_to_del:
            del productos[key_to_del]
            del stock[key_to_del]
            return True
    return False

def programa_petmarket():
    productos = {
     'M001': ['Alimento Premium', 'comida', 'DogPlus', 10.0, True, False],
     'M002': ['Arena aglomerante', 'higiene', 'CatClean', 8.0, False, False],
     'M003': ['Snack Dental', 'snack', 'BiteJoy', 1.0, True, True],
     'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
     'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
     'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2.0, False, False],
     'M007': ['Collar Perro', 'accesorio', 'NeckCute', 0.3, True, True],
     'M008': ['Collar Gato', 'accesorio', 'NekoKat', 0.1, False, False],
     'M009': ['Alimento Hepatico', 'comida', 'HepaSany', 25.0, True, False],
     'M010': ['Raton de cordel', 'juguete', 'MouseCatch', 0.4, False, True],
     'M011': ['Pelota con Sonido', 'juguete', 'BallMusic', 0.2, True, True],
     'M012': ['Peine mascota', 'accesorio', 'HairCare', 0.2, True, True],
     'M013': ['Colonia para perros o gatos', 'higiene', 'PerfumEDPMascota', 1.0, True, True],
     'M014': ['Alimento Conejo', 'comida', 'RabbitFood', 25.0, True, True],
     'M015': ['Alimento Aves', 'comida', 'CanaryFOOD', 10.0, False, False],
     'M016': ['Alimento Humedo Perros', 'comida', 'FoodiePLUS', 0.5, True, True],
     'M017': ['Galletas Vegetarianas', 'snack', 'NotMeat', 0.5, True, True],
     'M018': ['Toalla mascotas', 'higiene', 'TowelFresh', 0.3, False, True],
     'M019': ['Shampoo y Acondicionador 2 en 1', 'higiene', 'OnlyPet', 1.0, True, True],
     'M020': ['Bolsito para Mascota', 'accesorio', 'TravelPack', 0.2, True, True]   
    }
    stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
    'M007': [6990, 30],
    'M008': [6990, 30],
    'M009': [59990, 12],
    'M010': [4990, 3],
    'M011': [4990, 12],
    'M012': [5990, 23],
    'M013': [12990, 12],
    'M014': [9990, 3],
    'M015': [12990, 6],
    'M016': [5990, 32],
    'M017': [3990, 2],
    'M018': [9990, 1],
    'M019': [9990, 11],
    'M020': [11990, 2]
    }
    while True:
        print("////----MENÚ PRINCIPAL PETMARKET----////")
        print("Seleccione la opción que desea realizar:")
        print("1. Unidades por categoria")
        print("2. Búsqueda de productos por rango de precio")
        print("3. Actualizar precio de un producto")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Salir del programa")
        opcion = leer_opcion()
        
        if opcion == 1:
            categoria = input("Ingrese la categoria que desea buscar: ")
            unidades_categoria(categoria, productos, stock)
        elif opcion == 2:
            while True:
                try:
                    p_min_op = input("Ingrese el precio mínimo que desea filtrar: ")
                    p_max_op = input("Ingrese el precio máximo que desea filtrar: ")
                    p_min = int(p_min_op)
                    p_max = int(p_max_op)
                    if p_min >= 0 and p_max >= 0 and p_min < p_max:
                        busqueda_precios(p_min, p_max, productos, stock)
                        break
                except ValueError:
                    print("Error, debe ingresar valores enteros")
        elif opcion == 3:
            while True:
                codigo = input("Ingrese el codigo del producto: ")
                nuevo_precio_op = input("Ingrese el nuevo precio del producto: ")
                try:
                    nuevo_precio = int(nuevo_precio_op)
                    if nuevo_precio > 0:
                        if actualizar_precio(codigo, nuevo_precio, stock):
                            print("Precio actualizado")
                        else:
                            print("El codigo no existe")
                    else:
                        print("El precio debe ser un numero entero mayor que 0")
                except ValueError:
                    print("Debe ingresar un valor entero para el precio del producto")
                resp = input("Desea actualizar otro precio (s/n)?: ").lower().strip()
                if resp == 'n':
                    break
        elif opcion == 4:
            codigo = input("Ingrese el codigo del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoria del producto: ")
            marca = input("Ingrese la marca del producto: ")
            peso_kg = input("Ingrese el peso (en kg) del producto: ")
            es_importado = input("Ingrese si el producto es importado o no (s/n): ")
            es_para_cachorro = input("Ingrese si el producto es apto para cachorros o no (s/n): ")
            precio = input("Ingrese el precio del producto: ")
            unidades = input("Ingrese las unidades disponibles del producto: ")
            
            if not validar_codigo(codigo, productos):
                print("Error en validacion de codigo")
            elif not validar_nombre(nombre):
                print("Error en validacion del nombre")
            elif not validar_categoria(categoria):
                print("Error en validar la categoria")
            elif not validar_marca(marca):
                print("Error en validar la marca del producto")
            elif not validar_peso(peso_kg):
                print("Error en la validacion del peso del producto")
            elif not validar_es_importado(es_importado):
                print("Error en validar si el producto es importado o no")
            elif not validar_es_para_cachorro(es_para_cachorro):  
                print("Error en validar si el producto es para cachorros o no")
            elif not validar_precio(precio):
                print("Error en validar el precio del producto")
            elif not validar_unidades(unidades):
                print("Error en validar las unidades del producto")
            else:
                if agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades, productos, stock):
                    print("Producto agregado")
                else:
                    print("El codigo ya existe")
        elif opcion == 5:
            codigo = input("Ingrese el codigo del producto que desea eliminar: ")
            if eliminar_producto(codigo, productos, stock):
                print("Producto eliminado con exito")
            else:
                print("No se ha encontrado el producto a eliminar")
        elif opcion == 6:
            print("Programa finalizado")
            break
        else:
            print("Ingrese una opcion valida")


programa_petmarket()