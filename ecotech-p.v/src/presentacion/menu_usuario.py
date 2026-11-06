import getpass
from entradas import pedir_dato
from servicios.autenticacion import registrar_usuario, autenticar
from dominio.usuario import Usuario
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.registro_tiempo_dao import RegistroTiempoDAO
from presentacion.entrada import limpiar_consola, pausar
from presentacion.menu_principal import iniciar_menu_principal
from servicios.divisas import consultar_cotizacion_dolar, obtener_historial_divisas

def solicitar_registro():
    try:
        empleado_id = pedir_dato("ID del empleado: ", int)
        nombre = pedir_dato("Nuevo usuario: ", Usuario.normalizar_usuario)
        clave = pedir_dato("Contraseña: ", Usuario.validar_clave, getpass.getpass)
        
        if clave != getpass.getpass("Repita la contraseña: "):
            print("Las contraseñas no coinciden. Vuelva al registro.")
            return None
            
        usuario_id = registrar_usuario(empleado_id, nombre, clave)
    except (TypeError, ValueError) as error:
        print(error)
        return None
        
    print(f"Cuenta creada correctamente. ID: {usuario_id}")
    return usuario_id

def solicitar_login():
    nombre = input("Usuario: ")
    clave = getpass.getpass("Contraseña: ")
    try:
        usuario = autenticar(nombre, clave)
    except (TypeError, ValueError):
        print("No se pudo validar el acceso.")
        return None

    if usuario is None:
        print("Usuario o contraseña incorrectos.")
    return usuario

def mostrar_perfil(usuario_actual):
    if usuario_actual is None:
        print("Inicie sesión para ver el perfil.")
        return

    empleado = EmpleadoDAO.obtenerPorId(usuario_actual.get("empleado_id"))
    if empleado is None:
        print(f"Usuario: {usuario_actual['nombre_usuario']}")
        print(f"Empleado: {usuario_actual['empleado_id']}")
        print(f"Rol: {usuario_actual.get('rol', 'empleado')}")
        return

    print("\n--- Mi perfil ---")
    print(f"Usuario: {usuario_actual['nombre_usuario']}")
    print(f"Nombre completo: {empleado.nombre}")
    print(f"Correo: {empleado.email}")
    print(f"Teléfono: {empleado.telefono}")
    print(f"Dirección: {empleado.direccion}")
    print(f"Fecha de inicio: {empleado.fechaInicioContrato}")
    print(f"Salario: ${empleado.salario:,.0f}")
    print(f"Rol: {usuario_actual.get('rol', 'empleado')}")


def consultar_indicador(usuario_actual):
    if usuario_actual is None:
        print("Inicie sesión para consultar indicadores.")
        return

    empleado = EmpleadoDAO.obtenerPorId(usuario_actual.get("empleado_id"))
    if empleado is None:
        print("No se encontraron datos del empleado para evaluar indicadores.")
        return

    registros = RegistroTiempoDAO.listarPorEmpleado(empleado.id)
    total_horas = sum(registro.horas for registro in registros)
    proyectos = {registro.proyecto_id for registro in registros}

    print("\n--- Indicadores personales ---")
    print(f"Empleado: {empleado.nombre}")
    print(f"Total de horas registradas: {total_horas:g} h")
    print(f"Cantidad de registros: {len(registros)}")
    print(f"Proyectos asociados: {len(proyectos)}")
    if registros:
        promedio = total_horas / len(registros)
        print(f"Promedio por registro: {promedio:.2f} h")
    else:
        print("No hay registros aún.")


def mostrar_historial_divisas():
    historial = obtener_historial_divisas()
    if not historial:
        print("\n--- Historial de divisas ---")
        print("Todavía no se han consultado cotizaciones.")
        return

    print("\n--- Historial de divisas ---")
    for consulta in reversed(historial):
        resultado = consulta.get("resultado", {})
        print(
            f"{consulta.get('fecha', 'Sin fecha')} | USD: {consulta.get('cantidad_usd', 0)} | "
            f"CLP: {resultado.get('CLP', '-')}, ARS: {resultado.get('ARS', '-')}, BRL: {resultado.get('BRL', '-')}"
        )


def consultar_dolar_desde_menu():
    while True:
        valor = input("Ingrese la cantidad en USD a convertir: ").strip().replace(".", ".")
        try:
            cantidad = float(valor)
            break
        except ValueError:
            print("Ingrese un número válido.")

    resultado = consultar_cotizacion_dolar(cantidad)
    print("\n--- Cotización del dólar ---")
    print(f"USD: {cantidad:.2f}")
    print(f"CLP: {resultado['CLP']:.2f}")
    print(f"ARS: {resultado['ARS']:.2f}")
    print(f"BRL: {resultado['BRL']:.2f}")
    return resultado


def usuario_es_admin(usuario_actual):
    return usuario_actual is not None and usuario_actual.get("rol") == "admin"


def menu_privado(usuario_actual):
    if usuario_actual is None:
        print("Debe iniciar sesión.")
        return "9"

    while True:
        limpiar_consola()
        print("\n" * 2)
        if usuario_es_admin(usuario_actual):
            print("\n1 Registrar usuario, 2 Perfil, 3 Indicador, 4 Gestión del sistema, 5 Consultar dólar, 6 Historial de divisas, 9 Cerrar sesión, 0 Salir")
        else:
            print("\n1 Mi perfil, 2 Gestión de mi tiempo, 3 Ver indicadores, 4 Consultar dólar, 5 Historial de divisas, 9 Cerrar sesión, 0 Salir")
        opcion = input("Opción: ").strip()

        if opcion in ("0", "9"):
            return opcion

        if usuario_es_admin(usuario_actual):
            if opcion == "1":
                solicitar_registro()
            elif opcion == "2":
                mostrar_perfil(usuario_actual)
            elif opcion == "3":
                consultar_indicador(usuario_actual)
            elif opcion == "4":
                iniciar_menu_principal()
            elif opcion == "5":
                consultar_dolar_desde_menu()
            elif opcion == "6":
                mostrar_historial_divisas()
            else:
                print("Opción no válida.")
        else:
            if opcion == "1":
                mostrar_perfil(usuario_actual)
            elif opcion == "2":
                from presentacion.menu_registro_tiempo import menu_registro_tiempo
                menu_registro_tiempo(usuario_actual)
            elif opcion == "3":
                consultar_indicador(usuario_actual)
            elif opcion == "4":
                consultar_dolar_desde_menu()
            elif opcion == "5":
                mostrar_historial_divisas()
            else:
                print("Opción no válida.")

        if opcion not in {"0", "9"}:
            pausar()
