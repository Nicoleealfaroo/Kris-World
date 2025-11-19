"""
@file modelo.py
@brief Clases de dominio para la práctica (POO + archivos).
"""

from pathlib import Path
from typing import Dict, List


class Estudiante:
    """
    @brief Modelo de estudiante con datos básicos.
    """

    def __init__(self, nombre: str, correo: str, materias: List[str] | None = None) -> None:
        self.nombre = nombre.strip()
        self.correo = correo.strip()
        self.materias = [m.strip() for m in (materias or []) if m.strip()]

    def resumen(self) -> str:
        lineas = [
            f"Nombre: {self.nombre}",
            f"Correo: {self.correo}",
            f"Materias: {', '.join(self.materias) if self.materias else 'N/A'}",
        ]
        return "\n".join(lineas)


class GestorArchivos:
    """
    @brief Utilidades para leer/escribir archivos de texto plano.
    """

    @staticmethod
    def leer_kv(ruta: Path) -> Dict[str, str]:
        """
        @brief Lee pares clave=valor, ignora líneas vacías y comentarios (#).
        @param ruta: Ruta del archivo de datos.
        @return Diccionario con claves en mayúscula.
        """
        datos: Dict[str, str] = {}
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                if "=" not in linea:
                    continue
                clave, valor = linea.split("=", 1)
                datos[clave.strip().upper()] = valor.strip()
        return datos

    @staticmethod
    def escribir_texto(ruta: Path, contenido: str) -> None:
        """
        @brief Escribe texto en la ruta indicada, crea carpetas si no existen.
        """
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)