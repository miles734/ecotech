from persistencia.crear_db import crear_tablas
from persistencia.semilla_bd import preparar_base_datos
from presentacion.menu_principal import iniciar_menu_principal
from presentacion.menu_usuario import solicitar_login, menu_privado

def main():
    try:
        crear_tablas()
        preparar_base_datos()
    except Exception as error:
        raise SystemExit(f"No fue posible inicializar la base de datos: {error}") from error

    while True:
        usuario_actual = solicitar_login()
        if usuario_actual is None:
            if input("Enter para reintentar o 0 para salir: ") == "0":
                return
            continue
            
        opcion = menu_privado(usuario_actual)
        usuario_actual = None  # Terminar el acceso de esta sesión (Logout)
        
        if opcion == "0":
            return
        print("Sesión cerrada. Ingrese nuevamente.")

if __name__ == "__main__":
    main()
