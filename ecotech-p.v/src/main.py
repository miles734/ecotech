from persistencia.crear_db import crear_tablas
from persistencia.semilla_bd import preparar_base_datos, asegurar_usuario_admin
from presentacion.entrada import limpiar_consola
from presentacion.menu_usuario import solicitar_login, menu_privado


def main():
    try:
        crear_tablas()
        preparar_base_datos()
        asegurar_usuario_admin()
    except Exception as error:
        raise SystemExit(f"No fue posible inicializar la base de datos: {error}") from error

    limpiar_consola()

    while True:
        print("Inicie sesión.")
        usuario_actual = solicitar_login()
        if usuario_actual is None:
            respuesta = input("Presione Enter para reintentar o 0 para salir: ").strip()
            if respuesta == "0":
                limpiar_consola()
                return
            limpiar_consola()
            continue

        limpiar_consola()
        opcion = menu_privado(usuario_actual)
        usuario_actual = None

        if opcion == "0":
            limpiar_consola()
            return

        limpiar_consola()


if __name__ == "__main__":
    main()
