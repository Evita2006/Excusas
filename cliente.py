import os
import time
import random

DIRECTORIO_TAREAS = "cola_de_tareas"

EXCUSAS_POSIBLES = [
    "Mi perro se comió el ordenador",
    "Tuve una emergencia familiar muy grave",
    "Me quedé dormido estudiando toda la noche",
    "El metro se averió y llegué tarde a todo",
    "Mi hermano pequeño borró el archivo sin querer",
    "Tuve un virus en el ordenador que lo borró todo",
    "Fui a una boda y se me fue el tiempo",
    "El profesor anterior me puso la fecha mal",
    "Mi gato caminó por el teclado y borró el trabajo",
    "Estuve en el hospital por un problema de salud"
]

def enviar_excusa():
    for i in range(12):  # 12 excusas aleatorias (puedes cambiar el número)
        excusa_texto = random.choice(EXCUSAS_POSIBLES)
        nombre_archivo = f"excusa_{i:03d}.txt"
        ruta = os.path.join(DIRECTORIO_TAREAS, nombre_archivo)
        
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(excusa_texto)
        
        print(f"[CLIENTE UAX] 📤 Enviando excusa: {nombre_archivo} → \"{excusa_texto}\"")
        time.sleep(1.2)

if __name__ == "__main__":
    print("[CLIENTE UAX] 🎓 Generando excusas de alumnos...")
    enviar_excusa()
    print("[CLIENTE UAX] ✅ Todas las excusas enviadas al sistema. ¡Que empiece la evaluación!")
