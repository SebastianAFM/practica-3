# Chess SAN Parser

**Lenguajes de Programación - ST0244**  
**Universidad EAFIT**  
**Práctica III - Analizador Sintáctico de Partidas de Ajedrez con Árbol Binario**

## Descripción
Este proyecto consiste en un analizador sintáctico de partidas de ajedrez escritas en notación algebraica estándar (SAN), basado en una gramática BNF simplificada. El programa valida la partida y la representa como un árbol binario intercalado por turnos. 

La visualización se realiza mediante una interfaz gráfica desarrollada con PyQt5.

## Integrantes
- Nombre Estudiante 1
- Nombre Estudiante 2 *(si aplica)*

## Lenguaje y Herramientas
- **Lenguaje:** Python 3.10+
- **Librerías:** PyQt5
- **IDE recomendado:** PyCharm / VSCode

## Requisitos
Instala los paquetes necesarios con:
```bash
pip install pyqt5
```

## Cómo ejecutar

1. Clona el repositorio:
```bash
git clone https://github.com/usuario/repositorio-chess-parser.git
cd repositorio-chess-parser
```

2. Ejecuta la aplicación:
```bash
python main.py
```

## Funcionalidades
- Validación de partidas de ajedrez SAN basadas en una gramática BNF.
- Reporte de errores sintácticos con mensajes claros.
- Visualización gráfica de la partida como un árbol binario.

## Estructura del Proyecto
```
├── main.py         # Punto de entrada
├── parser.py       # Lógica de análisis sintáctico
├── tree.py         # Representación del árbol binario
├── gui.py          # Interfaz gráfica con PyQt5
├── utils.py        # Funciones auxiliares (placeholder)
└── README.md
```

## Video de demostración
[Enlace al video explicativo aquí]

## Licencia
Este proyecto es parte de una práctica académica para el curso ST0244. Uso educativo solamente.

---
**Profesor:** Alexander Narváez Berrío