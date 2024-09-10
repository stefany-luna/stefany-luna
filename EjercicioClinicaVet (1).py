listaPerros = []
listaGatos = []
contPerros = 0
contGatos = 0

# print("Bienvenido al sistema de la clinica veterinaria UdeA\n".upper().center(90))
mjsBvda="Bienvenido al sistema de la clinica veterinaria UdeA"
print(f"{mjsBvda:>90}")
while True:
    # opcion = input("Ingrese:\n\n\r1- Ingresar nuevo paciente\n2- Ver Cantidad de pacientes\n3- Mostrar promedio de edades\n4- Cantidad de pacientes criticos y graves\n5- Ver paciente\n6- Ver todos los pacientes\n7- Salir\n ")
    menu = int(input("""Ingrese:\n
            1- Ingresar nuevo paciente
            2- Ver Cantidad de pacientes
            3- Mostrar promedio de edades
            4- Cantidad de pacientes criticos y graves
            5- Ver paciente
            6- Ver todos los pacientes
            7- Salir\n """))
    
    if menu == 1:
        mas = []
        mas.append(input("Nombre de la mascota: \n"))
        tipo = int(input("Ingrese: \n0 - Si es perro \n1- Si es gato\n"))
        if tipo == 0:
            mas.append("Perro")
        else:
            mas.append("Gato")
        mas.append(int(input("Edad de la mascota: ")))
        est = (int(input("Ingrese: \n0-Si es grave \n1-Si es critico\n")))
        if est == 0:
            mas.append("Grave")
        else:
            mas.append("Critico")
        if tipo==0: # Perro
            contPerros+=1 # esta una variable q aumetara en cada ciclo para contar los perros
            # codigo="Caninos{:03d}".format(contPerros)
            codigo = f"Caninos{contPerros:03d}"
            mas.append(codigo)
            listaPerros.append(mas)
        elif tipo==1: # Gato
            contGatos+=1
            codigo="Felinos{:03d}".format(contGatos)
            mas.append(codigo)
            listaGatos.append(mas)
        else:
            print("Ingrese el valor correcto , es 1 ó 0")
            continue

    elif menu == 2: # Cantidad de mascotas
        op=int(input("Ingrese para ver: \n1- Cantidad Perros \n2- Ver Cantidad gatos: \n3- Total animales\n "))
        if op==1:
            print("\nHay %d perros en el sistema \n" % len(listaPerros))
        elif op==2:
            print("\nHay %d gatos en el sistema \n" % len(listaGatos))
        elif op==3:
            print("\nHay %d animales en el sistema \n" % (len(listaPerros)+len(listaGatos)))
        else:
            print("Ingrese valor correcto es 0,1 o 2")
            continue

    elif menu == 3:
        # sum_ages = 0 # Acumulador
        ages = []
        for i in listaGatos:
            # sum_ages+= i[2]
            ages.append(i[2])
        for i in listaPerros:
            # sum_ages+= i[2]
            ages.append(i[2])
        # print(f"El promedio de edad es : {sum_ages/(len(listaGatos)+len(listaPerros)):.2f}")
        print(f"El promedio de edad es : {sum(ages)/len(ages):.2f}")

    elif menu == 4:
        C_graves = 0
        C_criticos = 0
        for i in listaGatos:
            if i[3] == "Grave":
                C_graves+=1
            elif i[3] == "Critico":
                C_criticos+=1
        for i in listaPerros:
            if i[3] == "Grave":
                C_graves+=1
            else:
                C_criticos+=1 

        print(f"Hay {C_graves} pacientes graves y {C_criticos} criticos en el sistema")

    elif menu == 5: # Ver un solo paciente
        cod = (input("Ingrese código del animal que desea buscar")).capitalize()
        if cod.startswith("Fe"):
            for i in listaGatos:
                if i[4] == cod:
                    print(f"Nombre: {i[0]} \nTipo : {i[1]}\n Edad: i[2]\n Estado: {i[3]}\nCodigo {i[4]}")
        elif cod.startswith("Ca"):
            for i in listaPerros:
                if i[4] == cod:
                    print(f"Nombre: {i[0]} \nTipo : {i[1]}\n Edad: i[2]\n Estado: {i[3]}\nCodigo {i[4]}")
    
    # elif menu == 6: # Ver todos los pacientes de pero ó de gatos
    #     cod = (input("Ingrese código del animal que desea buscar")).capitalize()
    #     if cod.startswith("Fe"):
    #         for i in listaGatos:
    #             print(f"Nombre: {i[0]} \nTipo : {i[1]}\n Edad: {i[2]}\n Estado: {i[3]}\nCodigo {i[4]}")
    #     elif cod.startswith("Ca"):
    #         for i in listaPerros:
    #             print(f"Nombre: {i[0]} \nTipo : {i[1]}\n Edad: {i[2]}\n Estado: {i[3]}\nCodigo {i[4]}")
    
    elif menu == 6:
        listaTotal = listaPerros+listaGatos
        for i in listaTotal:       
            print(f"Nombre: {i[0]} \nTipo : {i[1]}\n Edad: {i[2]}\n Estado: {i[3]}\nCodigo {i[4]}")

    elif menu == 7:
        fallos = 0
        while fallos < 3: 
            SubMenu = input("\n1.Aceptar 🤙\n2.Rechazar ❌ 👌\n")
            if SubMenu == 1:
                break
            elif SubMenu == 2:
                break
            else:
                fallos+=1
                print("Ingrese la opción correcta...🚫\n")
        
        if SubMenu == 1:
            break
        if SubMenu == 2 or SubMenu != 1:
            continue 
