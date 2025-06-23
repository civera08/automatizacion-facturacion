# insertar_datos.py
import random
from faker import Faker
from datetime import datetime, timedelta
from conexion_sql import get_connection

fake = Faker()
Faker.seed(42)
random.seed(42)

def insertar_empleados(cursor):
    departamentos = ['Administración', 'RRHH', 'Finanzas', 'Operaciones', 'Sistemas']
    empleados = []
    for i in range(1, 41):
        nombre = fake.first_name()
        apellido = fake.last_name()
        departamento = random.choice(departamentos)
        fecha_ingreso = fake.date_between(start_date='-5y', end_date='-1y')
        correo = f"{nombre.lower()}.{apellido.lower()}@empresa.com"
        empleados.append((i, nombre, apellido, departamento, fecha_ingreso, correo))

    cursor.executemany("""
        INSERT INTO empleados (id, nombre, apellido, departamento, fecha_ingreso, correo)
        VALUES (?, ?, ?, ?, ?, ?)
    """, empleados)

def insertar_asistencias(cursor):
    start_date = datetime(2024, 3, 1)
    tipos = ['presencial', 'remoto', 'ausencia']
    asistencias = []
    for emp_id in range(1, 41):
        for i in range(90):
            fecha = start_date + timedelta(days=i)
            tipo = random.choices(tipos, weights=[0.75, 0.2, 0.05])[0]
            if tipo == 'ausencia':
                entrada = salida = None
            else:
                entrada = (datetime(2024,1,1,8,0) + timedelta(minutes=random.randint(0,30))).time()
                salida = (datetime(2024,1,1,17,0) + timedelta(minutes=random.randint(0,30))).time()
            asistencias.append((emp_id, fecha.date(), entrada, salida, tipo))

    cursor.executemany("""
        INSERT INTO asistencias (id_empleado, fecha, hora_entrada, hora_salida, tipo)
        VALUES (?, ?, ?, ?, ?)
    """, asistencias)

def insertar_tareas(cursor):
    estados = ['completada', 'pendiente', 'retrasada']
    tareas = []
    for _ in range(1000):
        emp_id = random.randint(1, 40)
        asignacion = fake.date_between(start_date='-90d', end_date='-1d')
        entrega = (datetime.strptime(str(asignacion), '%Y-%m-%d') + timedelta(days=random.randint(1, 10))).date()
        estado = random.choices(estados, weights=[0.6, 0.3, 0.1])[0]
        descripcion = fake.sentence(nb_words=6)
        tareas.append((emp_id, descripcion, asignacion, entrega, estado))

    cursor.executemany("""
        INSERT INTO tareas (id_empleado, descripcion, fecha_asignacion, fecha_entrega, estado)
        VALUES (?, ?, ?, ?, ?)
    """, tareas)

def insertar_respuestas(cursor):
    respuestas = []
    for _ in range(1000):
        emp_id = random.randint(1, 40)
        fecha_ticket = fake.date_between(start_date='-90d', end_date='-2d')
        tiempo = random.randint(15, 480)
        fecha_respuesta = (datetime.strptime(str(fecha_ticket), '%Y-%m-%d') + timedelta(minutes=tiempo)).date()
        respuestas.append((emp_id, fecha_ticket, fecha_respuesta, tiempo))

    cursor.executemany("""
        INSERT INTO respuestas (id_empleado, fecha_ticket, fecha_respuesta, tiempo_respuesta_min)
        VALUES (?, ?, ?, ?)
    """, respuestas)

def poblar_bd():
    conn = get_connection()
    cursor = conn.cursor()

    insertar_empleados(cursor)
    insertar_asistencias(cursor)
    insertar_tareas(cursor)
    insertar_respuestas(cursor)

    conn.commit()
    conn.close()
    print("Datos insertados correctamente.")

if __name__ == "__main__":
    poblar_bd()