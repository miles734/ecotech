# src/persistencia/semilla_bd.py
import sqlite3
import sys
import os

# Ajuste de rutas para que Python encuentre los módulos hermanos desde la carpeta persistencia
directorio_src = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if directorio_src not in sys.path:
    sys.path.append(directorio_src)

from persistencia.conexion import abrir_conexion
from servicios.autenticacion import registrar_usuario
from persistencia.usuario_dao import UsuarioDAO

EMPLEADOS_INICIALES = (
    {
        "id": 1,
        "nombre": "Administrador General",
        "direccion": "Calle Central 100, Santiago",
        "telefono": "555-0001",
        "email": "admin@ecotech.com",
        "fechaInicioContrato": "2026-01-01",
        "salario": 0,
    },
    {
        "id": 2,
        "nombre": "Ana Torres",
        "direccion": "Avenida Las Flores 220, Santiago",
        "telefono": "555-0002",
        "email": "ana.torres@ecotech.com",
        "fechaInicioContrato": "2026-01-10",
        "salario": 1850000,
    },
    {
        "id": 3,
        "nombre": "Carlos Morales",
        "direccion": "Calle Los Pinos 15, Valparaíso",
        "telefono": "555-0003",
        "email": "carlos.morales@ecotech.com",
        "fechaInicioContrato": "2025-03-10",
        "salario": 1600000,
    },
    {
        "id": 4,
        "nombre": "Sofía García",
        "direccion": "Avenida Brasil 420, Concepción",
        "telefono": "555-0004",
        "email": "sofia.garcia@ecotech.com",
        "fechaInicioContrato": "2025-04-11",
        "salario": 1750000,
    },
    {
        "id": 5,
        "nombre": "Javier López",
        "direccion": "Pasaje El Roble 84, Rancagua",
        "telefono": "555-0005",
        "email": "javier.lopez@ecotech.com",
        "fechaInicioContrato": "2024-11-02",
        "salario": 1680000,
    },
    {
        "id": 6,
        "nombre": "Mariana Ruiz",
        "direccion": "Calle de la Paz 58, Temuco",
        "telefono": "555-0006",
        "email": "mariana.ruiz@ecotech.com",
        "fechaInicioContrato": "2025-01-20",
        "salario": 1720000,
    },
    {
        "id": 7,
        "nombre": "Diego Herrera",
        "direccion": "Av. San Martín 201, Antofagasta",
        "telefono": "555-0007",
        "email": "diego.herrera@ecotech.com",
        "fechaInicioContrato": "2025-05-14",
        "salario": 1650000,
    },
    {
        "id": 8,
        "nombre": "Valentina Castro",
        "direccion": "Calle Norte 77, Iquique",
        "telefono": "555-0008",
        "email": "valentina.castro@ecotech.com",
        "fechaInicioContrato": "2024-09-18",
        "salario": 1780000,
    },
    {
        "id": 9,
        "nombre": "Andrés Silva",
        "direccion": "Avenida Libertad 332, La Serena",
        "telefono": "555-0009",
        "email": "andres.silva@ecotech.com",
        "fechaInicioContrato": "2025-06-03",
        "salario": 1700000,
    },
    {
        "id": 10,
        "nombre": "Camila Flores",
        "direccion": "Calle Los Cerezos 44, Chillán",
        "telefono": "555-0010",
        "email": "camila.flores@ecotech.com",
        "fechaInicioContrato": "2025-02-17",
        "salario": 1820000,
    },
    {
        "id": 11,
        "nombre": "Mateo Ortega",
        "direccion": "Los Álamos 60, Viña del Mar",
        "telefono": "555-0011",
        "email": "mateo.ortega@ecotech.com",
        "fechaInicioContrato": "2024-08-15",
        "salario": 1740000,
    },
    {
        "id": 12,
        "nombre": "Natalia Rojas",
        "direccion": "Avenida Los Huertos 120, Puerto Montt",
        "telefono": "555-0012",
        "email": "natalia.rojas@ecotech.com",
        "fechaInicioContrato": "2025-03-28",
        "salario": 1690000,
    },
    {
        "id": 13,
        "nombre": "Sebastián Díaz",
        "direccion": "Calle Lincoyan 98, Talca",
        "telefono": "555-0013",
        "email": "sebastian.diaz@ecotech.com",
        "fechaInicioContrato": "2024-12-05",
        "salario": 1760000,
    },
    {
        "id": 14,
        "nombre": "Lucía Álvarez",
        "direccion": "Pasaje España 145, Coquimbo",
        "telefono": "555-0014",
        "email": "lucia.alvarez@ecotech.com",
        "fechaInicioContrato": "2025-07-10",
        "salario": 1710000,
    },
    {
        "id": 15,
        "nombre": "Pablo Moreno",
        "direccion": "Calle Sur 12, Copiapó",
        "telefono": "555-0015",
        "email": "pablo.moreno@ecotech.com",
        "fechaInicioContrato": "2024-10-22",
        "salario": 1800000,
    },
    {
        "id": 16,
        "nombre": "Renata Torres",
        "direccion": "Avenida Alemania 76, Punta Arenas",
        "telefono": "555-0016",
        "email": "renata.torres@ecotech.com",
        "fechaInicioContrato": "2025-02-08",
        "salario": 1670000,
    },
    {
        "id": 17,
        "nombre": "Samuel Salazar",
        "direccion": "Calle del Sol 303, Calama",
        "telefono": "555-0017",
        "email": "samuel.salazar@ecotech.com",
        "fechaInicioContrato": "2025-01-15",
        "salario": 1730000,
    },
    {
        "id": 18,
        "nombre": "Emilia Vargas",
        "direccion": "Avenida Oeste 89, Arica",
        "telefono": "555-0018",
        "email": "emilia.vargas@ecotech.com",
        "fechaInicioContrato": "2024-11-11",
        "salario": 1790000,
    },
    {
        "id": 19,
        "nombre": "Daniel Vega",
        "direccion": "Calle Maipú 410, Osorno",
        "telefono": "555-0019",
        "email": "daniel.vega@ecotech.com",
        "fechaInicioContrato": "2025-06-25",
        "salario": 1660000,
    },
    {
        "id": 20,
        "nombre": "Gabriela Paredes",
        "direccion": "Calle El Mirador 22, Puerto Varas",
        "telefono": "555-0020",
        "email": "gabriela.paredes@ecotech.com",
        "fechaInicioContrato": "2025-04-07",
        "salario": 1810000,
    },
    {
        "id": 21,
        "nombre": "Tomás Castillo",
        "direccion": "Av. Huérfanos 410, Santiago",
        "telefono": "555-0021",
        "email": "tomas.castillo@ecotech.com",
        "fechaInicioContrato": "2024-07-20",
        "salario": 1750000,
    },
    {
        "id": 22,
        "nombre": "Isidora Núñez",
        "direccion": "Calle El Bosque 12, Curicó",
        "telefono": "555-0022",
        "email": "isidora.nunez@ecotech.com",
        "fechaInicioContrato": "2025-03-01",
        "salario": 1685000,
    },
    {
        "id": 23,
        "nombre": "Rodrigo Benavides",
        "direccion": "Avenida Independencia 510, San Fernando",
        "telefono": "555-0023",
        "email": "rodrigo.benavides@ecotech.com",
        "fechaInicioContrato": "2025-02-12",
        "salario": 1775000,
    },
    {
        "id": 24,
        "nombre": "Paula Ibáñez",
        "direccion": "Calle La Compañía 31, La Florida",
        "telefono": "555-0024",
        "email": "paula.ibanez@ecotech.com",
        "fechaInicioContrato": "2024-09-01",
        "salario": 1705000,
    },
    {
        "id": 25,
        "nombre": "Alejandro Pinto",
        "direccion": "Calle Los Olivos 18, Quilpué",
        "telefono": "555-0025",
        "email": "alejandro.pinto@ecotech.com",
        "fechaInicioContrato": "2025-05-05",
        "salario": 1830000,
    },
    {
        "id": 26,
        "nombre": "Cristina León",
        "direccion": "Avenida El Bosque 200, Rengo",
        "telefono": "555-0026",
        "email": "cristina.leon@ecotech.com",
        "fechaInicioContrato": "2024-10-18",
        "salario": 1695000,
    },
    {
        "id": 27,
        "nombre": "Ignacio Bravo",
        "direccion": "Calle Los Lavandares 91, Linares",
        "telefono": "555-0027",
        "email": "ignacio.bravo@ecotech.com",
        "fechaInicioContrato": "2025-04-22",
        "salario": 1725000,
    },
    {
        "id": 28,
        "nombre": "Fernanda Cárdenas",
        "direccion": "Avenida del Mar 60, Hualpén",
        "telefono": "555-0028",
        "email": "fernanda.cardenas@ecotech.com",
        "fechaInicioContrato": "2025-01-30",
        "salario": 1765000,
    },
    {
        "id": 29,
        "nombre": "Maximiliano Gutiérrez",
        "direccion": "Calle Las Araucarias 70, San Antonio",
        "telefono": "555-0029",
        "email": "maximiliano.gutierrez@ecotech.com",
        "fechaInicioContrato": "2024-12-12",
        "salario": 1745000,
    },
    {
        "id": 30,
        "nombre": "Daniela Navarro",
        "direccion": "Pasaje Las Encinas 35, Peñalolén",
        "telefono": "555-0030",
        "email": "daniela.navarro@ecotech.com",
        "fechaInicioContrato": "2025-06-20",
        "salario": 1785000,
    },
)


def limpiar_empleados_duplicados(cursor):
    cursor.execute("DELETE FROM registro_tiempo")
    cursor.execute("DELETE FROM usuario")
    cursor.execute("DELETE FROM empleado")


def preparar_base_datos():
    conn = abrir_conexion()
    cursor = conn.cursor()

    try:
        limpiar_empleados_duplicados(cursor)

        for empleado in EMPLEADOS_INICIALES:
            cursor.execute(
                """
                INSERT INTO empleado
                    (id, nombre, direccion, telefono, email, fechaInicioContrato, salario)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    empleado["id"],
                    empleado["nombre"],
                    empleado["direccion"],
                    empleado["telefono"],
                    empleado["email"],
                    empleado["fechaInicioContrato"],
                    empleado["salario"],
                ),
            )
            conn.commit()

        print(f"Semilla de empleados lista: {cursor.execute('SELECT COUNT(*) FROM empleado').fetchone()[0]} registros.")

    except sqlite3.Error as e:
        print(f"Nota en tabla empleados: {e}")
    finally:
        conn.close()

    return


def asegurar_usuario_admin():
    try:
        cuenta_existente = UsuarioDAO.buscar_por_nombre("admin")

        if cuenta_existente is None:
            registrar_usuario(empleado_id=1, nombre="admin", clave="admin123")

        cuenta_ana = UsuarioDAO.buscar_por_nombre("ana")
        if cuenta_ana is None:
            registrar_usuario(empleado_id=2, nombre="ana", clave="ana123")
    except Exception as e:
        print(f"No se pudo verificar o crear las cuentas iniciales: {e}")

if __name__ == "__main__":
    preparar_base_datos()
