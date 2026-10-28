# src/persistencia/usuario_dao.py
import sqlite3
from dominio.usuario import Usuario
from persistencia.conexion import abrir_conexion

class UsuarioDAO:

    @classmethod
    def insertar(cls, usuario):
        conn = abrir_conexion()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO usuario (nombre_usuario, password_hash, empleado_id)
                VALUES (?, ?, ?)
                """,
                (usuario.nombre_usuario, usuario.password_hash, usuario.empleado_id)
            )
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error al insertar usuario: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def buscar_por_nombre(cls, nombre_usuario):
        conn = abrir_conexion()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT id, nombre_usuario, password_hash, empleado_id 
                FROM usuario 
                WHERE nombre_usuario = ?
                """,
                (nombre_usuario,)
            )
            fila = cursor.fetchone()
            if fila:
                # 🛠️ CORRECCIÓN: Acceder por índices a la tupla de la BD
                return Usuario(
                    id=fila[0],
                    nombre_usuario=fila[1],
                    password_hash=fila[2],
                    empleado_id=fila[3]
                )
            return None
        except sqlite3.Error as e:
            print(f"Error al buscar usuario por nombre: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def buscar_por_empleado(cls, empleado_id):
        conn = abrir_conexion()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT id, nombre_usuario, password_hash, empleado_id 
                FROM usuario 
                WHERE empleado_id = ?
                """,
                (empleado_id,)
            )
            fila = cursor.fetchone()
            if fila:
                # 🛠️ CORRECCIÓN: Acceder por índices a la tupla de la BD
                return Usuario(
                    id=fila[0],
                    nombre_usuario=fila[1],
                    password_hash=fila[2],
                    empleado_id=fila[3]
                )
            return None
        except sqlite3.Error as e:
            print(f"Error al buscar usuario por empleado: {e}")
            return None
        finally:
            conn.close()
