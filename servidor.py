import os
import time

DIRECTORIO_TAREAS = "cola_de_tareas"

def leer_excusas():
    while True:
        # Solo excusas pendientes (no las que ya están en procesamiento)
        excusas_pendientes = sorted(
            [f for f in os.listdir(DIRECTORIO_TAREAS) if not f.startswith("procesando_")]
        )
        
        if excusas_pendientes:
            excusa = excusas_pendientes[0]
            nuevo_nombre = f"procesando_{excusa}"
            
            print(f"[SERVIDOR UAX] 📨 Recibiendo excusa: {excusa} → Asignando a evaluadores")
            
            os.rename(
                os.path.join(DIRECTORIO_TAREAS, excusa),
                os.path.join(DIRECTORIO_TAREAS, nuevo_nombre)
            )
            print(f"[SERVIDOR UAX] ✅ Excusa asignada: {nuevo_nombre}")
        time.sleep(1)

if __name__ == "__main__":
    print("[SERVIDOR UAX] 🚀 Iniciando el Centro de Gestión de Excusas de Alumnos...")
    leer_excusas()
