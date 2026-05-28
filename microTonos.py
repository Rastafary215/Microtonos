import winsound #libreria que permite activar sonidos
import time
print("Simulador de microtonos")
max_micro = 25
micro_libres = 25
micro_activos = 0
ejecutando = True
while ejecutando:
    print("\n== Panel de microtonos ===")
    print("1.- Ver cuanos microtonos quedan libres")
    print("2.- Activar microtonos (Activación de sonidos)")
    print("3.- Recuperar microtonos")
    print("4.- Monitorear el sonido actual")
    print("5.- Salir")
    opcion = int(input("Elije 1 opción(1-5): "))
    if opcion == 1:
        print(f"\n[INFO] Tienes {micro_libres} microtonos disponibles para usar")
    elif opcion == 2:
        print(f"\n ACTIVAR MICROTONOS (Disponibles: {micro_libres})")
        if micro_libres == 0:
            print("Ya no se pueden emitir más microtonos, sonidos al límite")
        else:
            try:
                cantidad = int(input("¿Cuántos microtonos quieres activar?:"))
                if cantidad <= 0:
                    print("tienes que activar al menos 1 microtono")
                elif cantidad > micro_libres:
                    print(f"Solo puedes activar hasta {micro_libres} microtonos")
                else:
                    micro_libres -= cantidad
                    micro_activos += cantidad
                    print("Reproduciendo microtonos")
                    #for i in range (1,cantidad +1):
                    #    print(f"Microtono {i} activado...")
                    #    winsound.Beep(440,300) # 440 Hz por 300 milesimas de segundo
                    #    time.sleep(0.05)
                    frecuencias = [440,440,440,587,880,784,740,659,1174,880,784,740,659,1174,880,784,740,784,659,523,587]
                    duraciones = [250,250,250,600,600,180,180,180,600,300,180,180,180,600,300,180,180,180,500,250,800]
                    for i in range(1, cantidad +1):
                        nota_actual = frecuencias[(i-1) % len(frecuencias)]
                        duracion_actual = duraciones[(i -1) % len(duraciones)]
                        winsound.Beep(nota_actual,duracion_actual)
                        time.sleep(0.04)
            except ValueError:
                print("Error")
    elif opcion == 3:
        try:
            print(f"\n Recuperar microtonos, actualmente hay {micro_activos} microtonos activos")
            cantidad = int(input("¿Cuántos mirotonos quieres recuperar?: "))
            if cantidad <= 0:
                print("Error, la cantidad de microtonos a recuperar debe ser mayor a 0")
            elif micro_libres + cantidad > max_micro:
                print(f"Error, no puedes apagar tantos microtonos porque el máximo es {max_micro}")
            else:
                micro_libres += cantidad
                micro_activos -= cantidad
                print(f"Recuperaste {cantidad} de microtonos para ser usados en otro momento")
                winsound.Beep(440,150)
        except ValueError:
            print("Error, debes colocar un número entero")
    elif opcion == 4:
        print(f"Hay {micro_activos} microtonos activos haciendo vibrar el ambiente")
    elif opcion == 5:
        print("Saliendo del sistema")
        ejecutando = False
    else:
        print("Error")