#Importando los módulos
import msvcrt
import platform
import os
import time
from colorama import Fore, init, just_fix_windows_console

init()
just_fix_windows_console()

aprendices = []
aprendicesresultado = []

def ingreso():
    print(Fore.LIGHTYELLOW_EX)
    print("---------------------------------------------------------------")
    print("|                                                             |")
    print("|                                                             |")
    print("|                                                             |")
    print("|              BIENVENIDO AL MENÚ DE SENA ADSO                |")
    print("|          PARA INGRESAR PRESIONE CUALQUIER TECLA             |")
    print("|                                                             |")
    print("|                                                             |")
    print("|                                                             |")
    print("---------------------------------------------------------------")
    msvcrt.getch()
    platform.system() == "Windows"
    os.system("cls")


def parametrizar(): #Definiendo la función parametrizar
    limpiar_pantalla()
    print("PARAMETRIZAR")
    print("")

    confirmacion = None
    while confirmacion != "S" and confirmacion != "N": #Preguntando si desea parametrizar
        print(Fore.WHITE, "¿Está seguro de que desea borrar toda la información registrada? (S/N): ")
        confirmacion = msvcrt.getwch()

        if confirmacion == "S":
            aprendices.clear() #Limpiando toda la lista de aprendices
            print(Fore.LIGHTYELLOW_EX, "Toda la información ha sido eliminada correctamente.")
        elif confirmacion == "N":
            print(Fore.LIGHTYELLOW_EX, "Operación cancelada.") #Cancelando la operación
        else:
            print(Fore.RED, "Carácter no válido") #Carácter no válido

    time.sleep(2)
    limpiar_pantalla()
    menu() #Regresando al menú principal
    
    
def ingresaraprendiz(): #Definiendo la función para ingresar un aprendiz
    limpiar_pantalla()
    print("INGRESAR APRENDÍZ")
    print("")
    
    nombre = input("Ingrese el nombre del aprendíz: ")
    documento = None #Definiendo documento como None
    ficha = None #Definiendo ficha como None

    while documento is None: #En caso de NO escribir un número, el programa vuelve a pedirle al usuario que lo haga
        try:
            print(Fore.LIGHTYELLOW_EX)
            documento = int(input("Ingrese el documento del aprendíz: "))
        except ValueError:
            print(Fore.RED)
            print("Caracter inválido, solo se admiten números.")

    while ficha is None: #En caso de NO escribir un número, el programa vuelve a pedirle al usuario que lo haga
        try:
            print(Fore.LIGHTYELLOW_EX)
            ficha = int(input("Ingrese la ficha a la que pertenece el aprendíz: "))
        except ValueError:
            print(Fore.RED)
            print("Caracter inválido, solo se admiten números.")

    print("Por favor ingrese el resultado del aprendiz: 1. APRUEBA 2. DESAPRUEBA")
    calificar = msvcrt.getwch()
    
    #Definiendo los resultados del aprendiz
    if calificar == "1":
        evaluacion = "APRUEBA"
    elif calificar == "2":
        evaluacion = "DESAPRUEBA" 
    else: #En caso de no escribir uno de los índices, la evaluación se define como "INDEFINIDA"
        print("Los datos no serán registrados.")
        evaluacion = "INDEFINIDO"

    aprendiz = {"Nombre": nombre, "Documento": documento, "Ficha": ficha, "Resultado": evaluacion,} #Creando el diccionario para el aprendiz agregado
    aprendices.append(aprendiz) #Agregando el aprendiz creado a la lista
    print(f"{nombre} con el documento {documento}, ficha {ficha} y resultado {evaluacion} ha sido registrado exitosamente")

    time.sleep(2)
    limpiar_pantalla()
    menu() #Regresando al menú principal

    return aprendiz #Retornando aprendiz


def listadeaprendices(): #Definiendo la función para mostrar los aprendices
    limpiar_pantalla()
    print("LISTA DE APRENDICES")
    print("")

    for aprendiz in aprendices:
        print(Fore.LIGHTYELLOW_EX, "------------------------------------------------")
        print(Fore.WHITE, "\n" .join("{}: {}".format(k, v) for k, v in aprendiz.items())) #Mostrando los aprendices que hay en la lista
        print(Fore.LIGHTYELLOW_EX, "------------------------------------------------")
    
    time.sleep(3)
    limpiar_pantalla()
    menu() #Regresando al menú principal
    
    
def listadeaprendicesficha(): #Definiendo la función para mostrar los aprendices de una ficha
    limpiar_pantalla()
    print("LISTA DE APRENDICES POR FICHA")
    print("")

    buscar = None

    while buscar is None: #En caso de NO escribir un número, el programa vuelve a pedirle al usuario que lo haga
        try:
            print(Fore.LIGHTYELLOW_EX)
            buscar = int(input("Digite la ficha que desee buscar: "))
        except ValueError:
            print(Fore.RED)
            print("Caracter inválido, solo se admiten números.")

    try:
        resultados = [aprendiz for aprendiz in aprendices if aprendiz["Ficha"] == buscar] #Buscando la ficha
        if resultados:
            for resultado in resultados:
                print(Fore.LIGHTYELLOW_EX, "------------------------------------------------")
                print(Fore.WHITE, "\n" .join("{}: {}".format(k, v) for k, v in resultado.items())) #Si la ficha se encuentra, imprime los aprendices que hay en ella
                print(Fore.LIGHTYELLOW_EX, "------------------------------------------------")
        else:
            limpiar_pantalla()
            print(Fore.LIGHTYELLOW_EX, "No se encontraron aprendices para la ficha especificada.") #Si no, devuelve un mensaje de alerta
    except UnboundLocalError:
        print("")

    time.sleep(2)
    limpiar_pantalla()
    menu() #Regresando al menú principal
    

def resultadodeaprendiz(): #Definiendo la función para mostrar el resultado de los aprendices
    limpiar_pantalla()
    print("RESULTADO DE APRENDICES POR FICHA")
    print("")

    buscar = None

    while buscar is None: #En caso de NO escribir un número, el programa vuelve a pedirle al usuario que lo haga
        try:
            print(Fore.LIGHTYELLOW_EX)
            buscar = int(input("Digite la ficha que desee buscar: ")) #Buscando la ficha
        except ValueError:
            print(Fore.RED)
            print("Caracter inválido, solo se admiten números.")

    try:
        resultados1 = [aprendiz for aprendiz in aprendices if aprendiz["Ficha"] == buscar and aprendiz["Resultado"] == "APRUEBA"]
        resultados2 = [aprendiz for aprendiz in aprendices if aprendiz["Ficha"] == buscar and aprendiz["Resultado"] == "DESAPRUEBA"]

        if resultados1: #Si la ficha se encuentra, imprime los aprendices que hay en ella (En este caso los que aprobaron)
            print(Fore.WHITE, "\nAprendices que APRUEBAN:\n")
            for resultado in resultados1:
                print(Fore.LIGHTYELLOW_EX, "------------------------------------------------")
                print(Fore.GREEN, "\n" .join("{}: {}".format(k, v) for k, v in resultado.items()))
                print(Fore.LIGHTYELLOW_EX, "------------------------------------------------")
                    
        if resultados2: #Si la ficha se encuentra, imprime los aprendices que hay en ella (En este caso los que desaprobaron)
            print(Fore.WHITE, "\nAprendices que DESAPRUEBAN:\n")
            for resultadox in resultados2:
                print(Fore.LIGHTYELLOW_EX, "------------------------------------------------")
                print(Fore.RED, "\n" .join("{}: {}".format(k, v) for k, v in resultadox.items()))
                print(Fore.LIGHTYELLOW_EX, "------------------------------------------------")
                
        else:
            print(Fore.LIGHTYELLOW_EX, "No se encontraron aprendices para la ficha especificada.") #Si no, devuelve un mensaje de alerta
    except UnboundLocalError:
        print("")
        
    time.sleep(4)
    limpiar_pantalla()
    menu() #Regresando al menú principal
    
    
def borraraprendiz(): #Definiendo la función para borrar un aprendiz
    limpiar_pantalla()
    print("BORRAR APRENDÍZ")
    print("")

    documento = None
    while documento is None: #En caso de NO escribir un número, el programa vuelve a pedirle al usuario que lo haga
        try:
            print(Fore.LIGHTYELLOW_EX)
            documento = int(input("Ingrese el número de documento del aprendiz que desee borrar: ")) #Pidiendo el número de documento
        except:
            print(Fore.RED)
            print("Caracter inválido, solo se admiten números.")

    try:
        aprendiz_encontrado = False
        for aprendiz in aprendices:
            if aprendiz["Documento"] == documento: #Buscando el documento del aprendiz
                aprendiz_encontrado = True
                limpiar_pantalla()
                aprendices.remove(aprendiz) #Si lo encuentra, se borra de la lista
                print(Fore.LIGHTYELLOW_EX, "Aprendiz eliminado correctamente.")

        if not aprendiz_encontrado:
            limpiar_pantalla()
            print(Fore.LIGHTYELLOW_EX, "El aprendiz no está registrado.") #Si no, devuelve un mensaje de alerta
    except UnboundLocalError:
        print("")

    time.sleep(2)
    limpiar_pantalla()
    menu() #Regresando al menú principal
    
    
def actualizarinformacion(): #Definiendo la función para actualizar información
    limpiar_pantalla()
    print("ACTUALIZAR INFORMACIÓN")
    print("")

    documento = None
    while documento is None: #En caso de NO escribir un número, el programa vuelve a pedirle al usuario que lo haga
        try:
            print(Fore.LIGHTYELLOW_EX)
            documento = int(input("Ingrese el documento del aprendiz para actualizar su información: ")) #Pidiendo el número de documento
        except ValueError:
            print(Fore.RED)
            print("Caracter inválido, solo se admiten números.")

    aprendiz_encontrado = False
    for aprendiz in aprendices:
        if aprendiz["Documento"] == documento: #Buscando el documento del aprendiz
            aprendiz_encontrado = True
            limpiar_pantalla()
            print(Fore.WHITE, "Aprendiz encontrado. Ingrese la nueva información:") #Registrando la nueva información
            print("")
            nombre = input(f"Ingrese el nuevo nombre para {aprendiz['Nombre']}: ")

            documento_nuevo = None
            while documento_nuevo is None: #En caso de NO escribir un número, el programa vuelve a pedirle al usuario que lo haga
                try:
                    print(Fore.LIGHTYELLOW_EX)
                    documento_nuevo = int(input(f"Ingrese el nuevo documento para {aprendiz['Documento']}: "))
                except ValueError:
                    print(Fore.RED)
                    print("Caracter inválido, solo se admiten números.")

            ficha_nueva = None
            while ficha_nueva is None: #En caso de NO escribir un número, el programa vuelve a pedirle al usuario que lo haga
                try:
                    print(Fore.LIGHTYELLOW_EX)
                    ficha_nueva = int(input(f"Ingrese la nueva ficha para {aprendiz['Ficha']}: "))
                except ValueError:
                    print(Fore.RED)
                    print("Caracter inválido, solo se admiten números.")

            #Agregando los nuevos datos al diccionario
                aprendiz["Nombre"] = nombre 
                aprendiz["Documento"] = documento_nuevo
                aprendiz["Ficha"] = ficha_nueva

            print("Por favor ingrese el nuevo resultado del aprendiz: 1. APRUEBA 2. DESAPRUEBA")
            calificar_nuevo = msvcrt.getwch()
    
            #Definiendo los resultados del aprendiz
            if calificar_nuevo == "1":
                evaluacion_nuevo = "APRUEBA"
            elif calificar_nuevo == "2":
                evaluacion_nuevo = "DESAPRUEBA" 
            else:
                print("Los datos no serán registrados.")
                evaluacion_nuevo = "INDEFINIDO"

            aprendiz["Resultado"] = evaluacion_nuevo

            print("")
            print(Fore.WHITE, f"{nombre} con el documento {documento_nuevo}, ficha {ficha_nueva} y resultado {evaluacion_nuevo} ha sido registrado exitosamente")

    if not aprendiz_encontrado:
        limpiar_pantalla()
        print(Fore.LIGHTYELLOW_EX, "El aprendiz no está registrado.") #Si no, devuelve un mensaje de alerta

    time.sleep(2)
    limpiar_pantalla()
    menu() #Regresando al menú principal
    
    
def chao():
    limpiar_pantalla()
    print("Hasta pronto...") #Se cierra el programa


def limpiar_pantalla(): #Definiendo la función para limpiar pantalla
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def menu(): #Definiendo la función de menú
    print(Fore.LIGHTYELLOW_EX)
    print("MENÚ \n")
    print("1. PARAMETRIZAR")
    print("2. INGRESAR APRENDÍZ")
    print("3. LISTA DE APRENDICES")
    print("4. LISTA DE APRENDICES POR FICHA")
    print("5. RESULTADO DE APRENDICES POR FICHA")
    print("6. BORRAR APRENDÍZ")
    print("7. ACTUALIZAR INFORMACIÓN")
    print("0. SALIR \n")

    resp = None #El usuario solo puede responder del 1 al 7
    while resp != "1" and resp != "2" and resp != "3" and resp != "4" and resp != "5" and resp != "6" and resp != "7" and resp != "0":
        
        print("Digite el número para ingresar a una sección: ")
        resp = msvcrt.getwch()
    
    
        if resp == "1":
            parametrizar()
            
        elif resp == "2":
            ingresaraprendiz()
        
        elif resp == "3":
            listadeaprendices()
            
        elif resp == "4":
            listadeaprendicesficha()
            
        elif resp == "5":
            resultadodeaprendiz()
            
        elif resp == "6":
            borraraprendiz()
            
        elif resp == "7":
            actualizarinformacion()
            
        elif resp == "0": 
            chao()
                
if __name__ == "__main__":           
    ingreso()
    menu()