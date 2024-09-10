
menopausia = ""
lh=float(input("ingrese el valor de Hormona Luteinizante(LH):"))
edad=int(input("ingrese la edad del paciente:"))
sexo=int(input("ingrese el genero del paciente.1-Hombre o -2-mujer:"))
if sexo ==1:
    if edad>=18:
        if lh>=1.8 and lh<=8.6:
            print("paciente normal")
        else:
            print("resultados fuera de rango, solicitar examen complementario ")
    else:
        print("los niveles de HL son normalamente bajos en la infancia.")  
    if edad>=18:
        menopausia = input("ingresar 'si'o 'no' si a la mujer le ha llegado la meonpausia:")
        if menopausia=="no":
            if lh >=5.0 and lh<=25.0:
                print("paciente normal")
            else:
                print("resultados fuera de rango, solicitar examen complementario.")
        else:
            if lh >=14.2 and lh <= 52.3:
                print("paciente normal")
            else:
                print("resultado fuera de rango, solicitr examen complementario")
else:
    print("los niveles de Hl son normalmente bajos en la infancia.")