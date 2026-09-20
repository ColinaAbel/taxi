import sys
import time

# =====================================================================
# CONSTANTES DE TARIFAS (Valores simulados por segundo en euros)
# =====================================================================
TARIFA_PARADO = 0.02        # 0.02€ por segundo
TARIFA_MOVIMIENTO = 0.05    # 0.05€ por segundo

def mostrar_bienvenida():
    """Imprime las instrucciones de uso en la terminal."""
    print("=" * 50)
    print("      🚕 BIENVENIDO AL TAXÍMETRO CLI (MVP) 🚕      ")
    print("=" * 50)
    print("Instrucciones de uso:")
    print("  [I] - Iniciar una nueva carrera")
    print("  [P] - Cambiar estado a: VEHÍCULO PARADO")
    print("  [M] - Cambiar estado a: VEHÍCULO EN MOVIMIENTO")
    print("  [F] - Finalizar carrera actual y ver total")
    print("  [E] - Salir de la aplicación")
    print("=" * 50)

def iniciar_taximetro():
    """Bucle principal con motor de tarifas y acumulación de importes."""
    mostrar_bienvenida()
    
    # Variables de control de estado del taxi
    en_carrera = False
    estado_actual = None  # Puede ser 'PARADO' o 'MOVIMIENTO'
    tiempo_cambio_estado = None  # Guardará el reloj exacto del último cambio
    importe_acumulado = 0.0  # <--- NUEVA: Guarda el dinero total acumulado

    while True:
        comando = input("\nIngrese un comando (I, P, M, F, E): ").strip().upper()
        
        if comando == 'I':
            if en_carrera:
                print("⚠️ Ya hay una carrera activa en este momento.")
            else:
                en_carrera = True
                estado_actual = 'PARADO'
                tiempo_cambio_estado = time.time()
                importe_acumulado = 0.0  # Reseteamos el contador para la nueva carrera
                print("▶️ Carrera iniciada. El vehículo arranca en estado: PARADO.")
        
        elif comando == 'P':
            if not en_carrera:
                print("⚠️ No puedes cambiar de estado si no has iniciado una carrera [I].")
            elif estado_actual == 'PARADO':
                print("🚨 El vehículo ya se encuentra PARADO.")
            else:
                # 1. Calcular tiempo del tramo anterior (Movimiento)
                tiempo_actual = time.time()
                segundos_transcurridos = tiempo_actual - tiempo_cambio_estado
                
                # 2. Calcular dinero de ese tramo usando la constante
                euros_tramo = segundos_transcurridos * TARIFA_MOVIMIENTO
                importe_acumulado += euros_tramo  # Lo sumamos al total
                
                print(f"🛑 Cambiando a PARADO. Pasaste {segundos_transcurridos:.2f}s en movimiento (+{euros_tramo:.2f}€).")
                
                # 3. Actualizar estado y reloj
                estado_actual = 'PARADO'
                tiempo_cambio_estado = tiempo_actual

        elif comando == 'M':
            if not en_carrera:
                print("⚠️ No puedes cambiar de estado si no has iniciado una carrera [I].")
            elif estado_actual == 'MOVIMIENTO':
                print("🚨 El vehículo ya se encuentra EN MOVIMIENTO.")
            else:
                # 1. Calcular tiempo del tramo anterior (Parado)
                tiempo_actual = time.time()
                segundos_transcurridos = tiempo_actual - tiempo_cambio_estado
                
                # 2. Calcular dinero de ese tramo usando la constante
                euros_tramo = segundos_transcurridos * TARIFA_PARADO
                importe_acumulado += euros_tramo  # Lo sumamos al total
                
                print(f"🚗 Cambiando a EN MOVIMIENTO. Pasaste {segundos_transcurridos:.2f}s parado (+{euros_tramo:.2f}€).")
                
                # 3. Actualizar estado y reloj
                estado_actual = 'MOVIMIENTO'
                tiempo_cambio_estado = tiempo_actual

        elif comando == 'F':
            if not en_carrera:
                print("⚠️ No hay ninguna carrera activa para finalizar.")
            else:
                # 1. Calcular el último tramo antes de cerrar
                tiempo_actual = time.time()
                segundos_transcurridos = tiempo_actual - tiempo_cambio_estado
                
                # 2. Aplicar la tarifa según el estado en el que se encontraba el taxi
                tarifa_aplicada = TARIFA_PARADO if estado_actual == 'PARADO' else TARIFA_MOVIMIENTO
                euros_tramo = segundos_transcurridos * tarifa_aplicada
                importe_acumulado += euros_tramo
                
                print(f"🏁 Finalizando último tramo de {segundos_transcurridos:.2f}s en estado {estado_actual} (+{euros_tramo:.2f}€).")
                
                # 3. LOGRADO: Mostrar el importe total con dos decimales y símbolo €
                print("-" * 40)
                print(f"💰 IMPORTE TOTAL A COBRAR: {importe_acumulado:.2f}€")
                print("-" * 40)
                print("🔄 Sistema reiniciado. Listo para encadenar una nueva carrera de inmediato.")
                
                # 4. LOGRADO: Reiniciar variables para encadenar servicios sin cerrar la app
                en_carrera = False
                estado_actual = None
                tiempo_cambio_estado = None
                importe_acumulado = 0.0

        elif comando == 'E':
            print("👋 Saliendo del taxímetro. ¡Buen viaje!")
            sys.exit()
            
        else:
            print("⚠️ Comando no válido. Por favor, use I, P, M, F o E.")

if __name__ == "__main__":
    iniciar_taximetro()
