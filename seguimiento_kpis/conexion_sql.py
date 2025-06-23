# conexion_sql.py
import pyodbc
import configparser

def get_connection():
    config = configparser.ConfigParser()
    config.read(r'C:\Ruta\Al\Proyecto\seguimiento_kpis\config.ini')

    server = config['SQL']['server']
    database = config['SQL']['database']
    trusted_connection = config['SQL'].getboolean('trusted_connection', True)

    conn_str = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes' if trusted_connection else ''
    )
    return pyodbc.connect(conn_str)
