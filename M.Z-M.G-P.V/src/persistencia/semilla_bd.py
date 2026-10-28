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

def preparar_base_datos():
    conn = abrir_conexion()
    cursor = conn.cursor()
    
    # 1. Asegurar que exista un empleado base para el administrador (Requerimiento Página 22)
    try:
        cursor.execute("SELECT id FROM empleado WHERE id = 1")
        empleado = cursor.fetchone()
        
        if not empleado:
            cursor.execute(
                """
                INSERT INTO empleado
                    (id, nombre, direccion, telefono, email, fechaInicioContrato, salario)
                VALUES (1, 'Administrador General', 'Sin dirección', '555-0001',
                        'admin@ecotech.com', '2026-01-01', 0)
                """
            )
            conn.commit()
            print("Empleado base 'Admin' creado con ID 1.")
            
        # 2. Asegurar que exista el empleado Ana para la prueba del laboratorio (Requerimiento Página 21)
        cursor.execute("SELECT id FROM empleado WHERE id = 2")
        ana = cursor.fetchone()
        if not ana:
            cursor.execute(
                """
                INSERT INTO empleado
                    (id, nombre, direccion, telefono, email, fechaInicioContrato, salario)
                VALUES (2, 'Ana Torres', 'Sin dirección', '555-0002',
                        'ana.torres@ecotech.com', '2026-01-01', 0)
                """
            )
            conn.commit()
            print("Empleado 'Ana Torres' creado con ID 2 listo para tu registro.")
            
    except sqlite3.Error as e:
        print(f"Nota en tabla empleados: {e}")
    finally:
        conn.close()

    # 3. Vincular la cuenta admin inicial comprobando que no se duplique (Requerimiento Página 23)
    print("\nComprobando cuenta de usuario inicial...")
    try:
        cuenta_existente = UsuarioDAO.buscar_por_nombre("admin")
        
        if cuenta_existente is None:
            # Registramos el usuario usando tu servicio (que genera el hash con bcrypt)
            registrar_usuario(empleado_id=1, nombre="admin", clave="admin123")
            print("¡Semilla exitosa! Cuenta 'admin' creada con éxito.")
        else:
            print("La cuenta 'admin' ya existe en la base de datos. No se duplicaron registros.")
    except Exception as e:
        print(f"No se pudo verificar o crear la cuenta de administrador: {e}")

if __name__ == "__main__":
    preparar_base_datos()
