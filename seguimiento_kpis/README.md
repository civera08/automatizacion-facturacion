# Automatización del Seguimiento de Indicadores de Desempeño Administrativo

Este proyecto demuestra un flujo completo de automatización para tareas administrativas relacionadas con KPIs, utilizando herramientas profesionales como:

- **SQL Server** para almacenamiento de datos  
- **Python** para extracción, transformación, cálculo y generación de reportes  
- **Power Automate Desktop** para programación y envío automatizado por correo electrónico  

---

## Estructura del Proyecto
```
seguimiento_kpis/
├── conexion_sql.py # Conexión a SQL Server con pyodbc
├── insertar_datos.py # Inserta datos sintéticos con Faker (solo una vez)
├── calcular_kpis.py # Calcula indicadores clave por empleado
├── generar_reporte.py # Genera un reporte profesional en Excel
├── main.py # Ejecuta todo el flujo completo
├── config.ini # Configuración de conexión a SQL Server
└── reporte_kpis.xlsx # Archivo de salida generado automáticamente
```
---
## Requisitos

- Windows 10/11 Pro con Power Automate Desktop instalado  
- SQL Server (local o remoto)  
- Python 3.9 o superior  
- Librerías Python: `pyodbc`, `pandas`, `faker`, `openpyxl`  

## Instalación de dependencias

```bash
pip install -r requirements.txt
```

## Automatización del Proceso
Elimina archivos .xlsx antiguos automáticamente

Ejecuta main.py cada lunes a las 9:00 a.m.

Verifica si se generó correctamente reporte_kpis.xlsx

Envía el reporte generado como adjunto por correo usando Outlook

## Aplicaciones Profesionales
Automatización administrativa eficiente

Generación de reportes dinámicos en Excel

Integración fluida entre Python, SQL Server y Outlook

Orquestación de tareas con Power Automate Desktop

## Indicadores Incluidos

|Indicador	               |Descripción                                   |
|--------------------------|----------------------------------------------|
| Porcentaje de asistencia | Asistencias vs. ausencias por empleado       |
| Cumplimiento de tareas   | Porcentaje de tareas completadas             |
| Tiempo promedio de respuesta | Tiempo promedio (minutos) para atender un ticket |

## Contacto
Email: civera.ds@outlook.com 
LinkedIn: https://linkedin.com/in/civera/
GitHub: https://github.com/civera08

## Licencia
Este proyecto está licenciado bajo los términos de la Licencia MIT.


---
