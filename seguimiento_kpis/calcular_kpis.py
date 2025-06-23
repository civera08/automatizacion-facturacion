# calcular_kpis.py
import pandas as pd
from conexion_sql import get_connection

def calcular_asistencia(cursor):
    query = """
    SELECT e.id, e.nombre, e.apellido, COUNT(a.id) AS total_registros,
           SUM(CASE WHEN a.tipo = 'ausencia' THEN 1 ELSE 0 END) AS ausencias
    FROM empleados e
    LEFT JOIN asistencias a ON e.id = a.id_empleado
    GROUP BY e.id, e.nombre, e.apellido
    """
    df = pd.read_sql(query, cursor)
    df['porcentaje_asistencia'] = 100 * (df['total_registros'] - df['ausencias']) / df['total_registros']
    return df[['id', 'nombre', 'apellido', 'porcentaje_asistencia']]

def calcular_tareas(cursor):
    query = """
    SELECT e.id, COUNT(t.id) AS total_tareas,
           SUM(CASE WHEN t.estado = 'completada' THEN 1 ELSE 0 END) AS completadas
    FROM empleados e
    LEFT JOIN tareas t ON e.id = t.id_empleado
    GROUP BY e.id
    """
    df = pd.read_sql(query, cursor)
    df['cumplimiento_tareas'] = 100 * df['completadas'] / df['total_tareas']
    return df[['id', 'cumplimiento_tareas']]

def calcular_respuestas(cursor):
    query = """
    SELECT e.id, AVG(r.tiempo_respuesta_min) AS promedio_respuesta
    FROM empleados e
    LEFT JOIN respuestas r ON e.id = r.id_empleado
    GROUP BY e.id
    """
    df = pd.read_sql(query, cursor)
    return df[['id', 'promedio_respuesta']]

def unificar_kpis():
    conn = get_connection()
    cursor = conn.cursor()

    df_asistencia = calcular_asistencia(conn)
    df_tareas = calcular_tareas(conn)
    df_respuestas = calcular_respuestas(conn)

    df_final = df_asistencia.merge(df_tareas, on='id').merge(df_respuestas, on='id')
    df_final = df_final.round(2)
    conn.close()
    return df_final

if __name__ == "__main__":
    kpis = unificar_kpis()
    print(kpis.head())