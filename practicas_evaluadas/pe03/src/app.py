"""
@file app.py
@brief Programa principal de la práctica PE03.
"""

from pathlib import Path
from modelo import Estudiante, GestorArchivos

RUTA_BASE = Path(__file__).resolve().parents[1]
RUTA_DATOS = RUTA_BASE / "data" / "estudiante.txt"
RUTA_SALIDA = RUTA_BASE / "salida" / "resumen.txt"


def construir_estudiante() -> Estudiante:
    if not RUTA_DATOS.exists():
        raise FileNotFoundError(f"No se encontró el archivo de datos: {RUTA_DATOS}")

    kv = GestorArchivos.leer_kv(RUTA_DATOS)
    nombre = kv.get("NOMBRE", "N/A")
    correo = kv.get("CORREO", "N/A")

    materias = []
    if "MATERIAS" in kv and kv["MATERIAS"]:
        materias = [m.strip() for m in kv["MATERIAS"].split(",")]

    return Estudiante(nombre, correo, materias)


def main() -> None:
    estudiante = construir_estudiante()
    texto = estudiante.resumen()
    print(texto)
    GestorArchivos.escribir_texto(RUTA_SALIDA, texto)
    print(f"\nResumen generado correctamente en: {RUTA_SALIDA}")


if __name__ == "__main__":
    main()