import sys

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
    """Bucle principal que mantiene la aplicación ejecutándose."""
    mostrar_bienvenida()
    
    while True:
        # Captura el comando del conductor y lo pasa a mayúsculas
        comando = input("\nIngrese un comando (I, P, M, F, E): ").strip().upper()
        
        if comando == 'I':
            print("▶️ Carrera iniciada. El taxímetro está activo.")
        elif comando == 'P':
            print("🛑 Vehículo PARADO. Aplicando tarifa de parada.")
        elif comando == 'M':
            print("🚗 Vehículo EN MOVIMIENTO. Aplicando tarifa de movimiento.")
        elif comando == 'F':
            print("🏁 Carrera finalizada. Importe total: 0.00€")
            print("🔄 Sistema listo para encadenar el siguiente servicio...")
        elif comando == 'E':
            print("👋 Saliendo del taxímetro. ¡Buen viaje!")
            sys.exit()
        else:
            print("⚠️ Comando no válido. Por favor, use I, P, M, F o E.")

if __name__ == "__main__":
    iniciar_taximetro()
