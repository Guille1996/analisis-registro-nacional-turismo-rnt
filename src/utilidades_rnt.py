"""Utilidades para el proyecto Registro Nacional de Turismo — RNT."""

from __future__ import annotations

import unicodedata
from pathlib import Path
import pandas as pd


def normalizar_columna(nombre: str) -> str:
    """Convierte un nombre de columna a formato simple: minúsculas y guion bajo."""
    texto = str(nombre).strip().lower()
    texto = "".join(
        c for c in unicodedata.normalize("NFKD", texto)
        if not unicodedata.combining(c)
    )
    for ch in [" ", "-", ".", "/", "\\", "(", ")", "[", "]", ":"]:
        texto = texto.replace(ch, "_")
    while "__" in texto:
        texto = texto.replace("__", "_")
    return texto.strip("_")


def normalizar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve una copia del DataFrame con columnas normalizadas."""
    copia = df.copy()
    copia.columns = [normalizar_columna(c) for c in copia.columns]
    return copia


def buscar_columna(df: pd.DataFrame, candidatos: list[str]) -> str | None:
    """Busca la primera columna existente en una lista de nombres candidatos."""
    columnas = set(df.columns)
    for candidato in candidatos:
        if candidato in columnas:
            return candidato
    return None


def convertir_numerica(df: pd.DataFrame, columna: str | None) -> pd.DataFrame:
    """Convierte una columna a numérica si existe."""
    copia = df.copy()
    if columna is not None and columna in copia.columns:
        copia[columna] = pd.to_numeric(copia[columna], errors="coerce")
    return copia


def guardar_tabla(df: pd.DataFrame, ruta: str | Path) -> None:
    """Guarda una tabla CSV creando las carpetas necesarias."""
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(ruta, index=False, encoding="utf-8")
