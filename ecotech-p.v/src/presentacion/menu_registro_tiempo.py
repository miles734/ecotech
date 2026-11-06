from dominio.registro_tiempo import RegistroTiempo
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.proyecto_dao import ProyectoDAO
from persistencia.registro_tiempo_dao import RegistroTiempoDAO
from presentacion.entrada import (
    convertir_decimal,
    leer_decimal,
    leer_entero,
    leer_entidad_existente,
    leer_fecha,
    leer_opcion,
    leer_texto,
    limpiar_consola,
    pausar,
)


def usuario_es_admin(usuario_actual):
    return usuario_actual is not None and usuario_actual.get("rol") == "admin"


def registrar_tiempo(usuario_actual=None):
    print("\n--- Registrar Tiempo Trabajado ---")
    try:
        if usuario_actual is not None and not usuario_es_admin(usuario_actual):
            empleado = EmpleadoDAO.obtenerPorId(usuario_actual["empleado_id"])
            if empleado is None:
                raise ValueError("No se encontró el empleado asociado a la sesión.")
        else:
            empleado = leer_entidad_existente(
                "ID del empleado: ", EmpleadoDAO.obtenerPorId, "un empleado"
            )
        proyecto = leer_entidad_existente(
            "ID del proyecto: ", ProyectoDAO.obtenerPorId, "un proyecto"
        )

        fecha = leer_fecha("Fecha del registro (AAAA-MM-DD): ")
        horas = leer_decimal("Horas trabajadas: ", minimo=0, estrictamente_mayor=True)
        descripcion = leer_texto("Descripción de las tareas: ", maximo=1000)

        registro = RegistroTiempo(
            fecha=fecha,
            horas=horas,
            descripcion=descripcion,
            empleado_id=empleado.id,
            proyecto_id=proyecto.id,
            empleado=empleado,
            proyecto=proyecto,
        )
        registro = RegistroTiempoDAO.insertar(registro)
        print(f"Registro guardado correctamente con ID: {registro.id}")
    except Exception as error:
        print(f"No fue posible guardar el registro: {error}")


def listar_registros(usuario_actual=None):
    print("\n--- Lista de Registros de Tiempo ---")
    try:
        registros = (
            RegistroTiempoDAO.listarPorEmpleado(usuario_actual["empleado_id"])
            if usuario_actual is not None and not usuario_es_admin(usuario_actual)
            else RegistroTiempoDAO.listar()
        )
        if not registros:
            print("No hay registros de tiempo.")
            return
        for registro in registros:
            print(
                f"ID: {registro.id} | Fecha: {registro.fecha} "
                f"| Horas: {registro.horas:g} "
                f"| Empleado: {registro.empleado.nombre} "
                f"| Proyecto: {registro.proyecto.nombre} "
                f"| Descripción: {registro.descripcion}"
            )
    except Exception as error:
        print(f"Error al listar registros: {error}")


def buscar_registro(usuario_actual=None):
    print("\n--- Buscar Registro de Tiempo ---")
    try:
        id_registro = leer_entero("Ingrese el ID del registro: ")
        registro = RegistroTiempoDAO.obtenerPorId(id_registro)
        if registro is None:
            print("No existe un registro con ese ID.")
            return
        if usuario_actual is not None and not usuario_es_admin(usuario_actual):
            if registro.empleado_id != usuario_actual["empleado_id"]:
                print("No tienes permisos para ver ese registro.")
                return
        print(f"ID: {registro.id} | Fecha: {registro.fecha}")
        print(f"Horas: {registro.horas:g}")
        print(f"Empleado: {registro.empleado.nombre} (ID {registro.empleado_id})")
        print(f"Proyecto: {registro.proyecto.nombre} (ID {registro.proyecto_id})")
        print(f"Descripción: {registro.descripcion}")
    except Exception as error:
        print(f"Error al buscar el registro: {error}")


def actualizar_registro(usuario_actual=None):
    print("\n--- Actualizar Registro de Tiempo ---")
    try:
        id_registro = leer_entero("Ingrese el ID del registro: ")
        registro = RegistroTiempoDAO.obtenerPorId(id_registro)
        if not registro:
            print("No existe un registro con ese ID.")
            return
        if usuario_actual is not None and not usuario_es_admin(usuario_actual):
            if registro.empleado_id != usuario_actual["empleado_id"]:
                print("No tienes permisos para actualizar ese registro.")
                return

        horas_input = input(f"Horas [{registro.horas:g}] (Enter conserva): ").strip()
        if horas_input:
            while True:
                try:
                    horas = convertir_decimal(
                        horas_input,
                        minimo=0,
                        estrictamente_mayor=True,
                    )
                    break
                except ValueError as error:
                    print(error)
                    horas_input = input("Ingrese nuevamente las horas: ").strip()
        else:
            horas = registro.horas
        descripcion = leer_texto(
            f"Descripción [{registro.descripcion}] (Enter conserva): ",
            obligatorio=False,
            maximo=1000,
        )

        if horas_input or descripcion:
            registro.modificarRegistro(horas, descripcion or registro.descripcion)
            if RegistroTiempoDAO.actualizar(registro):
                print("Registro actualizado correctamente.")
            else:
                print("No se encontró el registro para actualizar.")
        else:
            print("No se realizaron cambios.")
    except Exception as error:
        print(f"Error al actualizar el registro: {error}")


def eliminar_registro(usuario_actual=None):
    print("\n--- Eliminar Registro de Tiempo ---")
    try:
        id_registro = leer_entero("Ingrese el ID del registro: ")
        registro = RegistroTiempoDAO.obtenerPorId(id_registro)
        if registro is None:
            print("No existe un registro con ese ID.")
            return
        if usuario_actual is not None and not usuario_es_admin(usuario_actual):
            if registro.empleado_id != usuario_actual["empleado_id"]:
                print("No tienes permisos para eliminar ese registro.")
                return
        if RegistroTiempoDAO.eliminar(id_registro):
            print("Registro eliminado correctamente.")
        else:
            print("No existe un registro con ese ID.")
    except Exception as error:
        print(f"No fue posible eliminar el registro: {error}")


def mostrar_menu_registro(usuario_actual=None):
    print("\n===== GESTIÓN DE TIEMPO =====")
    if usuario_actual is not None and not usuario_es_admin(usuario_actual):
        print("1. Registrar mi tiempo trabajado")
        print("2. Ver mis registros")
        print("3. Buscar mi registro")
        print("4. Actualizar mi registro")
        print("5. Eliminar mi registro")
    else:
        print("1. Registrar tiempo trabajado")
        print("2. Listar registros")
        print("3. Buscar registro")
        print("4. Actualizar registro")
        print("5. Eliminar registro")
    print("0. Volver al menú principal")


def menu_registro_tiempo(usuario_actual=None):
    while True:
        limpiar_consola()
        print("\n" * 2)
        mostrar_menu_registro(usuario_actual)
        opcion = leer_opcion(
            "Seleccione una opción: ", {"0", "1", "2", "3", "4", "5"}
        )
        if opcion == "0":
            limpiar_consola()
            return
        acciones = {
            "1": lambda: registrar_tiempo(usuario_actual),
            "2": lambda: listar_registros(usuario_actual),
            "3": lambda: buscar_registro(usuario_actual),
            "4": lambda: actualizar_registro(usuario_actual),
            "5": lambda: eliminar_registro(usuario_actual),
        }
        acciones[opcion]()
        pausar()
