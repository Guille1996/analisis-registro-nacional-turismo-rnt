# Análisis reproducible del Registro Nacional de Turismo — RNT en Colombia

## 1. Descripción del proyecto

Este repositorio contiene un análisis exploratorio y reproducible del **Registro Nacional de Turismo — RNT** en Colombia, a partir de datos abiertos publicados en el portal Datos Abiertos Colombia.

El proyecto está diseñado para cumplir los requisitos de un trabajo final de GitHub: repositorio organizado, Jupyter Notebook, código reproducible, documentación clara, uso de datos abiertos, visualizaciones, conclusiones y registro del uso de IA.

## 2. Pregunta de análisis

**¿Cómo se distribuyen los prestadores de servicios turísticos inscritos en el Registro Nacional de Turismo en Colombia según departamento, municipio, categoría, estado del registro y capacidad reportada?**

## 3. Preguntas específicas

1. ¿Qué departamentos concentran mayor número de registros turísticos?
2. ¿Qué municipios presentan mayor concentración de prestadores turísticos?
3. ¿Cuáles son las categorías y subcategorías más frecuentes del RNT?
4. ¿Cómo se distribuyen los registros según su estado?
5. ¿Qué departamentos o categorías reportan mayor capacidad en habitaciones, camas y empleados?

## 4. Fuente de datos

- Nombre del dataset: **Registro Nacional de Turismo - RNT**.
- Portal: Datos Abiertos Colombia.
- Sector: Comercio, Industria y Turismo.
- Descripción: registro público en el cual deben inscribirse los prestadores de servicios turísticos que efectúan operaciones en el territorio colombiano.
- Identificador del dataset en Datos Abiertos Colombia: `thwd-ivmp`.
- Formato de trabajo: CSV descargado desde el portal o desde la API pública de datos.gov.co.

## 5. Estructura del repositorio

```text
analisis-registro-nacional-turismo-rnt/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   └── processed/
│       └── .gitkeep
│
├── notebooks/
│   └── analisis_rnt_colombia.ipynb
│
├── outputs/
│   ├── graficos/
│   │   └── .gitkeep
│   └── tablas/
│       └── .gitkeep
│
├── src/
│   └── utilidades_rnt.py
│
└── docs/
    └── uso_ia.md
```

## 6. Cómo reproducir el análisis

### 6.1 Crear entorno virtual

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

### 6.2 Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6.3 Abrir Jupyter Notebook

```bash
jupyter notebook notebooks/analisis_rnt_colombia.ipynb
```

Luego ejecute las celdas en orden.

El notebook intenta descargar automáticamente el dataset desde la API pública. Si la descarga falla, descargue manualmente el CSV desde Datos Abiertos Colombia y guárdelo en:

```text
data/raw/registro_nacional_turismo_rnt.csv
```

## 7. Archivos grandes

La carpeta `data/raw/` está excluida del control de versiones para evitar subir archivos crudos pesados. El notebook guarda una versión procesada en `data/processed/`.

## 8. Resultados esperados

El proyecto genera:

- tablas resumen por departamento, municipio, categoría, subcategoría y estado del registro;
- gráficos de barras con los principales departamentos y municipios;
- gráficos de categorías del RNT;
- análisis descriptivo de habitaciones, camas y empleados;
- archivos procesados en `data/processed/`;
- tablas y gráficos en `outputs/`.

## 9. Uso de IA

El uso de IA se documenta en `docs/uso_ia.md`.
